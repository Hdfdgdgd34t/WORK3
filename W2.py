import requests
from requests.auth import HTTPBasicAuth
BASE_URL = 'http://127.0.0.1:5555/items'
AUTH = HTTPBasicAuth('admin', 'password')
def make_request(method, endpoint='', data=None):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.request(method, url, json=data, auth=AUTH)
        response.raise_for_status()
        if response.text:
            return response.json()
        return None
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err.response.status_code} - {err.response.text}")
    except Exception as e:
        print(f"Error: {e}")
    return None
def fetch_items():
    print("Fetching all items...")
    items = make_request('GET')
    if items:
        print("Items in catalog:")
        for item in items:
            print(item)
def add_item(name, price, size, weight, color):
    print(f"Adding new item: {name}")
    item_data = {
        'name': name,
        'price': price,
        'size': size,
        'weight': weight,
        'color': color
    }
    response = make_request('POST', data=item_data)
    if response:
        print(f"Item added successfully: {response}")
def update_item(item_id, **kwargs):
    print(f"Updating item with ID {item_id}...")
    response = make_request('PUT', f"/{item_id}", data=kwargs)
    if response:
        print(f"Item updated successfully: {response}")
def delete_item(item_id):
    print(f"Deleting item with ID {item_id}...")
    response = make_request('DELETE', f"/{item_id}")
    if response is None:
        print("Item deleted successfully")
if __name__ == '__main__':
    fetch_items()
    add_item("New Item", 150.0, "L", 2.5, "Green")
    update_item(1, price=200.0, size="XL", color="Yellow")
    delete_item(1)
    fetch_items()