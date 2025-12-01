import pygame
import os

class Jogador:
    def __init__(self, tela, x, y):
        self.posicao = [x, y]
        self.tamanho = [32, 32]
        self.rect = pygame.Rect(self.posicao, self.tamanho)
        self.tela = tela

        # caminho absoluto dos assets
        caminho_assets = os.path.join(os.path.dirname(__file__), "..", "assets")

        self.contador = 0
        self.imagemAtual = 0
        self.listaImagens = []

        for i in range(3):
            imagem_path = os.path.join(caminho_assets, f"passaro-{i}.png")
            imagem = pygame.image.load(imagem_path)
            imagem = pygame.transform.scale(imagem, self.tamanho)
            self.listaImagens.append(imagem)

        self.velocidadeAtual = 0
        self.velocidadeMaxima = 12
        self.gravidade = 1/60 * 10

    def desenhar(self):
        self.contador += 1
        if self.contador > 5:
            self.imagemAtual = (self.imagemAtual + 1) % 3
            self.contador = 0

        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    def atualizar(self):
        self.velocidadeAtual = min(
            self.velocidadeAtual + self.gravidade, self.velocidadeMaxima
        )

        self.posicao = [self.posicao[0],
                        self.posicao[1] + self.velocidadeAtual]

        self.rect = pygame.Rect(self.posicao, self.tamanho)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.velocidadeAtual = -self.velocidadeMaxima * 0.3

    def getRect(self):
        return pygame.Rect(self.posicao, self.tamanho)
