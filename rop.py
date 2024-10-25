class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}")



class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)  # Llamada al constructor de la clase padre
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tela, color):
        super().__init__(nombre, precio, talla)
        self.tela = "algodon"
        self.color = "blanco"
        

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Color: {self.color}")
        print(f"Tipo de tela: {self.tela}")
        
class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, material, color):
        super().__init__(nombre, precio, talla)
        self.material = "lino"
        self.color = "negro"

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        
class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, marca):
        super().__init__(nombre, precio, talla)
        self.marca = "munich"
        

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Marca: {self.marca}")
    


class Carrito:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def mostrar_carrito(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda
    

productos = {
    "camisa" : {
        "color" : {
            "blanco" : 21.00,
            "negro" : 25.00,
            "azul claro" : 32.00
        },
        
        "tela" : {
            "popelina" : 35.00,
            "algodon" : 42.00,
            "oxford" : 37.00
        }
        
    },
    "pantalon" : {
        
        "material" : {
            "lino" : 65.00,
            "lycra" : 49.50,
            "seda" : 72.00
        },
        
        "color" : {
            "gris" : 46.00,
            "negro" : 15.00,
            "azul marino" : 25.00
        }
        
    },
    
    "zapato" : {
        "marca" : {
            "converse" : 51.00,
            "munich" : 63.00,
            "dude" : 34.00
        }
        
    }

}


inventario = Carrito()
precio = 0.00
precio_camisa = 0.00
precio_pantalon = 0.00
precio_zapato = 0.00

while 1:
    
    print("Bienvenido a la tienda!")
    print("Ingrese la clase de ropa")
    
    categoria = input("camisa/pantalon/zapato: ")
    
    if categoria == "camisa":
        
        print("Has elegido camisa")
        
        talla = input("Ingrese talla: ")
        tela = input("Ingrese tipo de tela: ")
        color = input("Ingrese color: ")
        
        
        precio_camisa = precio_camisa + productos["camisa"]["tela"][tela] + productos["camisa"]["color"][color]
        
        new_producto = Camisa("Camisa", precio_camisa, talla, tela, color)
        
        inventario.agregar_prenda(new_producto)
        
    elif categoria == "pantalon":
        print("Has elegido pantalon")
        
        talla = input("Ingrese talla: ")
        material = input("Ingrese tipo de material: ")
        color = input("Ingrese color: ")
        
        precio_pantalon = precio_pantalon + productos["pantalon"]["material"][material] + productos["pantalon"]["color"][color]
        
        new_producto = Pantalon("Pantalon", precio_pantalon, talla, material, color)
        
        inventario.agregar_prenda(new_producto)
        
    elif categoria == "zapato":
        print("Has elegido zapato")
        
        talla = input("Ingrese talla: ")
        marca = input("Ingrese marca: ")
        
        precio_zapato = precio_zapato + productos["zapato"]["marca"][marca]
        
        new_producto = Zapato("Zapato", precio_zapato, talla, marca)
        
        inventario.agregar_prenda(new_producto)
        
    else:
        
        precio = precio + precio_camisa + precio_zapato + precio_pantalon
    
        print("----------Gracias----------")
        print(f"----------Total a pagar: {precio}----------")
        inventario.mostrar_carrito()
        exit()
        
    