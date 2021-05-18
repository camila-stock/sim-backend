from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import request
import colas
import congruencial_lineal as cl  
import congruencial_multiplicativo as cm  
import full_random as fr
import exponencial as ex
import normal as nr
import montecarlo as mc
import uniforme_a_b as unif
import chi
import table as t
import file_writer
import json
app = Flask(__name__)
CORS(app)


@app.route('/colas-peluqueria', methods=["GET"])
@cross_origin()
def getColasPeluqueria():
    n = int(request.args.get('n'))
    tiempo = float(request.args.get('tiempo'))
    iteraciones = int(request.args.get('iteraciones'))
    hora_desde = float(request.args.get('hora_desde'))
    hora_hasta = float(request.args.get('hora_hasta'))
    fila = colas.colasPeluqueria(n, tiempo, iteraciones, hora_desde, hora_hasta)
    return jsonify({'res': fila})


@app.route('/montecarlo', methods=["GET"])
@cross_origin()
def getMontecarlo():
    n = int(request.args.get('n'))    
    probabilidad_venta_mujer = float(request.args.get('probabilidad_venta_mujer'))
    probabilidad_venta_hombre = float(request.args.get('probabilidad_venta_hombre'))
    probabilidad_1_subscripcion_mujer = float(request.args.get('probabilidad_1_subscripcion_mujer'))
    probabilidad_2_subscripcion_mujer = float(request.args.get('probabilidad_2_subscripcion_mujer'))
    probabilidad_3_subscripcion_mujer = float(request.args.get('probabilidad_3_subscripcion_mujer'))
    probabilidad_4_subscripcion_mujer = float(request.args.get('probabilidad_4_subscripcion_mujer'))
    probabilidad_1_subscripcion_hombre = float(request.args.get('probabilidad_1_subscripcion_hombre'))
    probabilidad_2_subscripcion_hombre = float(request.args.get('probabilidad_2_subscripcion_hombre'))
    probabilidad_3_subscripcion_hombre = float(request.args.get('probabilidad_3_subscripcion_hombre'))
    probabilidad_4_subscripcion_hombre = float(request.args.get('probabilidad_4_subscripcion_hombre'))
    probabilidad_puerta = float(request.args.get('probabilidad_puerta'))
    probabilidad_puerta_mujer = float(request.args.get('probabilidad_puerta_mujer'))
    probabilidad_puerta_hombre = float(request.args.get('probabilidad_puerta_hombre'))
    utilidad_vendedor = float(request.args.get('utilidad_vendedor'))
    headers = [
        "n", "rnd_puerta", "rnd_venta_hombre", "rnd_venta_mujer", "sub_hombre_1","sub_hombre_2","sub_hombre_3","sub_hombre_4","sub_mujer_1","sub_mujer_2","sub_mujer_3","sub_mujer_4", "utilidad", "utilidad_total", "subscripciones_total", "prob_venta", "promedio_suscrib_x_casa"
    ]
    row_santi = mc.montecarlo(n,
        probabilidad_venta_mujer,
        probabilidad_venta_hombre,
        probabilidad_1_subscripcion_mujer,
        probabilidad_2_subscripcion_mujer,
        probabilidad_3_subscripcion_mujer,
        probabilidad_4_subscripcion_mujer,
        probabilidad_1_subscripcion_hombre,
        probabilidad_2_subscripcion_hombre,
        probabilidad_3_subscripcion_hombre,
        probabilidad_4_subscripcion_hombre,
        probabilidad_puerta,
        probabilidad_puerta_mujer,
        probabilidad_puerta_hombre,
        utilidad_vendedor)
    file_writer.montecarlo(headers,row_santi)
    file_writer.montecarloMemoria(headers,row_santi)
    return jsonify({'res': row_santi})


@app.route('/uniforme-a-b', methods=["GET"])
@cross_origin()
def getUniform():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    n = int(request.args.get('n'))
    intervalos = int(request.args.get('intervalos'))
    data = unif.uniformAB(n, a, b, intervalos)
    table = t.table(data['data'])
    for i in range(0, len(data['data'])):
        data['data'][i].cota_superior = str(round(data['data'][i].cota_superior, 4))
        data['data'][i].cota_inferior = str(round(data['data'][i].cota_inferior, 4))
        data['data'][i] = json.dumps(data['data'][i].__dict__)
    for i in range(0,len(table)):
        table[i].intervalo = str(table[i].intervalo)
        table[i] = json.dumps(table[i].__dict__)
    file_writer.numbers(data['numbers'])
    return jsonify({'chart': data['data'], 'table': table, 'numbers': data['numbers']})

@app.route('/exponencial', methods=["GET"])
@cross_origin()
def getExponent():
    n = int(request.args.get('n'))
    lambd = float(request.args.get('lambda'))
    intervalos = int(request.args.get('intervalos'))
    data = ex.exponencial(n, lambd, intervalos)
    table = t.tableExponencial(data['data'], lambd)
    for i in range(0,len(data['data'])):
        data['data'][i].cota_superior = str(round(data['data'][i].cota_superior, 4))
        data['data'][i].cota_inferior = str(round(data['data'][i].cota_inferior, 4))
        data['data'][i] = json.dumps(data['data'][i].__dict__)
    for i in range(0,len(table)):
        table[i].intervalo = str(table[i].intervalo)
        table[i] = json.dumps(table[i].__dict__)
    file_writer.numbers(data['numbers'])
    return jsonify({'chart': data['data'], 'table': table, 'numbers': data['numbers']})

@app.route('/normal', methods=["GET"])
@cross_origin()
def getNormal():
    n = int(request.args.get('n'))
    media = int(request.args.get('media'))
    desviacion = int(request.args.get('desviacion'))
    intervalos = int(request.args.get('intervalos'))
    data = nr.normal(n, media, desviacion, intervalos)
    table = t.tableNormal(data['data'],media, n, desviacion)
    for i in range(0,len(data['data'])):
        data['data'][i].cota_superior = str(round(data['data'][i].cota_superior,4))
        data['data'][i].cota_inferior = str(round(data['data'][i].cota_inferior, 4))
        data['data'][i] = json.dumps(data['data'][i].__dict__)
    for i in range(0,len(table)):
        table[i].intervalo = str(table[i].intervalo)
        table[i] = json.dumps(table[i].__dict__)
    file_writer.numbers(data['numbers'])
    return jsonify({'chart': data['data'], 'table': table, 'numbers': data['numbers']})


@app.route('/congruencial-lineal', methods=["GET"])
@cross_origin()
def getLinear():
    n = int(request.args.get('n'))
    x = int(request.args.get('x'))
    k = int(request.args.get('k'))
    g = int(request.args.get('g'))
    c = int(request.args.get('c'))
    intervalos = int(request.args.get('intervalos'))
    data = cl.linearMethod(n,x,k,c,g, intervalos)
    chi_data = chi.chiMethod(data['data'])
    for i in range(0,len(data['data'])):
        data['data'][i] = json.dumps(data['data'][i].__dict__)
    for i in range(0,len(chi_data)):
        chi_data[i] = json.dumps(chi_data[i].__dict__)
    file_writer.numbers(data['numbers'])
    return jsonify({'chart': data['data'], 'table': chi_data, 'numbers': data['numbers']})

@app.route('/congruencial-multiplicativo', methods=["GET"])
@cross_origin()
def getMultiplicative():
    n = int(request.args.get('n'))
    x = int(request.args.get('x'))
    k = int(request.args.get('k'))
    g = int(request.args.get('g'))
    intervalos = int(request.args.get('intervalos'))
    data = cm.multiplicativeMethod(n,x,k,g, intervalos)
    chi_data = chi.chiMethod(data['data'])
    for i in range(0,len(data['data'])):
        data['data'][i] = json.dumps(data['data'][i].__dict__)
    for i in range(0,len(chi_data)):
        chi_data[i] = json.dumps(chi_data[i].__dict__)
    file_writer.numbers(data['numbers'])
    return jsonify({'chart': data['data'], 'table': chi_data, 'numbers': data['numbers']})

@app.route('/full-random', methods=["GET"])
@cross_origin()
def getRandom():
    n = int(request.args.get('n'))
    intervalos = int(request.args.get('intervalos'))
    data = fr.fullRandomMethod(n, intervalos)
    chi_data = chi.chiMethod(data['data'])
    for i in range(0,len(data['data'])):
        data['data'][i] = json.dumps(data['data'][i].__dict__)
    for i in range(0,len(chi_data)):
        chi_data[i] = json.dumps(chi_data[i].__dict__)
    file_writer.numbers(data['numbers'])
    return jsonify({'chart': data['data'], 'table': chi_data, 'numbers': data['numbers']})


@app.route('/histogram', methods=["GET"])
@cross_origin()
def hello():
    data = [
        ['Dinosaur', 'Length'],
        ['Acrocanthosaurus (top-spined lizard)', 12.2],
        ['Albertosaurus (Alberta lizard)', 9.1],
        ['Allosaurus (other lizard)', 12.2],
        ['Apatosaurus (deceptive lizard)', 22.9],
        ['Archaeopteryx (ancient wing)', 0.9],
        ['Argentinosaurus (Argentina lizard)', 36.6],
        ['Baryonyx (heavy claws)', 9.1],
        ['Brachiosaurus (arm lizard)', 30.5],
        ['Ceratosaurus (horned lizard)', 6.1],
        ['Coelophysis (hollow form)', 2.7],
        ['Compsognathus (elegant jaw)', 0.9],
        ['Deinonychus (terrible claw)', 2.7],
        ['Diplodocus (double beam)', 27.1],
        ['Dromicelomimus (emu mimic)', 3.4],
        ['Gallimimus (fowl mimic)', 5.5],
        ['Mamenchisaurus (Mamenchi lizard)', 21.0],
        ['Megalosaurus (big lizard)', 7.9],
        ['Microvenator (small hunter)', 1.2],
        ['Ornithomimus (bird mimic)', 4.6],
        ['Oviraptor (egg robber)', 1.5],
        ['Plateosaurus (flat lizard)', 7.9],
        ['Sauronithoides (narrow-clawed lizard)', 2.0],
        ['Seismosaurus (tremor lizard)', 45.7],
        ['Spinosaurus (spiny lizard)', 12.2],
        ['Supersaurus (super lizard)', 30.5],
        ['Tyrannosaurus (tyrant lizard)', 15.2],
        ['Ultrasaurus (ultra lizard)', 30.5],
        ['Velociraptor (swift robber)', 1.8]]
    return jsonify(data)


if __name__ == '__main__':
    app.run()
