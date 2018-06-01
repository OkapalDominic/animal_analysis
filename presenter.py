from view_header import Route, PresentView

class Presenter:
    def __init__(self,model):
        self.model = model

    def index(self):
    """
    Present index.html

    """
        return 'index.html'
