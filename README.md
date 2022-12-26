# File Transfer System

A simple file transfer system that can transfer files between two systems using the IP addresses provided they are connected through the same network. Socket programming in python is used for development. Threading is added to allow the sender to send the same file to atmost 4 receivers simultaneously.

This repository contains:

1. Python code for [GUI](GUI.py)
2. Python code for [Sender](Sender.py)
3. Python code for [Receiver](Receiver.py)
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
Sender.py
Receiver.py
```

Run GUI.py
```
cd directory-where-the-files-are-saved
python3 GUI.py
```
