from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def alo_mundo():
    msg = "Alo mundo"
    return msg

@app.route("/numero_informado")
def numero_informado():
    num = input("Informe um numero")
    return num

@app.route("/dois_numeros")
def dois_numeros():
    a = int(input("Digite o primeiro numero: "))
    b = int(input("Digite o segundo numero: "))
    soma = a + b

    return f" {soma}"

@app.route("/notas_bimestrais")
def notas_bimestrais():
    a = int(input("Digite a primeira nota: "))
    b = int(input("Digite a segunda nota: "))
    c = int(input("Digite a terceira  nota: "))
    d = int(input("Digite a quarta nota: "))

    media = (a + b + c + d) / 4
    return f" {media}"

@app.route("/metros_centimetros")
def metros_centimetros():
    a = int(input("Digite os metros: "))
    cent = a * 100
    return f" {cent}"

@app.route("/area_circulo")
def area_circulo():
    a = int(input("Digite a área do circulo: "))
    area = (a * a) * 3.14
    return f" {area}"

@app.route("/area_quadrado_dobro")
def area_quadrado_dobro():
    a = int(input("Digite a área do quadrado "))
    area_quadrado = a * a
    area2 = area_quadrado * 2

    return jsonify("F: ", area_quadrado, area2)

@app.route("/valor_salario")
def valor_salario():
    a_hora = int(input("Quanto você ganha por hora: "))
    a_numero_hora_trabalhada = int(input("Quantas horas você trabalhou: "))
    salario_valor = a_hora * a_numero_hora_trabalhada
    return f" {salario_valor}"

@app.route("/farenheit_celsius")
def farenheit_celsius():
    F_float = float(input("Digite a temperatura em Farenheit: "))
    C = (5 * (F_float - 32) / 9)
    return f" {C}"

app.route("/celsius_farenheit")
def celsius_farenheit():
    F = float(input('Digite a temperatura em Celsius: '))
    C = (F - 32) * (5 / 9)

    return f" {C}"



#função principal
if __name__ == '__main__':
    app.run(debug=True, port=3000)
