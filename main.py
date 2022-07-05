import PySimpleGUI as sg
import pages.page_main as page_main
import pages.page_about as page_about

window_main, window_about = page_main.create_window(sg), None

while True:
     window, event, values = sg.read_all_windows()

     if event in [sg.WIN_CLOSED, 'Sair']:
          window.close()
          break
     
     if event == '-ABOUT-':
          if window_about: window_about.hide()
          window_about = page_about.create_window(sg)
     
