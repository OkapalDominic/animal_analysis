from view_header import Route, PresentView
from pathlib import Path
import os
import copy
import uuid

class Presenter:

    def __init__(self, model):
        self.model = model

    """
        Present index.html

    """

    def index(self):

        return 'index.html'

    """
        The analyze function will determine what is in the picture,
            and how you feel about it.
        @params: data is the request from a POST of the form
        Returns a Route with data to fill in the page
    """

    def analyze(self, data):
        # Ask model for a description of the image
        photo = data.files['file']
        if photo.filename != '':
            filename = str(uuid.uuid4()) + '-' + photo.filename
            path = Path.cwd() / 'static' / filename
            image = filename
            path.touch()
            path.write_bytes(photo.read())
            photo.seek(0)
            labels = self.model.labelImage(photo)
            label = labels[0].description
            photo.seek(0)
        else:
            label = None
            image = None
        # Ask model for sentiment analysis on the description entered
        description = data.form['description']
        if description == '':
            feelings = None
        else:
            feelings_output = self.model.sentiment_text(description)
            if feelings_output > 0.5:
                feelings = "really like"
            elif feelings_output > 0:
                feelings = "like"
            elif feelings_output > -0.5:
                feelings = "dislike"
            else:
                feelings = "really dislike"
        # If both an image was uploaded and sentiment indicates like or really like,
        # ask model more information about what's in the image
        if label != None and (feelings == "like" or feelings == "really like"):
            detail = self.model.knowledgeGraph(label)
        else:
            detail = None
        # translate label into Spanish
        if label == None:
            labeloutput = ''
        else:
            labeloutput = label+"s"
        translatedText = self.model.translate_text("es", labeloutput)

        # Fill data into the Route
        image_data = {
            'label': label,
            'feelings': feelings,
            'image': image,
            'translatedText': translatedText,
            'detail': detail
        }
        args = {'image_data': image_data}
        route = Route(False, 'index.html', args)
        return PresentView(route)
