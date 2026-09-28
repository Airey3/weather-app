import requests 


base_url = "https://api.neshan.org/v2/reverse"

params = {
    'lat': 34.7901,
    'lon': 48.5132,
}

headers = {
    'Api-Key': 'service.6a874f0656f34e00ba911d3aeca209ec',
}

response = requests.get(base_url, headers=headers, params=params, timeout=10)
address_data = response.json()

print("\n --- received data ---")
print(address_data['formatted_address'])
