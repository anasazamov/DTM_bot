import requests
from pprint import pprint

response = requests.get("https://shahzodbek.avotra.uz/mandat/api.php?id=3807445")

print(response.status_code)
print(response.url)
# print(response.content.decode())
print(response.cookies.add_cookie_header(response))
pprint(response.json())