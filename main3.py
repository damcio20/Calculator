import tkinter
import customtkinter
import random

question = {
    'qustion' : ['Jaka jest stolicja Francji', 'Jaka jest stolica Polski']
}

answer = {
    'answer' : ['Paryż', 'Polska']
}

var = 0
point = 0
def check():
    global var, point
    check_result = entry_label_var.get()
    try:
        if check_result == answer['answer'][var]:
            var = var + 1
            point = point + 1
            question_label.configure(text = f'{question["qustion"][var]}' )
            point_label.configure(text = f'Liczba punktów: {point}' )
        else:
            var = var + 1
            question_label.configure(text = f'{question["qustion"][var]}' )
    except IndexError:
        alert_label.configure(text = 'End of the list of question')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.title('Quiz App')
app.geometry('300x300')
app.resizable(False,False)

question_label = customtkinter.CTkLabel(app, text = f'{question["qustion"][var]}')
question_label.grid(column = 5, row = 0)

entry_label_var = tkinter.StringVar()
entry_label = customtkinter.CTkEntry(app,textvariable= entry_label_var)
entry_label.grid(column = 5, row = 1)

button_check = customtkinter.CTkButton(app, text = "Check", command = check)
button_check.grid(column = 5, row = 2)

point_label = customtkinter.CTkLabel(app, text = f'Liczba punktów: {point}')
point_label.grid(column = 5, row = 3)

alert_label = customtkinter.CTkLabel(app, text='', fg_color='transparent')
alert_label.grid(column = 5, row = 4)
app.mainloop()