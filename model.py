from IModel import IModel
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import storage
from google.cloud import language
from google.cloud import translate
from google.cloud.language import enums
from google.cloud.language import types
import six
import os
import sys
import json
import urllib.request
from urllib.parse import urlencode
import io


class AppModel(IModel):
    def __init__(self, app):
        self.app = app

    """
		Finds labels for the photo passed in
		@params: photo is the image to check, use photo = request.files['file']
		Returns a tuple containing an array of labels and the uri to the image
    """

    def labelImage(self, photo):
        # Instantiates a client
        client = vision.ImageAnnotatorClient()
        try:
            response = client.annotate_image({
                'image': photo,
                'features': [{'type': vision.enums.Feature.Type.LABEL_DETECTION}],
            })
        except Exception as error:
            print(error)
        labels = response.label_annotations
        # Returns the labels detected in the image
        return labels

    """
        Sends query to google knowledge graph
        @params: label is a string that is sent
        Returns a description of the first search result obtained.
    """

    def knowledgeGraph(self, label):
        api_key = open('.api_key').read()
        query = label
        service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
        params = {
            'query': query,
            'limit': 1,
            'indent': True,
            'key': api_key,
        }
        url = service_url + '?' + urlencode(params)
        response = json.loads(urllib.request.urlopen(url).read())
        return response['itemListElement'][0]['result']['detailedDescription']['articleBody']

    """
        Asks google language to analyze the sentiment
        @params: text is the string to analyze
        Returns a value from -1 to 1, which corresponds to how positive text is.
    """

    def sentiment_text(self, text):
        client = language.LanguageServiceClient()

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')
        response = client.analyze_sentiment({
            'content': text,
            'type': enums.Document.Type.PLAIN_TEXT,
        }).document_sentiment
        feeling = response.score
        return (feeling)

    """
        Takes in a target language and a text to translate
        using google.cloud translate API
        
        Returns the translated string in the target language
	    
    """

    def translate_text(self, target, text):
        translate_client = translate.Client()

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        result = translate_client.translate(
            text, target_language=target)

        return result['translatedText']
