use std::time::{Instant};

// Função para calcular a soma de todos os números de 1 a N
fn calcular_soma_ate(n: u64) -> u64 {
    (1..=n).sum()
}

fn main() {
    // Defina o valor de N
    let n: u64 = 1000000000;

    // Marque o tempo de início
    let start_time = Instant::now();

    // Chame a função para calcular a soma
    let resultado = calcular_soma_ate(n);

    // Marque o tempo de término
    let end_time = Instant::now();

    // Calcule a diferença de tempo
    let elapsed_time = end_time.duration_since(start_time);

    // Converta o tempo decorrido em segundos com precisão de milissegundos
    let elapsed_seconds = elapsed_time.as_secs() as f64 + elapsed_time.subsec_millis() as f64 / 1000.0;

    // Imprima o resultado e o tempo de execução
    println!("Resultado da soma até {}: {}", n, resultado);
    println!("Tempo decorrido: {:.6} segundos", elapsed_seconds);
}
