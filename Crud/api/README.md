# Instruções para executar extrato_do_cartao_de_credito.py 

### Primeiro tem que cadastrar uma sessão:
1. SELECT * FROM sessoes;
2. INSERT INTO sessoes (1, 2017);

### Segundo tem que cadastrar um usuário porque o pedido precisa do usuário da sessão:
3. SELECT * FROM usuarios;
4. INSERT INTO usuarios (Id, Email, Nome, Sobrenome, Ativo)
VALUES (1, 'andreza@teste.com.br', 'Andreza', 'End', '1')

### Terceiro agora pode fazer um pedido para poder cadastrar uma transação
5. SELECT * FROM pedidos;
6. INSERT INTO pedidos(Id, Data_pedido, Total, Id_cupom, Id_sessao, Id_usuario)
VALUES(1, '2023-12-01', 100, NULL, 1, 1)

### Quarto agora FINALMENTE cadastrar uma transação 
7. SELECT * from transacao_cc;

8. 
```
INSERT INTO transacao_cc (Id, Codigo, Id_pedido, Data_transacao, Operador, Valor, Num_cc, Resposta) 
VALUES ('1', '1010', 1, '2023-12-01', 'Visa', 50, '5122030003177580', 'Sim');

INSERT INTO transacao_cc (Id, Codigo, Id_pedido, Data_transacao, Operador, Valor, Num_cc, Resposta) 
VALUES ('2', '1011', 1, '2023-12-02', 'Mastercard', 50, '5122030003177580', 'Sim');

INSERT INTO transacao_cc (Id, Codigo, Id_pedido, Data_transacao, Operador, Valor, Num_cc, Resposta) 
VALUES ('3', '1011', 1, '2023-12-02', 'Mastercard', 18, '5122030003177580', 'Sim');
```
# Instruções para executar listagem_deprodutos_por_tag.py
1. SELECT * from tags;
2. 
```
   INSERT INTO tags(Id, Nome) VALUES (1, 'Eletrodomesticos')
   INSERT INTO tags(Id, Nome) VALUES (2, 'Lar')
   INSERT INTO tags(Id, Nome) VALUES (3, 'Jardim')
   INSERT INTO tags(Id, Nome) VALUES (4, 'Roupas')
   INSERT INTO tags(Id, Nome) VALUES (5, 'Decoração')
```

3. SELECT * from produtos;
```   
INSERT INTO produtos(Id, Cod_barras, Nome, Descricao, Id_status_produto, Preco_normal, Preco_com_desconto, Quantidade) 
VALUES (2, '1212', 'Geladeira', 'Geladeira grande', 1, 2999, NULL, 2)

INSERT INTO produtos(Id, Cod_barras, Nome, Descricao, Id_status_produto, Preco_normal, Preco_com_desconto, Quantidade) 
VALUES (3, '1213', 'Flor', 'Girassol', 1, 15, 13, 1)

INSERT INTO produtos(Id, Cod_barras, Nome, Descricao, Id_status_produto, Preco_normal, Preco_com_desconto, Quantidade) 
VALUES (4, '1214', 'Calcinha', 'Calcinha grande, pequena, media', 1, 40, NULL, 1)
```
4. SELECT * from produtos_tags ;
- Para essa inserção é necessário o id_produto e o id_tag
```
INSERT INTO produtos_tags(Id_produto, Id_tag)
VALUES (2, 1)

INSERT INTO produtos_tags(Id_produto, Id_tag)
VALUES (3, 3)

INSERT INTO produtos_tags(Id_produto, Id_tag)
VALUES (4, 4)
```
5. Para organizar e verificar o Id e a Tag necessário realizar um JOIN
```
SELECT produtos.Id, tags.Nome 
FROM produtos
INNER JOIN produtos_tags 
ON produtos.Id = produtos_tags.Id_produto 
INNER JOIN tags 
ON tags.Id = produtos_tags.Id_tag 
