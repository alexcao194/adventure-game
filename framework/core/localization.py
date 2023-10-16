from framework.core.singleton import Singleton
class Localization(Singleton):
    language = 'en'
    languages = set()
    strings = dict()
    languages = {'en', 'vi'}
    strings = {'en': {'all_settings': 'Settings', 'all_back': 'Back', 'setting_audio_toggle': 'Audio Effects', 'setting_music_toggle': 'Music', 'setting_language': 'Language', 'setting_language_en': 'English', 'setting_language_vi': 'Vietnamese', 'continue_button': 'Continue', 'restart_button': 'Restart', 'menu_button': 'Menu', 'setting_button': 'Setting', 'start_button': 'Start', 'about_button': 'About', 'lose_message_1': 'You lose!', 'lose_message_2': 'Press any key to play again', 'lose_message_3': 'Press ESC to go back to menu'}, 'vi': {'all_settings': 'Cài đặt', 'all_back': 'Quay lại', 'setting_audio_toggle': 'Hiệu ứng âm thanh', 'setting_music_toggle': 'Âm nhạc', 'setting_language': 'Ngôn ngữ', 'setting_language_en': 'Tiếng Anh', 'setting_language_vi': 'Tiếng Việt', 'continue_button': 'Tiếp tục', 'restart_button': 'Làm mới', 'menu_button': 'Menu', 'setting_button': 'Cài đặt', 'start_button': 'Bắt đầu', 'about_button': 'Giới thiệu', 'lose_message_1': 'Bạn đã thua!', 'lose_message_2': 'Nhấn phím bất kì để chơi lại', 'lose_message_3': 'Nhấn ESC để trở về màn hình chính'}}

    @property
    def all_settings(self):
        return Localization.strings[Localization.language]['all_settings']
    
    @property
    def all_back(self):
        return Localization.strings[Localization.language]['all_back']
    
    @property
    def setting_audio_toggle(self):
        return Localization.strings[Localization.language]['setting_audio_toggle']
    
    @property
    def setting_music_toggle(self):
        return Localization.strings[Localization.language]['setting_music_toggle']
    
    @property
    def setting_language(self):
        return Localization.strings[Localization.language]['setting_language']
    
    @property
    def setting_language_en(self):
        return Localization.strings[Localization.language]['setting_language_en']
    
    @property
    def setting_language_vi(self):
        return Localization.strings[Localization.language]['setting_language_vi']
    
    @property
    def continue_button(self):
        return Localization.strings[Localization.language]['continue_button']
    
    @property
    def restart_button(self):
        return Localization.strings[Localization.language]['restart_button']
    
    @property
    def menu_button(self):
        return Localization.strings[Localization.language]['menu_button']
    
    @property
    def setting_button(self):
        return Localization.strings[Localization.language]['setting_button']
    
    @property
    def start_button(self):
        return Localization.strings[Localization.language]['start_button']
    
    @property
    def about_button(self):
        return Localization.strings[Localization.language]['about_button']
    
    @property
    def lose_message_1(self):
        return Localization.strings[Localization.language]['lose_message_1']
    
    @property
    def lose_message_2(self):
        return Localization.strings[Localization.language]['lose_message_2']
    
    @property
    def lose_message_3(self):
        return Localization.strings[Localization.language]['lose_message_3']
    