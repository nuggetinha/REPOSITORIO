#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

struct Nodo {
    int key;
    Nodo* left;
    Nodo* right;
    Nodo(int k) : key(k), left(nullptr), right(nullptr) {}
};

class BST {
private:
    Nodo* root;

    Nodo* insert(Nodo* n, int key) {
        if (!n) return new Nodo(key);
        if (key < n->key) n->left = insert(n->left, key);
        else if (key > n->key) n->right = insert(n->right, key);
        return n;
    }

    bool search(Nodo* n, int key, vector<int>& ruta) {
        if (!n) return false;
        ruta.push_back(n->key);
        if (n->key == key) return true;
        if (key < n->key) return search(n->left, key, ruta);
        return search(n->right, key, ruta);
    }

    Nodo* minValueNode(Nodo* n) {
        while (n && n->left) n = n->left;
        return n;
    }

    Nodo* remove(Nodo* n, int key) {
        if (!n) return n;
        if (key < n->key) n->left = remove(n->left, key);
        else if (key > n->key) n->right = remove(n->right, key);
        else {
            if (!n->left) {
                Nodo* temp = n->right;
                delete n;
                return temp;
            }
            if (!n->right) {
                Nodo* temp = n->left;
                delete n;
                return temp;
            }
            Nodo* temp = minValueNode(n->right);
            n->key = temp->key;
            n->right = remove(n->right, temp->key);
        }
        return n;
    }

    void inorder(Nodo* n) {
        if (!n) return;
        inorder(n->left);
        cout << n->key << " ";
        inorder(n->right);
    }

    void preorder(Nodo* n) {
        if (!n) return;
        cout << n->key << " ";
        preorder(n->left);
        preorder(n->right);
    }

    void postorder(Nodo* n) {
        if (!n) return;
        postorder(n->left);
        postorder(n->right);
        cout << n->key << " ";
    }

    int height(Nodo* n) {
        if (!n) return -1;
        return 1 + max(height(n->left), height(n->right));
    }

    int size(Nodo* n) {
        if (!n) return 0;
        return 1 + size(n->left) + size(n->right);
    }

    void exportInorder(Nodo* n, ofstream& f) {
        if (!n) return;
        exportInorder(n->left, f);
        f << n->key << " ";
        exportInorder(n->right, f);
    }

    // ---- IMPRESION ASCII DEL ARBOL (COMPATIBLE CON WINDOWS) ----
    void printTree(Nodo* n, string prefix, bool isLeft) {
        if (!n) return;

        cout << prefix;
        cout << (isLeft ? "|-- " : "+-- ");
        cout << n->key << endl;

        printTree(n->left, prefix + (isLeft ? "|   " : "    "), true);
        printTree(n->right, prefix + (isLeft ? "|   " : "    "), false);
    }

public:
    BST() : root(nullptr) {}

    void insert(int key) { root = insert(root, key); }

    void search(int key) {
        vector<int> ruta;
        if (search(root, key, ruta)) {
            cout << "Encontrado. Ruta: ";
        } else {
            cout << "No encontrado. Ruta recorrida: ";
        }
        for (int v : ruta) cout << v << " ";
        cout << endl;
    }

    void remove(int key) { root = remove(root, key); }

    void inorder() { inorder(root); cout << endl; }
    void preorder() { preorder(root); cout << endl; }
    void postorder() { postorder(root); cout << endl; }

    int height() { return height(root); }
    int size() { return size(root); }

    void export_inorder(const string& file) {
        ofstream f(file);
        if (!f) {
            cout << "Error al crear archivo\n";
            return;
        }
        exportInorder(root, f);
        f.close();
        cout << "Recorrido guardado en " << file << endl;
    }

    void showTree() {
        if (!root) {
            cout << "Arbol vacio\n";
            return;
        }
        cout << "\nArbol BST:\n";
        cout << root->key << endl;
        printTree(root->left, "", true);
        printTree(root->right, "", false);
    }
};

void help() {
    cout << "Comandos disponibles:\n";
    cout << "insert <n>\nsearch <n>\ndelete <n>\n";
    cout << "inorder\npreorder\npostorder\n";
    cout << "height\nsize\nexport <archivo>\n";
    cout << "help\nexit\n";
}

int main() {
    BST tree;
    string cmd;

    cout << "Gestor de Numeros con BST\n";
    help();

    while (true) {
        cout << "> ";
        cin >> cmd;

        if (cmd == "insert") {
            int n; cin >> n;
            tree.insert(n);
        }
        else if (cmd == "search") {
            int n; cin >> n;
            tree.search(n);
        }
        else if (cmd == "delete") {
            int n; cin >> n;
            tree.remove(n);
        }
        else if (cmd == "inorder") tree.inorder();
        else if (cmd == "preorder") tree.preorder();
        else if (cmd == "postorder") tree.postorder();
        else if (cmd == "height") {
            tree.showTree();
            cout << "\nAltura: " << tree.height() << endl;
        }
        else if (cmd == "size") cout << tree.size() << endl;
        else if (cmd == "export") {
            string f; cin >> f;
            tree.export_inorder(f);
        }
        else if (cmd == "help") help();
        else if (cmd == "exit") break;
        else cout << "Comando no valido\n";
    }
    return 0;
}
