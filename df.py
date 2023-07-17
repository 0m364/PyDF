import subprocess

def calculate_distance(ip_address):
    try:
        ping_process = subprocess.Popen(["ping", "-c", "4", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = ping_process.communicate()
        output = output.decode()

        if "ping: unknown host" in output:
            print(f"Could not resolve host: {ip_address}")
            return

        if "0% packet loss" not in output:
            print(f"Lost connection to host: {ip_address}")
            return

        lines = output.split("\n")

        for line in lines:
            if "min/avg/max/stddev" in line:
                latency = line.split("=")[1].split("/")[1]
                distance = int(latency)  # Modify as per your conversion formula
                print(f"Distance to {ip_address}: {distance}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
calculate_distance("8.8.8.8")
