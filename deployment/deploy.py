```python
import os
import subprocess

def install_dependencies():
    print("Installing dependencies...")
    subprocess.check_call(["python3", "-m", "pip", "install", "-r", "requirements.txt"])

def setup_environment():
    print("Setting up environment...")
    os.environ['STREAMLIT_SERVER_PORT'] = '8501'

def run_application():
    print("Running application...")
    subprocess.Popen(["streamlit", "run", "../frontend/streamlit_app.py"])

def main():
    install_dependencies()
    setup_environment()
    run_application()

if __name__ == "__main__":
    main()
```