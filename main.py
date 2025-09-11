import winreg
import json
import shutil
import os
#id = 1139308826 append
id = {}
mode = 1

try:
    with open('pyconfig.json', 'r') as f:
        id = json.load(f)
except:
    print('файла нет')

try:
    with open('path.txt', 'r+') as f:
        path = f.read()
except:
    print('файла нет')


def get_steam_path():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
        path, _ = winreg.QueryValueEx(key, "SteamPath")
        winreg.CloseKey(key)
        return path
    except FileNotFoundError:
        return None


path = get_steam_path()
path = path + '/userdata/'

print(path)

if not os.path.isdir('files'):  
    os.mkdir('files')
    print('создал папку')
    
while mode: #добавить поиск папки стим
    def new():  
        try:
            print('доступные аккаунты: ' + str(os.listdir(path)))
            acc=input('введи название аккаунта и ip через пробел ')
            
            accName, accId = acc.split()
            if accId in os.listdir(path):
                try:
                    with open('pyconfig.json', 'w') as f:    
                        shutil.copytree(path+accId, f'files\\'+accId)
                        id[accName] = accId
                        json.dump(id, f)
                except:
                    print('ошибка копирования, id не записан')

            else:
                print(str('актуальные аккаунты: ' + os.listdir(path)))
        except:
            print('в копировании произошла ошибка.')
           
    def exit():
        os._exit(0)

    def clear():
        try:
            os.remove('pyconfig.json')
            shutil.rmtree('files')
            os._exit(0)
        except:
            os._exit(0)
 
    def set(): #сначала удалить, потом добавить, добавить принт словаря ID
        print(id)
        ac1, ac2 = input('выбери с чего и куда скопировать настройки через пробел ').split()
        if ac1 in id:
            if ac2 in id:
                shutil.rmtree(path+id[ac2])
                shutil.copytree(f'files\\'+id[ac1], path+id[ac2], dirs_exist_ok=True)
                print('настройки замененны ')
            else:
                print('нет куда копировать')
        else:
            print('нет что копировать')
            print(ac1)
            print(ac2)
            print(id)
    def udpate():
        for i in range(len(id)):
            key = list(id.values())[i]
            print('обработан' + key)
            shutil.rmtree('files\\'+key)
            shutil.copytree(path+key, 'files\\'+key)
            
    def pr():
        print(id)
    
    
    action = input('введи действие ') 
    if action == 'new':
        new()
    elif action == 'exit':
        exit()
    elif action == 'clear':
        clear()
    elif action == 'set':
        set()
    elif action == 'print':
        pr()

    elif action == 'update':
        udpate()
    elif action == 'help':
        print('new, set, update, clear, print')


        
    else:
        print('def не найден')

