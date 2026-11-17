import os
import random
import time

# ---------- Configurações da loja ----------
TAXA = 6
FRETE_GRATIS = 60
MINIMO = 20

MENU = [
    {"id": 1,  "cat": "Lanches",    "nome": "X-Burger da Casa",     "preco": 28.90},
    {"id": 2,  "cat": "Lanches",    "nome": "Hot Dog Duplo",        "preco": 19.90},
    {"id": 3,  "cat": "Lanches",    "nome": "Sanduíche de Frango",  "preco": 22.50},
    {"id": 4,  "cat": "Pratos",     "nome": "Macarrão à Bolonhesa", "preco": 34.90},
    {"id": 5,  "cat": "Pratos",     "nome": "Prato Feito Completo", "preco": 32.00},
    {"id": 6,  "cat": "Pratos",     "nome": "Camarão ao Alho",      "preco": 49.90},
    {"id": 7,  "cat": "Pizzas",     "nome": "Pizza Margherita",     "preco": 44.00},
    {"id": 8,  "cat": "Pizzas",     "nome": "Pizza Calabresa",      "preco": 46.00},
    {"id": 9,  "cat": "Bebidas",    "nome": "Refrigerante Lata",    "preco": 6.00},
    {"id": 10, "cat": "Bebidas",    "nome": "Suco Natural",         "preco": 9.00},
    {"id": 11, "cat": "Sobremesas", "nome": "Pudim de Leite",       "preco": 12.00},
    {"id": 12, "cat": "Sobremesas", "nome": "Brownie com Sorvete",  "preco": 18.00},
]

ETAPAS = [
    "Pedido recebido pela Cantina do Zé",
    "Em preparo na cozinha",
    "Saiu para entrega",
    "Entregue. Bom apetite!",
]


# ---------- Funções de apoio ----------
def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def pausa():
    input("\nEnter para continuar...")


def real(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def ler_numero(texto):
    valor = input(texto).strip()
    return int(valor) if valor.isdigit() else None


def buscar(id_prato):
    for prato in MENU:
        if prato["id"] == id_prato:
            return prato
    return None


def subtotal(carrinho):
    return sum(buscar(i)["preco"] * q for i, q in carrinho.items())


def taxa(carrinho):
    return 0 if subtotal(carrinho) >= FRETE_GRATIS else TAXA


# ---------- Login e cadastro ----------
def entrar(usuarios):
    email = input("Informe seu email ou user\n login: ")
    senha = input("Informe sua senha\n senha: ")
    if usuarios.get(email) == senha:
        print("Login realizado!")
        pausa()
        return email          # devolve quem entrou
    print("Email ou senha incorretos")
    pausa()
    return None


def cadastrar(usuarios):
    email = input("Informe seu email\n email: ")
    if email in usuarios:
        print("Esse email já está cadastrado")
        pausa()
        return

    print("A senha deve conter apenas letras")
    senha = input("Informe a senha\n senha: ")
    while not senha.isalpha():
        print("A senha deve conter apenas letras")
        senha = input("Informe a senha\n senha: ")

    confirmar = input("Informe novamente a senha\n senha: ")
    while confirmar != senha:
        print("As senhas não coincidem")
        confirmar = input("Informe novamente a senha\n senha: ")

    usuarios[email] = senha
    print("Cadastro completo")
    pausa()


# ---------- Cardápio ----------
def cardapio(carrinho):
    categorias = ["Todos"] + list(dict.fromkeys(p["cat"] for p in MENU))
    limpar()
    print("--Cardápio: Cantina do Zé--")
    for n, c in enumerate(categorias, start=1):
        print(f"  {n}-{c}")
    escolha = ler_numero("  categoria: ")
    if escolha is None or not 1 <= escolha <= len(categorias):
        print("Inválido")
        pausa()
        return
    cat = categorias[escolha - 1]

    while True:
        limpar()
        print(f"--{cat}--")
        for p in MENU:
            if cat == "Todos" or p["cat"] == cat:
                print(f"  {p['id']:>2} - {p['nome']:<24} {real(p['preco'])}")
        print("\n  Digite o número do prato (0 para voltar)")
        id_prato = ler_numero("  prato: ")
        if id_prato == 0:
            return
        prato = buscar(id_prato) if id_prato else None
        if prato is None:
            print("Prato inválido")
            pausa()
            continue
        qtd = ler_numero("  quantidade: ")
        if not qtd:
            print("Quantidade inválida")
            pausa()
            continue
        carrinho[prato["id"]] = carrinho.get(prato["id"], 0) + qtd
        print(f"{qtd}x {prato['nome']} adicionado(s)!")
        pausa()


# ---------- Carrinho ----------
def mostrar_resumo(carrinho):
    for i, q in carrinho.items():
        p = buscar(i)
        print(f"  {i:>2} - {q}x {p['nome']:<24} {real(p['preco'] * q)}")
    t = taxa(carrinho)
    print(f"\n  Subtotal: {real(subtotal(carrinho))}")
    print(f"  Entrega:  {real(t) if t else 'Grátis'}")
    print(f"  Total:    {real(subtotal(carrinho) + t)}")


def ver_carrinho(carrinho):
    while True:
        limpar()
        print("--Seu carrinho--")
        if not carrinho:
            print("  Carrinho vazio")
            pausa()
            return
        mostrar_resumo(carrinho)
        print("\n  Digite o número de um prato para remover 1 unidade (0 para voltar)")
        id_prato = ler_numero("  remover: ")
        if id_prato == 0:
            return
        if id_prato in carrinho:
            carrinho[id_prato] -= 1
            if carrinho[id_prato] <= 0:
                del carrinho[id_prato]


# ---------- Pagamento ----------
def pagar(total):
    """Devolve o nome da forma de pagamento, ou None se cancelar."""
    print("\n--Pagamento--")
    print("  1-Pix\n  2-Cartão\n  3-Dinheiro\n  0-Cancelar")
    opcao = input("  digite: ").strip()

    match opcao:
        case "1":
            print("\n  Chave Pix: cantinadoze@pix.com")
            print(f"  Valor: {real(total)}")
            input("  Pague e aperte Enter para confirmar...")
            print("  Pagamento via Pix confirmado!")
            return "Pix"
        case "2":
            numero = input("  número do cartão (16 dígitos): ").replace(" ", "")
            if not (numero.isdigit() and len(numero) == 16):
                print("  Cartão inválido")
                return None
            print(f"  Cartão final {numero[-4:]} aprovado!")
            return "Cartão"
        case "3":
            texto = input("  troco para quanto? (ex: 100): ").replace(",", ".")
            try:
                valor = float(texto)
            except ValueError:
                print("  Valor inválido")
                return None
            if valor < total:
                print("  O valor é menor que o total do pedido")
                return None
            troco = valor - total
            print(f"  Troco: {real(troco)}" if troco else "  Sem troco")
            return "Dinheiro"
        case _:
            return None


# ---------- Finalizar pedido ----------
def finalizar(carrinho, email, historico):
    limpar()
    if subtotal(carrinho) < MINIMO:
        print(f"Pedido mínimo: {real(MINIMO)}")
        pausa()
        return

    print("--Finalizar pedido--")
    mostrar_resumo(carrinho)
    total = subtotal(carrinho) + taxa(carrinho)

    print("\n--Entrega--")
    endereco = input("  endereço (rua, número, bairro): ").strip()
    telefone = input("  telefone: ").strip()
    if not endereco or not telefone:
        print("Preencha todos os campos")
        pausa()
        return

    pagamento = pagar(total)
    if pagamento is None:
        print("\nPagamento não concluído. Pedido cancelado.")
        pausa()
        return

    pedido = {
        "num": random.randint(1000, 9999),
        "endereco": endereco,
        "pagamento": pagamento,
        "total": total,
        "itens": [f"{q}x {buscar(i)['nome']}" for i, q in carrinho.items()],
        "entregador": random.choice(["Carlos", "Marina", "Rafael", "Júlia"]),
    }
    historico.setdefault(email, []).append(pedido)
    carrinho.clear()
    pausa()
    acompanhar(pedido)


# ---------- Sistema de entrega ----------
def acompanhar(pedido):
    previsoes = ["40 min", "30 min", "10 min", "Entregue"]
    for etapa in range(len(ETAPAS)):
        limpar()
        print(f"--Pedido #{pedido['num']}--")
        print(f"  Previsão:   {previsoes[etapa]}")
        print(f"  Entregador: {pedido['entregador']}")
        print(f"  Destino:    {pedido['endereco']}")
        print(f"  Total:      {real(pedido['total'])} ({pedido['pagamento']})\n")
        for j, texto in enumerate(ETAPAS):
            marca = "[x]" if j <= etapa else "[ ]"
            print(f"  {marca} {texto}")

        if etapa == 2:
            print()
            for pos in range(21):
                print("\r  Loja " + "-" * pos + ">" + " " * (20 - pos) + " Casa",
                      end="", flush=True)
                time.sleep(0.2)
            print()
        elif etapa < len(ETAPAS) - 1:
            time.sleep(3)   # demonstração: muda a cada 3 segundos
    pausa()


# ---------- Histórico ----------
def meus_pedidos(email, historico):
    limpar()
    print("--Meus pedidos--")
    lista = historico.get(email, [])
    if not lista:
        print("  Você ainda não fez pedidos")
    for p in lista:
        print(f"\n  Pedido #{p['num']} | {real(p['total'])} | {p['pagamento']}")
        for item in p["itens"]:
            print(f"    - {item}")
    pausa()


# ---------- Loja (área logada) ----------
def loja(email, historico):
    carrinho = {}
    while True:
        limpar()
        print(f"--Cantina do Zé-- (logado como {email})")
        print(f"  Taxa {real(TAXA)} | Grátis acima de {real(FRETE_GRATIS)} | Mínimo {real(MINIMO)}\n")
        qtd = sum(carrinho.values())
        print(f"  1-Ver cardápio")
        print(f"  2-Carrinho ({qtd} itens | {real(subtotal(carrinho))})")
        print(f"  3-Finalizar pedido")
        print(f"  4-Meus pedidos")
        print(f"  5-Sair da conta")
        opcao = input("  digite: ").strip().lower()

        match opcao:
            case "1":
                cardapio(carrinho)
            case "2":
                ver_carrinho(carrinho)
            case "3":
                if carrinho:
                    finalizar(carrinho, email, historico)
                else:
                    print("Seu carrinho está vazio")
                    pausa()
            case "4":
                meus_pedidos(email, historico)
            case "5":
                return
            case _:
                print("Inválido")
                pausa()


# ---------- Programa principal ----------
usuarios = {}     # email: senha
historico = {}    # email: lista de pedidos

while True:
    limpar()
    print("--EuComida--")
    opcao = input("  1-entrar\n  2-cadastrar\n  3-sair\n  digite: ").lower()
    limpar()

    match opcao:
        case '1' | 'entrar':
            logado = entrar(usuarios)
            if logado:
                loja(logado, historico)
        case '2' | 'cadastrar':
            cadastrar(usuarios)
        case '3' | 'sair':
            break
        case _:
            print("Inválido")
            pausa()