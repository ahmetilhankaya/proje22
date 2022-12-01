import pygame 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

WHİTE = (255, 255, 255)
RED = (255, 0 , 0)
BLACK = (0, 0 , 0)

FPS = 15

pygame.init()

#pencere büyüklüğü, bilgisayarda oluşturulan pencerelerde 
#koordinatlar sol üstten başlar, sağ alta doğru büyür.
#sol üstteki koordinat noktası (0,0) dır 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#pencerenin adı
pygame.display.set_caption("PyGame Direnc Hesaplama")




