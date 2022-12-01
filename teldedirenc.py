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

#genel olarak kullanılacak font değişkeni :
#pygame.font.get_default_font() fonksiyonunun kullanılma sebebi, pygame kütüphanesiyle otomatik gelen 
#sadece bir font olması, diğer fontları kullanmak başka bilgisayarlarda uygulamanın hata almasına sebep olabilir.

font = pygame.font.Font(pygame.font.get_default_font(), 18)

#sıfırlama yazısı

reset_text = font.render("Sıfırla", True , (0,0,0))


#ÖZDİRENÇ
#özdirenci hesaplamak için gerekli olan kırmızı kaydırma kutucuğu 
#ve kırmızı kutunun üzerinde duracağı siyah çizgi 
#koordinatların ve boyutların tanımlanması

rho_scroll_bar_x , rho_scroll_bar_y = 100 , 100
rho_scroll_bar_width , rho_scroll_bar_height = 2 , 99
rho_scroll_bar_width , rho_scroll_box_height = 20 , 10 