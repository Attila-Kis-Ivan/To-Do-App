import functions
import PySimpleGUI as sg
import time

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label], 
          [input_box, add_button], 
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window("My To-Do App", 
                   layout=layout, 
                   font=('Montserrat ', 20))
# this loop prevent the app to close if we click on the add button
while True:
    event, values = window.read(timeout=300)
    window["clock"].update(value=time.strftime("%d %b, %Y %H:%M:%S"))
    # print(1,event)
    # print(2,values)
    # print(3,values["todos"])
    
    # adding todo to the list
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]    
                new_todo = values["todo"] + "\n"
                
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please, select an item first", font=("Montserrat", 20))    
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please, select an item first", font=("Montserrat", 20))
        case "Exit":
            break    
                
        #Update and place the current selection in the textbox
        case "todos":
            window["todo"].update(value=values["todos"][0])    
        # this prevent to break the app if we click on the red x to close. Only the looop stopped
        case sg.WIN_CLOSED:
            break 
            
            
            
            
window.close()