import requests
import socket

def get_subdomains(domain):
    subdomains = set()
    url = f'https://crt.sh/?q=%.{domain}&output=json'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        for item in data:
            subdomains.add(item['name_value'])
    for subdomain in subdomains.copy():
        try:
            socket.gethostbyname(subdomain)
        except socket.error:
            subdomains.remove(subdomain)
    return subdomains

# Prompt user to enter domain
domain = input("Enter domain: ")

# Call get_subdomains function with user input
subdomains = get_subdomains(domain)

# Print the subdomains on the screen
print(f"Subdomains for {domain}:")
for subdomain in subdomains:
    print(subdomain)
