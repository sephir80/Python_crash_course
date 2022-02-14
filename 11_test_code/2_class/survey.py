class AnonymousSurvey:
    """Raccogli le risposte anonime a una domanda del sondaggio"""

    def __init__(self, question):
        """Memorizza una domanda, e alloca risposta memorizzata"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Mostra la domanda del sondaggio"""
        print(self.question)

    def store_response(self, new_response):
        """Memorizza una singola risposta al sondaggio"""
        self.responses.append(new_response)

    def show_results(self):
        """Mostra tutte le risposte che sono state date"""
        print("Risultato Questionario:")
        for response in self.responses:
            print(f"- {response}")

