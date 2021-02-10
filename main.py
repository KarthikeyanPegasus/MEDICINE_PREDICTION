import json
import ast
import pickle
from flask import Flask, request, jsonify
from model_files.ml_model import dosage_prediction

app = Flask("dosage_prediction")

@app.route('/',methods = ['POST'])
def predict():
    detai = (request.get_json())
    print(detai)
    de = json.dumps(detai)
    print(de)
    detail = json.loads(de)
    print(detail)
    deta = detail["list"]
    print(deta)
    details = ast.literal_eval(deta)
    print(details, type(details))
    pre = []
    pre.append(details[0])
    pre.append(details[1])
    prediction = list([pre])
    print(prediction)

    with open('./model_files/dosage_prediction.bin', 'rb') as f_in:
        dosemodel = pickle.load(f_in)
        f_in.close()

    dosepredict = dosemodel.predict(prediction)

    dosage = dosepredict[0]
    clmname = ["morning","afternoon","night","totalmedicin1","totalmedicine2","avoid","take"]

    response = {clmname[i]: dosage[i] for i in range(len(clmname))}


    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host = '127.0.0.1', port = 8080)
