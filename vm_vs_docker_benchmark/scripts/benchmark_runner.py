# benchmark_runner.py
import subprocess
import threading
import time

def run_java_app():
    subprocess.run(["javac", "Fifa.java"])
    subprocess.run(["java", "Fifa"])

def run_benchmark():
    monitor_thread = threading.Thread(
        target=lambda: subprocess.run(["python3", "monitor_metrics.py", "10", "results.csv"])
    )
    monitor_thread.start()
    
    time.sleep(1)  # asegúrate de que la monitorización arranca primero
    run_java_app()
    monitor_thread.join()

if __name__ == "__main__":
    run_benchmark()
