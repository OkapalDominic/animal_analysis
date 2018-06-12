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
	"""
	The analyze function will determine what is in the picture, and how you feel about it.
	"""
    def analyze(self,data):
    	try:
    		photo = data.files['file']
    		(labels,uri) = self.model.labelImage(photo)
    		labels = labels[0].description
    	except:
    		labels = None
    		uri = None
    	# Get sentiment from data.form['description'] and set feelings below to it.
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
    	image_data = dict(label=labels, feelings=feelings, image=uri)
    	args = {'image_data':image_data}
    	route = Route(False, 'index.html', args)
    	return PresentView(route)
	
	