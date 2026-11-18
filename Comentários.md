
# Devolutiva formativa — Atividade 01 da SA

**Estudante:** Matheus Brey  
**Turma:** Rio Negrinho — Manhã  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** Delivery de Comida — EuComida / Cantina do Zé  
**Código analisado:** `codigo/app.py`  
**Referência:** Situação de Aprendizagem nº 1 — *Da Ideia ao Código*

## O que você já conseguiu desenvolver

Matheus, você desenvolveu uma aplicação de delivery com cadastro, login, cardápio, carrinho, pagamento simulado e acompanhamento de pedidos. O projeto demonstra compreensão de diferentes regras de negócio e de como organizar uma sequência de operações.

Pontos positivos identificados:

- Organizou o código em funções como `entrar()`, `cadastrar()`, `cardapio()`, `ver_carrinho()`, `pagar()`, `finalizar()` e `acompanhar()`.
- Utilizou **listas e dicionários** para representar produtos, usuários, carrinho e histórico de pedidos.
- Criou categorias para organizar o cardápio.
- Implementou regras de pedido mínimo, taxa de entrega e frete grátis.
- Permitiu adicionar produtos ao carrinho e remover unidades.
- Criou diferentes opções de pagamento simulado.
- Implementou etapas de acompanhamento do pedido.
- Utilizou **condicionais, repetições, funções e tratamento de entradas numéricas**.
- Incluiu comentários que identificam as funcionalidades.

## O que precisa ser corrigido

### 1. Proteger as senhas dos usuários

O cadastro armazena as senhas diretamente no dicionário `usuarios`, sem proteção. O programa também exige que a senha contenha somente letras, mas essa regra não torna a autenticação mais segura.

**Como melhorar:** utilizar uma função apropriada para gerar hashes de senha e outra para verificar as credenciais no login. Evitar guardar senhas em texto simples.

### 2. Identificar os pagamentos como simulações

Na opção de Pix, o programa informa que o pagamento foi confirmado após o usuário pressionar Enter. Na opção de cartão, basta informar 16 dígitos para apresentar uma mensagem de aprovação.

Essas operações não verificam pagamentos reais.

**Como melhorar:** identificar claramente essas telas como simulações educacionais. Utilizar somente informações fictícias e não solicitar dados reais de cartão. Uma integração de pagamento exigiria mecanismos próprios, que não fazem parte da Atividade 01.

### 3. Melhorar a identificação dos pedidos

O programa utiliza `random.randint(1000, 9999)` para gerar números de pedido. Isso não garante que dois pedidos diferentes receberão identificadores exclusivos.

**Como melhorar:** utilizar um contador sequencial para a versão inicial ou outro mecanismo que assegure a identificação única.

## Oportunidades de melhoria

### 4. Diferenciar simulação de acompanhamento em tempo real

A função `acompanhar()` apresenta etapas do pedido após intervalos de tempo definidos no código. Isso é útil para demonstrar o fluxo, mas não representa uma atualização real da entrega.

**Como melhorar:** indicar que se trata de uma simulação e, futuramente, controlar as etapas por alterações explícitas de situação.

### 5. Melhorar o tratamento dos dados monetários

Os preços e totais são calculados com `float`, o que pode produzir pequenas diferenças de precisão em operações financeiras.

**Como melhorar:** considerar o uso de `Decimal` ou valores em centavos. Para a versão inicial, conferir cuidadosamente os cálculos e a apresentação dos resultados.

### 6. Modularizar o programa

O código apresenta várias funções com responsabilidades reconhecíveis, mas concentra todas elas em um único arquivo.

**Como melhorar:** separar gradualmente autenticação, cardápio, carrinho, pedidos e pagamentos simulados. Centralizar as regras de valores e validações.

### 7. Melhorar a documentação e a verificação do código

O README ainda contém principalmente as instruções gerais da atividade.

**Como melhorar:** incluir as instruções de execução, as funcionalidades do EuComida, as regras do pedido mínimo e as limitações das simulações. Registrar os resultados de testes com entradas válidas e inválidas.

## Testes recomendados

1. Cadastrar um usuário e testar o login.
2. Tentar cadastrar um usuário já existente.
3. Selecionar produtos de categorias diferentes.
4. Adicionar e remover quantidades do carrinho.
5. Tentar finalizar um pedido abaixo do valor mínimo.
6. Conferir o cálculo do frete grátis.
7. Testar as três opções de pagamento simulado.
8. Verificar o histórico após concluir pedidos.
9. Confirmar que dois pedidos possuem identificadores diferentes.
10. Verificar as etapas simuladas de acompanhamento.

## Prioridades para a próxima versão

1. **Corrigir o armazenamento das senhas.**
2. **Identificar claramente os pagamentos como simulações.**
3. **Garantir identificadores únicos para os pedidos.**
4. **Revisar os cálculos monetários e o controle das situações.**
5. **Complementar a documentação e criar testes das regras principais.**

## Mensagem final

Matheus, seu trabalho demonstra compreensão de **funções, listas, dicionários, validação de entradas e regras de negócio**. Você conseguiu desenvolver um fluxo de delivery com várias etapas relacionadas.

Continue aprimorando principalmente a segurança das informações, a clareza das simulações e a confiabilidade dos cálculos. Você já possui uma boa base para desenvolver as próximas funcionalidades do sistema.
