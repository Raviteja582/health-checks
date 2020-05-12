import shutil
def disk(disk):
    space=shutil.disk_usage(disk)
    d=space.free/space.total*100
    return d>20
print("OK") if disk("/") else print("Not ok!") 
