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


def get_new_username():
    """Richiedi il nome utente"""
    username = input("come ti chiami? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username



def saluta_utente():
    """Saluta utente per nome"""
    username = get_stored_username()
    if username:
        print(f"Bentornato , {username}")
    else:
        username = get_new_username()
        print(f"Ci ricorderemo di te quando torni , {username}")


saluta_utente()
