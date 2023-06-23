import re
from Config import *
import os

class FileManager:
    def __init__(self) -> None:
        self.contents = ""

    def write(self, filename, configbundle):
        new_cont = ""
        for config_cat in configbundle.configs:
            if(config_cat in configbundle.common):
                common = configbundle.common[config_cat]
                new_cont = new_cont + self.write_sec(common)

            for config_sec in configbundle.configs[config_cat]:
                new_cont = new_cont + self.write_sec(config_sec)
                new_cont = new_cont + "\n"
        with open(filename, 'r') as file:
            if "[" in file.read():
                print(f'(Error) file {filename} not empty, not writing.')
        with open(filename, 'w') as file:
            file.write(new_cont)

    def write_sec(self, config):
        config_sec = ""
        config_sec = config_sec + f'[{config.category}:{config.name}]\n'
        for attr in config.attrs:
            config_sec = config_sec + (f'{attr.name} = {attr.value}\n')
        config_sec = config_sec + "\n"
        
        return config_sec

    def load(self, filename):
        # Read file
        if(not os.path.exists(filename)):
            print("Error, file not fount, Exiting.")
            return
        with open(filename, 'r') as file:
            self.contents = file.read()
        contents = self.contents
        # Get all Config Sections
        sections = re.findall(r'\[.*\:.*\]', contents)
        print(f'Found {len(sections)} config sections in file')

        # Create Config objects based on contents
        configs = []
        index = 0
        while index < len(sections):
            # Get Config category and name
            sec = sections[index]
            category, name = sec.split(":")
            name = name[:-1]
            category = category [1:]
            config = Config(name, category)


            if(index < len(sections)-1):
                attrs_str = contents[contents.index(sec):contents.index(sections[index+1])]
            else:
                attrs_str = contents[contents.index(sec):]
                
            attrs = re.findall(r'.*=.*', attrs_str)
            for attr in attrs:
                setting, value = attr.split(" = ", 1)
                if "#" in setting:
                    continue
                # print(f'Adding config {setting}:{value}')
                config.addAttr(setting, value)

            configs.append(config)
            index = index + 1
        
        return configs
    
