from flask import Flask, Response

import json
import pymysql
import datetime

from datetime import datetime
from Compras import Compras

connection = pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   database="comercio")

cursor = connection.cursor()
app = Flask(__name__)


@app.route('/compras_usuario/<int:id>', methods=['GET'])
def extrato_cartao(id):
    vetor = []
    cursor.execute("SELECT pedidos.* FROM usuarios INNER JOIN pedidos ON pedidos.Id_usuario = usuarios.Id WHERE usuarios.Id = %s", (id))
    compras = cursor.fetchall()
    print(compras)
    for compra in compras:
      vetor.append(Compras(compra[0], datetime.strftime(compra[1], "%Y-%m-%d"), float(compra[2]), compra[3], compra[4], compra[5],
                           datetime.strftime(compra[6], "%Y-%m-%d"), datetime.strftime(compra[7], "%Y-%m-%d")).to_dict())

    return Response(response=json.dumps(vetor), status=200, content_type="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)