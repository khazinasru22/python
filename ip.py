import socket

def get_default_gateway():
    try:
        # Create a socket object and connect to a remote server using a well-known address
        # (we use Google's DNS server 8.8.8.8 as an example)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            # Get the local endpoint address, which is the IP address of your computer
            local_ip = s.getsockname()[0]

        return local_ip
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    gateway = get_default_gateway()
    if gateway:
        print(f"Default Gateway (Router) IP Address: {gateway}")
    else:
        print("Unable to determine the Default Gateway (Router) IP Address.")
