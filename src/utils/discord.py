from src import *

class discord:
    # Not leaking my hard work database :sob:
    NOT_LEAKING = '0'

    # Not leaking my hard work database :sob:
    def errordatabase(text):
        db = {
            discord.NOT_LEAKING: 'NOT_LEAKING',
        }

        for key, message in db.items():
            if key in text:
                return message, key

        if isinstance(text, str):
            try:
                import json
                text = json.loads(text)
            except:
                return text, None

        if isinstance(text, dict) and 'message' in text:
            return text['message'], None

        return text, None
