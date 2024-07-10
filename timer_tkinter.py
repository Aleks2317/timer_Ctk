import time
import pygame
import customtkinter


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
    if seconds.get() != '' or minutes.get() != '' or hours.get() != '':
        duration = int(seconds.get()) if seconds.get() != '' else 0  # duration - продолжительномть
        duration += int(minutes.get()) * 60 if minutes.get() != '' else 0
        duration += int(hours.get()) * 60 * 60 if hours.get() != '' else 0

        while duration:
            m, s = divmod(int(duration), 60)
            h, m = divmod(m, 60)  # divmod(a, b) == (b//a, b)
            print(f'{h = }: {m = }: {s = }')
            min_sec_format = f'{h:02}:{m:02}:{s:02}'
            count_digit.configure(text=min_sec_format)
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
customtkinter.set_appearance_mode("dark")
app.title('Таймер')
app.geometry('200x300')
app.grid_columnconfigure(0, weight=1)
app.resizable(0, 0)

# 5 создание виджетов
count_digit = customtkinter.CTkLabel(app, text='0', font=('Caveat', 20))  # поле отображения текста
count_digit.pack(pady=5)

count_seconds = customtkinter.CTkLabel(app, text='seconds', font=('Caveat', 10))
count_seconds.pack()
seconds = customtkinter.CTkEntry(app, font=('Caveat', 15))  # поле для ввода seconds
seconds.pack(pady=5)

count_minutes = customtkinter.CTkLabel(app, text='minutes', font=('Caveat', 10))
count_minutes.pack(pady=5)
minutes = customtkinter.CTkEntry(app, font=('Caveat', 15))  # поле для ввода minutes
minutes.pack(pady=5)

count_hours = customtkinter.CTkLabel(app, text='hours', font=('Caveat', 10))
count_hours.pack(pady=1)
hours = customtkinter.CTkEntry(app, font=('Caveat', 15))  # поле для ввода hours
hours.pack(pady=1)

btn_start = customtkinter.CTkButton(app, text='Старт', font=('Caveat', 15), command=start)  # кнопка для старта
btn_start.pack(pady=5)

btn_stop = customtkinter.CTkButton(app, text='Стоп', font=('Caveat', 15), command=stop)  # кнопка для финиша


app.mainloop()  # запуск приложения
