import psutil

def get_battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery.power_plugged:
            status = "Plugged In"
        else:
            status = "Not Plugged In"

        percent = battery.percent
        power_plugged = battery.power_plugged
        power_status = battery.power_status

        return {
            "Status": status,
            "Battery Percentage": percent,
            "Power Plugged": power_plugged,
            "Power Status": power_status,
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    battery_info = get_battery_status()
    if battery_info:
        for key, value in battery_info.items():
            print(f"{key}: {value}")
    else:
        print("Unable to retrieve battery information.")
