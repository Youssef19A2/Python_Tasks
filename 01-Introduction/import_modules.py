import psutil

#get CPU usage percentage
print("CPU usage:" , psutil.cpu_percent())

#get memory usage statistics
memory=psutil.virtual_memory()
print("Total memory: ",memory.total/1000000000,"G")
print("Available memory: ",memory.available/1000000000,"G")
print("Used memory: ",memory.used/1000000000,"G")
print("Memory usage percentage: ",memory.percent)

#get disk usage statistics
disk=psutil.disk_usage('/')
print("Total disk space: ", disk.total/1000000000,"G")
print("Used disk space: ",disk.used/1000000000,"G")
print("Free disk space",disk.free/1000000000,"G")
print("Disk usage percentage: ",disk.percent)
