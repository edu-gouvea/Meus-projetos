#include <stdio.h>
#include <string.h>

typedef struct {
        char nome[50];
        char cor[20];
        char tamanho;
} tCamisas;

void TiraBarraN (char *str){
    int i;
    for (i = 0; str[i] != '\0'; i++);
    if (str[i-1] == '\n'){
        str[i-1] = '\0';
    }
    return;
}

void TrocaCamisas (tCamisas *a, tCamisas *b){
    tCamisas aux; 
    aux = *a; 
    *a = *b; 
    *b = aux; 
    return;
}

int ComparaTamanho(char t) {
    if (t == 'P') 
        return 0;
    if (t == 'M') 
        return 1;
    return 2;
}

void OrdenaTudo(tCamisas camisas[], int n) {
    int i, trocou = 1;

    while (trocou){
        trocou = 0;
        for (i = 0; i < n - 1; i++){

            int troca = 0;

            int cmpCor = strcmp(camisas[i].cor, camisas[i+1].cor);
            
            if (cmpCor > 0) 
                troca = 1;
            else if (cmpCor == 0){
                int t1 = ComparaTamanho(camisas[i].tamanho);
                int t2 = ComparaTamanho(camisas[i+1].tamanho);

                if (t1 > t2) 
                    troca = 1;
                else if (t1 == t2){
                        if (strcmp(camisas[i].nome, camisas[i+1].nome) > 0)
                            troca = 1;
                }
            }
            if (troca){
                TrocaCamisas(&camisas[i], &camisas[i+1]);
                trocou = 1;
            }
        }
    }
}


int main(){

    int n, i;

    while (1){
        scanf ("%d", &n);
        getchar();
        if (n == 0) break;
        tCamisas camisas[n];
        for (i = 0; i < n; i++){
            fgets (camisas[i].nome, 50, stdin);
            TiraBarraN(camisas[i].nome);
            scanf ("%s %c", camisas[i].cor, &camisas[i].tamanho);
            getchar();
        }
        OrdenaTudo(camisas, n);
        for (i = 0; i < n; i++){
            printf ("%s %c %s\n", camisas[i].cor, camisas[i].tamanho, camisas[i].nome);
        }
        puts("");
    }
    return 0;
}