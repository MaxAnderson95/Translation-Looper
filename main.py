import random
import argparse
import requests
import uuid
import os

argparse = argparse.ArgumentParser()
argparse.add_argument("--phrase", required=True)
argparse.add_argument("--source-language", default='en')
argparse.add_argument("--rounds", type=int, default=20)
args = argparse.parse_args()
phrase = args.phrase
source = args.source_language
rounds = args.rounds


class Translator:
    def __init__(self):
        if "SUBSCRIPTION_KEY" not in os.environ:
            raise Exception("Please export env var SUBSCRIPTION_KEY with your Azure Translation Service API key")
        else:
            subscription_key = os.environ.get("SUBSCRIPTION_KEY")

        if "LOCATION" not in os.environ:
            raise Exception("Please export env var LOCATION with your Azure Translation Service API key")
        else:
            location = os.environ.get("LOCATION")

        self.headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    base_url = "https://api.cognitive.microsofttranslator.com"

    def translate(self, text: str, src: str, dest: str):
        params = {
            'api-version': '3.0',
            'from': src,
            'to': dest
        }
        body = [{
            'text': text
        }]

        request = requests.post(self.base_url + '/translate', params=params, headers=self.headers, json=body)
        response = request.json()
        return response[0]["translations"][0]["text"]

    @staticmethod
    def get_supported_languages():
        params = {
            'api-version': '3.0',
            'scope': 'translation'
        }
        request = requests.get(Translator.base_url + '/languages', params=params)
        response = request.json()
        return response['translation']

    @staticmethod
    def get_random_language():
        choice = random.choice(list(Translator.get_supported_languages().keys()))
        if choice == "tlh-Latn" or choice == "tlh-Piqd":  # Exclude Klingon because it completely destroys the meaning of the sentence
            choice = Translator.get_random_language()
        return choice


def rotate(translator: Translator, phrase: str, source: str, rounds: int):
    last_translation = phrase
    src = source
    print(f"Original phrase: {phrase}")
    print("")

    for i in range(rounds):
        if i == rounds - 1:  # If it's the final round, set the destination language to be the original source language.
            language = source
        else:
            language = Translator.get_random_language()
        last_translation = translator.translate(last_translation, src, language)
        language_name = Translator.get_supported_languages()[language]["name"]
        print(f"Translating to {language_name} => {last_translation}")
        src = language  # Set the next source language to be the current iteration's destination language

    print("")
    print(f"Final translation after {rounds} rounds => {last_translation}")


def main():
    translator = Translator()
    rotate(translator, phrase, source, rounds)


if __name__ == "__main__":
    main()
