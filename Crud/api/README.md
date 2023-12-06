## Primeiro tem que cadastrar uma sessão:
1. SELECT * FROM sessoes;
2. INSERT INTO sessoes (1, 2017);

## Segundo tem que cadastrar um usuário porque o pedido precisa do usuário da sessão:
3. SELECT * FROM usuarios;
4. INSERT INTO usuarios (Id, Email, Nome, Sobrenome, Ativo)
VALUES (1, 'andreza@teste.com.br', 'Andreza', 'End', '1')

## Terceiro agora pode fazer um pedido para poder cadastrar uma transação
5. SELECT * FROM pedidos;
6. INSERT INTO pedidos(Id, Data_pedido, Total, Id_cupom, Id_sessao, Id_usuario)
VALUES(1, '2023-12-01', 100, NULL, 1, 1)

## Quarto agora FINALMENTE cadastrar uma transação 
7. SELECT * from transacao_cc;
8. INSERT INTO transacao_cc (Id, Codigo, Id_pedido, Data_transacao, Operador, Valor, Num_cc, Resposta) 
VALUES ('1', '1010', 1, '2023-12-01', 'Visa', 50, '5122030003177580', 'Sim');

INSERT INTO transacao_cc (Id, Codigo, Id_pedido, Data_transacao, Operador, Valor, Num_cc, Resposta) 
VALUES ('2', '1011', 1, '2023-12-02', 'Mastercard', 50, '5122030003177580', 'Sim');

INSERT INTO transacao_cc (Id, Codigo, Id_pedido, Data_transacao, Operador, Valor, Num_cc, Resposta) 
VALUES ('3', '1011', 1, '2023-12-02', 'Mastercard', 18, '5122030003177580', 'Sim');


