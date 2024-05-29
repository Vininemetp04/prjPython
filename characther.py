import funcs as FN
import menu as MN
import time
import os

class Characther:
    def __init__(self):
        self.name = ""
        self.typepower = 0
        self.power = 0
        self.arpon = 0
        self.type = 0
        self.tesouro = None
        self.cl = 'white'
        self.hp = 100
        self.xp = 0
        self.parte = 0

    def showType(self):
        return pltype_list[self.type]

    def showName(self):
        return FN.textColor(self.name, self.cl)

    def save(self):
        if os.path.isfile('./save'):
            os.remove('./save')
        save = open('./save', 'x')
        save.write(f"{self.name};{self.typepower};{self.power};{self.arpon};{self.type};{self.tesouro};{self.cl};{self.hp};{self.xp};{self.parte}")
        save.close()

    def charactherCreatorFormSave(self, dados):
        # 0 name| 1 typepower | 2 power | 3 arpon | 4 type | 5 tesouro | 6 cl | 7 hp | 8 xp | 9 parte
        self.name = dados[0]
        self.typepower = int(dados[1])
        self.power = int(dados[2])
        self.arpon = int(dados[3])
        self.type = int(dados[4])
        self.tesouro = dados[5]
        self.cl = dados[6]
        self.hp = dados[7]
        self.xp = dados[8]
        self.parte = dados[9]
        return self.parte

    def charactherCreator(self):
        FN.cls()
        print('Crie seu personagem')
        self.name = input("Digite o nome do jogador:").strip()
        
        FN.cls()
        mn = MN.menu(list_power, 2, 2, 'Poder')
        mn.draw(0)
        mn.wait()
        self.typepower = mn.ans
        mn.close()
        
        FN.cls()
        mn1 = MN.menu(pltype_list, 2, 2, "Tipo")
        mn1.draw(0)
        mn1.wait()
        self.type = mn1.ans
        mn1.close()
        
        FN.cls()
        mn2 = MN.menu(list_arpon, 2, 2, "Arma")
        mn2.draw(0)
        mn2.wait()
        self.arpon = mn2.ans
        mn2.close()
        
        FN.cls()

        match self.type:
            case 1:
                self.cl = 'cyan'
            case 8:
                self.cl = 'purple'
            case 3:
                self.cl = 'gray'
            case 4 | 5:
                self.cl = 'red'
            case 6:
                self.cl = 'green'
            case _:
                self.cl = 'white'

        print(f"Olá {self.showName()} o {self.showType()} seja bem-vindo ao jogo!")
        time.sleep(1)
        self.save()
        
list_power = [
    FN.textColor('Magia', 'cyan'),
    'Físico', 
    FN.textColor('Psiquicos', 'purple'), 
    FN.textColor('Natural', 'green'), 
    FN.textColor('Sombrio', 'gray'), 
    FN.textColor('Divinos', 'yellow')
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
    FN.textColor('Mago', 'cyan'),
    "Arqueiro",
    FN.textColor('Ladino', 'gray'),
    FN.textColor('Clerigo', 'red'),
    FN.textColor('Bárbaro', 'red'),
    FN.textColor('Druida', 'green'),
    "Paladino",
    FN.textColor('Feiticeiro', 'purple'),
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
