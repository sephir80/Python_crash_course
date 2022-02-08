import json

username = input("Come ti chiami?")

filename = "username.json"

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"Il tuo nome <{username}> è stato salvato! ")
