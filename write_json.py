import json


def write_json(note_json, file_name):
    with open(file_name, "a", encoding='utf-8') as f:
        json.dump(note_json, f, indent=4, ensure_ascii=False)

        '''
        Если sure_ascii имеет значение true (по умолчанию), 
        в выводе гарантированно будут экранированы все входящие символы, отличные от ASCII. 
        Если sure_ascii имеет значение false, эти символы будут выводиться как есть.  
        '''
