import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


# Test

def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Sebas"))

r = requests.get("https://coreyms.com")
print(r.status_code)
