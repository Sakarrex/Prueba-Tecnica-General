import requests

baseurl = "http://127.0.0.1:5000/"

def cargarProf(nombre,rubro,ubicacion,descripcion):
    data = {
    "nombre" : nombre,
    "rubro" : rubro,
    "ubicacion" : ubicacion,
    "descripcion" : descripcion
    }
    url = baseurl + "cargarprof"
    response = requests.post(url,json=data)
    return response

def listarProf():
    url = baseurl + "profesionales"
    response = requests.get(url)
    print(type(response))
    return response
    
def buscarProf(rubro,ubicacion):
    url = baseurl + ("buscarprof?rubro={}&ubicacion={}".format(rubro,ubicacion))
    response = requests.get(url)
    return response

if __name__ == '__main__':
    opcion = 5 

    while opcion != 4:
        if opcion == 1:
            nombre = input("Nombre de profesional: ")
            rubro = input("Rubro de profesional: ")
            ubicacion = input("Ubicacion de profesional: ")
            descripcion = input("Descripcion de profesional: ")
            print(cargarProf(nombre,rubro,ubicacion,descripcion).text)
        elif opcion == 2:
            print(listarProf().text)
        elif opcion == 3:
            rubro = input("Rubro: ")
            ubicacion = input("Ubicacion: ")
            print(buscarProf(rubro,ubicacion).text)
        
        opcion = int(input("Eligir opcion: \n"
        "1: cargar profesional \n"
        "2: listar porfesionales \n"
        "3: buscar profesionales por rubro o ubicacion \n" 
        "4: salir \n"))