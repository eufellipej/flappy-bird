import pygame
import random
import os

class Cano:
    def __init__(self, tela):
        caminho_assets = os.path.join(os.path.dirname(__file__), "..", "assets")
        self.imagem = pygame.image.load(os.path.join(caminho_assets, "cano.png"))
        self.tela = tela

        self.x = self.tela.get_width()
        self.altura_base = random.randint(100, 300)
        self.distancia = 50

        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
        self.cano_baixo = self.altura_base + self.distancia

    def atualizar(self):
        self.x -= 2

        if self.x + self.imagem.get_width() < 0:
            self.x = self.tela.get_width()
            self.altura_base = random.randint(100, 300)
            self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
            self.cano_baixo = self.altura_base + self.distancia

    def desenhar(self):
        imagem_invertida = pygame.transform.flip(self.imagem, False, True)
        self.tela.blit(imagem_invertida, (self.x, self.cano_cima))
        self.tela.blit(self.imagem, (self.x, self.cano_baixo))

    def detectarColisao(self, rectJogador):
        rectCima = pygame.Rect((self.x, self.cano_cima), self.imagem.get_size())
        rectBaixo = pygame.Rect((self.x, self.cano_baixo), self.imagem.get_size())

        return rectJogador.colliderect(rectCima) or rectJogador.colliderect(rectBaixo)
