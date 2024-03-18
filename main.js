// Função para calcular a soma de todos os números de 1 a N
function calcularSomaAte(n) {
    let soma = 0;
    for (let i = 1; i <= n; i++) {
        soma += i;
    }
    return soma;
}

function main() {
    // Defina o valor de N
    const n = 1000000000;

    // Marque o tempo de início
    const startTime = new Date();

    // Chame a função para calcular a soma
    const resultado = calcularSomaAte(n);

    // Marque o tempo de término
    const endTime = new Date();

    // Calcule a diferença de tempo
    const elapsedTime = (endTime - startTime) / 1000; // Converter para segundos

    // Imprima o resultado e o tempo de execução
    console.log(`Resultado da soma até ${n}: ${resultado}`);
    console.log(`Tempo decorrido: ${elapsedTime.toFixed(6)} segundos`);
}

main();
