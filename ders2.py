# # print(type(8.5) , 'kesir')

# # x = "5" # str
# # y = 5  # int
# # z = 5.0  # float
# # print( x == y )
# # x == y ?  eşit değildir.  print ( type(x) == type(y))
# # y == z ? eşit

# # a = 100
# # b = " bir daha yaramazlık yapmayacağım! \n"
# # print ( a * b )

# # a = 5
# # b = 'dünya'
# # c = str(a)+ ' ' + b
# # print(c)

# t = "False"
# print(bool(t))

# t = 0
# print(t == False)
# t=1
# print(t==True)

# import random
# rastgele = random.randrange(1,10)
# kul_veri = int(input("1 ve 10 arası rastgele sayo giriniz:"))
# if kul_veri == rastgele:
#     print('tebrikler sayıyı buldunuz...')
# else:
#     print("bilgisayarın tuttuğu sayı:" , rastgele)
#     print("sizin girdiğiniz sayı:" , kul_veri)
#     print("tekrar deneyiniz")

# iç içe if durumları
# a , b , c = 1 , 2 , 3

# if 3 > 1 :
#     print("3 bir rakamından büyüktür")
#     if 3 > 2 :
#         print("2 rakamından da büyüktür")
#         if 3 == 3 :
#             print("bu değerler birbirlerine eşittir")
#         else:
#             print("eşit değildir")
#         print("bu kimin altında")
#     print("bu kimin altında")
# else: 
#     print("3 rakamından büyük değil")

# birden fazl şart bulunduran durumlar

# if 3 > 2 and 2 > 1 :
#     print("iki şart da doğru")
# else:
#     print(" ikisi de veya birisi yanlış")

# if 3 >= 2 and 3 <= 4 and 3 < 4 and 3!=4:
#     print("tüm şartlar doğru")

# print( True and True   )
# print(1 and 1)
# print(False and False)
# print(0 and 0)
# print(True and False)
# print(0 and 1)
# print(False and True)


# print( True or True )
# print( False or True )
# print( False or False )

# if (True and False) or (False or True) :
#     if ((True and False) or False) or True :
#         if True and (False or (False or True)) :
#             if True and ((False or False) or True) :
#                 print("Çalışır mı?")

# import math

# vize = int(input("vize sonucunu giriniz:"))
# if vize < 50 :
#     final_için_gerekli_not=((50 - 0.4 * vize) / 0.6 )
#     print("final için almanız gereken not:" , math.ceil(final_için_gerekli_not))
# else :
#     print("final için almanız gereken not: 50")






