from excepciones import WrongPasswordException
class Usuario:
    def __init__(self, nombre, apellidos, nombre_usuario, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nombre_usuario = nombre_usuario
        self.password = password

    def login(self, password):
        if self.password == password:
            return True
        else:
            raise WrongPasswordException("")

user = Usuario("Francisco", "Martínez", "KikoMartinez", "KikoMartinez.55")

lista_usuarios = []
lista_usuarios.append(user)

usr = input("Nombre de usuario: ")
pas = input("Contraseña: ")

for usuario_actual in lista_usuarios:
    if usuario_actual.nombre_usuario == usr:
        try:
            if usuario_actual.login(pas):
                print("Usuario logueado con éxito.")
        except WrongPasswordException:
            print("La contraseña introducida no es correcta.")
    else:
        print("El usuario introducido no existe.")