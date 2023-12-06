from flask import Flask, Response

import json
import pymysql
import datetime

from datetime import datetime
from Extrato import Extrato

connection = pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   database="comercio")

cursor = connection.cursor()
app = Flask(__name__)

# Customers list
customers = []


@app.route('/extrato_cartao/<int:codigo>', methods=['GET'])
def extrato_cartao(codigo):
    vetor = []
    cursor.execute("SELECT * FROM transacao_cc WHERE codigo = %s", (codigo))
    extratos = cursor.fetchall()
    for extrato in extratos:
      vetor.append(Extrato(extrato[0], extrato[1], extrato[2], datetime.strftime(extrato[3], "%Y-%m-%d"), extrato[4], float(extrato[5]), extrato[6], extrato[7],
                           datetime.strftime(extrato[8], "%Y-%m-%d"), datetime.strftime(extrato[9], "%Y-%m-%d")).to_dict())

    return Response(response=json.dumps(vetor), status=200, content_type="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)