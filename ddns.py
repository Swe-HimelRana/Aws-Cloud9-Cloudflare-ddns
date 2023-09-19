import requests
import json

def get_public_ip():
    try:
        response = requests.get('https://ifconfig.me')
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Unable to retrieve public IP"
    except requests.RequestException:
        return "Unable to connect to the public IP service"



# Replace with your Cloudflare API key and email
api_key = 'YOUR API KEY ZONE EDIT'
email = 'YOUR ACCOUNT EMAIL'

# The Zone ID for your domain (replace with your own)
zone_id = 'ZONE ID'

# The DNS record you want to update
record_id = 'RECORD ID'  # Replace with the specific record ID you want to update
new_record_value = get_public_ip()  # Replace with the new record value

# Cloudflare API endpoint URLs
base_url = 'https://api.cloudflare.com/client/v4/'
zone_dns_url = f'{base_url}zones/{zone_id}/dns_records/{record_id}'

# Headers for the API request
headers = {
    'Authorization': 'Bearer API_KEY',
    'X-Auth-Email': email,
}


# Data for updating the DNS record
data = {
    'content': new_record_value,
    "type": "A",
    "name": "ddns.yourdomain.com",
}

try:
    # Send a PUT request to update the DNS record
    response = requests.put(zone_dns_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print(f'DNS record updated successfully to {new_record_value}')
    else:
        print(f'Failed to update DNS record. Status code: {response.status_code}')
        print(response.text)

except Exception as e:
    print(f'An error occurred: {str(e)}')

