MAX_SIZE = 100  # Tamaño máximo de la pila
stack = [None] * MAX_SIZE  # Lista para almacenar los elementos de la pila
top = -1  # Índice del elemento superior de la pila

# Función para agregar un elemento a la pila
def push(item):
    global top
    if top == MAX_SIZE - 1:  # Verifica si la pila está llena
        print("Stack Overflow")  # Mensaje de error
        return  # Sale de la función
    top += 1  # Incrementa el índice
    stack[top] = item  # Agrega el elemento

# Función para eliminar y retornar el elemento superior de la pila
def pop():
    global top
    if top == -1:  # Verifica si la pila está vacía
        print("Stack Underflow")  # Mensaje de error
        return -1  # Retorna -1 para indicar que la pila está vacía
    item = stack[top]  # Guarda el elemento superior
    top -= 1  # Decrementa el índice
    return item  # Retorna el elemento

# Función para ver el elemento superior sin eliminarlo
def peek():
    if top == -1:  # Verifica si la pila está vacía
        print("Pila vacía")  # Mensaje de error
        return -1  # Retorna -1 para indicar que la pila está vacía
    return stack[top]  # Retorna el elemento superior sin modificar el índice

# Función para verificar si la pila está vacía
def is_empty():
    return top == -1  # Retorna True si está vacía, False en caso contrario

# Función para verificar si la pila está llena
def is_full():
    return top == MAX_SIZE - 1  # Retorna True si está llena, False en caso contrario

# Ejemplo de uso de la pila
push(10)  # Agrega elementos a la pila
push(20)  # agrega otro elemento
push(30)  # agrega otro elemento

print(f"Elemento Superior: {peek()}")  # Muestra el elemento superior
print(f"Extrae elemento: {pop()}")  # Elimina y muestra el elemento superior
print(f"Elemento Superior: {peek()}")  # Muestra el nuevo elemento superior