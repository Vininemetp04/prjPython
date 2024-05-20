import random

class Characther:
    def __init__(self, name, typepower, power, arpon, type, tesouro=None):
        self.name = name
        self.typepower = typepower
        self.power = power
        self.arpon = arpon
        self.type = type
        self.tesouro = tesouro

list_power = ['Magia', 'Físico','Psiquicos','Natural','Sombrio', 'Divinos']
list_typepowermagic = ['Bola de Fogo: Lança uma bola de fogo que explode ao atingir o alvo, causando dano em área.'
                        'Cura Divina: Restaura uma quantidade significativa de pontos de vida a um aliado.',
                        'Escudo Arcano: Cria uma barreira mágica que absorve danos por um tempo limitado.',
                    'Invocação de Elemental: Conjura um elemental (fogo, água, terra, ar) para lutar ao seu lado.',
                    'Controle Mental: Permite controlar temporariamente as ações de um inimigo.']
list_fisicos = ['Golpe Poderoso: Executa um ataque físico com força aumentada, causando dano adicional.', 
                'Reflexos Rápidos: Aumenta a velocidade e a capacidade de esquiva por um curto período',
                'Fúria Berserker: Entra em um estado de fúria, aumentando o dano de ataque mas diminuindo a defesa.',
                'Soco Quake: Um soco no chão que causa um pequeno terremoto, derrubando inimigos próximos.',
                'Arremesso de Arma: Lança uma arma com precisão mortal, capaz de atingir alvos à distância.']
list_powerfisico = ['Controle de Plantas: Manipula plantas para atacar, defender ou criar obstáculos',
                'Forma Animal: Transforma-se em um animal, ganhando suas habilidades e características.',
                'Chamado da Natureza: Invoca animais ou criaturas naturais para auxiliar em combate.',
                'Cura Natural: Usa a energia da natureza para curar feridas e doenças.',
                'Manipulação do Clima: Altera as condições climáticas, como provocar tempestades ou nevascas.']
list_powerdark = ['Toque da Morte: Um ataque que drena a vida do inimigo e cura o usuário.',
                  'Caminho das Sombras: Permite se mover pelas sombras, tornando-se invisível e intangível.',
                  'Necromancia: Reanima cadáveres para lutar como servos zumbis.',
                  'Explosão Sombria: Libera uma onda de energia sombria que causa dano e pode amedrontar inimigos.',
                  'Corrupção Espiritual: Envenena a alma de um alvo, causando dano contínuo e debilitando-o.']
list_powerdivine = ['Luz Sagrada: Emite uma luz purificadora que causa dano a criaturas das trevas e cura aliados.',
                    'Julgamento Divino: Invoca o poder de uma entidade divina para julgar e punir um inimigo.',
                    'Aura de Proteção: Cria uma aura que protege aliados próximos de ataques.',
                    'Chama Celestial: Conjura chamas sagradas que queimam apenas os inimigos.',
                    'Benção dos Ancestrais: Recebe um poder ancestral que aumenta todas as capacidades do usuário por um tempo.']

list_arpon = [
    "Arma1: Espada Longa",
    "Arma2: Machado de Guerra",
    "Arma3: Arco Longo",
    "Arma4: Cajado Mágico",
    "Arma5: Adaga Envenenada",
    "Arma6: Martelo de Batalha",
    "Arma7: Lança de Caça",
    "Arma8: Livro Proibido",
    "Arma9: Foice Sombria",
    "Arma10: Espada de Luz"
]

type = [
    "Guerreiro",
    "Mago",
    "Arqueiro",
    "Ladino",
    "Clerigo",
    "Bárbaro",
    "Druida",
    "Paladino",
    "Feiticeiro",
    "Bardo"]
def tesouro():
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

player = Player

