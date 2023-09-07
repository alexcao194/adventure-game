class AnimationManager:
    '''
    When you want to use animation, you must create a AnimationManager object.
    AnimationManager has two dictionaries: action_animation and repeat_animation.
    action_animation is a dictionary that contains ActionAnimation objects.
    repeat_animation is a dictionary that contains RepeatAnimation objects.

    You can use play_action() to play an action animation.
    You can use change_animation() to change a repeat animation.
    '''
    current_repeat_animation = None
    current_action_animation = None
    def __init__(self, action_animation: dict, repeat_animation: dict, current_animation: str):
        self.action_animation = action_animation
        self.repeat_animation = repeat_animation
        self.current_repeat_animation = current_animation
        if(current_animation not in repeat_animation.keys()):
            raise Exception("current_animation must be in repeat_animation")

    def render(self, display):
        if(self.current_action_animation != None):
            self.action_animation[self.current_action_animation].render(display)
        else:
            self.repeat_animation[self.current_repeat_animation].render(display)

            
        if(self.current_action_animation != None and self.action_animation[self.current_action_animation].isStart == False):
            self.current_action_animation = None
            self.repeat_animation[self.current_repeat_animation].reset()
    
    def play_action(self, animation: str):
        if(animation in self.action_animation.keys()):
            self.current_action_animation = animation
            self.action_animation[self.current_action_animation].reset()
        else:
            raise Exception("Animation not found")
    
    def change_animation(self, animation: str):
        if(animation in self.repeat_animation.keys()):
            self.current_repeat_animation = animation
            self.repeat_animation[self.current_repeat_animation].reset()
        else:
            raise Exception("Animation not found")