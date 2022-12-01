# absolute path vs relative path
# tam yol veya bağıl yol
# .. üst klasörü gösterir...

# f= open('c:\\users\\ASILKAN\\desktop\\py\\test.txt')
# print(f.read())
# f.close()


# import random as rnd
# print(rnd.randrange(0,100))
# print(rnd.random())


#def selam_soyle() :
#    print('merhaba')
#selam_soyle()

# import benimfonksiyonlarım
#benimfonksiyonlarım.selam_soyle()
#from benimfonksiyonlarım import selam_soyle

# def selam_soyle():
#   print('besinciden')
    
# selam_soyle()
# benimfonksiyonlarım.selam_soyle()

#from benimfonksiyonlarım import *

# import math

# print(math.pow(2,10))
# print(math.sqrt(25))
# print(math.pi)
# print(math.log(2))
# log 3 tabanında 5 nedir?

# print(math.log(5,3))


#if __name__ == '__main__' :
#     print('python yorumlayıcısının çağırdığı dosya içerisindesiniz') 

import math

a = 3
b = math.pi
c = '001'
d = 5.2
e = 1_000_000
# print(a , " " , "pi=" ,b , " " , c , " ", d , " ",sep="")
# print(   "d:{1} pi={0:.2f}".format(b,d)     )

print( "{0:>7}\t{0:0>7}\t{0}" .format(a) ) # ':>7' ile 7 basamak sağa yasladık
print( "{0}\t{0}\t{0}" .format(e) )  # '\t' ile sutunları esitledik
#  ':>7' formatının önüne kodugumuz harf-rakamı dizer

