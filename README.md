![alt text][header]

# Adobe Discord Rich Presence

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/719bbef946084e78b20a1c7c63420e86)](https://www.codacy.com/app/imsmokie/adobe-rpc?utm_source=github.com&utm_medium=referral&utm_content=smokes/adobe-rpc&utm_campaign=Badge_Grade)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues/smokes/adobe-rpc.svg)](https://GitHub.com/smokes/adobe-rpc/issues/)

Rich Presence for Discord to display what you're currently doing in most of adobe's applications

## Requirements

- Python 3.4+ with Pip
- If you're running a 64bit version of python, download the pywin32 binaries from [here!](https://github.com/mhammond/pywin32/releases)
- Adobe apps (obviously)
- [AutoHotKey (AHK) **For AUTOMATION of your RPC** ](https://www.autohotkey.com)

## How to use

- Clone the repo `$ git clone https://github.com/smokes/adobe-rpc.git`
- Make sure you're running an Adobe application.
- Install the required packages `$ pip install -r requirements.txt`
- Run the script `$ python rpc.py`
- Enjoy!

## For Automation of the RPC

- Upon running an AHK script you can automate your tasks. Here we have two scripts:<br>**1)**[**RPC.ahk**](https://github.com/smokes/adobe-rpc/blob/master/RPC.ahk) which would ensure running of the [**RPC.exe**](https://github.com/smokes/adobe-rpc/releases) in the background upon startup and also "re-run" it as soon as it gets terminated due to closing of any Adobe app or Discord.<br>**2)**[**Failsafe.ahk**](https://github.com/smokes/adobe-rpc/blob/master/failsafe.ahk) which would be helpful if any inconvenience occurs such as if Discord stop displaying your RP even though the **.exe** file is running along with your Adobe application and Discord (Trust me, it happens and I don't know why or what bug causes it. Subject to improvement). The script would, upon certain specific keypress, kill the **.exe** file which is already running and re-run it.<br>
- 
- Install [AHK](https://www.autohotkey.com) (Takes up <15 Mb worth of space)
- Set your AHK file to run automatically on startup everytime you boot. If you already don't know how then just follow these instructions:
  - RUN shell:startup<br><br>
  <img src = "https://i.imgur.com/Umr4unL.jpeg" /><br><br>
  - It will open this directory -> (C:\Users\<NAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup)<br><br>
  <img src = "https://i.imgur.com/EY22e9A.png"/><br><br>
  - If the directory (Startup Folder) doesn't already exist...THEN MAKE ONE 🙂
  - Place your .AHK file **shortcut** in this directory. Now your AHK file will run on startup every time you boot up your PC.

## Binaries

The easiest way to use **adobe-rpc** is to download the **.exe** from the [releases!](https://github.com/smokes/adobe-rpc/releases) page.

## Preview

<div align="center">
   <img src="https://i.imgur.com/h1ipmi8.png" width="30%" />
   <img src="https://i.imgur.com/Zf6drg7.png" width="30%" />
   <img src="https://i.imgur.com/CIneIrh.png" width="30%" />
</div>

## TODOs

- Macos support
- Better error handling
- Prevent app from exiting when Discord or any app isn't running.

## Contributing

**adobe-rpc** currently doesn't support: Media Encoder, Xd and Audition. Please submit a PR where you add an app that we haven't included yet to the file **meta.json**, where you specify the app's process name.

[header]: https://i.imgur.com/zGFYunZ.png "Repo header"
