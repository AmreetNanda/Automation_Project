import os
import glob
import subprocess
import threading 
import time
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from framework.test_registry import list_test_cases, get_test_pytest_path
from utils.appium_server import AppiumServer
from utils.port_checker import is_port_open

#_________________________________________________________________________
# Colors
#_________________________________________________________________________
DARK_BG = "#1d1f21"
DARK_FG = "#c5c6c7"
BTN_BG = "#3b3f41"
ACCENT = "#5bc0be"
PASS = "#2ecc71"
FAIL = "#e74c3c"

#_________________________________________________________________________
# GUI Class
#_________________________________________________________________________
class TestRunnerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AAOS Test Runner Framework")
        self.root.geometry("1400x800")
        self.root.configure(bg = DARK_BG)

        self.server = AppiumServer()
        self.server_running = False
        self.selected_tests = []
        self.report_path = None

        self.build_ui()

    #_________________________________________________________________________
    # Build UI
    #_________________________________________________________________________
    def build_ui(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Tabs
        self.tab_main = tk.Frame(self.notebook, bg=DARK_BG)
        self.tab_appium = tk.Frame(self.notebook, bg = DARK_BG)
        self.tab_pytest = tk.Frame(self.notebook, bg = DARK_BG)

        self.notebook.add(self.tab_main, text="Dashboard")
        self.notebook.add(self.tab_appium, text="Appium Logs")
        self.notebook.add(self.tab_pytest, text="Pytest Logs")

        # Build each tab
        self.build_dashboard(self.tab_main)
        self.build_appium_tab(self.tab_appium)
        self.build_pytest_tab(self.tab_pytest)

    #_________________________________________________________________________
    # Dashboard
    #_________________________________________________________________________
    def build_dashboard(self, frame):
        frame.columnfigure(0, weight=1)
        frame.columnfigure(1, weight=2)
        frame.columnfigure(2, weight=3)

        #Left Panel - Server & Test Control
        left = tk.Frame(frame, bg = DARK_BG, padx=15, pady=10)
        left.grid(row=0, column=0, sticky="nsew")

        tk.Label(left, text="SERVER & TEST CONTROL", fg=ACCENT, bg=DARK_BG, 
                 font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=10)
        
        tk.Button(left, text="Start Appium Server", bg=ACCENT, fg="black",
                  font=("Segoe UI", 13, "bold"), command=self.start_server).pack(fill="x", pady=5)
        
        tk.Button(left, text="Stop Appium Server", bg=ACCENT, fg="white",
                  font=("Segoe UI", 13, "bold"), command=self.stop_server).pack(fill="x", pady=5)
        
        self.server_status = tk.Label(left, text="Server: Stopped", fg=FAIL, bg=DARK_BG, font=("Segoe UI", 11))
        self.server_status.pack(pady=10)

        # Test selection
        tk.Label(left, text="Select Test Case:", fg=DARK_FG, bg=DARK_BG, font=("segoe UI", 11)).pack(anchor="w", pady=8)
        self.test_var = tk.StringVar()
        self.dropdown = ttk.Combobox(left, textvariable=self.test_var, value=list_test_cases(), width=30, state="readonly")
        self.dropdown.pack()

        tk.Button(left, text="Add Test", bg=BTN_BG, fg="white", font=("Segoe UI", 11), command=self.add_test).pack(fill="x", pady=5)
        self.listbox = tk.Listbox(left, height=8, width=35, bg="#121314", fg="white")
        self.listbox.pack(fill="both", pady=5)

        tk.Button(left, text="Remove Selected", bg=FAIL, fg="white", font=("Segoe UI", 11), command=self.remove_selected).pack(fill="x", pady=5)

        self.run_button = tk.Button(left, text="RUN SELECTED TESTS", bg="#7d3c98", fg="white", font=("Segoe UI", 12, "bold"), command=self.run_test_threaded)
        self.run_button.pack(fill="x", pady=20)

        self.status_label = tk.Label(left, text="Status: Idle", fg=ACCENT, bg=DARK_BG, font=("Segoe UI", 11))
        self.status_label.pack(pady=5)

        # Report button (disabled until the test is finished)
        self.open_report_btn = tk.Button(left, text="Open HTML Report", bg=ACCENT, fg="black", font=("Segoe UI", 12, "bold"), 
                                         state=tk.DISABLED, command=self.open_report)
        self.open_report_btn.pack(fill="x", pady=10)

        # Open latest log file button
        self.open_log_btn = tk.Button(left, text="Open Lastest Log File", bg=ACCENT, fg="black", font=("Segoe UI", 12, "bold"), 
                                      command=self.open_latest_log)
        self.open_log_btn.pack(fill="x", pady=10)

        #_________________________________________________________________________
        # MIDDLE PANEL - Appium Logs Shortcut
        #_________________________________________________________________________
        middle = tk.Frame(frame, bg=DARK_BG)
        middle.grid(row=0, column=1, sticky="nsew")
        tk.Label(middle, text="APPIUM REAL-TIME LOGS", fg=ACCENT, bg=DARK_BG, font=("Segoe UI", 12, "bold")).pack(anchor="center", pady=10)
        self.dashboard_appium = tk.Text(middle, bg="green", fg="white")
        self.dashboard_appium.pack(fill="both", expand=True, padx=10, pady=10)

        #_________________________________________________________________________
        # RIGHT PANEL - Pytest Logs shortcut
        #_________________________________________________________________________
        right = tk.Frame(frame, bg=DARK_BG)
        right.grid(row=0, column=2, sticky="nsew")
        tk.Label(right, text="PYTEST LIVE LOGS", fg=ACCENT, bg=DARK_BG, font=("Segoe UI", 12, "bold")).pack(anchor="center", pady=10)
        self.dashboard_pytest = tk.Text(right, bg="green", fg="white")
        self.dashboard_pytest.pack(fill="both", expand=True, padx=10, pady=10)

    #_________________________________________________________________________
    # Appium Tab
    #_________________________________________________________________________
    def build_appium_tab(self, frame):
        tk.Label(frame, text="FULL APPIUM LOGS", fg=ACCENT, bg=DARK_BG, font=("Segoe UI", 13, "bold")).pack()
        self.appium_text = tk.Text(frame, wrap="none", bg="green", fg="white")
        self.appium_text.pack(fill="both", expand=True, padx=10, pady=10)

    def append_appium_log(self, text):
        self.appium_text.insert(tk.END, text)
        self.appium_text.see(tk.END)
        self.dashboard_appium.insert(tk.END, text)
        self.dashboard_appium.see(tk.END)

    #_________________________________________________________________________
    # Pytest Tab
    #_________________________________________________________________________
    def build_pytest_tab(self, frame):
        tk.Label(frame, text="PYTEST EXECUTION LOGS", fg=ACCENT, bg=DARK_BG, font=("Segoe UI", 13, "bold")).pack()
        self.pytest_text = tk.Text(frame, wrap="none", bg="green", fg="white")
        self.pytest_text.pack(fill="both", expand=True, padx=10, pady=10)

    def append_pytest_log(self, text):
        self.pytest_text.insert(tk.END, text+ "\n")
        self.pytest_text.see(tk.END)
        self.dashboard_pytest.insert(tk.END, text + "\n")
        self.dashboard_pytest.see(tk.END)

    #_________________________________________________________________________
    # Server Control
    #_________________________________________________________________________
    def start_server(self):
        if self.server_running:
            return
        
        def callback(success):
            if success:
                # Wait for port 4723
                for i in range(10):
                    if is_port_open(4723):
                        self.server_running = True
                        self.server_status.config(text="Server: Running", fg=PASS)
                        threading.Thread(target=self.stream_appium_logs, daemon=True).start()
                        return
                    time.sleep(1)
                self.server.stop()
                self.server.start(callback=callback)
            else:
                self.server_status.config(text="Server: Failed", fg=FAIL)
        self.server.start(callback=callback)

    def stop_server(self):
        self.server.stop()
        self.server_running = False
        self.server_status.config(text="Server: Stopped", fg=FAIL)

    def stream_appium_logs(self):
        if not self.server.process:
            return
        for line in iter(self.server.process.stdout.readline, ""):
            if not line:
                break
            self.append_appium_log(line)

    #_________________________________________________________________________
    # Test Selection
    #_________________________________________________________________________
    def add_test(self):
        test = self.test_var.get()
        if test and test not in self.selected_tests:
            self.selected_tests.append(test)
            self.listbox.insert(tk.END, test)

    def remove_selected(self):
        sel = self.listbox.curseselection()
        if sel:
            t = self.listbox.get(sel)
            self.listbox.delete(sel)
            self.selected_tests.remove(t)

    #_________________________________________________________________________
    # Test Execution
    #_________________________________________________________________________
    

