from framework.core.singleton import Singleton
class Localization(Singleton):
    language = 'en'
    languages = set()
    strings = dict()
    languages = {'en', 'vi'}
    strings = {'en': {}, 'vi': {}}
