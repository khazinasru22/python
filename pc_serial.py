import subprocess

def get_serial_number():
    try:
        command = "dmidecode -t system | grep 'Serial Number'"
        result = subprocess.check_output(command, shell=True, text=True)
        serial_number = result.strip().split(":")[1].strip()
        return serial_number
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    serial_number = get_serial_number()
    if serial_number:
        print("PC Serial Number:", serial_number)
    else:
        print("Unable to retrieve the PC Serial Number.")
