from pathlib import Path
import json

folder_path = 'strings/'

folder = Path(folder_path)

def create_property(key, value, script):
    script.write(f'''
    @property
    def {key}(self):
        return Localization.strings[Localization.language]['{key}']
    ''')

script = open('framework/core/localization.py', 'w', encoding='utf-8')
script.write('''from framework.core.singleton import Singleton
class Localization(Singleton):
    language = 'en'
    languages = set()
    strings = dict()
''')

if folder.exists() and folder.is_dir():
    files = list(folder.glob('*'))
    dic = dict()
    languages = set()
    for file in files:
        local = file.name.split('.')[0]
        data = json.load(file.open(encoding='utf-8'))
        dic[local] = data
        languages.add(local)
else:
    print(f"Folder does not exist or is not a directory: {folder}")

script.write('''    languages = ''' + str(languages) + '\n')
script.write('''    strings = ''' + str(dic) + '\n')

for key, value in dic['en'].items():
        create_property(key, value, script)

script.close()
print("Generated localization.py successfully!!!")