import winreg
import json
import shutil
import os
from tkinter import *
from tkinter import ttk

import steam_web_api._version
steam_web_api._version.__version__ = "0.0.0"
import steam_web_api
from steam_web_api import Steam




steam = Steam("YOUR STEAM KEY")


def exit():
    os._exit(0)

tk = Tk()
Id = {}
tk.protocol("WM_DELETE_WINDOW", exit)
tk.geometry("1000x600+450+250")
AccInFolder = {}

try:
    with open('pyconfig.json', 'r',encoding='utf-8') as f:
        Id = json.load(f)
except:
    print('файла нет')
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
    path, _ = winreg.QueryValueEx(key, "SteamPath")
    winreg.CloseKey(key)
    path = path + '/userdata/'
except FileNotFoundError:
    print('что у тебя со стимом?')

for i in (set(os.listdir(path))-set(list(Id.values()))):
    try:
        folder = os.listdir(path)
        i = int(i)
        user = steam.users.get_user_details(str(76561197960265728+i))
        AccInFolder[user.get('player', {}).get('personaname')] = i
        print(AccInFolder)
    except:
        print('какое то говно в папке ' + str(i))
        shutil.rmtree(path + str(i))


if not os.path.isdir('files'):  
    os.mkdir('files')
    print('создал папку')
    




def New():
    global Id  
    try:
        accName = idlist.get()
        accId = AccInFolder[accName]
        accId = str(accId)
        try:
            shutil.copytree(path+accId, f'files\\'+accId)
            try:
                with open('pyconfig.json', 'w', encoding='utf-8') as f:
                    Id[accName] = accId
                    print(Id)
                    json.dump(Id, f,ensure_ascii=False,)
                    list_Set.configure(values=list(Id.keys()), state="readonly")
                    list_Set_1.configure(values=list(Id.keys()), state="readonly")
                    idlist.configure(values=list(set(AccInFolder.keys()) - set(Id.keys())))
                    idlist.current(0)

            except:
                print("ошибка №3 NEW записи в словарь")
        except:
            print('ошибка №2 NEW копирования')
    except:
        print('ошибка NEW 1')
    
 
        
       


def Clear():
    try:
        os.remove('pyconfig.json')
        shutil.rmtree('files')
        os._exit(0)
    except:
        os._exit(0)
def Set(): 
    try:
        ac1 = list_Set.get()
        ac2 = list_Set_1.get()
        if ac1 in Id:
            if ac2 in Id:
                shutil.rmtree(path+Id[ac2])
                shutil.copytree(f'files\\'+Id[ac1], path+Id[ac2], dirs_exist_ok=True)
                print('настройки замененны ')
            else:
                print('нет куда копировать')
        else:
            print('нет что копировать')
            print(ac1)
            print(ac2)
            print(Id)
    except:
        print('Ошибка Set')
def Update():
    try:
        for i in range(len(Id)):
            key = list(Id.values())[i]
            print('обработан ' + key)
            shutil.rmtree('files\\'+key)
            shutil.copytree(path+key, 'files\\'+key)
    except:
        print('ошибка Update')
        
def pr():
    print(Id)


ttk.Label(text='Для смены настроек ').place(relx=0.4, rely=0.08, anchor="c", relwidth=0.2, relheight=0.05)
ttk.Label(text='Добавление аккаунтов').place(relx=0.1, rely=0.08, anchor="c", relwidth=0.2, relheight=0.05)


list_Set_1 = ttk.Combobox(values=list(Id.keys()), state="readonly") # список ключей
list_Set = ttk.Combobox(values=list(Id.keys()), state="readonly") # список ключей


idlist = ttk.Combobox(values=list(set(AccInFolder.keys()) - set(list(Id.keys()))), state="readonly") 
idlist.place(relx=0.1, rely=0.15, anchor="c", relwidth=0.2, relheight=0.07)
ttk.Button(text='New', command=New).place(relx=0.25, rely=0.15, anchor="c", relwidth=0.1, relheight=0.07)


ttk.Button(text='Set', command=Set).place(relx=0.56, rely=0.15, anchor="c", relwidth=0.1, relheight=0.07)
ttk.Button(text='Clear', command=Clear).place(relx=0.25, rely=0.45, anchor="c", relwidth=0.1, relheight=0.07)
ttk.Button(text='Print', command=pr).place(relx=0.35, rely=0.45, anchor="c", relwidth=0.1, relheight=0.07)
ttk.Button(text='Update', command=Update).place(relx=0.45, rely=0.45, anchor="c", relwidth=0.1, relheight=0.07)


list_Set.place(relx=0.4, rely=0.15, anchor="c", relwidth=0.2, relheight=0.07)
list_Set_1.place(relx=0.4, rely=0.23, anchor="c", relwidth=0.2, relheight=0.07)
tk.mainloop()
