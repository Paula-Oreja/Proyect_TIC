
import psutil
import time
import csv

def monitor(duration=10, output_file="results.csv"):
    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "cpu_percent", "memory_percent"])
        for _ in range(duration):
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory().percent
            timestamp = time.strftime("%H:%M:%S")
            writer.writerow([timestamp, cpu, mem])
            print(f"{timestamp} | CPU: {cpu}% | RAM: {mem}%")

if __name__ == "__main__":
    import sys
    duration = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    output = sys.argv[2] if len(sys.argv) > 2 else "results.csv"
    monitor(duration=duration, output_file=output)
