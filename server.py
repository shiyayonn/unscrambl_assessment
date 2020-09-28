import json

from flask import Flask
from flask import jsonify
from methods import *

app = Flask(__name__)



@app.route("/assignment/transaction/<int:id>")
def getTransactionById(id):
    
    data = {}
    record = TransactionById(id)
    if(record == False):
        return jsonify({"Message":"No record was found"}), 404
    
    return record,200

@app.route("/assignment/transactionSummaryByProducts/<int:last_n_days>")
def getTransactionSummaryByProducts(last_n_days):
    
    data = {}
    record = TransactionSummaryByProductsByDays(last_n_days)
    
    if(record == False):
        return jsonify({"Message":"No record was found"}), 404
    
    return jsonify(summary=json.loads(record)),200   


@app.route("/assignment/transactionSummaryByManufacturingCity/<int:last_n_days>")
def getTransactionSummaryByManufacturingCity(last_n_days):
    
    data = {}
    record = TransactionSummaryByManufacturingCityByDays(last_n_days)
    
    if(record == False):
        return jsonify({"Message":"No record was found"}), 404
    
    return jsonify(summary=json.loads(record)),200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)