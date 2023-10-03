import requests

def get_public_ip():
    try:
        # Use a public API to fetch your public IP address
        response = requests.get("https://api4.ipify.org?format=json")
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            public_ip = data["ip"]
            return public_ip
        else:
            print("Failed to retrieve public IP. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))
    
    return None

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print("Your public IP address is:", public_ip)
    else:
        print("Unable to retrieve public IP address.")
