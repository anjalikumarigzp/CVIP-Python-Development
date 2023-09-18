from tkinter import *
from tkinter import messagebox
import random

timeleft = 60
def timer():
    global timeleft, i
    if timeleft > 0:
        timeleft -= 1
        time_countLabel.config(text=timeleft)
        time_countLabel.after(1000, timer)
    else:
        wordEntry.config(state=DISABLED)
        result = correct_word - worng_word
        instructionLabel.config(text=f'Correct_words {correct_word}\n Worng Words {worng_word}\n Final Score {result}')
        if result < 10 :
            appreciationLabel.config(text='Try Next')
        if 20 > result > 10:
            appreciationLabel.config(text='Well Tried')
        if result > 20:
            appreciationLabel.config(text='Fabulous')
        res = messagebox.askyesno('Confirm', 'Do you want to play again?')
        if res:
            i = 0
            timeleft = 60
            countLabel.config(text='0')
            time_countLabel.config(text='60')
            wordEntry.config(state=NORMAL)
            instructionLabel.config(text='Type Word And Hit Enter')
            appreciationLabel.config(text='')


correct_word = 0
worng_word = 0
i = 0
def play_game(event):
    if wordEntry.get() != '':
        global i, correct_word, worng_word
        i += 1
        countLabel.config(text=i)


        instructionLabel.config(text='')
        if timeleft == 60:
            timer()

        if wordEntry.get() == word_list_Label['text']:
            correct_word += 1
        else:
            worng_word += 1

        random.shuffle(word_list)
        word_list_Label.config(text=word_list[0])
        wordEntry.delete(0, END)


word_list = ['Amplify', 'Pamper', 'Philosophy', 'Invest','Wait', 'Usage', 'Lovely', 'Average', 'Intelligence',
             'Creature', 'Deposit', 'Noise', 'Passion', 'Reveal', 'Wasting', 'Trees', 'Birds', 'Aesthetic']

# Function Part
sliderwords = ''
count=0
def slider():
    global sliderwords, count
    text='Test Your Typing Speed'
    if count>=len(text):
        count=0
        sliderwords=''
    sliderwords= sliderwords+text[count] # T
    movingLabel.config(text=sliderwords)
    count += 1
    movingLabel.after(200,slider)



root=Tk()
root.title('Typing speed')
root.iconbitmap('icon.ico')
# root.geometry('700×600+250+50')
root.config(bg='purple')
# root.resizable(0,0)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage, bg='purple')
logoLabel.place(x=220, y=60)

movingLabel = Label(root, text='Test Your Typing Speed', bg='purple', font=('arial', 25, 'bold italic')
                    , width=35, fg='white')
movingLabel.place(x=0, y=10)
slider()
random.shuffle(word_list)
word_list_Label=Label(root, text=word_list[0], font=('cooper black', 38,'italic bold'), bg='purple', fg='white')
word_list_Label.place(x=350, y=350, anchor=CENTER)

wordLabel = Label(root, text='Words', font=('Casteller', 28, 'bold'), bg='purple', fg='white')
wordLabel.place(x=30, y=150)

countLabel = Label(root, text='0', font=('Casteller', 28, 'bold'), bg='purple', fg='white')
countLabel.place(x=80, y=200)

timeLabel = Label(root, text='Timer', font=('Casteller', 28, 'bold'), bg='purple', fg='white')
timeLabel.place(x=530, y=150)

time_countLabel = Label(root, text='60', font=('Casteller', 28, 'bold'), bg='purple', fg='white')
time_countLabel.place(x=560, y=200)

wordEntry = Entry(root, font=('arial', 25,'bold'), bd=8, justify=CENTER)
wordEntry.place(x=160, y=390)
wordEntry.focus_set()

instructionLabel = Label(root, text='Type Word And Hit Enter', font=('chiller', 28,'bold'), bg='purple', fg='white')
instructionLabel.place(x=200, y=460)

good='Well Tried'
poor= 'Try Next'
pro= 'Well Done'
appreciationLabel = Label(root, font=('cooper black', 28, 'bold'), bg='purple', fg='white')
appreciationLabel.place(x=240, y=580)

root.bind('<Return>', play_game)

root.mainloop()


