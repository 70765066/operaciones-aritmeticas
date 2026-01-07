class AlgoritmoEuclides:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obtener_mcd(self):
        """
        Calcula el MCD usando el método de residuos sucesivos.
        """
        # Trabajamos con copias para no modificar los atributos originales
        x = abs(self.a)
        y = abs(self.b)
        
        while y != 0:
            # Aplicamos: mcd(x, y) = mcd(y, x % y)
            residuo = x % y
            x = y
            y = residuo
        
        return x

    def imprimir_proceso(self):
        mcd = self.obtener_mcd()
        print(f"Resultado: El MCD de {self.a} y {self.b} es {mcd}")

# --- Ejecución ---
num1 = 105
num2 = 45

calculadora = AlgoritmoEuclides(num1, num2)
calculadora.imprimir_proceso()