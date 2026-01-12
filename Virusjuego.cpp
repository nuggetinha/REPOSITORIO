#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <conio.h>
#include <windows.h>

using namespace std;

const int MAX_FILAS = 20;
const int MAX_COLUMNAS = 20;

struct Jugador {
    int x, y;
    int barreras;
    int antidotos;
};

struct Nivel {
    int filas, columnas;
    int barrerasIniciales;
    int antidotosIniciales;
    int numVirusIniciales;
};

class JuegoVirus {
private:
    char tablero[MAX_FILAS][MAX_COLUMNAS];
    Jugador jugador;
    Nivel nivelActual;
    int nivel;
    int salidaX, salidaY;
    int turno;
    bool virusContenido;
    int celdasLibres;
    int celdasVirus;
    
public:
    JuegoVirus() {
        nivel = 1;
        turno = 0;
        virusContenido = false;
    }
    
    void inicializarNivel(int n) {
        nivel = n;
        turno = 0;
        virusContenido = false;
        
        // Configurar dificultad según nivel
        switch(n) {
            case 1:
                nivelActual = {20, 20, 8, 2, 2};
                break;
            case 2:
                nivelActual = {20, 20, 6, 1, 3};
                break;
            case 3:
                nivelActual = {20, 20, 5, 1, 4};
                break;
            default:
                nivelActual = {20, 20, 3, 0, 5};
                break;
        }
        
        // Limpiar tablero
        for(int i = 0; i < nivelActual.filas; i++) {
            for(int j = 0; j < nivelActual.columnas; j++) {
                tablero[i][j] = '0';
            }
        }
        
        // Colocar jugador
        jugador.x = 1;
        jugador.y = 1;
        jugador.barreras = nivelActual.barrerasIniciales;
        jugador.antidotos = nivelActual.antidotosIniciales;
        tablero[jugador.x][jugador.y] = 'P';
        
        // Colocar salida
        salidaX = nivelActual.filas - 2;
        salidaY = nivelActual.columnas - 2;
        tablero[salidaX][salidaY] = 'S';
        
        // Colocar virus iniciales
        srand(time(0) + n);
        for(int i = 0; i < nivelActual.numVirusIniciales; i++) {
            int x, y;
            do {
                x = rand() % nivelActual.filas;
                y = rand() % nivelActual.columnas;
            } while(tablero[x][y] != '0');
            tablero[x][y] = 'V';
        }
        
        contarCeldas();
    }
    
    void contarCeldas() {
        celdasLibres = 0;
        celdasVirus = 0;
        for(int i = 0; i < nivelActual.filas; i++) {
            for(int j = 0; j < nivelActual.columnas; j++) {
                if(tablero[i][j] == '0') celdasLibres++;
                if(tablero[i][j] == 'V') celdasVirus++;
            }
        }
    }
    
    void limpiarPantalla() {
        system("cls");
    }
    
    void mostrarTablero() {
        limpiarPantalla();
        cout << "          CONTENCION DE VIRUS - NIVEL " << nivel << "                    " << endl;
        
        cout << "\n  ";
        for(int j = 0; j < nivelActual.columnas; j++) {
            cout << j % 10;
        }
        cout << endl;
        
        for(int i = 0; i < nivelActual.filas; i++) {
            cout << i % 10 << " ";
            for(int j = 0; j < nivelActual.columnas; j++) {
                char celda = tablero[i][j];
                if(celda == 'P') {
                    cout << "\033[1;36mP\033[0m"; // Cian
                } else if(celda == 'V') {
                    cout << "\033[1;31mV\033[0m"; // Rojo
                } else if(celda == 'B') {
                    cout << "\033[1;33m#\033[0m"; // Amarillo
                } else if(celda == 'S') {
                    cout << "\033[1;32mS\033[0m"; // Verde
                } else {
                    cout << ".";
                }
            }
            cout << endl;
        }
        
        cout << " Turno: " << turno << "  Barreras: " << jugador.barreras 
             << "  Antidotos: " << jugador.antidotos << "           " << endl;
        cout << " Celdas libres: " << celdasLibres << "  Virus: " << celdasVirus << "              │" << endl;
        
        cout << "\n[WASD] Mover | [B] Barrera | [A] Antidoto | [Q] Salir" << endl;
    }
    
    void propagarVirus() {
        vector<pair<int,int>> nuevosVirus;
        
        for(int i = 0; i < nivelActual.filas; i++) {
            for(int j = 0; j < nivelActual.columnas; j++) {
                if(tablero[i][j] == 'V') {
                    // Propagar a celdas adyacentes
                    int dx[] = {-1, 1, 0, 0};
                    int dy[] = {0, 0, -1, 1};
                    
                    for(int k = 0; k < 4; k++) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        
                        if(nx >= 0 && nx < nivelActual.filas && 
                           ny >= 0 && ny < nivelActual.columnas) {
                            if(tablero[nx][ny] == '0') {
                                nuevosVirus.push_back({nx, ny});
                            } else if(tablero[nx][ny] == 'P') {
                                // El virus alcanzó al jugador
                                return;
                            }
                        }
                    }
                }
            }
        }
        
        // Aplicar nuevas infecciones
        for(auto pos : nuevosVirus) {
            tablero[pos.first][pos.second] = 'V';
        }
        
        // Verificar si el virus está contenido
        if(nuevosVirus.empty() && celdasVirus > 0) {
            virusContenido = true;
        }
    }
    
    bool moverJugador(int dx, int dy) {
        int nx = jugador.x + dx;
        int ny = jugador.y + dy;
        
        if(nx < 0 || nx >= nivelActual.filas || 
           ny < 0 || ny >= nivelActual.columnas) {
            return false;
        }
        
        if(tablero[nx][ny] == 'B') {
            return false;
        }
        
        if(tablero[nx][ny] == 'V') {
            cout << "\n¡Has pisado virus! ¡GAME OVER!" << endl;
            Sleep(2000);
            return false;
        }
        
        // Mover jugador
        tablero[jugador.x][jugador.y] = '0';
        jugador.x = nx;
        jugador.y = ny;
        
        if(tablero[nx][ny] == 'S') {
            return true; // Llegó a la salida
        }
        
        tablero[jugador.x][jugador.y] = 'P';
        return true;
    }
    
    void colocarBarrera() {
        if(jugador.barreras <= 0) {
            cout << "\n¡No tienes barreras disponibles!" << endl;
            Sleep(1000);
            return;
        }
        
        mostrarTablero();
        cout << "\nDirección para barrera [WASD]: ";
        char dir = getch();
        
        int dx = 0, dy = 0;
        if(dir == 'w' || dir == 'W') dx = -1;
        else if(dir == 's' || dir == 'S') dx = 1;
        else if(dir == 'a' || dir == 'A') dy = -1;
        else if(dir == 'd' || dir == 'D') dy = 1;
        else return;
        
        int nx = jugador.x + dx;
        int ny = jugador.y + dy;
        
        if(nx >= 0 && nx < nivelActual.filas && 
           ny >= 0 && ny < nivelActual.columnas) {
            if(tablero[nx][ny] == '0') {
                tablero[nx][ny] = 'B';
                jugador.barreras--;
                turno++;
                propagarVirus();
            }
        }
    }
    
    void usarAntidoto() {
        if(jugador.antidotos <= 0) {
            cout << "\n¡No tienes antídotos disponibles!" << endl;
            Sleep(1000);
            return;
        }
        
        // Eliminar virus en área 3x3 alrededor del jugador
        for(int i = jugador.x - 1; i <= jugador.x + 1; i++) {
            for(int j = jugador.y - 1; j <= jugador.y + 1; j++) {
                if(i >= 0 && i < nivelActual.filas && 
                   j >= 0 && j < nivelActual.columnas) {
                    if(tablero[i][j] == 'V') {
                        tablero[i][j] = '0';
                    }
                }
            }
        }
        
        jugador.antidotos--;
        cout << "\n¡Antídoto usado! Virus eliminados en área cercana." << endl;
        Sleep(1000);
    }
    
    bool verificarDerrota() {
        contarCeldas();
        
        // Verificar si el virus ocupó casi todo el mapa
        int totalCeldas = nivelActual.filas * nivelActual.columnas;
        if(celdasVirus > totalCeldas * 0.7) {
            return true;
        }
        
        // Verificar si el jugador está rodeado
        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};
        bool puedeMoverse = false;
        
        for(int k = 0; k < 4; k++) {
            int nx = jugador.x + dx[k];
            int ny = jugador.y + dy[k];
            
            if(nx >= 0 && nx < nivelActual.filas && 
               ny >= 0 && ny < nivelActual.columnas) {
                if(tablero[nx][ny] != 'V' && tablero[nx][ny] != 'B') {
                    puedeMoverse = true;
                    break;
                }
            }
        }
        
        return !puedeMoverse;
    }
    
    void jugar() {
        inicializarNivel(nivel);
        
        while(true) {
            mostrarTablero();
            contarCeldas();
            
            // Verificar victoria por contención
            if(virusContenido) {
                cout << "\n¡VICTORIA! ¡Has contenido el virus!" << endl;
                Sleep(2000);
                nivel++;
                if(nivel <= 4) {
                    cout << "\nAvanzando al nivel " << nivel << "..." << endl;
                    Sleep(2000);
                    inicializarNivel(nivel);
                    continue;
                } else {
                    cout << "\n¡FELICIDADES! ¡Has completado todos los niveles!" << endl;
                    Sleep(3000);
                    return;
                }
            }
            
            // Verificar derrota
            if(verificarDerrota()) {
                cout << "\n¡DERROTA! El virus se ha propagado demasiado." << endl;
                Sleep(3000);
                return;
            }
            
            char tecla = getch();
            
            if(tecla == 'q' || tecla == 'Q') {
                break;
            } else if(tecla == 'w' || tecla == 'W') {
                if(moverJugador(-1, 0)) {
                    if(jugador.x == salidaX && jugador.y == salidaY) {
                        cout << "\n¡VICTORIA! ¡Has llegado a la salida!" << endl;
                        Sleep(2000);
                        nivel++;
                        if(nivel <= 4) {
                            cout << "\nAvanzando al nivel " << nivel << "..." << endl;
                            Sleep(2000);
                            inicializarNivel(nivel);
                            continue;
                        } else {
                            cout << "\n¡FELICIDADES! ¡Has completado todos los niveles!" << endl;
                            Sleep(3000);
                            return;
                        }
                    }
                    turno++;
                    propagarVirus();
                }
            } else if(tecla == 's' || tecla == 'S') {
                if(moverJugador(1, 0)) {
                    if(jugador.x == salidaX && jugador.y == salidaY) {
                        cout << "\n¡VICTORIA! ¡Has llegado a la salida!" << endl;
                        Sleep(2000);
                        nivel++;
                        if(nivel <= 4) {
                            cout << "\nAvanzando al nivel " << nivel << "..." << endl;
                            Sleep(2000);
                            inicializarNivel(nivel);
                            continue;
                        } else {
                            cout << "\n¡FELICIDADES! ¡Has completado todos los niveles!" << endl;
                            Sleep(3000);
                            return;
                        }
                    }
                    turno++;
                    propagarVirus();
                }
            } else if(tecla == 'a' || tecla == 'A') {
                if(moverJugador(0, -1)) {
                    if(jugador.x == salidaX && jugador.y == salidaY) {
                        cout << "\n¡VICTORIA! ¡Has llegado a la salida!" << endl;
                        Sleep(2000);
                        nivel++;
                        if(nivel <= 4) {
                            cout << "\nAvanzando al nivel " << nivel << "..." << endl;
                            Sleep(2000);
                            inicializarNivel(nivel);
                            continue;
                        } else {
                            cout << "\n¡FELICIDADES! ¡Has completado todos los niveles!" << endl;
                            Sleep(3000);
                            return;
                        }
                    }
                    turno++;
                    propagarVirus();
                }
            } else if(tecla == 'd' || tecla == 'D') {
                if(moverJugador(0, 1)) {
                    if(jugador.x == salidaX && jugador.y == salidaY) {
                        cout << "\n¡VICTORIA! ¡Has llegado a la salida!" << endl;
                        Sleep(2000);
                        nivel++;
                        if(nivel <= 4) {
                            cout << "\nAvanzando al nivel " << nivel << "..." << endl;
                            Sleep(2000);
                            inicializarNivel(nivel);
                            continue;
                        } else {
                            cout << "\n¡FELICIDADES! ¡Has completado todos los niveles!" << endl;
                            Sleep(3000);
                            return;
                        }
                    }
                    turno++;
                    propagarVirus();
                }
            } else if(tecla == 'b' || tecla == 'B') {
                colocarBarrera();
            } else if(tecla == 'A') {
                usarAntidoto();
                turno++;
                propagarVirus();
            }
        }
    }
};

int main() {
    cout << "                 CONTENCION DE VIRUS                      " << endl;
    cout << "\nMISION: Contener el virus y llegar a la salida" << endl;
    cout << "\nLEYENDA:" << endl;
    cout << "  P (Cian)    = Tu posición" << endl;
    cout << "  V (Rojo)    = Virus (¡evítalo!)" << endl;
    cout << "  # (Amarillo)= Barrera" << endl;
    cout << "  S (Verde)   = Salida" << endl;
    cout << "  .           = Espacio vacío" << endl;
    
    cout << "\nCONTROLES:" << endl;
    cout << "  WASD = Movimiento" << endl;
    cout << "  B    = Colocar barrera" << endl;
    cout << "  A    = Usar antídoto (elimina virus cercanos)" << endl;
    cout << "  Q    = Salir" << endl;
    
    cout << "\nESTRATEGIA:" << endl;
    cout << "  - El virus se propaga cada turno a celdas adyacentes" << endl;
    cout << "  - Usa barreras para bloquear la expansión" << endl;
    cout << "  - Ganas si contienes el virus o llegas a la salida" << endl;
    cout << "  - Pierdes si el virus te alcanza o cubre el mapa" << endl;
    
    cout << "\nPresiona cualquier tecla para comenzar..." << endl;
    getch();
    
    JuegoVirus juego;
    juego.jugar();
    
    cout << "\n¡Gracias por jugar!" << endl;
    
    return 0;
}