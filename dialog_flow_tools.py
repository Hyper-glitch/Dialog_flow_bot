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
