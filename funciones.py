

def hitAPI(host="https://api.dojo.com/api/v1/auth"):
    print("check el statis del API")
    return True


def login(usuario, password, host="https://api.dojo.com/api/v1/auth", hitAPI):
    print("iniciando sesion")
    print(usuario, password)

    print(f"consutlando {host}")
    if usuario == "dojo" and password == "1234":
        return True

    return False




salida = login("dojo", "1234", hitAPI)

# print(salida)

# print(hitAPI)


