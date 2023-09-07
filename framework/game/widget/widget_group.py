from framework.game.widget.widget import Widget


'''
WidgetGroup is a group of widgets.
name: str - the name of the widget group
widgets: list - the list of widgets
'''
class WidgetGroup:
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