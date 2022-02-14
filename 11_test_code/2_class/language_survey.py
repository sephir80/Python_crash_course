from survey import AnonymousSurvey

# Define a question, and make a survey

question = "Qual'è stato la prima lingua che hai imparato a parlare?"
my_survey = AnonymousSurvey(question)

# Show the question and store responses to the question.
my_survey.show_question()
print("Inserisci 'q' in qualsiasi momento per uscire.\n")
while True:
    response = input("Linguaggio: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nGrazie a tutti quelli che hanno partecipato al questionario!")
my_survey.show_results()