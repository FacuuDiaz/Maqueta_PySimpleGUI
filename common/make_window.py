import PySimpleGUI as sg

def create_window(name:str,layout:list[list],actions:any,windows_conf:list[any]) -> None:
    """
    funcion create_windows

    Def:
        Crea una ventana generica con los atributos enviados, y asimismo genera un loop que 
        permite la persistencia de la ventana, tomando como por default el EXIT de la ventana

    Args: 
        - name (str): Nombre de la ventana a renderizar
        - layout(list): Contenido de la ventana a renderizar
        - actions(function): Funcion que contiene la logistica de la Ventana a renderizar
        - windows_conf (dict): Lista de parametros para la configuración de la ventana a renderizar 
    """
    window = sg.Window(name,layout=layout,**windows_conf)
    while True:
        event,values = window.Read()
        match event:
            case None | "EXIT" :
                print('entro al match')
                break
        actions(event,values)
    
