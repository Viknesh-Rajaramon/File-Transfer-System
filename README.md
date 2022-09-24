# File Transfer System

An attempt to develop a simple file transfer system that can transfer files between two systems using the IP addresses provided they are connected through the same network. Socket programming in python is used for development.

This repository contains:

1. Python code for [GUI](GUI.py)
2. Python code for [sender](sender.py)
3. Python code for [receiver](receiver.py)
4. [ReadMe file](README.md) itself


## To Run

Make sure you have the following libraries installed before running the code.
```
pyqt5
socket
tqdm
threading
```

Download the following files in the same directory.
```
GUI.py
sender.py
receiver.py
```

Run GUI.py
```
cd directory-where-the-files-are-saved
python3 GUI.py
```