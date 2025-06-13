""" Python"""
def get_price(cantidad,producto):
    producto = producto.capitalize()    
    productos_data =  {
        'Leche': 20,
        'Whisky': 40,
        'Yerba': 20,
        'Huevos': 1,
        'Laser': 25,
        'Sillon': 120,
        'Bicicleta': 200,
        'Guitarra': 750,
        'Aspiradora': 2000,
        'Cocina': 600,
        'Heladera': 500
    }
    
    db_productos = productos_data[producto]
    db_precio = productos_data[cantidad]
    
    subtotal = db_productos * db_precio
    resultado = f"{producto} || Precio: ${productos_data[producto]} | Unidades: {cantidad} | Total: ${subtotal}"
    
    return resultado
