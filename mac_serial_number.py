import subprocess

def get_mac_serial_number():
    try:
        # Run the system_profiler command to obtain hardware information
        result = subprocess.check_output(["system_profiler", "SPHardwareDataType"], text=True)

        # Search for the line containing the serial number
        for line in result.splitlines():
            if "Serial Number (system)" in line:
                serial_number = line.split(":")[1].strip()
                return serial_number

    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None

if __name__ == "__main__":
    serial_number = get_mac_serial_number()
    if serial_number:
        print("Mac Serial Number:", serial_number)
    else:
        print("Unable to retrieve the Mac Serial Number.")
