
import tkinter as tk
import psutil
import threading
import time

class PainelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Painel de Desempenho")
        self.root.geometry("400x200")
        self.root.configure(bg="#1e1e1e")

        self.cpu_label = tk.Label(root, text="Uso de CPU: --%", font=("Segoe UI", 14), fg="white", bg="#1e1e1e")
        self.cpu_label.pack(pady=10)

        self.mem_label = tk.Label(root, text="Uso de Memória: --%", font=("Segoe UI", 14), fg="white", bg="#1e1e1e")
        self.mem_label.pack(pady=10)

        self.quit_button = tk.Button(root, text="Encerrar", command=self.root.quit, font=("Segoe UI", 12), bg="#333", fg="white")
        self.quit_button.pack(pady=10)

        self.update_metrics()

    def update_metrics(self):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        self.cpu_label.config(text=f"Uso de CPU: {cpu}%")
        self.mem_label.config(text=f"Uso de Memória: {mem}%")
        self.root.after(1000, self.update_metrics)

def run():
    root = tk.Tk()
    app = PainelApp(root)
    root.mainloop()

if __name__ == "__main__":
    run()
