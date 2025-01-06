import pygame
import random
import math
from pygame import mixer

#Inicializar Pygame
pygame.init()

#Crear pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e Imagenes
pygame.display.set_caption('Invasion Espacial')
icono=pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

#Musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#Variables Jugador
img_jugador = pygame.image.load('cohete.png')
jx=368
jy=500
jx_cambio = 0

#Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))


#Variables enemigo
img_enemigo = []
enemigo_x=[]
enemigo_y= []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(40)


#Funcion enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

#Variables bala
balas=[]
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


#Funcion colision
def colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow((x_1-x_2),2) + math.pow((y_1-y_2),2))
    if distancia < 27:
        return True
    else:
        return False


#Variable puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
puntaje_x = 10
puntaje_y = 10

#Texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf',40)

def texto_final():
    final = fuente_final.render('JUEGO TERMINADO',True,(255,255,255))
    pantalla.blit(final,(200,200))

#Funcion puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntaje: {puntaje}',True,(255,255,255))
    pantalla.blit(texto,(x,y))

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
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.set_volume(0.3)
                sonido_bala.play()
                nueva_bala = {
                    "x": jx,
                    "y": jy,
                    "velocidad": -1
                }
                balas.append(nueva_bala)

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
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

        #Fin del juego
        if enemigo_y[e] > 255:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        # Mantener jugador dentro de los bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]


        #Colision balas
        for bala in balas:
            colision_bala_enemigo = colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e],e)



    # Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)


    jugador(jx,jy)
    mostrar_puntaje(puntaje_x,puntaje_y)


    pygame.display.update()