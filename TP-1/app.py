from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import request
import congruencial_lineal as cl  
import congruencial_multiplicativo as cm  
import full_random as fr  
import chi 
import json
app = Flask(__name__)
CORS(app)

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
    chi_data = chi.chiMethod(data)
    for i in range(0,len(data)):
        data[i] = json.dumps(data[i].__dict__)
    for i in range(0,len(chi_data)):
        chi_data[i] = json.dumps(chi_data[i].__dict__)
    return jsonify({'chart': data, 'table': chi_data})

@app.route('/congruencial-multiplicativo', methods=["GET"])
@cross_origin()
def getMultiplicative():
    n = int(request.args.get('n'))
    x = int(request.args.get('x'))
    k = int(request.args.get('k'))
    g = int(request.args.get('g'))
    intervalos = int(request.args.get('intervalos'))
    data = cm.multiplicativeMethod(n,x,k,g, intervalos)
    chi_data = chi.chiMethod(data)
    for i in range(0,len(data)):
        data[i] = json.dumps(data[i].__dict__)
    for i in range(0,len(chi_data)):
        chi_data[i] = json.dumps(chi_data[i].__dict__)
    return jsonify({'chart': data, 'table': chi_data})

@app.route('/full-random', methods=["GET"])
@cross_origin()
def getRandom():
    n = int(request.args.get('n'))
    intervalos = int(request.args.get('intervalos'))
    data = fr.fullRandomMethod(n, intervalos)
    chi_data = chi.chiMethod(data)
    for i in range(0,len(data)):
        data[i] = json.dumps(data[i].__dict__)
    for i in range(0,len(chi_data)):
        chi_data[i] = json.dumps(chi_data[i].__dict__)
    return jsonify({'chart': data, 'table': chi_data})


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
