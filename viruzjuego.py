import random
import os
import sys
import time

# Emojis para el juego
AGUA = "🌊"
BARCO = "🚢"
IMPACTO = "💥"
FALLO = "❌"
HUNDIDO = "💀"
OCULTO = "🔵"

class Barco:
    def __init__(self, nombre, tamaño, emoji):
        self.nombre = nombre
        self.tamaño = tamaño
        self.emoji = emoji
        self.posiciones = []
        self.impactos = 0
    
    def esta_hundido(self):
        return self.impactos >= self.tamaño
    
    def recibir_impacto(self):
        self.impactos += 1

class Jugador:
    def __init__(self, nombre, es_maquina=False):
        self.nombre = nombre
        self.es_maquina = es_maquina
        self.tablero_propio = [[AGUA for _ in range(10)] for _ in range(10)]
        self.tablero_ataques = [[AGUA for _ in range(10)] for _ in range(10)]
        self.barcos = []
        self.puntuacion = 0
        self.racha_actual = 0
        self.mejor_racha = 0
        self.ataques_realizados = 0
        self.ataques_acertados = 0
        
        # Para la IA
        self.modo_caceria = False
        self.ultimo_impacto = None
        self.direcciones_probadas = []
        self.posibles_objetivos = []
    
    def crear_flota(self):
        self.barcos = [
            Barco("Portaaviones", 5, "🛩️"),
            Barco("Acorazado", 4, "⚓"),
            Barco("Crucero", 3, "🚢"),
            Barco("Submarino", 3, "🔱"),
            Barco("Destructor", 2, "⛵")
        ]
    
    def puede_colocar_barco(self, fila, col, tamaño, horizontal):
        if horizontal:
            if col + tamaño > 10:
                return False
            for i in range(tamaño):
                if self.tablero_propio[fila][col + i] != AGUA:
                    return False
                # Verificar espacio alrededor
                for df in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nf, nc = fila + df, col + i + dc
                        if 0 <= nf < 10 and 0 <= nc < 10:
                            if self.tablero_propio[nf][nc] != AGUA:
                                return False
        else:
            if fila + tamaño > 10:
                return False
            for i in range(tamaño):
                if self.tablero_propio[fila + i][col] != AGUA:
                    return False
                # Verificar espacio alrededor
                for df in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nf, nc = fila + i + df, col + dc
                        if 0 <= nf < 10 and 0 <= nc < 10:
                            if self.tablero_propio[nf][nc] != AGUA:
                                return False
        return True
    
    def colocar_barco(self, barco, fila, col, horizontal):
        barco.posiciones = []
        if horizontal:
            for i in range(barco.tamaño):
                self.tablero_propio[fila][col + i] = barco.emoji
                barco.posiciones.append((fila, col + i))
        else:
            for i in range(barco.tamaño):
                self.tablero_propio[fila + i][col] = barco.emoji
                barco.posiciones.append((fila + i, col))
    
    def colocar_barcos_aleatorio(self):
        for barco in self.barcos:
            colocado = False
            intentos = 0
            while not colocado and intentos < 1000:
                fila = random.randint(0, 9)
                col = random.randint(0, 9)
                horizontal = random.choice([True, False])
                
                if self.puede_colocar_barco(fila, col, barco.tamaño, horizontal):
                    self.colocar_barco(barco, fila, col, horizontal)
                    colocado = True
                intentos += 1
    
    def recibir_ataque(self, fila, col):
        celda = self.tablero_propio[fila][col]
        
        if celda == AGUA:
            self.tablero_propio[fila][col] = FALLO
            return "agua", None
        elif celda in [FALLO, IMPACTO, HUNDIDO]:
            return "repetido", None
        else:
            # Es un barco
            for barco in self.barcos:
                if (fila, col) in barco.posiciones:
                    barco.recibir_impacto()
                    if barco.esta_hundido():
                        # Marcar todas las posiciones como hundidas
                        for f, c in barco.posiciones:
                            self.tablero_propio[f][c] = HUNDIDO
                        return "hundido", barco
                    else:
                        self.tablero_propio[fila][col] = IMPACTO
                        return "impacto", barco
        return "agua", None
    
    def todos_barcos_hundidos(self):
        return all(barco.esta_hundido() for barco in self.barcos)
    
    def actualizar_puntuacion(self, resultado):
        if resultado in ["impacto", "hundido"]:
            self.racha_actual += 1
            self.mejor_racha = max(self.mejor_racha, self.racha_actual)
            # Puntuación base + bonus por racha
            puntos = 10 + (self.racha_actual - 1) * 5
            self.puntuacion += puntos
            return puntos
        else:
            self.racha_actual = 0
            return 0

class JuegoBatallaNaval:
    def __init__(self):
        self.jugador1 = None
        self.jugador2 = None
        self.turno_actual = 1
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_tablero(self, tablero, titulo, ocultar_barcos=False):
        print(f"\n{titulo}")
        print("    A  B  C  D  E  F  G  H  I  J")
        print("  ╔══════════════════════════════╗")
        
        for i in range(10):
            print(f"{i} ║", end=" ")
            for j in range(10):
                celda = tablero[i][j]
                if ocultar_barcos and celda not in [AGUA, FALLO, IMPACTO, HUNDIDO]:
                    print(OCULTO, end=" ")
                else:
                    print(celda, end=" ")
            print("║")
        print("  ╚══════════════════════════════╝")
    
    def mostrar_tableros_lado_a_lado(self, jugador, mostrar_enemigo=True):
        self.limpiar_pantalla()
        print(f"\n{'='*60}")
        print(f"  {jugador.nombre.upper()} - Puntuación: {jugador.puntuacion} | "
              f"Racha: {jugador.racha_actual} 🔥 | Mejor: {jugador.mejor_racha}")
        print(f"  Precisión: {jugador.ataques_acertados}/{jugador.ataques_realizados if jugador.ataques_realizados > 0 else 0}")
        print(f"{'='*60}")
        
        print("\n     TU FLOTA                          ATAQUES AL ENEMIGO")
        print("    A  B  C  D  E  F  G  H  I  J        A  B  C  D  E  F  G  H  I  J")
        print("  ╔══════════════════════════════╗    ╔══════════════════════════════╗")
        
        for i in range(10):
            # Tablero propio
            print(f"{i} ║", end=" ")
            for j in range(10):
                print(jugador.tablero_propio[i][j], end=" ")
            print("║", end="    ")
            
            # Tablero de ataques
            if mostrar_enemigo:
                print(f"{i} ║", end=" ")
                for j in range(10):
                    print(jugador.tablero_ataques[i][j], end=" ")
                print("║")
            else:
                print()
        
        print("  ╚══════════════════════════════╝    ╚══════════════════════════════╝")
        
        # Mostrar estado de los barcos
        print("\n  ESTADO DE TU FLOTA:")
        for barco in jugador.barcos:
            estado = f"{barco.impactos}/{barco.tamaño}"
            if barco.esta_hundido():
                print(f"  {HUNDIDO} {barco.nombre} - HUNDIDO")
            else:
                print(f"  {barco.emoji} {barco.nombre} - {estado} impactos")
    
    def obtener_coordenadas(self):
        while True:
            try:
                coord = input("\n  Ingresa coordenadas (ej: A5, B3): ").strip().upper()
                if len(coord) < 2:
                    print("  ❌ Coordenada inválida. Intenta de nuevo.")
                    continue
                
                col_letra = coord[0]
                fila = int(coord[1:])
                
                if col_letra not in "ABCDEFGHIJ" or fila < 0 or fila > 9:
                    print("  ❌ Coordenada fuera de rango. Intenta de nuevo.")
                    continue
                
                col = ord(col_letra) - ord('A')
                return fila, col
            except ValueError:
                print("  ❌ Formato inválido. Usa letra+número (ej: A5)")
            except KeyboardInterrupt:
                print("\n\n  ¡Hasta luego!")
                sys.exit(0)
    
    def colocar_barcos_manual(self, jugador):
        self.limpiar_pantalla()
        print(f"\n{jugador.nombre}, coloca tus barcos!")
        
        for barco in jugador.barcos:
            while True:
                self.mostrar_tablero(jugador.tablero_propio, f"  Colocando: {barco.emoji} {barco.nombre} (Tamaño: {barco.tamaño})")
                
                print(f"\n  {barco.emoji} {barco.nombre} - Tamaño: {barco.tamaño}")
                fila, col = self.obtener_coordenadas()
                
                orientacion = input("  Orientación (H)orizontal o (V)ertical: ").strip().upper()
                horizontal = orientacion == 'H'
                
                if jugador.puede_colocar_barco(fila, col, barco.tamaño, horizontal):
                    jugador.colocar_barco(barco, fila, col, horizontal)
                    break
                else:
                    print("  ❌ No se puede colocar el barco ahí. Intenta otra posición.")
                    time.sleep(2)
        
        self.mostrar_tablero(jugador.tablero_propio, f"  Flota de {jugador.nombre} - ¡Lista para el combate!")
        input("\n  Presiona ENTER para continuar...")
    
    def ataque_ia_inteligente(self, ia, objetivo):
        # Modo cacería: buscar barcos adyacentes después de un impacto
        if ia.modo_caceria and ia.ultimo_impacto:
            fila, col = ia.ultimo_impacto
            direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izq, der
            
            # Primero intentar direcciones no probadas adyacentes al último impacto
            for df, dc in direcciones:
                if (df, dc) not in ia.direcciones_probadas:
                    nf, nc = fila + df, col + dc
                    if 0 <= nf < 10 and 0 <= nc < 10:
                        if ia.tablero_ataques[nf][nc] == AGUA:
                            return nf, nc
            
            # Si hay objetivos pendientes en la cola
            if ia.posibles_objetivos:
                return ia.posibles_objetivos.pop(0)
            
            # Si no hay más objetivos, salir del modo cacería
            ia.modo_caceria = False
            ia.ultimo_impacto = None
            ia.direcciones_probadas = []
        
        # Modo búsqueda: patrón de tablero de ajedrez para ser más eficiente
        intentos = 0
        while intentos < 100:
            fila = random.randint(0, 9)
            col = random.randint(0, 9)
            
            # Patrón de tablero de ajedrez (mejora las probabilidades)
            if (fila + col) % 2 == 0 and ia.tablero_ataques[fila][col] == AGUA:
                return fila, col
            
            # Si no encuentra en patrón, aceptar cualquier celda libre
            if ia.tablero_ataques[fila][col] == AGUA:
                return fila, col
            
            intentos += 1
        
        # Última opción: buscar cualquier celda disponible
        for i in range(10):
            for j in range(10):
                if ia.tablero_ataques[i][j] == AGUA:
                    return i, j
        
        return None, None
    
    def realizar_ataque(self, atacante, defensor):
        if atacante.es_maquina:
            print(f"\n  🤖 {atacante.nombre} está pensando...")
            time.sleep(1)
            fila, col = self.ataque_ia_inteligente(atacante, defensor)
            if fila is None:
                return False
            col_letra = chr(col + ord('A'))
            print(f"  🎯 {atacante.nombre} ataca en {col_letra}{fila}!")
            time.sleep(1)
        else:
            print(f"\n  🎯 {atacante.nombre}, es tu turno de atacar!")
            fila, col = self.obtener_coordenadas()
            
            # Verificar si ya atacó esa posición
            if atacante.tablero_ataques[fila][col] != AGUA:
                print("  ⚠️  Ya atacaste esa posición. Intenta otra.")
                time.sleep(2)
                return False
        
        atacante.ataques_realizados += 1
        resultado, barco = defensor.recibir_ataque(fila, col)
        
        if resultado == "repetido":
            print("  ⚠️  Ya atacaste esa posición.")
            time.sleep(2)
            return False
        
        # Actualizar tablero de ataques del atacante
        if resultado == "agua":
            atacante.tablero_ataques[fila][col] = FALLO
            print(f"\n  {FALLO} ¡Agua! Fallaste.")
            puntos = atacante.actualizar_puntuacion("agua")
            if atacante.es_maquina:
                atacante.modo_caceria = False
        elif resultado == "impacto":
            atacante.tablero_ataques[fila][col] = IMPACTO
            atacante.ataques_acertados += 1
            print(f"\n  {IMPACTO} ¡IMPACTO! Le diste a un {barco.nombre}!")
            puntos = atacante.actualizar_puntuacion("impacto")
            print(f"  💰 +{puntos} puntos (Racha: {atacante.racha_actual} 🔥)")
            
            # Activar modo cacería para la IA
            if atacante.es_maquina:
                atacante.modo_caceria = True
                atacante.ultimo_impacto = (fila, col)
                # Agregar posiciones adyacentes a objetivos posibles
                for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nf, nc = fila + df, col + dc
                    if 0 <= nf < 10 and 0 <= nc < 10:
                        if atacante.tablero_ataques[nf][nc] == AGUA:
                            if (nf, nc) not in atacante.posibles_objetivos:
                                atacante.posibles_objetivos.append((nf, nc))
        elif resultado == "hundido":
            atacante.ataques_acertados += 1
            # Marcar todas las posiciones del barco hundido
            for f, c in barco.posiciones:
                atacante.tablero_ataques[f][c] = HUNDIDO
            print(f"\n  {HUNDIDO} ¡HUNDIDO! ¡Destruiste el {barco.nombre}! {barco.emoji}")
            puntos = atacante.actualizar_puntuacion("hundido")
            print(f"  💰 +{puntos} puntos (Racha: {atacante.racha_actual} 🔥)")
            
            # Salir del modo cacería después de hundir
            if atacante.es_maquina:
                atacante.modo_caceria = False
                atacante.ultimo_impacto = None
                atacante.posibles_objetivos = []
                atacante.direcciones_probadas = []
        
        time.sleep(2)
        return True
    
    def jugar_un_jugador(self):
        self.limpiar_pantalla()
        print("\n" + "="*60)
        print("  🎮 MODO UN JUGADOR - BATALLA CONTRA LA MÁQUINA")
        print("="*60)
        
        nombre = input("\n  Ingresa tu nombre: ").strip()
        if not nombre:
            nombre = "Jugador"
        
        self.jugador1 = Jugador(nombre, False)
        self.jugador2 = Jugador("🤖 Computadora", True)
        
        self.jugador1.crear_flota()
        self.jugador2.crear_flota()
        
        # Preguntar si quiere colocar barcos manual o automáticamente
        print("\n  ¿Cómo quieres colocar tus barcos?")
        print("  1. Manualmente")
        print("  2. Automáticamente")
        
        while True:
            opcion = input("\n  Selecciona (1/2): ").strip()
            if opcion == "1":
                self.colocar_barcos_manual(self.jugador1)
                break
            elif opcion == "2":
                self.jugador1.colocar_barcos_aleatorio()
                self.mostrar_tablero(self.jugador1.tablero_propio, f"  Flota de {self.jugador1.nombre}")
                input("\n  Barcos colocados automáticamente. Presiona ENTER...")
                break
            else:
                print("  ❌ Opción inválida.")
        
        # La IA coloca sus barcos
        self.jugador2.colocar_barcos_aleatorio()
        
        # Bucle principal del juego
        turno = 1
        while True:
            if turno == 1:
                self.mostrar_tableros_lado_a_lado(self.jugador1)
                if self.realizar_ataque(self.jugador1, self.jugador2):
                    if self.jugador2.todos_barcos_hundidos():
                        self.mostrar_victoria(self.jugador1, self.jugador2)
                        break
                    turno = 2
            else:
                self.mostrar_tableros_lado_a_lado(self.jugador2, mostrar_enemigo=False)
                if self.realizar_ataque(self.jugador2, self.jugador1):
                    if self.jugador1.todos_barcos_hundidos():
                        self.mostrar_victoria(self.jugador2, self.jugador1)
                        break
                    turno = 1
    
    def jugar_dos_jugadores(self):
        self.limpiar_pantalla()
        print("\n" + "="*60)
        print("  👥 MODO DOS JUGADORES")
        print("="*60)
        
        nombre1 = input("\n  Jugador 1, ingresa tu nombre: ").strip()
        nombre2 = input("  Jugador 2, ingresa tu nombre: ").strip()
        
        if not nombre1:
            nombre1 = "Jugador 1"
        if not nombre2:
            nombre2 = "Jugador 2"
        
        self.jugador1 = Jugador(nombre1, False)
        self.jugador2 = Jugador(nombre2, False)
        
        self.jugador1.crear_flota()
        self.jugador2.crear_flota()
        
        # Colocar barcos de ambos jugadores
        self.colocar_barcos_manual(self.jugador1)
        self.limpiar_pantalla()
        print("\n  ¡Turno del siguiente jugador!")
        input("  Presiona ENTER cuando esté listo...")
        self.colocar_barcos_manual(self.jugador2)
        
        # Bucle principal del juego
        turno = 1
        while True:
            if turno == 1:
                self.limpiar_pantalla()
                print(f"\n  🎯 Turno de {self.jugador1.nombre}")
                input("  Presiona ENTER para continuar...")
                
                self.mostrar_tableros_lado_a_lado(self.jugador1)
                if self.realizar_ataque(self.jugador1, self.jugador2):
                    if self.jugador2.todos_barcos_hundidos():
                        self.mostrar_victoria(self.jugador1, self.jugador2)
                        break
                    turno = 2
                    input("\n  Presiona ENTER para pasar el turno...")
            else:
                self.limpiar_pantalla()
                print(f"\n  🎯 Turno de {self.jugador2.nombre}")
                input("  Presiona ENTER para continuar...")
                
                self.mostrar_tableros_lado_a_lado(self.jugador2)
                if self.realizar_ataque(self.jugador2, self.jugador1):
                    if self.jugador1.todos_barcos_hundidos():
                        self.mostrar_victoria(self.jugador2, self.jugador1)
                        break
                    turno = 1
                    input("\n  Presiona ENTER para pasar el turno...")
    
    def mostrar_victoria(self, ganador, perdedor):
        self.limpiar_pantalla()
        print("\n" + "="*60)
        print("  🏆 ¡FIN DE LA BATALLA! 🏆")
        print("="*60)
        
        print(f"\n  🎉 ¡{ganador.nombre} HA GANADO! 🎉\n")
        
        print("  📊 ESTADÍSTICAS FINALES:")
        print("\n  " + ganador.nombre.upper())
        print(f"  💰 Puntuación Total: {ganador.puntuacion}")
        print(f"  🔥 Mejor Racha: {ganador.mejor_racha}")
        print(f"  🎯 Precisión: {ganador.ataques_acertados}/{ganador.ataques_realizados} "
              f"({int(ganador.ataques_acertados/ganador.ataques_realizados*100) if ganador.ataques_realizados > 0 else 0}%)")
        
        print(f"\n  " + perdedor.nombre.upper())
        print(f"  💰 Puntuación Total: {perdedor.puntuacion}")
        print(f"  🔥 Mejor Racha: {perdedor.mejor_racha}")
        print(f"  🎯 Precisión: {perdedor.ataques_acertados}/{perdedor.ataques_realizados} "
              f"({int(perdedor.ataques_acertados/perdedor.ataques_realizados*100) if perdedor.ataques_realizados > 0 else 0}%)")
        
        print("\n" + "="*60)

def main():
    print("\n" + "="*60)
    print("  ⚓ BATALLA NAVAL ⚓")
    print("="*60)
    print("\n  🌊 Bienvenido al juego de Batalla Naval")
    print("\n  LEYENDA:")
    print(f"  {AGUA} = Agua (no explorada)")
    print(f"  {OCULTO} = Zona desconocida")
    print(f"  {BARCO} = Tu barco")
    print(f"  {FALLO} = Ataque fallido")
    print(f"  {IMPACTO} = ¡Impacto!")
    print(f"  {HUNDIDO} = Barco hundido")
    
    print("\n  📈 SISTEMA DE PUNTUACIÓN:")
    print("  • Impacto: 10 puntos base")
    print("  • Racha: +5 puntos por cada impacto consecutivo")
    print("  • ¡Consigue la mayor racha posible!")
    
    while True:
        print("\n  MODOS DE JUEGO:")
        print("  1. Un Jugador (vs Computadora)")
        print("  2. Dos Jugadores")
        print("  3. Salir")
        
        opcion = input("\n  Selecciona un modo (1/2/3): ").strip()
        
        juego = JuegoBatallaNaval()
        
        if opcion == "1":
            juego.jugar_un_jugador()
        elif opcion == "2":
            juego.jugar_dos_jugadores()
        elif opcion == "3":
            print("\n  ⚓ ¡Hasta la próxima batalla, marinero! ⚓\n")
            break
        else:
            print("  ❌ Opción inválida.")
            continue
        
        jugar_otra = input("\n  ¿Jugar otra partida? (S/N): ").strip().upper()
        if jugar_otra != 'S':
            print("\n  ⚓ ¡Hasta la próxima batalla, marinero! ⚓\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  ⚓ ¡Hasta la próxima batalla! ⚓\n")
        sys.exit(0)