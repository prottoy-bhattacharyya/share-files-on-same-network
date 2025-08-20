import subprocess

def get_ip():
    try:
        result = subprocess.run(["ifconfig"], capture_output=True, text=True) #for linux
    except:
        result = subprocess.run(["ipconfig"], capture_output=True, text=True) #for windows
    
    return result.stdout