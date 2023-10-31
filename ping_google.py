import subprocess

def ping_google():
    try:
        # Run the ping command to Google's IP address (8.8.8.8)
        result = subprocess.run(["ping", "8.8.8.8", "-c", "4"], stdout=subprocess.PIPE, text=True)

        # Print the output of the ping command
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ping_google()
