import random
import os
import sys

class Celda:
    def __init__(self):
        self.tiene_barco = False
        self.fue_atacada = False
        self.simbolo_barco = None
        self.id_barco = None
    
    def __repr__(self):
        if self.fue_atacada:
            return 'X' if self.tiene_barco else 'O'
        return self.simbolo_barco if self.simbolo_barco else '~'

class Barco:
    TIPOS = [
        ('Portaaviones', 5, 'P'),
        ('Acorazado', 4, 'A'),
        ('Crucero', 3, 'C'),
        ('Submarino', 3, 'S'),
        ('Destructor', 2, 'D')
    ]
    
    def __init__(self, nombre, tamaño, simbolo, id_barco):
        self.nombre = nombre
        self.tamaño = tamaño
        self.simbolo = simbolo
        self.id = id_barco
        self.celdas_golpeadas = 0
    
    def recibir_impacto(self):
        self.celdas_golpeadas += 1
    
    def esta_hundido(self):
        return self.celdas_golpeadas >= self.tamaño

class Tablero:
    TAMAÑO = 10
    
    def __init__(self, nombre_jugador):
        self.nombre = nombre_jugador
        self.matriz = [[Celda() for _ in range(self.TAMAÑO)] for _ in range(self.TAMAÑO)]
        self.flota = []
        self.barcos_colocados = 0
    
    def dibujar(self, ocultar_barcos=False):
        print(f"\n{'='*40}")
        print(f"Tablero de {self.nombre}")
        print('='*40)
        print('   ' + ' '.join('ABCDEFGHIJ'))
        
        for i in range(self.TAMAÑO):
            fila = f'{i+1:2} '
            for j in range(self.TAMAÑO):
                celda = self.matriz[i][j]
                
                if celda.fue_atacada:
                    if celda.tiene_barco:
                        barco = self.obtener_barco(celda.id_barco)
                        if barco and barco.esta_hundido():
                            fila += '🔥 '
                        else:
                            fila += 'X '
                    else:
                        fila += 'O '
                elif ocultar_barcos and celda.tiene_barco:
                    fila += '~ '
                else:
                    fila += str(celda) + ' '
            print(fila)
        
        print('\n~ = Agua | O = Fallo | X = Impacto | 🔥 = Hundido\n')
    
    def obtener_barco(self, id_barco):
        for barco in self.flota:
            if barco.id == id_barco:
                return barco
        return None
    
    def es_posicion_valida(self, fila, col):
        return 0 <= fila < self.TAMAÑO and 0 <= col < self.TAMAÑO
    
    def puede_colocar_barco(self, fila_inicio, col_inicio, tamaño, es_horizontal):
        if es_horizontal:
            if col_inicio + tamaño > self.TAMAÑO:
                return False
            for c in range(col_inicio, col_inicio + tamaño):
                if self.matriz[fila_inicio][c].tiene_barco:
                    return False
        else:
            if fila_inicio + tamaño > self.TAMAÑO:
                return False
            for f in range(fila_inicio, fila_inicio + tamaño):
                if self.matriz[f][col_inicio].tiene_barco:
                    return False
        return True
    
    def colocar_barco(self, fila_inicio, col_inicio, barco, es_horizontal):
        id_barco = len(self.flota)
        nuevo_barco = Barco(barco[0], barco[1], barco[2], id_barco)
        
        if es_horizontal:
            for c in range(col_inicio, col_inicio + barco[1]):
                self.matriz[fila_inicio][c].tiene_barco = True
                self.matriz[fila_inicio][c].simbolo_barco = barco[2]
                self.matriz[fila_inicio][c].id_barco = id_barco
        else:
            for f in range(fila_inicio, fila_inicio + barco[1]):
                self.matriz[f][col_inicio].tiene_barco = True
                self.matriz[f][col_inicio].simbolo_barco = barco[2]
                self.matriz[f][col_inicio].id_barco = id_barco
        
        self.flota.append(nuevo_barco)
        self.barcos_colocados += 1
    
    def procesar_disparo(self, fila, col):
        if not self.es_posicion_valida(fila, col):
            return {'valido': False, 'mensaje': 'Coordenada fuera del tablero'}
        
        celda = self.matriz[fila][col]
        
        if celda.fue_atacada:
            return {'valido': False, 'mensaje': 'Ya disparaste aquí'}
        
        celda.fue_atacada = True
        
        if not celda.tiene_barco:
            return {'valido': True, 'impacto': False, 'mensaje': '💦 ¡Agua!'}
        
        barco = self.obtener_barco(celda.id_barco)
        barco.recibir_impacto()
        
        if barco.esta_hundido():
            return {
                'valido': True, 
                'impacto': True, 
                'hundido': True,
                'mensaje': f'🔥 ¡Hundiste el {barco.nombre}!'
            }
        
        return {'valido': True, 'impacto': True, 'mensaje': '💥 ¡Impacto!'}
    
    def todos_barcos_hundidos(self):
        return all(barco.esta_hundido() for barco in self.flota)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def parsear_coordenada(coord):
    if len(coord) < 2:
        return None
    
    col = ord(coord[0].upper()) - ord('A')
    try:
        fila = int(coord[1:]) - 1
    except ValueError:
        return None
    
    if 0 <= col < 10 and 0 <= fila < 10:
        return (fila, col)
    return None

def fase_colocacion(tablero):
    print(f"\n{'*'*50}")
    print(f"{tablero.nombre}, ¡es tu turno de colocar los barcos!")
    print('*'*50)
    input("\nPresiona Enter cuando estés listo (el otro jugador debe apartar la vista)...")
    limpiar_pantalla()
    
    for tipo_barco in Barco.TIPOS:
        while True:
            tablero.dibujar()
            print(f"\nColocando: {tipo_barco[0]} (Tamaño: {tipo_barco[1]} casillas)")
            
            coord = input("Coordenada inicial (ej: A1): ").strip()
            posicion = parsear_coordenada(coord)
            
            if not posicion:
                print("❌ Coordenada inválida. Usa formato A1 a J10")
                input("Presiona Enter para intentar de nuevo...")
                continue
            
            orientacion = input("Orientación (H=horizontal / V=vertical): ").strip().upper()
            
            if orientacion not in ['H', 'V']:
                print("❌ Orientación inválida. Usa H o V")
                input("Presiona Enter para intentar de nuevo...")
                continue
            
            es_horizontal = (orientacion == 'H')
            
            if tablero.puede_colocar_barco(posicion[0], posicion[1], tipo_barco[1], es_horizontal):
                tablero.colocar_barco(posicion[0], posicion[1], tipo_barco, es_horizontal)
                limpiar_pantalla()
                print(f"✅ {tipo_barco[0]} colocado correctamente!")
                break
            else:
                print("❌ No puedes colocar el barco ahí. Intenta otra posición.")
                input("Presiona Enter para intentar de nuevo...")
    
    tablero.dibujar()
    print(f"\n✅ {tablero.nombre}, todos tus barcos están listos!")
    input("\nPresiona Enter para continuar...")
    limpiar_pantalla()

def turno_jugador(atacante, defensor):
    print(f"\n{'='*50}")
    print(f"Turno de {atacante.nombre}")
    print('='*50)
    
    print(f"\n--- Tu tablero ---")
    atacante.dibujar()
    
    print(f"\n--- Tablero enemigo de {defensor.nombre} ---")
    defensor.dibujar(ocultar_barcos=True)
    
    while True:
        coord = input(f"\n{atacante.nombre}, ingresa tu disparo (ej: B5): ").strip()
        posicion = parsear_coordenada(coord)
        
        if not posicion:
            print("❌ Coordenada inválida")
            continue
        
        resultado = defensor.procesar_disparo(posicion[0], posicion[1])
        
        if not resultado['valido']:
            print(f"❌ {resultado['mensaje']}")
            continue
        
        print(f"\n{resultado['mensaje']}")
        
        if defensor.todos_barcos_hundidos():
            return True
        
        input(f"\nPresiona Enter para pasar el turno a {defensor.nombre}...")
        limpiar_pantalla()
        return False

def main():
    print("╔" + "═"*48 + "╗")
    print("║" + " "*15 + "BATALLA NAVAL" + " "*20 + "║")
    print("║" + " "*15 + "2 JUGADORES" + " "*22 + "║")
    print("╚" + "═"*48 + "╝")
    
    jugador1_nombre = input("\nNombre del Jugador 1: ").strip() or "Jugador 1"
    jugador2_nombre = input("Nombre del Jugador 2: ").strip() or "Jugador 2"
    
    print(f"\n¡Bienvenidos {jugador1_nombre} y {jugador2_nombre}!")
    input("\nPresiona Enter para comenzar...")
    limpiar_pantalla()
    
    tablero1 = Tablero(jugador1_nombre)
    tablero2 = Tablero(jugador2_nombre)
    
    # Fase de colocación
    fase_colocacion(tablero1)
    fase_colocacion(tablero2)
    
    # Decidir quién empieza
    jugadores = [(tablero1, tablero2), (tablero2, tablero1)]
    if random.random() < 0.5:
        jugadores.reverse()
    
    print(f"\n🎲 ¡{jugadores[0][0].nombre} ha sido elegido para disparar primero!")
    input("\nPresiona Enter para comenzar la batalla...")
    limpiar_pantalla()
    
    # Loop principal del juego
    turno = 0
    while True:
        atacante, defensor = jugadores[turno % 2]
        
        hay_ganador = turno_jugador(atacante, defensor)
        
        if hay_ganador:
            print("\n" + "="*50)
            print(f"🎉 ¡{atacante.nombre} GANA LA BATALLA! 🎉")
            print(f"Has hundido toda la flota de {defensor.nombre}")
            print("="*50)
            break
        
        turno += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Juego terminado. ¡Hasta pronto!")
        sys.exit(0)