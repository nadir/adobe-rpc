# Adobe Discord Rich Presence

![alt text][header]

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/719bbef946084e78b20a1c7c63420e86)](https://www.codacy.com/app/imsmokie/adobe-rpc?utm_source=github.com&utm_medium=referral&utm_content=smokes/adobe-rpc&utm_campaign=Badge_Grade)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues/smokes/adobe-rpc.svg)](https://GitHub.com/smokes/adobe-rpc/issues/)

Rich Presence for Discord to display what you're currently doing in most of adobe's applications

## Requirements

- Python 3.4+ with Pip
- If you're running a 64bit version of python, download the `pywin32` binaries from [here!](https://github.com/mhammond/pywin32/releases)
- Adobe apps (obviously)

## How to use

- Clone the repo `$ git clone https://github.com/smokes/adobe-rpc.git`
- Make sure you're running an Adobe application.
- Install the required packages `$ pip install -r -u requirements.txt`
- Run the script `$ python rpc.py`
- Enjoy!

### Building binaries

Building the binaries from source requires `pyinstaller`

- Install `$ pip install -u pyinstaller`
- If you are building on Python 3.8+, run `$ pip install -u https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz`
- Build `$ pyinstaller --onefile .\rpc.py`

## Binaries

The easiest way to use **adobe-rpc** is to download the **.exe** from the [releases!](https://github.com/smokes/adobe-rpc/releases) page.

## Preview

<div align="center">
   <img src="https://i.imgur.com/h1ipmi8.png" width="30%" />
   <img src="https://i.imgur.com/Zf6drg7.png" width="30%" />
   <img src="https://i.imgur.com/CIneIrh.png" width="30%" />
</div>

## TODOs

- Mac OS support
- Better error handling
- Prevent app from exiting when Discord or any app isn't running.

## Contributing

**adobe-rpc** currently doesn't support: Media Encoder, Xd and Audition. Please submit a PR where you add an app that we haven't included yet to the file **meta.json**, where you specify the app's process name.

[header]: https://i.imgur.com/zGFYunZ.png "Repo header"
