import pygame as pg
def main():
    #inicializar el modulo
    pg.init()
    #cargar y definir el logo
    logo = pg.image.load("heli.png")
    pg.display.set_icon(logo)
    pg.display.set_caption("PROGRAMA HELI")

    #crear una superficie en pantalla de tamaño 240x180
    screen = pg.display.set_mode((240,180))
    #definir una variable de control para el main loop
    running = True
    #main loop
    while running:
        #manejador de eventos, recibe todo evento de la cola de eventos
        for event in pg.event.get():
            #SOLO HACER ALGO SI EL EVENTO ES DE TIPO QUIT
            if event.type==pg.QUIT:
                running = False
#corre la función main solo si este programa es ejecutado como programa principal
#si lo importas como modulo nada se ejecuta
if __name__=="__main__":
    main()