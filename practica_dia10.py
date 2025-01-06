import pygame
import random

#Inicializar Pygame
pygame.init()

#Crear pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e Imagenes
pygame.display.set_caption('Invasion Espacial')
icono=pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

#Variables Jugador
img_jugador = pygame.image.load('cohete.png')
jx=368
jy=500
jx_cambio = 0

#Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))


#Variables enemigo
img_enemigo = pygame.image.load('enemigo.png')
enemigo_x=random.randint(0,736)
enemigo_y= random.randint(50,200)
enemigo_x_cambio = 0.1
enemigo_y_cambio = 40


#Funcion enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y))

#Variables bala
img_bala = pygame.image.load('bala.png')
bala_x=0
bala_y= 500
bala_x_cambio = 0
bala_y_cambio = 0.3
bala_visible = False


#Funcion bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10))



#Loop del juego
se_ejecuta = True
while se_ejecuta:
    #Imagen Fondo
    pantalla.blit(fondo,(0,0))

    #Iterar eventos
    for evento in pygame.event.get():

        #Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jx_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jx_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jx
                    disparar_bala(bala_x,bala_y)

        #Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jx_cambio = 0

    #Modificar jugador
    jx += jx_cambio

    #Mantener jugador dentro de los bordes
    if jx <= 0:
        jx = 0
    elif jx >= 736:
        jx = 736

    # Modificar enemigo
    enemigo_x += enemigo_x_cambio

    # Mantener jugador dentro de los bordes
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.1
        enemigo_y += enemigo_y_cambio


    #Movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio

    jugador(jx,jy)
    enemigo(enemigo_x,enemigo_y)

    pygame.display.update()