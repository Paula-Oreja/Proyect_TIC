# plot_results.py

import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo CSV
df = pd.read_csv("../results/results.csv")

# Convertir timestamps en eje X (opcional)
df["timestamp"] = pd.to_datetime(df["timestamp"], format="%H:%M:%S")

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(df["timestamp"], df["cpu_percent"], label="CPU (%)", color="blue", marker="o")
plt.plot(df["timestamp"], df["memory_percent"], label="RAM (%)", color="green", marker="o")

plt.title("Consumo de CPU y RAM - Benchmark Fifa.java")
plt.xlabel("Tiempo")
plt.ylabel("Porcentaje (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Guardar gráfico
plt.savefig("../results/benchmark_grafico.png")
plt.show()
