""" funcion para ingresar los productos, calcularlos y almacenarlos """

def enter_products():
    
    buying_data={}
    ingresar_productos = True
    
    while ingresar_productos:
        iniciar = input("Presione 'A' para agregar un producto o 'Q' para salir.").upper()
        if iniciar == "A":
            cantidad = int(input("Ingrese cantidad: "))
            producto = str(input("Ingrese producto: "))
            buying_data.update({producto:cantidad})                         
        elif iniciar ==  "Q":
            ingresar_productos = False
        else:
            print("Por favor seleccione la opción correcta.")
            iniciar = input("Presione 'A' para agregar un producto o 'Q' para salir.").upper()
            
    return buying_data
 

enter_products()

   
