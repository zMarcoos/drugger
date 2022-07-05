import PySimpleGUI as sg

def create_window(sg: sg):
  side_one = [
    [sg.Button('Agendar', size=(10, 1), button_color='#BFA36F')],
    [sg.Button('Alarmes', size=(10, 1), button_color='#BFA36F')],
    [sg.Button('Sobre', size=(10, 1), button_color='#BFA36F', enable_events=True, key='-ABOUT-')],
    [sg.Exit(button_text='Sair', size=(10, 1), button_color='#BFA36F')],
  ]

  side_two = [
      [sg.Frame('',layout=[[sg.Text('Drugger', font='Helvetica 15 bold', text_color='#FFFFFF', pad=(3,3), background_color='#9FB9BF')]],title_location='n', background_color='#9FB9BF')]
    ]

  layout = [
    [
      sg.Column(side_one),
      sg.VSeperator(),
      sg.Column(side_two, background_color='#9FB9BF'),
    ],
  ]

  window = sg.Window(title='Drugger', layout=layout, margins=(200, 100), resizable=False, background_color='#5A7E8C')

  return window