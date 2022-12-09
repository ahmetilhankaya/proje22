import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLACK = (  0,   0,   0)
FPS = 15

pygame.init()

# pencere büyüklüğü, bilgisayarda oluşturulan pencerelerde
# koordinatlar sol üstten başlar, sağ alta doğru büyür
# sol üstteki koordinat noktası (0,0)'dır. 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#pencerenin adı
pygame.display.set_caption("PyGame Direnc Hesaplama")

#genel olarak kullanılacak font değişkeni:
#   pygame.font.get_default_font() fonksiyonunun kullanılma sebebi, pygame kütüphanesiyle otomtik gelen sadece 1 font olması,
#   diğer fontları kullanmak başka bilgisayarlarda uygulamanın hata almasına sebep olabilir.

font = pygame.font.Font(pygame.font.get_default_font(), 18)

#sıfırlama yazsısı

reset_text = font.render("Sıfırla", True, (0,0,0))


# ÖZ DİRENÇ
# öz direnci hesaplamak için gerekli olan kırmızı kaydırma kutucuğu(rho_scroll_box)
# ve kırmızı kutunun üzerinde duracağı siyah çizgi(rho_scroll_bar)'nin
# koordinatlarının ve boyutlarının tanımlanması

rho_scroll_bar_x,rho_scroll_bar_y = 100, 100
rho_scroll_bar_width, rho_scroll_bar_height  = 2, 99
rho_scroll_box_width, rho_scroll_box_height = 20, 10
rho_scroll_box_x, rho_scroll_box_y = rho_scroll_bar_x - 9, 101 + (rho_scroll_bar_height - rho_scroll_box_height) / 2
rho_scroll_box = pygame.rect.Rect(rho_scroll_box_x, rho_scroll_box_y, rho_scroll_box_width, rho_scroll_box_height)
rho_scroll_bar = pygame.rect.Rect(rho_scroll_bar_x, rho_scroll_bar_y, rho_scroll_bar_width, rho_scroll_bar_height)

# ilk olarak öz direnç kutucuğu hareket etmiyormuş gibi kabul ediliyor
rho_scroll_box_dragging = False

# öz direnç çubuğunun biraz üstünde öz direnç yazısı bulunuyor.

rho_name_font = font.render('Resistivity(Ωcm)', True, pygame.Color(0,0,0,255))
rho_name_rect = rho_name_font .get_rect()
rho_name_rect.bottom = rho_scroll_bar_y - 10
rho_name_rect.centerx = rho_scroll_bar_x + int(rho_scroll_bar_width / 2)

# öz direnç simgesi ve yazısının fontları, pozisyonları ve renkleri:
#       pygame.Color sınıfına mensup bir değişken oluşturulurken, 4. sıradaki argüman yazının arkaplan renginin alfa değerini belirtir,
#       bu değeri 255 yaparsak yazıların arkaplanı tamamen transparan olur,
#       bu sayede yazılar çakışsa da birbirlerinin önünü kapatmazlar

rho_font = font.render('ρ', True, pygame.Color(0,0,0,255))
rho_rect = rho_font.get_rect()

# öz direnç çubuğunun biraz yukarısında olması için y eksenindeki değerini azalttık

rho_rect.bottom = rho_scroll_bar_y - 45

# yazının çubuk ile hizada durması için çubğun x ekseninde orta noktasını hesaplayıp yazının x eksenindeki merkezine atadık

rho_rect.centerx = rho_scroll_bar.centerx

# öz direnç hesaplama fonksiyonu, 
# bu fonksiyon kırmızı kutunun, arkaplanındaki siyah çubuğun tepesine olan uzaklığını hesaplayarak 0.01 ile çarpıyor
# ve round() fonksiyonunu kullanarak bu float türündeki sayının 2 decimal basamağını hesaplıyor 
# örneğin round(0.12345, 2) fonksiyonu 0.12 döndürür, kalan basamakları keser.

def resistivity():
    return round((rho_scroll_bar_y + rho_scroll_bar_height - rho_scroll_box.y - (rho_scroll_box.height / 2) + 1) * 0.01,2)

# kırmızı kutucuk(rho_scroll_box) hareket ettikçe, öz direnç değeri yeniden hesaplanacak ve metin güncellenecek

rho_value_font = font.render(f"%.2f" %resistivity(), True, pygame.Color(0,0,0,255)) 
rho_value_rect = rho_value_font.get_rect()
rho_value_rect.top = rho_scroll_bar_y + rho_scroll_bar_height + 10
rho_value_rect.centerx = rho_scroll_bar_x + int(rho_scroll_bar_width / 2)



# uzunluk değeri için gerekli scrollbar ve scrollbox'un koordinatları, ve büyüklükleri
#   öz direnç için kullanılan bar ve box ile aynı özelliklere sahip

len_scroll_bar_x,len_scroll_bar_y = 250, 100
len_scroll_bar_width, len_scroll_bar_height  = 2, 95
len_scroll_box_width, len_scroll_box_height = 20, 10
len_scroll_box_x, len_scroll_box_y = len_scroll_bar_x - 9, 101 + (len_scroll_bar_height - len_scroll_box_height) / 2
len_scroll_box = pygame.rect.Rect(len_scroll_box_x, len_scroll_box_y, len_scroll_box_width, len_scroll_box_height)
len_scroll_bar = pygame.rect.Rect(len_scroll_bar_x, len_scroll_bar_y, len_scroll_bar_width, len_scroll_bar_height)

# programın ilk açıldığı anda uzunluk değiştirilmediği için False olarak başlatıyoruz

len_scroll_box_dragging = False

#uzunluk simgesinin fontu ve koordinatları

len_font = font.render('L', True, pygame.Color(0,0,0,255))
len_rect = len_font.get_rect()
len_rect.bottom = len_scroll_bar_y - 45
len_rect.centerx = len_scroll_bar_x + int(len_scroll_bar_width / 2)

#uzunluk isminin koordinatları
len_name_font = font.render('Length(cm)', True, pygame.Color(0,0,0,255))
len_name_rect = len_name_font.get_rect()
len_name_rect.bottom = len_scroll_bar_y - 10
len_name_rect.centerx = len_scroll_bar_x + int(len_scroll_bar_width / 2)

# uzunluk hesaplama fonksiyonu
# bu fonksiyon da resistivity() gibi kırmızı kutunun siyah çubuğun tepesine olan uzaklığını kullanarak hesaplamasını yapar
# en az 1 uzunluğu elde etmek için return değerine + 1 koyarız, round() il virgül sonrası sadece 2 basamağı saklarız

def length():
        return round((len_scroll_bar_height + len_scroll_bar_y - len_scroll_box.y - (len_scroll_box.height / 2)) / 5 + 1,2)
    
# uzunluk değerinin yazıldığı metin kutusu, uzunluk çubuğunun altında yer alır, bu nedenle
# len_value_rect.top (bu yazının tepesi) uzunluk çubuğunun biraz altında olmalıdır.
# y ekseninde aşağı gittikçe değer artar bu nedenle 14 ekliyoruz.
# yazıyı da çubuk ile hizalamak için x ekseninde merkezini çubuğun tam orta noktasına eşitliyoruz
# çubuğun orta noktasını hesaplamak için de önce çubuğun x değerini(çubuğun sol üst noktası) 
# ile çubuğun genişliğinin yarısını toplarsak, ubuğun x ekseninde orta noktasını bulmuş oluruz
    
len_value_font = font.render(str(length()), True, pygame.Color(0,0,0,255))
len_value_rect = len_value_font.get_rect()
len_value_rect.top = len_scroll_bar_y + len_scroll_bar_height + 14
len_value_rect.centerx = len_scroll_bar_x + int(len_scroll_bar_width / 2)

# alanın değiştirilmesi için kullanılan siyah çubuk ve kırmızı kutunun koordinatları 
area_scroll_bar_x,area_scroll_bar_y = 400, 100
area_scroll_bar_width, area_scroll_bar_height  = 2, 99
area_scroll_box_width, area_scroll_box_height = 20, 10
area_scroll_box_x, area_scroll_box_y = area_scroll_bar_x - 9, 101 + (area_scroll_bar_height - area_scroll_box_height) / 1.5
area_scroll_box = pygame.rect.Rect(area_scroll_box_x, area_scroll_box_y, area_scroll_box_width, area_scroll_box_height)
area_scroll_bar = pygame.rect.Rect(area_scroll_bar_x, area_scroll_bar_y, area_scroll_bar_width, area_scroll_bar_height)

#oyun ilk çalıştığı an area değişmediği için false atıyoruz
area_scroll_box_dragging = False

#rho ve length ile aynı işlemler yine yapılıyor...
area_font = font.render('A', True, pygame.Color(0,0,0,255))
area_rect = area_font.get_rect()
area_rect.bottom = area_scroll_bar_y - 45
area_rect.centerx = area_scroll_bar_x + int(area_scroll_bar_width / 2)


area_name_font = font.render('Area(cm^2)', True, pygame.Color(0,0,0,255))
area_name_rect = area_name_font .get_rect()
area_name_rect.bottom = area_scroll_bar_y - 10
area_name_rect.centerx = area_scroll_bar_x + int(area_scroll_bar_width /2)


# areayı 0.01 ile 15 arasında tutmak için kırmızı çubuğun siyah çubuğun alt noktasına olan uzunlupunun ,
#siyah çubuğun boyuna olan oranını bulup (0-1 arası bir değer )
#bu değeri 14.99 ile çarpıp sonuca 0.01 ekliyoruz ve istediğimiz aralığı elde etmiş oluyoruz

def area():
    min = 0.1
    x = (area_scroll_bar.y + area_scroll_bar_height - (area_scroll_box.y + area_scroll_box_height /2)) / area_scroll_bar_height * 14.99
    return round(min + x,2)

#area değerinin ekrana yazılması

area_value_font = font.render(f"%.2f" %area(), True, pygame.color(0,0,0,255))
area_value_rect = area_value_font.get_rect()
area_value_rect.top = area_scroll_bar_y + area_scroll_bar_height + 10
area_value_rect.centerx = area_scroll_bar_x + int(area_scroll_bar_width /2)


#direnç hesabı
def resistance():
    _resistivity = resistivity()
    _lenght = lenght()
    _area = area()
    _resistance = _resistivity * _lenght / _area

    return round(_resistance, 3)


# direnç yazısının fontu
reistance_font = pygame.font.Font(pygame.font.get_default_font(), int(resistance()) + 10 ) # 2. değişken font büyüklüğünü temsil eder
division_r = reistance_font.render('R', False, pygame.Color(12,58,160,255)) # metin rengi için renk değeri seçildi
division_r_text = division_r.get_rect()
division_r_text.centery = area_scroll_bar_y + 70
division_r_text.centerx = area_scroll_bar_x + 130

# eşittir işareti
equal_sign = font.render('=', True, pygame.Color(0,0,0,255))
equal_sign_text = equal_sign.get_rect()
equal_sign_text.centery = area_scroll_bar_y + 70
equal_sign_text.centerx = area_scroll_bar_x + 210



resistivity_font = pygame.font.Font(pygame.font.get_default_font(), int(float(resistivity()) * 200) + 15)
division_rho = resistivity_font.render('ρ', True, pygame.Color(0,0,0,255))
division_rho_text = division_rho.get_rect()
division_rho_text.centery = area_scroll_bar_y