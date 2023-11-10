import jwt

# Dados do cabeçalho
header = {
    "alg": "HS256",
    "type": "JWT"
}
# dados do payload

payload = {
    "id": "47563423423",
    "name": "Andreza Silva",
    "phone": "47 99109 1234",
    "address": "Rua dos Imigrantes",
    "work": "Universidade Católica"
}

#chave secreta
#exemplo de senha "segura"
secret = "Catolica2023"

token = jwt.encode(payload, secret, algorithm=header["alg"])

print(token)

print(jwt.decode(token, secret, algorithms="HS256"))