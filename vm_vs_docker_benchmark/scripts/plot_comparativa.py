# scripts/plot_comparativa.py

import matplotlib.pyplot as plt
import numpy as np

# Datos estimados de rendimiento (puedes ajustar los tuyos reales aquí)
categorias = ['Uso CPU (%)', 'Uso RAM (MB)', 'Tamaño entorno (MB)', 'Tiempo arranque (s)']

# Valores: [CPU, RAM, Tamaño, Tiempo arranque]
valores_vm = [25, 512, 2048, 28]     # ← Puedes cambiar con tus datos reales
valores_docker = [3.5, 35, 250, 3]   # ← Datos medidos o estimados para Docker

x = np.arange(len(categorias))
ancho = 0.35  # ancho de barra

fig, ax = plt.subplots(figsize=(10, 6))
barras_vm = ax.bar(x - ancho/2, valores_vm, width=ancho, label='VM', color='skyblue')
barras_docker = ax.bar(x + ancho/2, valores_docker, width=ancho, label='Docker', color='lightgreen')

# Etiquetas
ax.set_ylabel('Valor')
ax.set_title('Comparativa de rendimiento: VM vs Docker (Fifa.java)')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()
ax.grid(True, axis='y', linestyle='--', alpha=0.6)

# Mostrar valores encima de cada barra
for barra in barras_vm + barras_docker:
    y = barra.get_height()
    ax.annotate(f'{y}', xy=(barra.get_x() + barra.get_width() / 2, y),
                xytext=(0, 5), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.savefig("../results/comparativa_vm_vs_docker.png")
print("✅ Gráfico guardado en: results/comparativa_vm_vs_docker.png")
