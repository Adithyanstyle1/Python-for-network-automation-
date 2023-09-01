import os

ip_add = "8.8.8.8"
for check in ip_add:
    ping = os.popen(f"ping {ip_add}").read()
    if "Received = 4" in ping:
        print(f"ping {ip_add} is successful")
        break
    else:
        print(f"ping {ip_add} is not successful")
        break