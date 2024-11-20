

# tipo de dato String

usuario = "rosa"

print( type(usuario) )

print( type(123) )

data = str(123)

print(type(data))


# print(dir(usuario))

email = "henry@gmail.com"
edad = 12

#resumen = " mi correo es {} y esta verificado  y la edad es {} ".format(email, edad)

resumen = f"mi correo es {email.upper()} y esta verificado  y la edad es {edad}"

print(resumen)

resumen = resumen.replace("GMAIL", "hotmail")


print(resumen)

print( resumen.find("@") )


# tipo de dato numero

precio = 123
precioEspecial = 9.5

print(type(precio))
print(type(precioEspecial))

int()
float()

precioNews = float("12.78")

print(type(precioNews))

#operacions basicas

suma = precio + 3
precio += 3
precio -= 3
precio *= 3
precio /= 3


# tipo de dato bool

isMemberVip = True
isAdmin = False

# print(type(isMemberVip))

# print(isAdmin)
# bool()


# tipo de dato listas

stack = [
    "python", "nodejs", "perl", "golang"
    ]

framework = [
    "django", "tensorflow", "opencv"
]

#list()

print(stack)

print(type(stack))

stack.append("swift")
stack.append("javascript")

print(stack)


print(stack[0])
print(stack[1])


print( len(stack) )


print(stack[-1])

stack.remove("golang")

# stack.pop()



# stack.copy()
stack.insert(1, "django")

stack.extend(framework)


print(stack)



# tipo de dato Dict

auto = {
    "color" : "verde",
    "precio": 999,
    "modelo": "tesla" 
}

print(auto)
print(type(auto))

# dict()

# print(auto["colorPrinicpal"])
print(auto.get("colorPrinicpal", "blanco"))

print( auto.keys())

auto["velociad"] = "500km/h"

auto["modelo"] = "ninssan x"


del auto["velociad"]

# auto.pop("color")

print(auto["modelo"])


print(auto)



# tuples

accessToken = ("at-01010011", "rt-918298128198291")
print(accessToken)