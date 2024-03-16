import requests
from string import Template 

html_template = Template('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
</head>
<body>

$body   

</body>
</html>                        
                        ''')


elem_template = Template('''<h2>Nombre:$nombre_ave_espanol</h2>
                            <h2>Name: $nombre_ave_ingles</h2>
                            <img src="$url">
                        
                        ''')


def requests_get(url):
    return requests.get(url).json()


def build_html(url):
    response=requests_get(url)[:20]   
    texto=''
    for aves in response:
        nombre = aves['name']['spanish']

        nombre_ingles=aves['name']['english']
        
        imagen_url=aves["images"]["main"]
        texto +=elem_template.substitute(nombre_ave_espanol=nombre,nombre_ave_ingles=nombre_ingles,url=imagen_url)
    return html_template.substitute(body=texto)



html=build_html('https://aves.ninjas.cl/api/birds')
with open("aves.html","w") as f:
    f.write(html)
