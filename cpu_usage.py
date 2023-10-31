import psutil

# Get the CPU usage
cpu_usage = psutil.cpu_percent()

print(f"CPU Usage: {cpu_usage}%")