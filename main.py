# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json


# ---------------------------- SAVE PASSWORD ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list_test = [random.choice(letters) for number in range(random.randint(8, 10))]
    password_list_test.extend([random.choice(numbers) for number in range(random.randint(2, 4))])
    password_list_test.extend([random.choice(symbols) for number in range(random.randint(2, 4))])
    random.shuffle(password_list_test)

    password = ''.join(password_list_test)

    print(password_list_test)
    print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def password_adder():
    web_name = website_entry.get()
    user_name = email_user_entry.get()
    pass_name = password_entry.get()
    new_data = {
        web_name: {
            'email': user_name,
            'password': pass_name,
        }}
    if len(pass_name) == 0 or len(web_name) == 0 or len(user_name) == 0:
        messagebox.showerror(title='Error, no entries',
                             message='one of more fields does not meet the minimum character length')
    else:
        is_ok = messagebox.askokcancel(title=web_name, message=f'These are the details entered \nEmail: {user_name}'
                                                               f'\nPassword: {pass_name}\nIs it ok to save? ')
        if is_ok:
            try:
                with open('password_test_file.json', 'r') as test_file:
                    # json.dump(new_data, test_file,indent= 4)
                    # reading the old data
                    data = json.load(test_file)
                    # print(data)
                    # updating the old data with the new data
                    data.update(new_data)
            except FileNotFoundError:
                with open('password_test_file.json','w') as test_file:
                    json.dump(new_data, test_file, indent=4)
            else:
                with open('password_test_file.json', 'w') as test_file:
                    # saving the updated data

                    json.dump(data, test_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)

###labels ###
website_label = Label(text='Website:', font=('Arial', 12, 'bold'))
website_label.grid(row=1, column=0)

email_user_label = Label(text='Email/Username:', font=('Arial', 12, 'bold'))
email_user_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=('Arial', 12, 'bold'))
password_label.grid(row=3, column=0)

####entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='ew')
website_entry.focus()
email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2, sticky='ew')
email_user_entry.insert(0, 'frazer_h@live.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='ew')

### buttons

generate_pass_button = Button(text='Generate Password', command=password_generator)
generate_pass_button.grid(row=3, column=2, sticky='ew')

add_button = Button(text='Add', width=36, command=password_adder)
add_button.grid(row=4, column=1, columnspan=2, sticky='ew')

window.mainloop()
