from framework.game.widget.widget import Widget
class WidgetGroup:
    def __init__(self, name, widgets):
        self.name = name
        self.widgets = widgets
        self.list = []
    
    def add(self, widget: Widget):
        self.list.append(widget)
    
    def remove(self, widget: Widget):
        self.list.remove(widget)
    
    def render(self, display):
        for widget in self.list:
            widget.render(display)
    def update(self, event):
        for widget in self.list:
            widget.update(event) 