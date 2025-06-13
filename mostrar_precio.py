""" Python"""
def ingresar_consulta():
    ingresar_producto = 'cocina'
    ingresar_cantidad = 5

def get_price(producto,cantidad):
    producto = producto.capitalize()    
    productos_data = {
        'Leche': 20,
        'Whisky': 40,
        'Yerba': 20,
        'Huevos': 1,
        'Laser': 25,
        'Sillon': 120,
        'Bicicleta': 200,
        'Guitarra': 750,
        'Espia': 2000,
        'Cocina': 600,
        'Heladera': 500
    }
    subtotal = productos_data[producto]* cantidad
    resultado = f"{producto}: ${productos_data[producto]} --- x {cantidad} unid. Total ${subtotal}"
    return resultado

print(get_price(ingresar_producto,ingresar_cantidad))
