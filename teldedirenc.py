import pygame as pg
import sys
pg.init()

en , boy = 800 , 600
siyah =  0 , 0 , 0 # RGB 0- 255
beyaz = 255 ,255, 255
gri = 100,100,100
kahverengi = 101,67,33
yesil = 102,255,0
ekran = pg.display.set_mode( (en,boy)  )
x , y = en//2,boy//2
x_speed = y_speed = 1
yari_cap = 40

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(kahverengi)
    pg.draw.circle(ekran,yesil,( en//2 , boy //2  ),20)
    pg.display.flip()
