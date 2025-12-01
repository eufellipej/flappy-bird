import pygame
from scripts.cenas import Partida, Menu

pygame.init()

tamanhoTela = [600, 400]
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("FlappyBird Clone")
relogio = pygame.time.Clock()
corFundo = (86, 148, 214)

# cria as cenas
listaCenas = {
    'partida': Partida(tela),
    'menu': Menu(tela)
}

cenaAtual = 'menu'

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    tela.fill(corFundo)

    novaCena = listaCenas[cenaAtual].atualizar()

    # se mudou de cena, recria ela
    if novaCena != cenaAtual:
        cenaAtual = novaCena
        listaCenas[cenaAtual] = Partida(tela) if cenaAtual == 'partida' else Menu(tela)

    pygame.display.flip()
    relogio.tick(60)
