import time
import pygame
import customtkinter
from tkinter import *


# 6 написание методов


# 6.3 создать метода stop
def stop():
    btn_start.pack()  # вывод кнопки start
    btn_stop.pack_forget()  # прячем кнопку stop
    pygame.mixer.music.pause()  # выключение мелодии


# 6.2 создание метода sound
def sound():
    btn_start.pack_forget()  # метод для скрытия кнопки
    btn_stop.pack()  # вывод кнопки stop
    pygame.mixer.music.play()  # запуск аудио файла


# 6.1 создание метода start
def start():
    duration = int(seconds.get())  # duration - продолжительномть
    while duration:
        m, s = divmod(int(duration), 60)  # divmod(a, b) == (b//a, b)
        min_sec_format = f'{m:02}:{s:02}'
        count_digit['text'] = min_sec_format
        count_digit.update()  # обновляем текст
        time.sleep(1 - time.time() % 1)
        duration -= 1
    sound()

# 1 загрузка мелодии в pygame
file = 'one_pice.mp3'
pygame.init()  # инитиализация pygqme
pygame.mixer.init()  # инитиализация pygame.mixer
pygame.mixer.music.load(file)  # 3 загружаем файл с аудио в pygame.mixer

# 4 создание графического интерфейса
app = customtkinter.CTk()
# customtkinter.set_appearance_mode("dark")
app.title('Таймер')
app.geometry('150x150')
app.grid_columnconfigure(0, weight=1)
app.resizable(0, 0)

# 5 создание виджетов
count_digit = customtkinter.CTkLabel(app, text='0', font=('Caveat', 20))  # поле отображения текста
count_digit.pack(pady=5)

seconds = customtkinter.CTkEntry(app, font=('Caveat', 15))  # поле для ввода
seconds.pack(pady=10)

btn_start = customtkinter.CTkButton(app, text='Старт', font=('Caveat', 15), command=start)  # кнопка для старта
btn_start.pack()

btn_stop = customtkinter.CTkButton(app, text='Стоп', font=('Caveat', 15), command=stop)  # кнопка для финиша


app.mainloop()  # запуск приложения
