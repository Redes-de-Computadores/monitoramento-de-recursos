import psutil

def set_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f}{unit}{suffix}"
        bytes /= factor

def mem():
    mem = psutil.virtual_memory()

    total = "total=" + str(set_size(mem.total))
    free = "free=" + str(set_size(mem.free))
    used = "used=" + str(set_size(mem.used))
    percent = "percent=" + str(mem.percent) + "%"

    mem_data = total + ";" + free + ";" + used + ";" + percent
    return mem_data

def cpu():
    logical = "logical=" + str(psutil.cpu_count())
    nonlogical = "nonlogical=" + str(psutil.cpu_count(logical=False))
    percent = "percent=" + str(psutil.cpu_percent(interval=1)) + "%"

    cpu_data = logical + ";" + nonlogical + ";" + percent
    return cpu_data

def disk():
    disk = psutil.disk_usage('C:\\')

    total = "total=" + str(set_size(disk.total))
    free = "free=" + str(set_size(disk.free))
    used = "used=" + str(set_size(disk.used))
    percentage = "percent=" + str(disk.percent) + '%'

    disk_data = total + ";" + free + ";" + used + ";" + percentage
    return disk_data