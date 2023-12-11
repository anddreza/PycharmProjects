class Extrato:
    def __init__(self, id, codigo, id_pedido, data_transacao, operador, valor, num_cc, resposta, criado_em, alterado_em):
        self.id = id
        self.codigo = codigo
        self.id_pedido = id_pedido
        self.data_transacao = data_transacao
        self.operador = operador
        self.valor = valor
        self.num_cc = num_cc
        self.resposta = resposta
        self.criado_em = criado_em
        self.alterado_em = alterado_em


    def to_dict(self):
        return {"id": self.id, "codigo": self.codigo, "id_pedido": self.id_pedido, "data_transacao": self.data_transacao,
                "operador": self.operador, "valor": self.valor, "num_cc": self.num_cc, "resposta": self.resposta,
                "criado_em": self.criado_em, "alterado_em": self.alterado_em}