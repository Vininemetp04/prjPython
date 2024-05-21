import main

def showList(lista):
    for i in range(0, len(lista)):
        print(f"[ {i} ] {lista[i]}")

class Characther:
    def __init__(self):
        self.name = ""
        self.typepower = 0
        self.power = 0
        self.arpon = 0
        self.type = 0
        self.tesouro = None
        self.cl = 'white'

    def showType(self):
        return main.textColor(pltype_list[self.type], self.cl)

    def showName(self):
        return main.textColor(self.name, self.cl)

    def charactherCreator(self):
        main.cls()
        self.name = input("Digite o nome do jogador:")
        main.cls()
        showList(list_power)
        self.typepower = int(input(f"Selecione entre os poderes da lista: "))
        main.cls()
        showList(pltype_list)
        self.type = int(input(f"Qual tipo de personagem você é:"))
        main.cls()
        showList(list_arpon)
        self.arpon = int(input(f"Que tipo de arma o seu personagem usa:"))
        main.cls()

        match self.type:
            case 1 | 8:
                self.cl = 'purple'
            case 3:
                self.cl = 'gray'
            case 4 | 5:
                self.cl = 'red'
            case 6:
                self.cl = 'green'
            case _:
                self.cl = 'white'

        self.begin = input(f"Olá {self.showName()} o {self.showType()} seja bem-vindo ao jogo!")
        

list_power = [
    main.textColor('Magia', 'purple'),
    'Físico', 
    main.textColor('Psiquicos', 'purple'), 
    main.textColor('Natural', 'green'), 
    main.textColor('Sombrio', 'gray'), 
    main.textColor('Divinos', 'yellow')
]
list_typepowermagic = [
    'Bola de Fogo: Lança uma bola de fogo que explode ao atingir o alvo, causando dano em área.'
    'Cura Divina: Restaura uma quantidade significativa de pontos de vida a um aliado.',
    'Escudo Arcano: Cria uma barreira mágica que absorve danos por um tempo limitado.',
    'Invocação de Elemental: Conjura um elemental (fogo, água, terra, ar) para lutar ao seu lado.',
    'Controle Mental: Permite controlar temporariamente as ações de um inimigo.'
]
list_fisicos = [
    'Golpe Poderoso: Executa um ataque físico com força aumentada, causando dano adicional.', 
    'Reflexos Rápidos: Aumenta a velocidade e a capacidade de esquiva por um curto período',
    'Fúria Berserker: Entra em um estado de fúria, aumentando o dano de ataque mas diminuindo a defesa.',
    'Soco Quake: Um soco no chão que causa um pequeno terremoto, derrubando inimigos próximos.',
    'Arremesso de Arma: Lança uma arma com precisão mortal, capaz de atingir alvos à distância.'
]
list_powerfisico = [
    'Controle de Plantas: Manipula plantas para atacar, defender ou criar obstáculos',
    'Forma Animal: Transforma-se em um animal, ganhando suas habilidades e características.',
    'Chamado da Natureza: Invoca animais ou criaturas naturais para auxiliar em combate.',
    'Cura Natural: Usa a energia da natureza para curar feridas e doenças.',
    'Manipulação do Clima: Altera as condições climáticas, como provocar tempestades ou nevascas.'
]
list_powerdark = [
    'Toque da Morte: Um ataque que drena a vida do inimigo e cura o usuário.',
    'Caminho das Sombras: Permite se mover pelas sombras, tornando-se invisível e intangível.',
    'Necromancia: Reanima cadáveres para lutar como servos zumbis.',
    'Explosão Sombria: Libera uma onda de energia sombria que causa dano e pode amedrontar inimigos.',
    'Corrupção Espiritual: Envenena a alma de um alvo, causando dano contínuo e debilitando-o.'
]
list_powerdivine = [
    'Luz Sagrada: Emite uma luz purificadora que causa dano a criaturas das trevas e cura aliados.',
    'Julgamento Divino: Invoca o poder de uma entidade divina para julgar e punir um inimigo.',
    'Aura de Proteção: Cria uma aura que protege aliados próximos de ataques.',
    'Chama Celestial: Conjura chamas sagradas que queimam apenas os inimigos.',
    'Benção dos Ancestrais: Recebe um poder ancestral que aumenta todas as capacidades do usuário por um tempo.'
]
list_arpon = [
    "Espada Longa",
    "Machado de Guerra",
    "Arco Longo",
    "Cajado Mágico",
    "Adaga Envenenada",
    "Martelo de Batalha",
    "Lança de Caça",
    "Livro Proibido",
    "Foice Sombria",
    "Espada de Luz"
]
pltype_list = [
    "Guerreiro",
    main.textColor('Mago', 'purple'),
    "Arqueiro",
    main.textColor('Ladino', 'gray'),
    main.textColor('Clerigo', 'red'),
    main.textColor('Bárbaro', 'red'),
    main.textColor('Druida', 'green'),
    "Paladino",
    main.textColor('Feiticeiro', 'purple'),
    "Bardo"
]
tesouros = [
    "Pote de ouro",
    "Grimório antigo com feitiços raros",
    "Colar de rubis",
    "Poção de cura",
    "Escudo encantado",
    "Mapa do tesouro perdido",
    "Adaga de prata",
    "Amuleto da sorte",
    "Anel de invisibilidade",
    "Elmo ornamental de um antigo herói",
    "Bálsamo de rejuvenescimento",
    "Elixir da força",
    "Relíquia sagrada de uma civilização perdida",
    "Armadura de dragão",
    "Estátua de ouro maciço",
    "Tomo de conhecimento oculto",
    "Coroa encantada",
    "Lança celestial",
    "Frasco de fogo alquímico",
    "Cajado da ressurreição"
]
