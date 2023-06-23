from FileManager import *
from Config import *

class ConfigBundle:
    def __init__(self, file) -> None:
        self.filename = file
        self.configs = {} # {category: Config}
        self.common = {} #{category: Config}
        self.filemanager = FileManager()
        config_sections = self.filemanager.load(file)
        for i in config_sections:
            if i.isDefault():
                self.common[i.category] = i
                continue

            if(i.category in self.configs):
                self.configs[i.category].append(i)
            else:
                self.configs[i.category] = [i]

    def merge(self, category):
        if len(self.configs[category]) <= 2:
            print(f'Ignoring category {category} as it only contains 2 sections.')
            return self
        attr_count = {} # {Name: [[name,value], count]}
        attr_common = []


        for i in self.configs[category]: # for each [category: name] section
            for attr in i.attrs: # for each of [name, value]
                if(attr.name in attr_count and attr == attr_count[attr.name][0]):
                    attr_count[attr.name][1] = attr_count[attr.name][1] + 1
                else:
                    attr_count[attr.name] = [attr, 1]

        config_count = len(self.configs[category])
        for i in attr_count:
            if(attr_count[i][1] >= config_count):
                # print(f'Attrb {i}  = {attr_count[i][0].value} repeated {attr_count[i][1]} times out of {config_count}.')
                attr_common.append(attr_count[i][0])

        new_bundle = self
        #Generate common attr
        if(category not in new_bundle.common):
            new_bundle.common[category] = Config(f'*{category}-common*', category)

        for attr in attr_common:
            new_bundle.common[category].addAttr(attr.name, attr.value)
            for config in new_bundle.configs[category]:
                config.delAttr(attr.name)
        
        for config in new_bundle.configs[category]:
                config.addAttr("inherits", new_bundle.common[category].name)

        return new_bundle
    
    def write(self, filename):
        self.filemanager.write(filename, self)

        


