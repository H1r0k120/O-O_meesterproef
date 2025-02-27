from jinja2 import Template
from pathlib import Path
import datetime
from datetime import date

html_template = """
<!DOCTYPE html>
<html>
<head>
<title>Jouw rooster</title>
<link rel="stylesheet" href="stylesheet.css">
</head>
<body>

<h1>Hallo, NAAM</h1>
<p>{{datum}}</p>
    
<table>
    {{uur_1}}
    {{uur_2}}
    {{uur_3}}
    {{uur_4}}
    {{uur_5}}
    {{uur_6}}
    {{uur_7}}
    {{uur_8}}
    {{uur_9}}
</table>
</body>
</html>
"""

my_file = Path("./schedule.txt")
f = open(my_file, 'r')
rooster_JSON = f.read()
f.close()

#Datum definiëren
vandaag_en = date.today()

dag_vandaag_en = str(vandaag_en.strftime("%w"))
dag_translator = {
    "0":"Zondag",
    "1":"Maandag",
    "2":"Dinsdag",
    "3":"Woensdag",
    "4":"Donderdag",
    "5":"Vrijdag",
    "6":"Zaterdag"
}
dag_vandaag = dag_translator[dag_vandaag_en]

dagnmr_vandaag = str(vandaag_en.strftime("%d"))

maand_vandaag_en = str(vandaag_en.strftime("%m"))
maand_translator = {
    "01":"januari",
    "02":"februari",
    "03":"maart",
    "04":"april",
    "05":"mei",
    "06":"juni",
    "07":"juli",
    "08":"augustus",
    "09":"september",
    "10":"oktober",
    "11":"november",
    "12":"december"
}
maand_vandaag = maand_translator[maand_vandaag_en]

jaar_vandaag = str(vandaag_en.strftime("%Y"))

datum_vandaag = f"{dag_vandaag}, {dagnmr_vandaag} {maand_vandaag} {jaar_vandaag}"

if rooster_JSON["Start Time"] == "08:30":






data = {"datum": datum_vandaag}
template = Template(html_template)
html_output = template.render(data)

with open("output.html", "w", encoding="utf-8") as f2:
    f2.write(html_output)