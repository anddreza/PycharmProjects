class ProdutoTag:
    def __init__(self, id, cod_barras, nome, descricao, id_status_produto, preco_normal, preco_com_desconto, quantidade, criado_em, alterado_em):
        self.id = id
        self.cod_barras = cod_barras
        self.nome = nome
        self.descricao = descricao
        self.id_status_produto = id_status_produto
        self.preco_normal = preco_normal
        self.preco_com_desconto = preco_com_desconto
        self.quantidade = quantidade
        self.criado_em = criado_em
        self.alterado_em = alterado_em

    def to_dict(self):
        return {"id": self.id,
                "cod_barras": self.cod_barras,
                "nome": self.nome,
                "descricao": self.descricao,
                "id_status_produto": self.id_status_produto,
                "preco_normal": self.preco_normal,
                "preco_com_desconto": self.preco_com_desconto,
                "quantidade": self.quantidade,
                "criado_em": self.criado_em,
                "alterado_em": self.alterado_em}
