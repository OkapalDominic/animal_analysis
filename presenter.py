from view_header import Route, PresentView

class Presenter:
    def __init__(self,model):
        self.model = model

    def index(self):
        """
        Present index.html

        """
        return 'index.html'

    def analyze(self,data):
    	photo = data.files['file']
    	(labels,uri) = self.model.labelImage(photo)
    	# TODO: Get sentiment from data.form['description'] and set feelings below to it.
    	image_data = dict(label=labels[0].description, feelings="really like", image=uri)
    	args = {'image_data':image_data}
    	route = Route(False, 'index.html', args)
    	return PresentView(route)
