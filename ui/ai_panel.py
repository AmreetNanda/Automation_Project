import tkinter as tk

class AIPanel:
    def __init__(self, parent, on_run_ai, on_analyze_failure):
        frame = tk.LabelFrame(parent, text="AI Test Control", bg="#1d1f21", fg="#5bc0be")
        frame.pack(fill="x", padx=10, pady=10)

        self.prompt = tk.Text(frame, height=4, bg="black", fg="white")
        self.prompt.pack(fill="x", padx=5, pady=5)

        btn_frame = tk.Frame(frame, bg="#1d1f21")
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="Run AI Test", command=lambda: on_run_ai(self.prompt.get("1.0", tk.END))).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Explain Last Failure", command=on_analyze_failure).pack(side="left", padx=5)
