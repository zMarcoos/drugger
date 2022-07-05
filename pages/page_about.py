import PySimpleGUI as sg

def create_window(sg: sg):
  layout = [
    sg.Text('Sobre')
  ]

  window = sg.Window(title='Drugger', layout=layout, margins=(200, 100), resizable=False, background_color='#5A7E8C')

  return window