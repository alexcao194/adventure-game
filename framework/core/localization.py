from framework.core.singleton import Singleton
class Localization(Singleton):
    language = 'en'
    languages = set()
    strings = dict()
    languages = {'vi', 'en'}
    strings = {'en': {'menu': 'Menu', 'home': 'Home', 'about': 'About', 'contact': 'Contact', 'welcome': 'Welcome', 'change_language': 'Change locale'}, 'vi': {'menu': 'Menu', 'home': 'Trang chủ', 'about': 'Giới thiệu', 'contact': 'Liên hệ', 'welcome': 'Chào mừng bạn đến với trang web của chúng tôi', 'change_language': 'Thay đổi ngôn ngữ'}}

    @property
    def menu(self):
        return Localization.strings[Localization.language]['menu']
    
    @property
    def home(self):
        return Localization.strings[Localization.language]['home']
    
    @property
    def about(self):
        return Localization.strings[Localization.language]['about']
    
    @property
    def contact(self):
        return Localization.strings[Localization.language]['contact']
    
    @property
    def welcome(self):
        return Localization.strings[Localization.language]['welcome']
    
    @property
    def change_language(self):
        return Localization.strings[Localization.language]['change_language']
    