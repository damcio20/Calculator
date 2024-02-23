import tkinter 
import customtkinter

def update(btn):
    
    current_value = label_var.get()
    label_var.set(current_value + btn)

def back():
    current_value = label_var.get()
    label_var.set(current_value[:-1])

def clear():
    label_var.set('')
    labe2_var.set('')

def result():
    current_value = label_var.get()
    try:
        result2 = eval(current_value)
        labe2_var.set(result2)
    except Exception as e:
        labe2_var.set("Error")

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.title('Culculator')
app.geometry('600x400')
app.resizable(False,False)

label_var = tkinter.StringVar()
label = customtkinter.CTkLabel(app, textvariable = label_var)
label.grid(column = 0, row = 0, columnspan = 4)

labe2_var = tkinter.StringVar()
label2 = customtkinter.CTkLabel(app, textvariable = labe2_var)
label2.grid(column = 0, row = 1,columnspan =  4)

buttons = [
    '7','8','9','+',
    '4','5','6','-',
    '1','2','3','/',
    'C','0','UNDO','*',
    '='

]

column_nr = 0
row_nr = 2

for button in buttons:
    if button == '=':
        button = customtkinter.CTkButton(app, text = button, command = result)
        button.grid(column = column_nr , row = row_nr,pady = 5, padx = 5 , columnspan = 4)
    elif button == 'C':
        button = customtkinter.CTkButton(app, text = button, command = clear)
        button.grid(column = column_nr , row = row_nr,pady = 5, padx = 5 )
    elif button == 'UNDO':
        button = customtkinter.CTkButton(app, text = button, command= back)
        button.grid(column = column_nr , row = row_nr,pady = 5, padx = 5 )

    else:
        button = customtkinter.CTkButton(app, text = button, command =lambda btn=button: update(btn))
        button.grid(column = column_nr , row = row_nr,pady = 5, padx = 5)

    column_nr += 1 
    if column_nr > 3:
        column_nr = 0
        row_nr += 1

app.mainloop()