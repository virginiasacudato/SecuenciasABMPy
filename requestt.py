import requests
import json
import pandas as pd
import datetime
import os
global html



# C:\Users\Maynar\TestVersion_8.3.16\logic && npx ts-node ./TruthTable.ts
#output_stream = os.popen(r'cd C:\Users\Maynar\TestVersion_8.3.16\logic && npx ts-node ./TruthTable.ts')
#out = output_stream.read()
#print(out.split())


arr = [
    ['A', 'G', 'not_a'], ['A', 'H', 'not_a'],
    ['A', 'I', 'not_a'], ['A', 'a'],
    ['B', 'G', 'not_a'], ['B', 'H', 'not_a'],
    ['B', 'I', 'not_a'], ['B', 'a'],
    ['C', 'not_a'], ['D', 'G', 'not_a'],
    ['D', 'H', 'not_a'], ['D', 'I', 'not_a'],
    ['D', 'a'], ['E', 'not_a'],
    ['F', 'G', 'not_a'], ['F', 'H', 'not_a'],
    ['F', 'I', 'not_a'], ['F', 'a']
]

results_tests = []


# GET

def post_secuencia():
    for a in arr:
        print(a)

        def waitForResourceAvailable(response, time):
            timer = 0
            while response.status_code == 400:
                time.sleep(10)
                timer += 10
                if timer > time:
                    break
                if response.status_code == 200:
                    break

        r = requests.post('http://localhost:3002/absenceCalculus/run', json={"test_id": a})
        waitForResourceAvailable(r, 10)
        # print(r.status_code)


def get_secuencia():
    global html
    global html_data
    html_data = []
    r = requests.get('http://localhost:3002/absenceCalculus/all')
    json_result = r.text
    data = json.loads(json_result)
    for d in data:
        x = json.dumps(d)
        w = json.loads(x)
        conditional = w.get('conditional')
        date = w.get('createdAt')
        result = w.get('result')
        fecha_hoy = str(date).startswith('2022-11-10')
        if fecha_hoy is True:
            df = pd.DataFrame({'Fecha de Prueba': [date], 'Condición': [conditional], 'Resultado': [result]})
            df = df.fillna(' ').T
            html = df.to_html()
            html_data.append(html)
    dia_hoy = str(datetime.datetime.now())
    f = open("SecuenciasABM.html", "w")
    f.write("<h1>Secuencias ABM</h1>"
            "<h4>Reporte generado: " + dia_hoy + "")
    for data in html_data:
        f.write(data)
        print(data)


get_secuencia()