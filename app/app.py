import flet as ft
import win32api
import win32con
import threading
import time


class AutoPresserApp:
    def __init__(self, page):
        self.page = page
        self.stop_pressing_f = False
        self.thread = None
        self.timer_label = ft.Text("", size=16, color="blue")

    def countdown(self, start_seconds, callback):
        for i in range(start_seconds, 0, -1):
            self.timer_label.value = f"Таймер: {i} секунд"
            self.page.update()
            time.sleep(1)
        self.timer_label.value = "Таймер завершён!"
        self.page.update()
        callback()

    def perform_actions(self):
        screen_width = win32api.GetSystemMetrics(0)
        screen_height = win32api.GetSystemMetrics(1)

        win32api.SetCursorPos((screen_width // 2, screen_height // 2))

        # click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        # one more click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        time.sleep(1)
        while not self.stop_pressing_f:
            win32api.keybd_event(0x46, 0, 0, 0)
            time.sleep(3)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)

    def start_button_handler(self, e):
        self.stop_pressing_f = False
        threading.Thread(
            target=self.countdown,
            args=(5, lambda: threading.Thread(target=self.perform_actions).start()),
        ).start()

    def stop_button_handler(self, e):
        self.stop_pressing_f = True
        if self.thread and self.thread.is_alive():
            self.thread.join()

        self.page.snack_bar = ft.SnackBar(
            content=ft.Container(
                ft.Text("Поток остановлен", color=ft.colors.WHITE, size=16, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center,
            ),
            bgcolor="#232b36",
            open=True,
        )
        self.page.update()

    def on_close(self, e):
        print("Приложение закрыто")
        self.stop_pressing_f = True
        if self.thread and self.thread.is_alive():
            self.thread.join()
        self.page.window_close()


def main(page: ft.Page):
    page.title = "Genshin Diologues"
    page.window_always_on_top = True
    page.window_width = 312
    page.window_height = 350
    page.window_resizable = False
    page.window.maximizable = False
    page.window_icon = "assets/icon.ico"

    app = AutoPresserApp(page)

    label = ft.Text("Авто пропуск диалогов!", size=20, weight="bold", color="blue")

    description = (
        "Кнопка 'Старт' выполняет следующее:\n"
        "1. Ждет пока вы откроете игру 10 секунд.\n"
        "2. Начинает нажимать клавишу 'F' каждые 2 секунды бесконечно.\n"
    )

    start_button = ft.ElevatedButton(
        "Старт",
        on_click=app.start_button_handler,
        style=ft.ButtonStyle(bgcolor=ft.colors.INDIGO_500, color=ft.colors.WHITE),
        tooltip=description,
    )

    stop_button = ft.ElevatedButton(
        "Стоп",
        on_click=app.stop_button_handler,
        style=ft.ButtonStyle(bgcolor=ft.colors.RED_600, color=ft.colors.WHITE),
        tooltip="Останавливает бесконечное нажатие клавиши 'F'.",
    )

    page.on_close = app.on_close

    page.add(
        ft.Column(
            controls=[
                label,
                start_button,
                app.timer_label,
                ft.Text(""),
                ft.Text(""),
                stop_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
        )
    )

