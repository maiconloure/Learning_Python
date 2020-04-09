import PySimpleGUI as sg

sg.theme('DarkBlue3')

layout = [ [sg.Text('USER REGISTRATION', font='Courier 12', text_color='blue')],
           [sg.Text('User'), sg.InputText()],
           [sg.Text('Password'), sg.InputText()],
           [sg.Button('OK'), sg.Button('Cancel')]]

window = sg.Window('CONTROL', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    print('Login', values[0])
    print('Password: ', values[1])