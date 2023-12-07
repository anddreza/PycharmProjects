class Compras:
    def __init__(self, id, data_pedido, total, id_cupom, id_sessao, id_usuario, criado_em, alterado_em):
        self.id = id
        self.data_pedido = data_pedido
        self.total = total
        self.id_cupom = id_cupom
        self.id_sessao = id_sessao
        self.id_usuario = id_usuario
        self.criado_em = criado_em
        self.alterado_em = alterado_em



    def to_dict(self):
        return {"id": self.id, "data_pedido": self.data_pedido, "total": self.total, "id_cupom": self.id_cupom,
                "id_sessao": self.id_sessao, "id_usuario": self.id_usuario,
                "criado_em": self.criado_em, "alterado_em": self.alterado_em}