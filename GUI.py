from tkinter import IntVar
import customtkinter
from main import MorseCode, HexCode, CaesarCode
from tkinter.messagebox import showerror, showwarning, showinfo

def start_code_morse():
    message = Text_1.get('1.0', 'end')
    text_morse = MorseCode.code_morse(message)
    Text_2.insert('end', text_morse)


def start_encode_morse():
    message = Text_1.get('1.0', 'end')
    morse_text = MorseCode.encode_morse(message)
    Text_2.insert('end', morse_text)


def start_code_hex():
    message = Text_1.get('1.0', 'end')
    text_hex = HexCode.code_hex(message)
    Text_2.insert('end', text_hex)


def start_encode_hex():
    message = Text_1.get('1.0', 'end')
    hex_text = HexCode.encode_hex(message)
    Text_2.insert('end', hex_text)


def start_code_caesar():
    message = Text_1.get('1.0', 'end')
    shift = int(rar.get())
    text_caesar = CaesarCode.code_caesar(message, shift)
    Text_2.insert('end', text_caesar)

def start_encode_caesar():
    message = Text_1.get('1.0', 'end')
    shift = int(rar.get())
    caesar_text = CaesarCode.encode_caesar(message, shift)
    Text_2.insert('end', caesar_text)

def check():
    if (step.get() == 1) and (code.get() == 1):
        start_code_morse()
    elif (step.get() == 2) and (code.get() == 1):
        start_encode_morse()
    elif (step.get() == 1) and (code.get() == 2):
        start_code_hex()
    elif (step.get() == 2) and (code.get() == 2):
        start_encode_hex()
    elif (step.get() == 1) and (code.get() == 3):
        start_code_caesar()
    elif (step.get() == 2) and (code.get() == 3):
        start_encode_caesar()
    else:
        showerror(title="Ошибка", message="Ошибка выбора шифра или действия!")

def check_sec():
    if (code.get() == 1):
        finish_sec()
    elif (code.get() == 2):
        finish_sec()
    elif (code.get() == 3):
        start_sec()

def start_sec():
    global rar
    global lab_sec
    rar = customtkinter.CTkEntry(root,justify='center',width=40,height=30)
    lab_sec = customtkinter.CTkLabel(root,text='Ключ')
    lab_sec.place(x=458,y=292)
    rar.place(x=455, y=320)

def finish_sec():
    rar.destroy()
    lab_sec.destroy()

def quit():
    root.quit()

def copy_text():
    copied_text = Text_2.get('1.0', 'end')
    root.clipboard_clear()
    root.clipboard_append(copied_text)

def paste_text():
    pasted_text = root.clipboard_get()
    Text_1.insert('end', pasted_text)


def clear_text():
    Text_1.delete('1.0', 'end')
    Text_2.delete('1.0', 'end')


def info():
    app = customtkinter.CTk()
    app.title("Информация")
    app.geometry("550x380")
    font_2 = customtkinter.CTkFont(family= "Arial", size=14, weight="normal", slant="roman")
    lab_info1 = customtkinter.CTkLabel(
        app,
        padx=18,
        pady=15,
        font=font_2,
        text='Программа "Шифратор/Дешифратор" представляет собой инструмент, \nкоторый позволяет безопасно и легко шифровать и дешифровать\n текстовые сообщения с использованием трех\n различных методов шифрования.\n')

    lab_info2 = customtkinter.CTkLabel(
        app,
        text='1)Шифровщик Цезаря позволяет создавать шифрованные сообщения\n с использованием простого алгоритма сдвига каждой буквы\n на определенное количество позиций в алфавите.\n',
        padx=18,
        pady=3,
        font=font_2)
    lab_info3 = customtkinter.CTkLabel(
        app,
        text='2)Азбука Морзе - это система шифрования, использующая комбинации\n длинных и коротких сигналов, называемых точками и тире,\nдля представления каждой буквы и числа.\n',
        padx=18,
        pady=3,
        font=font_2)
    lab_info4 = customtkinter.CTkLabel(
        app,
        text='3)Шифр HEX-кода позволяет преобразовывать каждый символ\n текста в шестнадцатеричное представление.\n',
        padx=18,
        pady=3,
        font=font_2)
    lab_info5 = customtkinter.CTkLabel(
        app,
        text='© Дмитрий Самылов, ИСП-321п',
        padx=18,
        pady=15)

    lab_info1.pack()
    lab_info2.pack()
    lab_info3.pack()
    lab_info4.pack()
    lab_info5.pack()
    app.mainloop()


customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.title("Шифратор/Дешифратор")
root.geometry("950x650")
root.resizable(width=False, height=False)


step = IntVar(value=0)
code = IntVar(value=0)

font = customtkinter.CTkFont(family= "Arial", size=24, weight="normal", slant="italic")
frame = customtkinter.CTkFrame(
    root,
    width=800,
    height=160)

Text_1 = customtkinter.CTkTextbox(
    root,
    width=370,
    height=230,
    font=('CTkTextFont', 16))
Text_2 = customtkinter.CTkTextbox(
    root,
    width=370,
    height=230,
    font=('CTkTextFont', 16))
Label_1 = customtkinter.CTkLabel(
    root,
    text='Введите текст: ',
    font=('CTkTextFont', 15))
Label_2 = customtkinter.CTkLabel(
    root,
    text='Результат конвертирования: ',
    font=('CTkTextFont', 15))
Label_3 = customtkinter.CTkLabel(
    frame,
    text='Выберите шифр:',
    font=('CTkTextFont', 19))
Label_4 = customtkinter.CTkLabel(
    frame,
    text='Выберите действие:',
    font=('CTkTextFont', 19))
Check_1 = customtkinter.CTkRadioButton(
    frame,
    value=1,
    variable=step,
    text='Шифровать',
    font=('CTkTextFont', 15),
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
Check_2 = customtkinter.CTkRadioButton(
    frame,
    value=2,
    variable=step,
    text='Дешифровать',
    font=('CTkTextFont', 15),
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
S_Check_1 = customtkinter.CTkRadioButton(
    frame,
    value=1,
    variable=code,
    text='Азбука Морзе',
    font=('CTkTextFont', 15),
    command=check_sec,
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
S_Check_2 = customtkinter.CTkRadioButton(
    frame,
    value=2,
    variable=code,
    text='HEX-шифр',
    font=('CTkTextFont', 15),
    command=check_sec,
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
S_Check_3 = customtkinter.CTkRadioButton(
    frame,
    value=3,
    variable=code,
    text='Шифр Цезаря',
    command=check_sec,
    font=('CTkTextFont', 15),
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
Btn_1 = customtkinter.CTkButton(
    root,
    command=check,
    height=40,
    width=120,
    text='Результат')
lab_sh = customtkinter.CTkLabel(
    frame,
    width=70,
    height=40,
    anchor='se',
    text='Шифратор',
    font=font,
    text_color='#007dd1'
)
lab_sr = customtkinter.CTkLabel(
    frame,
    text='Дешифратор',
    width=70,
    height=40,
    font=font,
    pady=3,
    padx=3,
    text_color='#007dd1'

)
Btn_quit = customtkinter.CTkButton(
    root,
    text='Выход',
    command=quit,
    height=35,
    width=100
)
Btn_copy = customtkinter.CTkButton(
    root,
    text='Копировать',
    command=copy_text,
    height=40,
    width=120
)
Btn_paste = customtkinter.CTkButton(
    root,
    text='Вставить',
    command=paste_text,
    height=40,
    width=120
)
Btn_delete = customtkinter.CTkButton(
    root,
    text='Очистить',
    command=clear_text,
    height=40,
    width=120
)
Btn_info = customtkinter.CTkButton(
    root,
    text='Информация',
    command=info,
    height=35,
    width=100
)

frame.place(x=75, y=20)

Label_3.place(x=15, y=5)
S_Check_1.place(x=15, y=50)
S_Check_2.place(x=15, y=75)
S_Check_3.place(x=15, y=100)
lab_sh.place(x=270,y=23)
lab_sr.place(x=350,y=67)


Label_4.place(x=600, y=5)
Check_1.place(x=635, y=60)
Check_2.place(x=635, y=85)
Label_1.place(x=85, y=200)
Text_1.place(x=75, y=230)
Label_2.place(x=523, y=200)
Text_2.place(x=505, y=230)

Btn_1.place(x=416, y=500)
Btn_quit.place(x=840, y=610)
Btn_copy.place(x=246,y=530)
Btn_paste.place(x=584,y=530)
Btn_delete.place(x=416,y=570)
Btn_info.place(x=10,y=610)

root.mainloop()


