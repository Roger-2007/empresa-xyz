#US1/create register

users = []
def createUser():
    user = []
    id = int(input("Ingrese su documento de identidad"))
    user.append(id)
    user_name = input("Ingrese su nombre")
    user.append(user_name)
    user_last_name = input("Ingrese su apellido")
    user.append(user_last_name)
    phone = input("Ingrese su numero de telefono")    
    user.append(phone)      
    user_email = input("Ingrese su correo electronico")
    user.append(user_email)
    user_password = input("Ingrese su contraseña")
    user.append(user_password)
    users.append(user)

def loginUser():
    emailLogin = input("Ingrese su email")
    passwordLogin = input("Ingrese su contraseña")
    for user in users:
        if(user[4]==emailLogin and user[5]==passwordLogin):
            print("Usted ha inciado sesion correctamente")

        else:
           print("Correo o contraseña incorrectos")

option = int(input("\nIngrese un numero\n1. Crear Usuario\n2. Iniciar sesion\n3. Salir"))
while option!=3:
    match option:
        case 1: createUser()
        case 2: loginUser()
        case 3: print("Te has salido correctamente")
    option = int(input("\nIngrese un numero\n1. Crear Usuario\n2. Iniciar sesion\n3. Salir"))
        

