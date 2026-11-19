
# Devolutiva formativa — Atividade 02 da SA

**Estudante:** Matheus Henrique Brey  
**Turma:** Rio Negrinho — Manhã  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** EuComida — Delivery  
**Atividade:** Interface funcional  
**Arquivos analisados:** `interface/index.html` e `codigo/app.py`

## O que você já conseguiu desenvolver

Matheus, você criou uma interface web com diferentes funcionalidades relacionadas a um sistema de delivery.

O projeto apresenta cadastro, login demonstrativo, cardápio, carrinho e opções de pagamento simulado.

Pontos positivos identificados:

- Criou formulários para cadastro e entrada de usuários.
- Organizou produtos em categorias.
- Desenvolveu recursos para aumentar e diminuir quantidades.
- Implementou atualização dos valores do carrinho.
- Criou funções para calcular subtotal e taxa de entrega.
- Implementou diferentes formas de pagamento demonstrativas.
- Incluiu validações de campos obrigatórios.
- Utilizou JavaScript para controlar as ações e atualizar os elementos da página.
- Aplicou funções reutilizáveis para cálculos e atualização dos resultados.
- Utilizou `localStorage` para armazenar determinadas informações.
- Criou uma interface com diferentes telas e componentes interativos.

## Comparação com a devolutiva anterior

### 1. Interface interativa — ATENDIDO

A avaliação anterior reconheceu as funcionalidades existentes no Python.

Agora essas operações foram representadas em uma interface web que permite interação por meio de botões e formulários.

### 2. Organização das funções — PARCIALMENTE ATENDIDO

O JavaScript possui funções para cálculos, operações de carrinho e atualização da tela.

Entretanto, grande parte do HTML, CSS e JavaScript permanece concentrada em `interface/index.html`.

**Como melhorar:** distribuir o CSS em `style.css` e o JavaScript em `script.js`.

### 3. Segurança das senhas — PENDENTE

A devolutiva anterior recomendou evitar o armazenamento de senhas em texto simples.

Na interface atual, os dados de login ainda são armazenados e comparados diretamente no navegador.

**Como melhorar:** manter esse recurso identificado como demonstração educacional. Quando houver autenticação real, realizar a verificação no servidor e utilizar mecanismos apropriados de proteção.

### 4. Identificação das simulações de pagamento — PARCIALMENTE ATENDIDO

A interface apresenta diferentes formas de pagamento, mas algumas mensagens podem ser interpretadas como confirmação real.

**Como melhorar:** informar claramente que os pagamentos são simulados e utilizar apenas dados fictícios.

## O que precisa ser corrigido

### 5. Não solicitar dados reais de cartão

A interface possui campos de número, validade e código de segurança do cartão.

**Como melhorar:** substituir a coleta de dados de cartão por uma seleção demonstrativa, sem solicitar informações financeiras reais.

### 6. Melhorar a separação dos arquivos

O arquivo HTML possui uma implementação extensa, incluindo estilos e JavaScript.

**Como melhorar:** separar a apresentação, os estilos e as interações em arquivos próprios. Isso facilita a leitura e a manutenção.

### 7. Melhorar a integração com o Python

As ações da interface utilizam principalmente JavaScript e armazenamento local.

**Como melhorar:** documentar se a interface web é uma simulação independente ou se será conectada posteriormente à lógica do Python.

## Oportunidades de melhoria

### 8. Ampliar os testes

**Como melhorar:** verificar os valores do carrinho, os limites das quantidades, a aplicação da taxa de entrega e o comportamento das diferentes opções de pagamento.

### 9. Melhorar a documentação

**Como melhorar:** explicar o funcionamento da interface, a utilização do `localStorage` e os recursos que ainda são demonstrativos.

### 10. Revisar a apresentação dos valores monetários

**Como melhorar:** conferir arredondamentos, parcelas e valores exibidos no carrinho. A futura integração deverá manter os cálculos centralizados.

## Testes recomendados

1. Cadastrar um usuário fictício.
2. Testar entradas inválidas no formulário.
3. Realizar um login demonstrativo.
4. Adicionar produtos de categorias diferentes.
5. Aumentar e diminuir quantidades.
6. Conferir subtotal, taxa e total.
7. Alternar entre entrega e retirada.
8. Simular pagamento em dinheiro com troco.
9. Verificar as mensagens de Pix e cartão simulados.
10. Atualizar a página e conferir os dados armazenados.

## Prioridades para a próxima versão

1. **Separar HTML, CSS e JavaScript.**
2. **Não coletar informações reais de cartão.**
3. **Identificar os pagamentos como simulações.**
4. **Revisar a proteção dos dados de login.**
5. **Documentar a relação entre a interface e o Python.**

## Mensagem final

Matheus, sua interface demonstra conhecimento de eventos, funções, manipulação de elementos HTML e cálculos relacionados ao delivery.

Você conseguiu transformar diferentes etapas do sistema em recursos interativos.

Continue aprimorando a organização do código, a clareza das simulações e a proteção das informações utilizadas.
