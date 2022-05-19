import PySimpleGUI as sg
from common.make_window import create_window


"""-------------------------MAQUETADO------------------------------"""
def interface():

    layout = [[sg.T("Configuración del Sistema", key="-TITLE-")],
              [sg.B("ATRAS",key="-ATRAS-")],
    ]

    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def windows_logic(event:dict,values:dict, window:sg.Window,) -> None:
    match event:
        case "-ATRAS-":
            return False
    return True
            

"""-------------------------EJECUCIÓN------------------------------"""
def run():
    layout = interface()
    create_window("CONFIGURACION",layout=layout,actions=windows_logic)
