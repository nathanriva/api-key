from conections import session
from models import Users

def CreateUser(newUser, newPassword):
    newClient = Users(username=newUser, password=newPassword)
    try:
        session.add(newClient)
        session.commit()
        return 'se a agregado un nuevo usuario'
    except:
        return 'hubo un error'


    #Corroborar cliente
def CheckUser(user, password):
    client = session.query(Users).filter(Users.username == user).first()

    #VER 0.2
    if (client is not None) and (password == client.password):
        return 'pasas'
    return 'usario o contraseña es incorrecto'  

"""
    #VER 0.1
    if client is not None:
        if client.password == password:
            return 'pasas'
        return 'la contraseña es incorrecta'
    return 'el usuario no existe'
"""         
