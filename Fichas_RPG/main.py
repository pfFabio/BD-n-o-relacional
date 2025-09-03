from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["trabalho1"]
fichas = db["fichas"]


def busca_fichas(fichas):
    for ficha in fichas.find():
        print(ficha["nome"])

def busca_ficha(fichas, nome):
    achado = fichas.find_one(nome)
    if achado:
        return achado
    print("conferimos todas as fichas")
    return None

def cadastra_ficha(fichas, nova_ficha):
    if not fichas.find_one({"nome": nova_ficha['nome']}):
        inserida = fichas.insert_one(nova_ficha)
        print(f"\na  ficha foi inserida com id {inserida.inserted_id}\n")
    else:
        print("ja existe uma ficha com esse nome")

def deletar_ficha(fichas, nome):
    if fichas.delete_one({"nome":nome}):
        print("a ficha foi deletada")
    else:
        print("não foi possivel deletar a ficha")

def atualiza_ficha(fichas, nome, atributo, valor):
    fichas.update_one({"nome": nome}, {"$set": {atributo:valor}})

ficha0 = {
  "nome": "Geralt de Rivia",
  "classe": "Bruxo",
  "nivel": 10,
  "HP": 250,
  "FOR": 20,
  "DEX": 18,
  "INT": 15,
  "CHA": 12,
  "habilidade": {
    "nome": "Sinal Igni",
    "explicacao": "Dispara uma onda de fogo para queimar inimigos."
  }
}


ficha1 = {
    "nome": "Sir Garetho",
    "classe": "Guerreiro",
    "nivel": 5,
    "HP": 120,
    "FOR": 18,
    "DEX": 12,
    "INT": 10,
    "CHA": 14,
    "habilidade": {"nome": "Ataque Poderoso", "explicacao": "Causa dano adicional em um único ataque."}
}



cadastra_ficha(fichas, ficha0)
cadastra_ficha(fichas, ficha1)


while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar nova ficha")
        print("2. Buscar todas as fichas")
        print("3. Buscar uma ficha específica")
        print("4. Atualizar uma ficha")
        print("5. Deletar uma ficha")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            nome = input("Nome da ficha: ")
            classe = input("Classe: ")
            nivel = int(input("Nível: "))
            hp = int(input("HP: "))
            forca = int(input("FOR: "))
            destreza = int(input("DEX: "))
            inteligencia = int(input("INT: "))
            carisma = int(input("CHA: "))
            habilidade_nome = input("Nome da habilidade: ")
            habilidade_explicacao = input("Explicação da habilidade: ")

            nova_ficha = {
                "nome": nome,
                "classe": classe,
                "nivel": nivel,
                "HP": hp,
                "FOR": forca,
                "DEX": destreza,
                "INT": inteligencia,
                "CHA": carisma,
                "habilidade": {"nome": habilidade_nome, "explicacao": habilidade_explicacao}
            }
            cadastra_ficha(fichas, nova_ficha)

        elif choice == '2':
            busca_fichas(fichas)

        elif choice == '3':
            nome = input("Digite o nome da ficha para buscar: ")
            ficha = busca_ficha(fichas, nome)
            if ficha:
                print("--- Detalhes da Ficha ---")
                for key, value in ficha.items():
                    print(f"{key}: {value}")
            else:
                print(f"A ficha '{nome}' não foi encontrada.")

        elif choice == '4':
            nome = input("Digite o nome da ficha para atualizar: ")
            campo = input("Digite o nome do campo para atualizar (ex: nivel, HP, FOR): ")
            valor = input(f"Digite o novo valor para '{campo}': ")
            if campo in ['nivel', 'HP', 'FOR', 'DEX', 'INT', 'CHA']:
                valor = int(valor)

            
            atualiza_ficha(fichas, nome, campo, valor)

        elif choice == '5':
            nome = input("Digite o nome da ficha para deletar: ")
            deletar_ficha(fichas, nome)

        elif choice == '6':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")



client.close()