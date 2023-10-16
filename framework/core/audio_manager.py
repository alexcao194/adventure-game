import pygame
from framework.core.singleton import Singleton


class AudioManager(Singleton):
    background_music = None
    is_background_music_on = True
    is_sound_effects_on = True

    def play_background(src):
        if AudioManager.is_background_music_on:
            if AudioManager.background_music:
                pygame.mixer.music.stop()
            pygame.mixer.music.load(src)
            pygame.mixer.music.play(-1)
        AudioManager.background_music = src
        
    def play_effect(src):
        if AudioManager.is_sound_effects_on:
            sound = pygame.mixer.Sound(src)
            sound.play()

    def turn_on_music():
        if AudioManager.background_music:
            pygame.mixer.music.load(AudioManager.background_music)
            pygame.mixer.music.play(-1)
        AudioManager.is_background_music_on = True

    def turn_off_music():
        if AudioManager.background_music:
            pygame.mixer.stop()
        AudioManager.is_background_music_on = False

    def turn_on_effects():
        AudioManager.is_sound_effects_on = True

    def turn_off_effects():
        AudioManager.is_sound_effects_on = False
