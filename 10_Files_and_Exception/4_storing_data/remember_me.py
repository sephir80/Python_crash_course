import json


def get_stored_username():
    """Acquisisce nome utente se disponibile"""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def saluta_utente():
    """Saluta utente per nome"""
    username = get_stored_username()
    if username:
        print(f"Bentornato , {username}")
    else:
        username = input("come ti chiami? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"Il tuo nome <{username}> è stato salvato! ")


saluta_utente()



