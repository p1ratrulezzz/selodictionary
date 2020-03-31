import markdown
from mako.template import Template
from xml.dom import minidom
from collections import OrderedDict
from transliterate import translit
from pathvalidate import sanitize_filename
import os.path
import datetime
import xml.etree.ElementTree

def RenderIndexHtml(model):
    tpl = Template(filename="templates/index.html.tpl", input_encoding='utf-8')
    html = tpl.render(page=model)

    output = open("index.html", "w")
    output.write(html)
    output.close()

def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

def RenderWordHtml(model):
    outputFile = translit(model['text'], reversed=True)
    outputFile = sanitize_filename(outputFile).\
        replace('\'', '').\
        replace('"', '').\
        replace(' ', '_').\
        lower()

    postfixBase = ''
    postfix = ''
    index = 1

    outputFilePath = 'words/' + outputFile + str(postfix) + '.html'
    # @todo: Handle same names?
    # while os.path.isfile(outputFilePath):
    #     postfix = postfixBase + str(index)
    #     outputFilePath = 'words/' + outputFile + str(postfix) + '.html'
    #     index += 1

    model['description_html'] = model['element'].toxml()
    model['description'] = remove_tags(model['description_html'])
    model['modified_iso'] = datetime.\
        datetime.\
        utcnow().\
        replace(microsecond=0).\
        isoformat()

    tpl = Template(filename="templates/one_letter.html.tpl", input_encoding='utf-8')
    html = tpl.render(word=model)

    output = open(outputFilePath, "w")
    output.write(html)
    output.close()

    model['uri'] = outputFilePath

# Prepare model data
page = {}
mdfile = open("README.md", "r")

html = markdown.markdown(mdfile.read())
mdfile.close()

doc = minidom.parseString('<html>' + html + '</html>')

headerEl = doc.getElementsByTagName('h1')[0]
page["title"] = headerEl.childNodes[0].data
headerEl.parentNode.removeChild(headerEl)

words = []
keywords = []
keywords.append("")

for pEl in doc.documentElement.childNodes:
    if (pEl.nodeType != pEl.ELEMENT_NODE):
        continue

    strongElData = pEl.getElementsByTagName('strong')[0].firstChild.data
    pEl.getElementsByTagName('strong')[0].firstChild.data = str(strongElData).capitalize()

    text = []
    for strongEl in pEl.getElementsByTagName('strong'):
        text.append(strongEl.firstChild.data)

    word = " ".join(text).capitalize()
    wordObj = {
        "text": word,
        "element": pEl,
    }

    # Render a page for a singe word.
    RenderWordHtml(wordObj)

    linkElement = doc.createElement('a')
    linkElement.setAttribute('href', wordObj['uri'])

    strongEls = pEl.getElementsByTagName('strong')
    lastStrongEl = strongEls.item(strongEls.length - 1)
    strongElsArrayReversed = []
    while lastStrongEl != None:
        strongElsArrayReversed.append(lastStrongEl)
        lastStrongEl = lastStrongEl.previousSibling

    for el in reversed(strongElsArrayReversed):
        linkElement.appendChild(el)

    pEl.insertBefore(linkElement, pEl.firstChild)

    words.append(wordObj)

    keywords.append(word.lower())
    keywords.append(word.lower() + ' что такое')


page["keywords"] = ",".join(keywords)


def sort_words(v):
    return str(v['text']).lower()

words.sort(key=sort_words)

page["dictionary"] = OrderedDict()

glossaryIndex = 0
for word in words:
    firstLetter = word['text'][0:1].lower()
    if (firstLetter not in page["dictionary"]):
        page["dictionary"][firstLetter] = {
            'words': [],
            'index': glossaryIndex,
            'letter': firstLetter.upper()
        }

        glossaryIndex += 1

    page["dictionary"][firstLetter]['words'].append(word['element'].toxml())

# Parse html and sort nodes alphabetically
# Remove the header

# Write output file
RenderIndexHtml(page)