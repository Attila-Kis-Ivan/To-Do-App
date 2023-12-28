import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.Input(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-D0 App", layout=[[[label], [input_box, add_button]]])
window.read()
window.close()