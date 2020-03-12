import markdown
from mako.template import Template
from xml.dom import minidom
from collections import OrderedDict

def RenderIndexHtml(model):
    tpl = Template(filename="templates/index.html.tpl", input_encoding='utf-8')
    html = tpl.render(page=model)

    output = open("index.html", "w")
    output.write(html)
    output.close()

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

    text = []
    for strongEl in pEl.getElementsByTagName('strong'):
        text.append(strongEl.firstChild.data)

    word = " ".join(text).capitalize()
    words.append({
        "text": word,
        "element": pEl,
    })

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