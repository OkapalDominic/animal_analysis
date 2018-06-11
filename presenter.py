from view_header import Route, PresentView

class Presenter:
    def __init__(self,model):
        self.model = model

    def index(self):
        """
        Present index.html

        """
        return 'index.html'
	
	# TODO: give this function a docstring?
    def analyze(self,data):
    	photo = data.files['file']
    	(labels,uri) = self.model.labelImage(photo)
    	# TODO: Get sentiment from data.form['description'] and set feelings below to it.
    	description = data.form['description']
    	feelings_output = self.model.sentiment_text(description)
    	if feelings_output > 0:
    	    feelings_output = "really like"
    	else:
    	    feelings_output = "really dislike"
    	image_data = dict(label=labels[0].description, feelings=feelings_output, image=uri)
    	args = {'image_data':image_data}
    	route = Route(False, 'index.html', args)
    	return PresentView(route)
	
	