![alt text][header]

# Adobe Discord Rich Presence

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/719bbef946084e78b20a1c7c63420e86)](https://www.codacy.com/app/imsmokie/adobe-rpc?utm_source=github.com&utm_medium=referral&utm_content=smokes/adobe-rpc&utm_campaign=Badge_Grade)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?logo=python)](https://www.python.org/)
<a href="https://www.autohotkey.com">
  <img src="https://img.shields.io/badge/Made%20With-AutoHotKey-006fff?logo=data:image/png;base64,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"/>
</a>
[![GitHub issues](https://img.shields.io/github/issues/smokes/adobe-rpc.svg)](https://GitHub.com/smokes/adobe-rpc/issues/)
[![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=smokes.adobe-rpc&color=C3447A&logo=GitHub&logoColor=FFFFFF&label=Visits)](https://github.com/bBSempai/adobe-rpc/)

Rich Presence for Discord to display what you're currently doing in most of adobe's applications

**UPDATE:** The script is now AUTOMATED! (Automation provided by [bBSempai](https://github.com/bBSempai))

## Requirements

- Python 3.4+ with Pip
- If you're running a 64bit version of python, download the pywin32 binaries from [here!](https://github.com/mhammond/pywin32/releases)
- Adobe apps (obviously)
- [AutoHotKey (AHK)](https://www.autohotkey.com) **For AUTOMATION of your RPC**

## How to use

- Clone the repo `$ git clone https://github.com/smokes/adobe-rpc.git`
- Make sure you're running an Adobe application.
- Install the required packages `$ pip install -r requirements.txt`
- Run the script `$ python rpc.py`
- Enjoy!

OR just download the **.exe** from the [releases!](https://github.com/smokes/adobe-rpc/releases) page and run it!

## For Automation of the RPC

- Upon running an AHK script you can automate your tasks. Here we have two scripts:<br>**1)**[**RPC.ahk**](https://github.com/smokes/adobe-rpc/blob/master/RPC.ahk) which would ensure running of the [**RPC.exe**](https://github.com/smokes/adobe-rpc/releases) in the background upon startup and also "re-run" it as soon as it gets terminated due to closing of any Adobe app or Discord.<br>**2)**[**Failsafe.ahk**](https://github.com/smokes/adobe-rpc/blob/master/failsafe.ahk) which would be helpful if any inconvenience occurs such as if Discord stops displaying your RP even though the **.exe** file is running along with your Adobe application and Discord (Trust me, it happens and I don't know why or what bug causes it. Subject to improvement). The script would, upon certain specific keypress(CTRL+ALT+SHIFT+\` by default; can be edited), kill the **.exe** file which is already running and re-run it.<br>Look at the script codes yourselves to understand properly if you want.
- Now in order to automate your RPC all you have to do is keep these scripts running in background. Don't worry, they will literally consume almost negligible memory leaving no trace in your taskbar and tray. If needed, you can manually control them from the Task Manager window. All you gotta do to make them autorun is follow the steps below:
- Install [AHK](https://www.autohotkey.com) (Takes up <15 Mb worth of space)
- Set your AHK file to run automatically on startup everytime you boot. If you already don't know how to then just follow these instructions:
  - RUN shell:startup<br><br>
  <img src = "https://i.imgur.com/Umr4unL.jpeg" /><br><br>
  - It will open this directory -> (C:\Users\<NAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup)<br><br>
  <img src = "https://i.imgur.com/J1FjIFH.png"/><br><br>
  - If the directory (Startup Folder) doesn't already exist...THEN MAKE ONE 🙂
  - Place your .AHK file **shortcuts** in this directory. Now your AHK files will run on startup every time you boot up your PC. **Meaning** the RPC.exe will run automatically now upon startup in hidden mode and would also not stop running even if you close your Adobe app or Discord. For further knowledge of the scripts' working you can check out the instructional comments provided in the scripts themselves. Restart your setup and Voila! It should be working perfectly!
  
**Note: You can always manually control the rpc.exe and the .ahk files from the Task Manager window if any issues occur.**

## Binaries

The easiest way to use **adobe-rpc** is to download the **.exe** and **.ahk** files from the [releases!](https://github.com/smokes/adobe-rpc/releases) page.

## Preview

<div align="center">
   <img src="https://i.imgur.com/h1ipmi8.png" width="30%" />
   <img src="https://i.imgur.com/Zf6drg7.png" width="30%" />
   <img src="https://i.imgur.com/CIneIrh.png" width="30%" />
</div>

## TODOs

- Macos support
- Better error handling

## Contributing

**adobe-rpc** currently doesn't support: Media Encoder, Xd and Audition. Please submit a PR where you add an app that we haven't included yet to the file **meta.json**, where you specify the app's process name.

<p align="center">Feel free to contact us regarding anything you need help with!</p>

<p align="center">
  <a href="https://GitHub.com/smokes/adobe-rpc/issues/new"><b><i>Feel free to open an issue and communicate!</i></b><br></a>
</p>

[header]: https://i.imgur.com/zGFYunZ.png "Repo header"
