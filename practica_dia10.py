import pygame

#Inicializar Pygame
pygame.init()

#Crear pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e Icono
pygame.display.set_caption('Invasion Espacial')
icono=pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

#Variables Jugador
img_jugador = pygame.image.load('cohete.png')
jx=368
jy=536
jx_cambio = 0

#Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#Loop del juego
se_ejecuta = True
while se_ejecuta:
    #RGB
    pantalla.fill((0, 255, 255))

    #Iterar eventos
    for evento in pygame.event.get():

        #Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jx_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jx_cambio = 0.3

        #Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jx_cambio = 0

    #Modificar jugador
    jx += jx_cambio
    jugador(jx,jy)

    pygame.display.update()