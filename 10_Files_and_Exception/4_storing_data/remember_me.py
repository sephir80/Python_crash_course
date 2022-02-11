import json


def saluta_utente():
    """Saluta utente per nome"""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("Come ti chiami?")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"Il tuo nome <{username}> è stato salvato! ")
    else:
        print(f"Bentornato , {username}")


saluta_utente()



