import pygame
from framework.core.singleton import Singleton


class AudioManager(Singleton):
    def __init__(self):
        pygame.mixer.init()
        self.background_music = None
        self.is_background_music_on = True
        self.is_sound_effects_on = True

    def play_background(self, src):
        if self.is_background_music_on:
            if self.background_music:
                pygame.mixer.music.stop()
            pygame.mixer.music.load(src)
            pygame.mixer.music.play(-1)
        self.background_music = src
        
    def play_effect(self, src):
        if self.is_sound_effects_on:
            sound = pygame.mixer.Sound(src)
            sound.play()

    def turn_on_music(self):
        if self.background_music:
            pygame.mixer.music.load(self.background_music)
            pygame.mixer.music.play(-1)
        self.is_background_music_on = True

    def turn_off_music(self):
        if self.background_music:
            pygame.mixer.stop()
        self.is_background_music_on = False

    def turn_on_effects(self):
        self.is_sound_effects_on = True

    def turn_off_effects(self):
        self.is_sound_effects_on = False
