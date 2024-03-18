package main

import (
    "fmt"
    "time"
)

// Função para calcular a soma de todos os números de 1 a N
func calcularSomaAte(n uint64) uint64 {
    var soma uint64
    for i := uint64(1); i <= n; i++ {
        soma += i
    }
    return soma
}

func main() {
    // Defina o valor de N
    n := uint64(1000000000)

    // Marque o tempo de início
    start := time.Now()

    // Chame a função para calcular a soma
    resultado := calcularSomaAte(n)

    // Marque o tempo de término
    end := time.Now()

    // Calcule a diferença de tempo
    elapsed := end.Sub(start)

    // Imprima o resultado e o tempo de execução
    fmt.Printf("Resultado da soma até %d: %d\n", n, resultado)
    fmt.Printf("Tempo decorrido: %.6f segundos\n", elapsed.Seconds())
}
