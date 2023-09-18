from framework.game.widget.widget import Widget

class WidgetGroup:
    '''
    WidgetGroup is a group of widgets.
    widgets: list - the list of widgets
    '''
    def __init__(self):
        self.widgets = []
    
    def add(self, widget: Widget):
        self.widgets.append(widget)
    
    def remove(self, widget: Widget):
        self.widgets.remove(widget)
    
    def render(self, display):
        for widget in self.widgets:
            widget.render(display)
    def update(self, event):
        for widget in self.widgets:
            widget.update(event) 