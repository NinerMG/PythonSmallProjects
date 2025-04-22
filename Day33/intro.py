# Application Programming Interfaces -> API
# API to zbiór komend, funkcji, protokołów i obiektów uzywanych do tworzenia oprogramownia
# lub interakcji z zewnętrznym systemem
# co to jest i do czego jest API Endpoint

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.text)