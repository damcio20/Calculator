import tkinter
import customtkinter
import random

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
computer_score = 0
user_score = 0
def play(user_choice):
    computer_choice = random.choice(['paper','rock','scizor'])
    if user_choice == computer_choice:
        result = 'Draw :/'

    elif (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "rock" and computer_choice == "scizor") or \
         (user_choice == "scizor" and computer_choice == "paper"):
        result = 'You win :o'
        global user_score 
        user_score += 1
    else:
        result = 'You lose XD'
        global computer_score
        computer_score += 1
    score_label.configure(text = f'Score:\n Computer {computer_score} : {user_score} User')
    result_label.configure(text =f'Computer choose {computer_choice}\n {result}')
app = customtkinter.CTk()
app.title('Scizor Game')
app.geometry('300x400')
app.resizable(False,False)

choices = ['rock','paper','scizor']

row_nr = 1

for choice in choices:
    button = customtkinter.CTkButton(app,text = choice, command = lambda c = choice: play(c))
    button.grid(column =  1, row = row_nr,pady = 2,padx = 2)
    row_nr += 1

result_label = customtkinter.CTkLabel(app,text = '')
result_label.grid(column = 1,row = 5)

score_label = customtkinter.CTkLabel(app,text = '')
score_label.grid(column = 1, row = 6)

app.mainloop()
