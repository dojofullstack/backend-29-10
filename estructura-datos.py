import time

""" Condciones """

isAdmin = False
rol = "editor"

# if isAdmin:
#     print("si es admin!")
#     name = input("cual es tu nombre?")
#     print(name)

#     if rol == "editor":
#         print("puedes crear publicaciones")
# else:
#     print("Eres invitado!!")


### codiciones multiples


planType = "Anonymous"

# if planType == "Free":
#     print("solo tienes 3 creditos")
# elif  planType == "Premium":
#     print("Tienes 10 creditos")
# elif  planType == "Gold":
#     print("Tienes 100 creditos")
# else:
#     print("solo tienes 0 creditos")





## iteradores for y while

marcasAuto = ["hynuday", "toyota", "tesla", "mercedez" ]

# for elemento in marcasAuto:
#     print(elemento)
#     print(marcasAuto.index(elemento))


for elemento in enumerate(marcasAuto) :
    index, item =  elemento
    # print(index)
    # print(item)
    if item == "tesla":
        print("no disponible en PERU")



planType = "Free"
contador = 0

while planType == "Free":
    time.sleep(1)
    print("procesando...")
    contador += 1
    if contador >= 5:
        break
        # planType = None


