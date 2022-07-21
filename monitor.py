import psutil

def set_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f}{unit}{suffix}"
        bytes /= factor

def mem():
    mem = psutil.virtual_memory()
    print(f'''
    ===============
      Memory Info  
    ===============
    Total:  {set_size(mem.total)}
    Free:  {set_size(mem.free)}
    In Use:  {set_size(mem.used)}
    Usage Percentage:  {mem.percent}%
    ''')

def cpu():
    print(f'''
    ============
      CPU Info  
    ============
    Logical Cores: {psutil.cpu_count()}
    Non-Logical Cores: {psutil.cpu_count(logical=False)}
    Usage Percentage: {psutil.cpu_percent(interval=1)}%
    ''')

def disk():
    disk = psutil.disk_usage('C:\\')
    print(f'''
    =============
      Disk Info  
    =============
    Total Usage: {set_size(disk.total)}
    Free: {set_size(disk.free)}
    In Use: {set_size(disk.used)}
    Usage Percentage: {disk.percent}%

    ''')