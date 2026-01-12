class Nodo:
    def __init__(self, v):
        self.dato = v
        self.sig = None

class Lista:
    def __init__(self):
        self.inicio = None

    def insertar_inicio(self, v):
        nuevo = Nodo(v)
        nuevo.sig = self.inicio
        self.inicio = nuevo

    def insertar_final(self, v):
        nuevo = Nodo(v)
        if self.inicio is None:
            self.inicio = nuevo
            return
        aux = self.inicio
        while aux.sig:
            aux = aux.sig
        aux.sig = nuevo

    def buscar(self, v):
        aux = self.inicio
        while aux:
            if aux.dato == v:
                return True
            aux = aux.sig
        return False

    def eliminar(self, v):
        if self.inicio is None:
            return

        if self.inicio.dato == v:
            self.inicio = self.inicio.sig
            return

        aux = self.inicio
        while aux.sig and aux.sig.dato != v:
            aux = aux.sig

        if aux.sig:
            aux.sig = aux.sig.sig

    def mostrar(self):
        aux = self.inicio
        while aux:
            print(aux.dato, "->", end=" ")
            aux = aux.sig
        print("NULL")

# Ejemplo
l = Lista()
l.insertar_inicio(10)
l.insertar_final(20)
l.insertar_final(30)
l.mostrar()
