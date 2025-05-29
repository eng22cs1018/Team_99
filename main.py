import sys
from pathlib import Path
import tkinter as tk
from src.main_app import MainApp

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parent / "src"))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x2000")  # Set the window size to 800x600
    app = MainApp(root)
    root.mainloop()