#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void troca(int *a, int *b){
    int aux = *a;
    *a = *b;
    *b = aux;
}

int *geraVetorOrdenado(int n){
    int *v = malloc(n*sizeof(int));
    for(int i=0; i<n; i++){
        v[i] = i+1;
    }
    return v;
}

int *geraVetorReverso(int n){
    int *v = malloc(n*sizeof(int));
    for(int i=0; i<n; i++){
        v[i] = n-i;
    }
    return v;
}

int *geraVetorAleatorio(int n){
    srand(time(NULL));
    int *v = geraVetorOrdenado(n);
    for(int i=n-1; i>0; i--){
        int j = rand()%(i+1);
        troca(&v[i], &v[j]);
    }
    return v;
}

void insertionSort(int *v, int n){
    int atual, j;
    for(int i=1; i<n; i++){
        atual = v[i];
        for(j = i; (j>0) && (atual<v[j-1]); j--){
            v[j] = v[j-1];
        }
        v[j] = atual;
    }
}


int main(int argc, char *argv[]){
    
    if(argc != 3){
        printf("Use: %s <tamanho> <tipo de vetor>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    int tipo = atoi(argv[2]);

    int *v;
    if(tipo == 0){
        v = geraVetorOrdenado(n);
    }else if(tipo == 1){
        v = geraVetorAleatorio(n);
    }else if(tipo == 2){
        v = geraVetorReverso(n);
    }else{
        printf("Tipo de vetor inválido.\n");
        return 1;
    }

    clock_t inicio = clock();
    insertionSort(v, n);
    clock_t fim = clock();
    double tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Vetor de %d elementos: %f segundos\n", n, tempo);
    printf("Consumo de memória: %ld bytes\n\n", n*sizeof(int));
    free(v);

    return 0;
}