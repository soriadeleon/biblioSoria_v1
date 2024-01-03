#selectores.py
#Guarda los nombres de los selectores por pantalla
#Los retorna cuando se lo solicitan

#Defino la funcion que devuelvo los datos
def obtener_selectores_home(): 

    selectores_home = {
        "link_login" : "Login"

    }

    
    return selectores_home


def obtener_selectores_login():
    
    selectores_login = {
        "txt_usuario" : "username",
        "txt_clave"   : "password",
        "bt_ingresar" : "loginButton"
    }

#Devuelve los datos de los nombres de los selectores del login

    return selectores_login 