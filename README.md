# python automatic download exe packaging + automaticly adding python to application Version 1.3 -> Youtube .ver

# Only for Windows users ↓

Youtube python version uses yt_dlp module requires ffmpeg

# ⓒ 2024. Diddmstjr Inc. All rights reserved.

# Example exe file

    https://eunseok07yang.store/Windows_youtube.exe

This packaging is for Python Developer want to convert, reveal to ordinary people.
Not lot people having python interpreter in their computer, while downloading exe file python interpreter will download automatically.
This automatic program will make packaging easly such as Visual studio C++ 2020 ~~~.

# Git Clone

    git clone https://github.com/diddmstjr07/python_interpreter_auto+kernal_youtube.git

# Setting

Converting Python file (.py) to exe file

1. Loacte your python file in ./python_file
2. Convert file (process_interpreter.bat) extension name .txt
3. Please change `"..\python_file\main.py"` main.py to your python file name

# python file set

    @echo off
    start "" "C:\Program Files\Python310\python.exe" "..\python_file\main.py"
    exit

4. Convert again (process_interpreter.txt) extension name .bat
5. Double click file .bat file is work .py file correctly
6. Double click ./bat to exe/Bat_To_Exe_Converter_x64.exe
7. Click Open, select process_interpreter.bat file, Click Covert
8. Set file name select process_interpreter and click store (!Store in same directory as select process_interpreter.bat!) -> process_interpreter.exe

Download inno Setup Compiler(Automatic python download + set your .py as application)

1. Download inno Setup Compiler -> https://jrsoftware.org/download.php/is.exe
2. Click File > New
3. Set personally, Application Files > Application main excutable file as ./process/process_interpreter.exe
4. Select Other application file as Python_Kernal_download.exe, ffmpeg_auto.exe
5. Application file associate > Application file type extension > .myp -> .exe
6. Compiler Setting > Compiler outer base file name > "Write your personal file name you want"
7. Compiler Setting > Custom Setup icon file > Select ./icon/python.ico or download .ico(only) you want
8. Finish process
9. Change [Run] bottom part to below one

# RUN

    [Run]
    Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
    Filename: "{app}\Python_Kernal_download.exe";
    Filename: "{app}\ffmpeg_auto.exe";

10. Click Build > Convert set file name "setting" and click store wait until process finishes
    You should set directory as python_interpreter_auto+kernal else, you will get error in result .exe file

11. Directory ./Output/("Number 5" file name you set)

# This Program is not allowed as using by bussiness ONLY FOR PERSONAL

DIRECTORY

    .
    ├── bat to exe
    │   └── Bat_To_Exe_Converter_x64.exe
    ├── icon
    │   └── python.ico
    ├── origin
    │   └── Python_Kernal_download.ps1
    ├── process
    │   ├── Python_Kernal_download.exe
    │   ├── process_interpreter.bat
    │   └── main.py
    ├── README.md
    └── .gitignore
