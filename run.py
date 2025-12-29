import tkinter as tk
from ui.runner_gui import TestRunnerGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = TestRunnerGUI(root)
    root.mainloop()