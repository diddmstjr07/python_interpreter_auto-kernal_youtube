import subprocess
import platform
subprocess.run(['pip', 'install', 'tqdm', '-q'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
from tqdm import tqdm
from tkinter import simpledialog, Tk

store = []

root = Tk()
root.withdraw()
user_input = simpledialog.askstring(title="질문", prompt="영상을 저장할 경로를 입력하여 주십시오")
store.append(user_input)

platform_name = []
platform_name.append(platform.system())

if platform_name[0] == "Windows":
    command = "cls"
    subprocess.call(command, shell=True)
else:
    command = "clear"
    subprocess.call(command, shell=True)

def logo():
    print("\033[38;5;214m" + "\nYOUTUBE COMPILER CRAWLER Ver 1.6\n\nⓒ 2024. Diddmstjr Inc. All rights reserved.\n"+ "\033[0m")

def process_yn():
    while True:
        try:
            store = input("This Process is necessary for your PC enough RAM Space\nAre you sure you having enough RAM space more than 7GB? (y/n): ")
            if store == 'y':
                print("\033[1m\033[92m" + "\nProcessing start....\n" + "\033[0m")
                raise ZeroDivisionError()
            elif store == 'n':
                print('\n\nThanks for your downloading. See you next time 😃\nFor Contact, please left message to https://github.com/serpentinesr/meme-compiler\n')
                os._exit(0)
            elif store == 'clear':
                if platform_name[0] == "Windows":
                    command = "cls"
                    subprocess.call(command, shell=True)
                else:
                    command = "clear"
                    subprocess.call(command, shell=True)
            elif store == "exit()":
                sys.exit()
            elif store == "--help":
                print("\033[96m" + "clear: cleans terminal, exit(): exit process, y: start processing, n: cancel processing" + "\033[0m")
            else:
                raise ValueError()
        except ValueError:
            print("\033[31m" + "You select wrong Key. Please select the correct key (usage help: --help)" + "\033[0m")
        except ZeroDivisionError:
            break

def downloading_module_auto():
    packages = ['requests', 'beautifulsoup4', 'yt_dlp']

    for package in tqdm(packages, colour='#FFA500', desc="Downloading Modules", unit="package", ascii=True):
        subprocess.run(['pip', 'install', package, '-q'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def module_downloaded():
    while True:
        try:
            uid = input("Did you downloaded module by requirements.txt? (y/n): ")
            if uid == "y":
                raise ZeroDivisionError
            elif uid == "n":
                downloading_module_auto()
                raise AssertionError
            else:
                print("\033[31m" + "You wrote wrong word" + "\033[0m")
                raise NameError
        except NameError:
            pass
        except ZeroDivisionError:
            break
        except AssertionError:
            break
        except Exception as e:
            print(e)

logo()
process_yn()
module_downloaded()

import requests
from bs4 import BeautifulSoup
import re
import yt_dlp
import json
import subprocess
import sys
import os

search_array = []
locate = []
real_video = []
Data = []
Url = []
Title = []
Search_result = []

def reset():
    if platform_name[0] == "Windows":
        command = "cls"
        subprocess.call(command, shell=True)
    else:
        command = "clear"
    subprocess.call(command, shell=True)
    print("\033[38;5;214m" + "\nYOUTUBE COMPILER CRAWLER Ver 1.6\n\nⓒ 2024. Diddmstjr Inc. All rights reserved.\n"+ "\033[0m")
    print("This Process is necessary for your PC enough RAM Space")
    print("Are you sure you having enough RAM space more than 7GB? (y/n): y\n")
    print("\033[1m\033[92m" + "\nProcessing start....\n" + "\033[0m")
    print("Did you downloaded module by requirements.txt? (y/n): y")
    print(f"Please input you want to search: {Search_result}")
    print("\033[1m\033[92m" + "\n✅ Successfully Checked Direcotries ✅\n" + "\033[0m")

def delete_part_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        pass
    for filename in os.listdir(directory):
        if filename.endswith(".part"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
        else:
            pass

def directory_clear():
    try:
        os.remove(f"{store[0]}/content_result.json")
        os.remove(f"{store[0]}/content_result.txt")
    except:
        print("Directory reseting Error")

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def inputment(max):
    print("\033[1m\033[92m" + "\n✅ Successfully Checked Direcotries ✅\n" + "\033[0m")
    amount = input(f"Please write a number you want to choose (Maximum: {max}): ")
    return amount

def url_input():
    try:
        amount = input(f"Please write a number you want to Download: ")
        return Url[int(amount)]
    except:
        print("\033[1m\033[91m" + 'Prototype ERROR ------> Finishing' + "\033[0m")
        os._exit(0)

def downloadment():
    try:
        jso = Data[0]
        length = int(len(real_video))
        for item in range(length):
            ep = jso[real_video[item]]['videoRenderer']['inlinePlaybackEndpoint']
            if 'url' in ep['commandMetadata']['webCommandMetadata']:
                url = ep['commandMetadata']['webCommandMetadata']['url']
                if '/watch' in url:
                    link = f"https://youtube.com/{url[:-14]}"
                    Url.append(link)
    except:
        pass

def search():
    search = input("Please input you want to search: ")
    Search_result.append(search)
    result = search.split()
    try:
        if int(len(result)) > 1:
            re_URL = search.replace(' ', "+")
            URL = f"https://www.youtube.com/results?search_query={str(re_URL)}"
            request = requests.get(URL)
        else:
            URL = f"https://www.youtube.com/results?search_query={search}"
            request = requests.get(URL)
        
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')

            with open(f'{store[0]}/content_result.txt', 'w', encoding='utf-8') as f:
                f.write(str(soup))
            with open(f'{store[0]}/content_result.txt', 'r', encoding='utf-8') as f:
                txt = f.read()

            pattern = re.compile(r'"contents":\[') 
            matches = list(re.finditer(pattern, txt))
            loc = matches[1].start()
            locate.append(loc)
            pattern = re.compile(r'continuationItemRenderer')
            matches = list(re.finditer(pattern, txt))
            loc = matches[0].start()
            locate.append(loc)

            with open(f'{store[0]}/content_result.json', 'w') as r:
                jso = txt[int(locate[0]) + 11:int(locate[1]) - 65]
                obj = json.loads(jso)
                json_formatted_str = json.dumps(obj, indent=4)
                r.write(json_formatted_str)
                data = json.loads(json_formatted_str)
                Data.append(data)
                amount = len(data)
                for e in range(amount):
                    try: 
                        data[e]['videoRenderer']
                        real_video.append(e)
                        e += 1
                    except:
                        e += 1

    except Exception as e:
        print("\033[1m\033[31m" + "None searched elements. Please recheck your keyword" + "\033[0m")
        print(e)

def show_result():
    resultment = int(inputment(len(real_video)))
    print('')
    for videoRen in range(resultment):
        title = f"{Data[0][real_video[videoRen]]['videoRenderer']['title']['runs'][0]['text']}"
        Title.append(title)
        print("\033[1m\033[92m" + f"[{videoRen}]" + "\033[0m", title)
    print('')

def download_video(url, output_directory):
    def progress_hook(d):
        if d['status'] == 'downloading':
            downloaded_bytes = d.get('downloaded_bytes')
            total_bytes = d.get('total_bytes')
            if downloaded_bytes and total_bytes:
                progress = downloaded_bytes / total_bytes * 100
                pbar.update(progress - pbar.n)
        elif d['status'] == 'finished':
            pass

    ydl_opts = {
        'format': 'bestvideo[ext=mov]+bestaudio[ext=m4a]/best[ext=mov]/best',
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
        'quiet': True,
        'progress_hooks': [progress_hook]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        with tqdm(total=100, unit='%',colour='#FFA500', ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', ascii=True) as pbar:
            ydl.download([url])

class arrange:
    search()
    show_result()
    downloadment()
    delete_part_files(store[0])
    link_address = url_input()
    reset()
    download_video(link_address, store[0])
    directory_clear()
    print("\033[1m\033[92m" + "\n\n✅ Download Completed ✅\n" + "\033[0m")

if __name__ == "__main__":
    arrange