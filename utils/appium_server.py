import subprocess
import time
import os
import psutil
from utils.port_checker import is_port_open


class AppiumServer:
    def __init__(self):
        self.process = None

    def stop_process_on_port(self, port):
        """Kill any process using this port"""
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                for conn in proc.connections(kind='inet'):
                    if conn.laddr.port == port:
                        print(f"Stopping process {proc.pid} ({proc.name()}) on port {port}")
                        proc.kill()
            except Exception:
                continue
    
    def start(self, callback=None):
        try:
            import shutil

            # Kill any existing process using port 4723
            if is_port_open(4723):
                self.stop_process_on_port(4723)
                time.sleep(1) # Wait for the port to release

            # Find appium executable
            appium_path = shutil.which("appium")
            if not appium_path:
                candidate = os.path.expanduser(r"~\Appdata\Roaming\npm\appium.cmd")
                if os.path.exists(candidate):
                    appium_path = candidate
            if not appium_path:
                raise FileNotFoundError("Appium not found in PATH")
            
            
            # Start Appium
            command = [appium_path, "--base-path", "/", "--port", "4723"]
            self.process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                shell=False
            )

            # Wait for the port to open 
            for _ in range(40):
                if is_port_open(4723):
                    if callback:
                        callback(True)
                    return 
                time.sleep(0.5)
            
            # If port is still not open and failed
            raise RuntimeError("Appium process started but port 4723 not open")
        
        except Exception as e:
            print("Failed to start appium server", e)
            if callback:
                callback(False)
        
    
    def stop(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
            self.process = None