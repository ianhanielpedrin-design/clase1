nombre = "Rant"
modulos = ["Fundamentos", "Primer agente", "Memoria"]
agente = {"nombre": "Asistente", "herramientas": ["buscar", "calcular"]}

def saludar(persona):
    return "Hola " + persona + ", bienvenido al curso"

print(saludar(nombre))
print(modulos[0])
print(agente["herramientas"])

def sumar(a, b):
    return a + b

def es_herramienta(nombre):
    return nombre in agente["herramientas"]

print(sumar(2, 3))
print(es_herramienta("buscar"))
print(es_herramienta("navegar"))
