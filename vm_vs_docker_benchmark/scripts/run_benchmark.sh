#!/bin/bash
echo "🧪 Ejecutando benchmark en entorno: $1"

if [ "$1" == "vm" ]; then
    output="results/benchmark_vm.csv"
elif [ "$1" == "docker" ]; then
    output="results/benchmark_docker.csv"
else
    echo "❌ Especifica 'vm' o 'docker'"
    exit 1
fi

mkdir -p results

python3 benchmark_runner.py "$output"

echo "✅ Benchmark completado. Resultados guardados en $output"
