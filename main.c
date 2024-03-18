#include <stdio.h>
#include <time.h>

// Função para calcular a soma de todos os números de 1 a N
unsigned long long calcular_soma_ate(unsigned long long n) {
    unsigned long long soma = 0;
    for (unsigned long long i = 1; i <= n; i++) {
        soma += i;
    }
    return soma;
}

int main() {
    // Defina o valor de N
    unsigned long long n = 1000000000;

    // Marque o tempo de início
    clock_t start_time = clock();

    // Chame a função para calcular a soma
    unsigned long long resultado = calcular_soma_ate(n);

    // Marque o tempo de término
    clock_t end_time = clock();

    // Calcule a diferença de tempo
    double elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    // Imprima o resultado e o tempo de execução
    printf("Resultado da soma até %llu: %llu\n", n, resultado);
    printf("Tempo decorrido: %.6f segundos\n", elapsed_time);

    return 0;
}
