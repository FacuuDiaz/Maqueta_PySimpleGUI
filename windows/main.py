import PySimpleGUI as sg
from common.make_window import create_window
from config.config import configuration
layout = [[sg.T("Creando un texto")],
[sg.B("PLAY",key="-PLAY-")],
[sg.B("CONFIGURATION",key="-CONFIGURATION-")],
[sg.B("PROFILE",key="-PROFILE-")],
[sg.B("HOW TO PLAY",key="-HOWTOPLAY-")],
]

print(configuration)

def windows_logic(event,values):
    match event:
        case "-PLAY-":
            print("-PLAY-")
        case "-CONFIGURATION-":
            print("-CONFIGURATION-")
        case "-PROFILE-":
            print("-PROFILE-")
        case "-HOWTOPLAY-":
            print("-HOWTOPLAY-")

def run():
    create_window("Main",layout=layout,actions=windows_logic)
