class Cola:
    def __init__(self, size):
        self.frente = -1
        self.atras = -1
        self.tam = size
        self.arr = [0] * size

    def estavacia(self):
        return self.frente == -1

    def estallena(self):
        return self.atras == self.tam - 1

    def enqueue(self, valor):
        if self.estallena():
            print("Cola llena")
            return
        if self.frente == -1:
            self.frente = 0
        self.atras += 1
        self.arr[self.atras] = valor

    def dequeue(self):
        if self.estavacia():
            print("Cola vacía")
            return -1
        x = self.arr[self.frente]
        if self.frente == self.atras:
            self.frente = self.atras = -1
        else:
            self.frente += 1
        return x

    def peek(self):
        if self.estavacia():
            return -1
        return self.arr[self.frente]


# Ejemplo
q = Cola(5)
q.enqueue(10)
q.enqueue(20)
print("Frente:", q.peek())
print("Dequeue:", q.dequeue())
