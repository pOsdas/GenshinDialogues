import flet as ft
import pyautogui
import threading
import time


stop_pressing_f = False


def main(page: ft.Page):
    page.title = "Genshin Diologues"
    page.window_always_on_top = True
    page.window_width = 312
    page.window_height = 300
    page.window_resizable = False
    page.window.maximizable = False
    page.window_icon = "assets/next-button.png"

    label = ft.Text("Авто пропуск диалогов!", size=20, weight="bold", color="blue")

    description = "Кнопка 'Старт' выполняет следующее:\n" \
                  "1. Ждет пока вы откроете игру 10 секунд.\n" \
                  "2. Начинает нажимать клавишу 'F' каждые 2 секунды бесконечно.\n"

    timer_label = ft.Text("", size=16, color="blue")

    empty_label = ft.Text("")

    def countdown(start_seconds, callback):
        for i in range(start_seconds, 0, -1):
            timer_label.value = f"Таймер: {i} секунд"
            page.update()
            time.sleep(1)
        timer_label.value = "Таймер завершён!"
        page.update()
        callback()

    def perform_actions():
        screen_width, screen_height = pyautogui.size()
        pyautogui.click(x=screen_width // 2, y=screen_height // 2)

        global stop_pressing_f
        while not stop_pressing_f:
            pyautogui.press("f")
            time.sleep(2)

    def start_button_handler(e):
        global stop_pressing_f
        stop_pressing_f = False
        threading.Thread(
            target=countdown, args=(10, lambda: threading.Thread(target=perform_actions).start())
        ).start()

    def stop_button_handler(e):
        global stop_pressing_f
        stop_pressing_f = True

    def on_close(e):
        print("Приложение закрыто")
        page.window_close()

    start_button = ft.ElevatedButton(
        "Старт",
        on_click=start_button_handler,
        tooltip=description,
    )

    stop_button = ft.ElevatedButton(
        "Стоп",
        on_click=stop_button_handler,
        tooltip="Останавливает бесконечное нажатие клавиши 'F'.",
    )

    page.on_close = on_close

    page.add(
        ft.Column(
            controls=[
                label,
                start_button,
                timer_label,
                empty_label,
                empty_label,
                stop_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
        )
    )

