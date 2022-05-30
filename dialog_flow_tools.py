import requests
from google.cloud import dialogflow


def detect_intent_texts(text_from_user):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project='useful-assistant-bot-mgib', session='123456789')
    text_input = dialogflow.TextInput(text=text_from_user, language_code='ru')
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={'session': session, 'query_input': query_input})
    dialogflow_answer = response.query_result.fulfillment_text
    return dialogflow_answer


def create_intent():
    url = 'https://dvmn.org/media/filer_public/a7/db/a7db66c0-1259-4dac-9726-2d1fa9c44f20/questions.json'
    training_phrases_devman = requests.get(url=url).json()
    questions = training_phrases_devman['Устройство на работу']['questions']
    answer = training_phrases_devman['Устройство на работу']['answer']

    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project='useful-assistant-bot-mgib')
    training_phrases = []

    for training_phrases_part in questions:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=answer)
    message = dialogflow.Intent.Message(text=text)
    intent = dialogflow.Intent(
        display_name='How to get a job', training_phrases=training_phrases, messages=[message],
    )
    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )
    print("Intent created: {}".format(response))


if __name__ == '__main__':
    create_intent()
