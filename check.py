import psutil
def cpu():
    if psutil.cpu_percent(1)<75:
        return True
    return False
print("Ok") if cpu() else print("Not OK")     
