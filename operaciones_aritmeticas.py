
class OperacionesAritmeticas:
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2

    # Suma los números almacenados en el objeto (self)
    def sumar(self):
        return self.numero1 + self.numero2

    # Suma dos números recibidos por parámetros, ignorando los del objeto
    def sumar_dos_numeros(self, n1, n2):
        return n1 + n2

# Ejemplo de uso:
operacion = OperacionesAritmeticas(10, 5)

print(f"Suma de instancia: {operacion.sumar()}")          # Resultado: 15
print(f"Suma de parámetros: {operacion.sumar_dos_numeros(20, 30)}") # Resultado: 50
