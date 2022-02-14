def get_formatted_name(nome, cognome, secondo_nome=''):
    """" Genera un ordinato nome completo"""
    if secondo_nome:
        full_name = f"{nome} {secondo_nome} {cognome}"
    else:
        full_name = f"{nome} {cognome}"
    return full_name.title()
