import psutil
import socket

# CPU 사용량 조회
# 현재 시스템 전체 CPU 사용률을 백분율로 나타내는 float를 반환합니다.
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(psutil.cpu_times_percent (interval=1))

# 논리적 cpu갯수
print(psutil.cpu_count())

# 물리적 cpu갯수
print(psutil.cpu_count(logical=False))
print(psutil.cpu_freq(percpu=True))
print(psutil.cpu_freq().current)
print(psutil.cpu_freq())



# 메모리 사용량 조회 #byte임
# total=34264621056, available=10772762624, percent=68.6, used=23491858432, free=10772762624
print(f"Memory Usage: {psutil.virtual_memory()}")
print(f"Memory Usage: {psutil.virtual_memory().percent}")
print(f"Memory total: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
print(f"Memory used: {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
print(f"Memory available: {psutil.virtual_memory().available / (1024 ** 3):.2f} GB")

# 디스크 사용량 조회
# disk_usage = p.disk_usage('/')
print(f"Disk Usage: {psutil.disk_usage('c:')}")
print(f"Disk Usage: {psutil.disk_usage('d:')}")

# 네트워크 정보 조회
# bytes_sent: number of bytes sent
# bytes_recv: number of bytes received
# packets_sent: number of packets sent
# packets_recv: number of packets received
# errin: total number of errors while receiving
# errout: total number of errors while sending
# dropin: total number of incoming packets which were dropped
# dropout: total number of outgoing packets which were dropped (always 0 on macOS and BSD)
print(psutil.net_io_counters())



hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
print (hostip)