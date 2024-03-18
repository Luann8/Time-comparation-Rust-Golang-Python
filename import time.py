import time

# Função para calcular a soma de todos os números de 1 a N
def calcular_soma_ate(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

def main():
    # Defina o valor de N
    n = 1000000000

    # Marque o tempo de início
    start_time = time.time()

    # Chame a função para calcular a soma
    resultado = calcular_soma_ate(n)

    # Marque o tempo de término
    end_time = time.time()

    # Calcule a diferença de tempo
    elapsed_time = end_time - start_time

    # Imprima o resultado e o tempo de execução
    print("Resultado da soma até {}: {}".format(n, resultado))
    print("Tempo decorrido: {:.6f} segundos".format(elapsed_time))

if __name__ == "__main__":
    main()
