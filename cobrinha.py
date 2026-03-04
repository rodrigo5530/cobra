import pygame
import random

# Inicializa
pygame.init()

# Tamanho da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Tamanho do bloco
bloco = 20
velocidade = 10

clock = pygame.time.Clock()

def desenhar_cobra(bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], bloco, bloco])

def jogo():
    game_over = False
    game_close = False

    x = largura / 2
    y = altura / 2

    x_mudanca = 0
    y_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - bloco) / 20.0) * 20.0

    while not game_over:

        while game_close:
            tela.fill(preto)
            fonte = pygame.font.SysFont(None, 35)
            mensagem = fonte.render("Você perdeu! Pressione C para jogar novamente ou Q para sair", True, vermelho)
            tela.blit(mensagem, [50, altura / 2])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = bloco
                    x_mudanca = 0

        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True

        x += x_mudanca
        y += y_mudanca
        tela.fill(preto)

        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, bloco, bloco])

        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        lista_cobra.append(cabeca)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for parte in lista_cobra[:-1]:
            if parte == cabeca:
                game_close = True

        desenhar_cobra(bloco, lista_cobra)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()
