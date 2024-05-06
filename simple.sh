#!/usr/bin/python3
import subprocess

def run_command(command):
    """
    Run a shell command and return the output.
    """
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Error executing command: {result.stderr.strip()}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def install_packages():
    """
    Install the required packages.
    """
    commands = [
        "pip3 uninstall Fabric",
        "sudo apt-get install libffi-dev",
        "sudo apt-get install libssl-dev",
        "sudo apt-get install build-essential",
        "sudo apt-get install python3.4-dev",
        "sudo apt-get install libpython3-dev",
        "pip3 install pyparsing",
        "pip3 install appdirs",
        "pip3 install setuptools==40.1.0",
        "pip3 install cryptography==2.8",
        "pip3 install bcrypt==3.1.7",
        "pip3 install PyNaCl==1.3.0",
        "pip3 install Fabric3==1.14.post1"
    ]

    for cmd in commands:
        print(f"Running: {cmd}")
        result = run_command(cmd)
        if result:
            print(f"Success: {result}")
        else:
            print(f"Failed: {cmd}")

if __name__ == "__main__":
    install_packages()

