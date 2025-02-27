from jinja2 import Template

html_template = """
<!DOCTYPE html>
<html>
<head>
<title>Jouw rooster</title>
<link rel="stylesheet" href="stylesheet.css">


</head>
<body>
    <h1>Python Output:</h1>
    <p>{{ output }}</p>
</body>
</html>
"""

data = {"output": "Dit is een gegenereerde HTML met Python!"}
template = Template(html_template)
html_output = template.render(data)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_output)