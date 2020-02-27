import markdown
from mako.template import Template

mdfile = open("README.md", "r")

page = {}
page['content'] = markdown.markdown(mdfile.read())
mdfile.close()

tpl = Template(filename="templates/index.html.tpl", input_encoding='utf-8')
html = tpl.render(page=(page))

output = open("index.html", "w")
output.write(html)
output.close()
