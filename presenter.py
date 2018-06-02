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
    	labels = self.model.labelImage(photo)
    	d = [dict(label=labels[0],feelings="really like")]
    	args = {'image_data':d}
    	route = Route(False, 'index.html', args)
    	return PresentView(route)
