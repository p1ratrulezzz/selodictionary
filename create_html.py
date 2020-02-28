import markdown
from mako.template import Template
from xml.dom import minidom

def RenderIndexHtml(model):
    tpl = Template(filename="templates/index.html.tpl", input_encoding='utf-8')
    html = tpl.render(page=model)

    output = open("index.html", "w")
    output.write(html)
    output.close()

# Prepare model data
mdfile = open("README.md", "r")

html = markdown.markdown(mdfile.read())
doc = minidom.parseString(html)

page = {}
page['content'] = html
mdfile.close()

# Parse html and sort nodes alphabetically
# Remove the header

# Write output file
RenderIndexHtml(page)