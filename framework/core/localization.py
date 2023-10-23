from framework.core.singleton import Singleton
class Localization(Singleton):
    language = 'en'
    languages = set()
    strings = dict()
    languages = {'vi', 'en'}
    strings = {'en': {'all_settings': 'Setting', 'all_back': 'Back', 'all_continue': 'Continue', 'all_restart': 'Restart', 'all_menu': 'Menu', 'all_start': 'Start', 'all_about': 'About', 'setting_audio_toggle': 'Audio Effects', 'setting_music_toggle': 'Music', 'setting_language': 'Language', 'setting_language_en': 'English', 'setting_language_vi': 'Vietnamese', 'loose_gameover': 'Game over!', 'get_key': 'You got a key!', 'hint_message': 'follow the ground to find the key'}, 'vi': {'all_settings': 'Cài đặt', 'all_back': 'Quay lại', 'all_continue': 'Tiếp tục', 'all_restart': 'Chơi lại', 'all_menu': 'Màn hình chính', 'all_start': 'Bắt đầu', 'all_about': 'Giới thiệu', 'setting_audio_toggle': 'Hiệu ứng âm thanh', 'setting_music_toggle': 'Âm nhạc', 'setting_language': 'Ngôn ngữ', 'setting_language_en': 'Tiếng Anh', 'setting_language_vi': 'Tiếng Việt', 'loose_gameover': 'Trò chơi kết thúc!', 'get_key': 'Bạn đã nhận được chìa khóa!', 'hint_message': 'Nhìn vào mặt đất để tìm chìa khóa'}}

    @property
    def all_settings(self):
        return Localization.strings[Localization.language]['all_settings']
    
    @property
    def all_back(self):
        return Localization.strings[Localization.language]['all_back']
    
    @property
    def all_continue(self):
        return Localization.strings[Localization.language]['all_continue']
    
    @property
    def all_restart(self):
        return Localization.strings[Localization.language]['all_restart']
    
    @property
    def all_menu(self):
        return Localization.strings[Localization.language]['all_menu']
    
    @property
    def all_start(self):
        return Localization.strings[Localization.language]['all_start']
    
    @property
    def all_about(self):
        return Localization.strings[Localization.language]['all_about']
    
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
    def loose_gameover(self):
        return Localization.strings[Localization.language]['loose_gameover']
    
    @property
    def get_key(self):
        return Localization.strings[Localization.language]['get_key']
    
    @property
    def hint_message(self):
        return Localization.strings[Localization.language]['hint_message']
    