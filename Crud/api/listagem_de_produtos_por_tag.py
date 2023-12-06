from flask import Flask, Response

import json
import pymysql
import datetime

from datetime import datetime
from ProdutoTag import ProdutoTag

connection = pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   database="comercio")

cursor = connection.cursor()
app = Flask(__name__)

# Customers list
customers = []

@app.route('/produto_tag/<int:id_tag>', methods=['GET'])
def produto_tag(id_tag):
    vetor = []
    cursor.execute("SELECT produtos.* "
                         "FROM produtos " 
                         "INNER JOIN produtos_tags ON produtos.Id = produtos_tags.Id_produto "
                         "INNER JOIN tags ON tags.Id = produtos_tags.Id_tag "
                         "WHERE tags.Id = %s", (id_tag))
    produtos = cursor.fetchall()
    print(produtos)
    for produto in produtos:
      vetor.append(ProdutoTag(produto[0],
                              produto[1],
                              produto[2],
                              produto[3],
                              produto[4],
                              float(produto[5]),
                              produto[6],
                              produto[7],
                              datetime.strftime(produto[8], "%Y-%m-%d"),
                              datetime.strftime(produto[9], "%Y-%m-%d")).to_dict())
    return Response(response=json.dumps(vetor), status=200, content_type="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)