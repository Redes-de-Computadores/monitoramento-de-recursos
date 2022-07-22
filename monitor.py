import psutil

def set_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f}{unit}{suffix}"
        bytes /= factor

def mem():
    mem = psutil.virtual_memory()

    total = "Total: " + str(set_size(mem.total))
    free = "Free: " + str(set_size(mem.free))
    used = "In Use: " + str(set_size(mem.used))
    percent = "Percentage of Use: " + str(mem.percent) + "%"

    mem_data = "Memory" + ";" + total + ";" + free + ";" + used + ";" + percent
    return mem_data

def cpu():
    logical = "Logical Cores: " + str(psutil.cpu_count())
    nonlogical = "Non-Logical Cores:" + str(psutil.cpu_count(logical=False))
    percent = "Percentage of Use: " + str(psutil.cpu_percent(interval=1)) + "%"

    cpu_data = "CPU" + ";" + logical + ";" + nonlogical + ";" + percent
    return cpu_data

def disk():
    disk = psutil.disk_usage('C:\\')

    total = "Total: " + str(set_size(disk.total))
    free = "Free: " + str(set_size(disk.free))
    used = "In Use: " + str(set_size(disk.used))
    percentage = "Percentage of Use: " + str(disk.percent) + '%'

    disk_data = "Disk" + ";" + total + ";" + free + ";" + used + ";" + percentage
    return disk_data