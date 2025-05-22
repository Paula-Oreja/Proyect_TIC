
# ⚽ Proyecto Benchmark: Máquina Virtual vs Docker

Este proyecto evalúa y compara el rendimiento de una aplicación Java (`Fifa.java`) ejecutada en dos entornos distintos: una máquina virtual (VM) Ubuntu y un contenedor Docker. La aplicación simula un partido de fútbol desde consola.

---

## 🖥️ ¿Qué son las máquinas virtuales y los contenedores? 🚢

Para entender las diferencias entre los entornos donde se ejecuta el servidor Snake, es fundamental conocer qué son las máquinas virtuales (VM) y los contenedores, dos tecnologías usadas ampliamente para aislar aplicaciones y facilitar su despliegue.

### 🖥️ Máquinas Virtuales (VM)

Una máquina virtual es una emulación completa de un sistema operativo que corre sobre hardware físico, gestionada por un software llamado *hipervisor* (por ejemplo, VirtualBox o VMware). Cada VM incluye su propio núcleo (kernel), sistema operativo, librerías y aplicaciones, funcionando de manera independiente del sistema operativo anfitrión.

- **Ventajas:**  
  - 🔒 Alto nivel de aislamiento y seguridad, pues cada VM es un sistema completo.  
  - 💻 Puede ejecutar sistemas operativos distintos al del host (por ejemplo, Windows host con Linux guest).  
  - ⚙️ Ideal para aplicaciones que requieren un entorno específico o un kernel modificado.

- **Desventajas:**  
  - 🐘 Consumo considerable de recursos (CPU, memoria, almacenamiento).  
  - 🕒 Inicio y parada más lentos comparados con contenedores.

### 🚢 Contenedores

Los contenedores, como los gestionados por Docker, son una forma más ligera de virtualización a nivel de sistema operativo. En lugar de virtualizar todo un sistema operativo, comparten el núcleo del host y aíslan únicamente los procesos y recursos necesarios para ejecutar la aplicación.

- **Ventajas:**  
  - ⚡ Uso eficiente de recursos, arrancan y se detienen rápidamente.  
  - 📦 Facilitan la portabilidad de aplicaciones al empaquetar dependencias y configuraciones.  
  - ☁️ Ideales para despliegues escalables y microservicios.

- **Desventajas:**  
  - 🔓 Menor aislamiento comparado con VM, ya que comparten el kernel del host.  
  - ⚠️ Limitaciones en personalización del sistema operativo o seguridad estricta.

### 🎯 Relación con el proyecto

En este proyecto se compara el rendimiento y uso de recursos de una aplicación Java que simula un partido de fútbol (Fifa.java), ejecutada en dos entornos distintos: una máquina virtual tradicional (Ubuntu sobre VirtualBox) y un contenedor Docker. El objetivo es evaluar cuál de las dos opciones resulta más eficiente para ejecutar aplicaciones Java sencillas, analizando el impacto de cada entorno sobre el rendimiento, el consumo de recursos y la experiencia de uso.

---

## ⚙️ Entorno de Pruebas

- **Host**: Intel Core i7, 8 GB RAM, Windows 11  
- **Virtual Machine (Guest)**: Ubuntu 22.04 LTS, 2 GB RAM, 2 vCPU, VirtualBox 7.0  
- **Docker**: Imagen base `openjdk:21-slim`, contenedor ejecutado con 2 CPUs por defecto  
- **Aplicación probada**: `Fifa.java` – Simulación de partido de fútbol desarrollado en Java  
- **Monitorización de recursos**:  
  - En VM: herramienta `htop`  
  - En Docker: comando `docker stats`  
- **Red y conexión**: Ambos entornos usan red NAT con salida a Internet, sin puertos expuestos  
- **Capturas de resultados**: realizadas localmente desde terminal en VM y desde PowerShell en Windows para Docker

---

## 📁 Estructura actual del proyecto



---

## 📚 Bibliografía y Recursos

A continuación, se presentan las principales herramientas, librerías y recursos que se han utilizado y consultado para el desarrollo y ejecución de este proyecto:

### 🛠️ Herramientas y Plataformas

- **Python 3.8+**  
  Lenguaje de programación principal para el servidor y scripts.  
  Instalación oficial: [python.org](https://www.python.org/downloads/)

- **Docker**  
  Plataforma para contenedores que permite empaquetar aplicaciones con sus dependencias.  
  Documentación e instalación: [docs.docker.com](https://docs.docker.com/get-docker/)

- **VirtualBox**  
  Software para crear y manejar máquinas virtuales.  
  Documentación e instalación: [virtualbox.org](https://www.virtualbox.org/wiki/Downloads)

- **Jupyter Notebook**  
  Entorno interactivo para análisis y visualización de datos con Python.  
  Instalación: `pip install notebook`  
  Documentación: [jupyter.org](https://jupyter.org/)

---

## ⚙️ Requisitos

```bash
Python 3.8+

Docker

VirtualBox (con Linux guest si aplica)

pip
```

---

## 📦 Librerías de Python utilizadas en el entorno

Aunque el proyecto principal se desarrolló en Java, el entorno automatizado preparado para análisis y benchmarking incluía algunas librerías de Python útiles para tareas de monitorización y visualización de resultados. Estas son:

- `jupyter` – Permite ejecutar y visualizar notebooks interactivos desde el navegador.
- `matplotlib` – Librería de gráficos utilizada para visualizar métricas de rendimiento.
- `psutil` – Permite acceder a estadísticas de uso de CPU, memoria, procesos y recursos del sistema.
- `pip` – Gestor de paquetes utilizado para instalar otras librerías.
- `sysbench` – Herramienta de benchmarking del sistema, usada desde la línea de comandos o integrada con Python (aunque no es una librería Python, forma parte del entorno).

Estas herramientas estaban disponibles en el contenedor Docker y/o en la máquina virtual como parte del entorno de pruebas, aunque no se usaron directamente en el desarrollo de la aplicación.


