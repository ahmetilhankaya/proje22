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
#özdirenci hesaplamak için gerekli olan kırmızı kaydırma kutucuğu (rho_scroll_box)
#ve kırmızı kutunun üzerinde duracağı siyah çizgi (rho_scroll_bar) nin 
#koordinatların ve boyutların tanımlanması

rho_scroll_bar_x , rho_scroll_bar_y = 100 , 100
rho_scroll_bar_width , rho_scroll_bar_height = 2 , 99
rho_scroll_box_width , rho_scroll_box_height = 20 , 10 
rho_scroll_box_x , rho_scroll_box_y = rho_scroll_bar_x - 9 , 101 + (rho_scroll_bar_height - rho_scroll_box_height) / 2
rho_scroll_box = pygame.rect.Rect(rho_scroll_box_x , rho_scroll_box_y , rho_scroll_box_width , rho_scroll_box_height)
rho_scroll_bar = pygame.rect.Rect(rho_scroll_bar_x , rho_scroll_bar_y , rho_scroll_bar_width , rho_scroll_bar_height)

#ilk olarak özdirenç kutucuğu hareket etmiyormuş gibi kabul ediliyor
rho_scroll_box_dragging = False


# öz direnç çubuğunun biraz üstünde öz direnç yazısı bulunuyor
rho_name_font = font.render('Resistivity(Ωcm', True, pygame.Color(0,0,0,255))
rho_name_rect = rho_name_font .get_rect()
rho_name_rect.bottom = rho_scroll_bar_y - 10
rho_name_rect.centerx = rho_scroll_bar_x + int(rho_scroll_bar_width / 2)

# öz direnç simgesi ve yazısının fontları, pozisyonları ve renkleri :
#        pygame.Color sınıfına mensup bir değişken oluşturulurken, 4. sıradaki argüman yazının arkaplan renginin alfa değerini belirtir,
#       bu değeri 255 yaparsak yazıların arkaplanı tamamen transparan olur,
#       bu sayede yazılar çakışsa da birbirlerinin önünü kapatmazlar

rho_font = font.render('ρ' , True , pygame.Color(0,0,0,255))
rho_font = rho_name_font.get_rect()

# öz direnç çubuğunun biraz yukarısında olması için y eksenindeki değerini azalttık
rho_rect.bottom = rho_scroll_bar_y - 45
# yazının çubuk ile hizada durması için çubğun x ekseninde orta noktasını hesaplayıp yazının x eksenindeki merkezine atadık
rho_rect.centerx = rho_scroll_bar.centerx

#  öz direnç hesaplama fonksiyonu, 
# bu fonksiyon kırmızı kutunun, arkaplanındaki siyah çubuğun tepesine olan uzaklığını hesaplayarak 0.01 ile çarpıyor
# ve round() fonksiyonunu kullanarak bu float türündeki sayının 2 decimal basamağını hesaplıyor 
# örneğin round(0.12345, 2) fonksiyonu 0.12 döndürür, kalan basamakları keser.

def resistivity():
    return round((rho_scroll_bar_y + rho_scroll_bar_height - rho_scroll_box.y - (rho_scroll_box.height / 2) + 1))
