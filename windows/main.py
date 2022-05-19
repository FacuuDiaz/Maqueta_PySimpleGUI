import PySimpleGUI as sg
from common.make_window import create_window, render_window
from config.config import configuration as cfg
from windows import configuration 


"""-------------------------MAQUETADO------------------------------"""
def interface():
    layout = [[sg.T("Creando un texto")],
    [sg.B("PLAY",key="-PLAY-")],
    [sg.B("CONFIGURATION",key="-CONFIGURATION-")],
    [sg.B("PROFILE",key="-PROFILE-")],
    [sg.B("HOW TO PLAY",key="-HOWTOPLAY-")],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def windows_logic(event:dict,values:dict, window:sg.Window,) -> None:
    match event:
        case "-PLAY-":
            render_window(window,configuration)
            print("-PLAY-")
        case "-CONFIGURATION-":
            print("-CONFIGURATION-")
        case "-PROFILE-":
            print("-PROFILE-")
        case "-HOWTOPLAY-":
            print("-HOWTOPLAY-")
    return True
    
"""-------------------------EJECUCIÓN------------------------------"""
def run():
    layout=interface()
    create_window("Main",layout=layout,actions=windows_logic)
