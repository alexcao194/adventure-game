import pygame


class Animation:
    '''
    Base class for all animations.
    src - path to the folder containing the frames
    frame_count - number of frames in the animation
    entity - the entity that the animation is attached to
    delay - delay between frames
    '''
    frame_count = 0
    def __init__(self, src: str, frame_count: int, entity, delay: int = 0):
        if(self.__class__.__name__ == 'Animation'):
            raise Exception("Animation cannot be instantiated")
        self.src = src
        self.frame_count = frame_count
        self.current_frame = 0
        self.images = []
        self.entity = entity
        self.delay = delay
        self.delay_count = 0
        self.init()

    def init(self):
        for i in range(self.frame_count):
            image = pygame.image.load(self.src + str(i) + '.png')
            width = image.get_width()
            height = image.get_height()
            image = pygame.transform.scale(image, self.entity.hitbox.to_tuple())            
            self.images.append(image)
    
    def next_frame(self):
        if self.delay_count < self.delay:
            self.delay_count += 1
        else:
            self.delay_count = 0
            self.current_frame += 1
            if(self.current_frame >= self.frame_count):
                self.current_frame = 0
        return self.images[self.current_frame]

    def reset(self):
        self.current_frame = 0
        self.delay_count = 0
    
    def render(self, display):
        display.blit(self.next_frame(), self.entity.position.to_tuple())



class ActionAnimation(Animation):
    '''
    Animation that plays once and stops.
    '''
    def __init__(self, src: str, frame_count: int, entity, delay: int = 0):
        super().__init__(src, frame_count, entity, delay)
        
    def reset(self):
        self.isStart = True
        super().reset()

    def next_frame(self):
        next_frame = super().next_frame()
        if(self.current_frame == self.frame_count - 1):
            self.isStart = False
        return next_frame

    def render(self, display):
        super().render(display)



class RepeatAnimation(Animation):
    '''
    Animation that plays repeatedly.
    '''
    def __init__(self, src: str, frame_count: int, entity, delay: int = 0):
        super().__init__(src, frame_count, entity, delay)

        


    