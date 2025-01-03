# Genshin Dialogues
##  🗺️ Описание проекта
Приложение для ПОЛНОГО пропуска диалогов: \
Быстрее, чем встроенный в игру пропуск \
С функцией выбора ответа в диалоге

---
## Содержание
- [Библиотеки](#Libraries)
- [Запуск](#Running)
  - [Для Windows](#Windows)
  - [Для Linux/MacOS](#Linux/MacOS)
- [Использование](#Usage) 
- [Лицензия](#License)
- [Автор](#Author)
---
## Libraries
* flet
* pyautogui

## Running

1. Скопируйте репозиторий
```sh
git clone https://github.com/pOsdas/GenshinDialogues.git
cd [ваше имя]
```
2. Создайте и активируйте свою виртуальную среду 
    ### Windows:
    ```sh
    python -m venv venv
    source venv/Scripts/activate
    ```
    ### Linux/MacOS:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

## Usage

1. Установить зависимости:
```commandline
pip install -r requirements.txt
```
2. Кнопка `Старт` выполняет пропуск диалогов (наведите на неё).
3. Кнопка `Стоп` завершает пропуск диалогов (наведите на неё).

> [!WARNING]  
> Для правильной работы приложения нажимайте кнопку `СТОП` перед выходом,
> иначе у вас не завершится поток нажатия кнопки 'f' и вам придется искать его через диспетчер задач.

> Постараюсь исправить в следующих релизах

## License
Распространяется под лицензией MIT.\
Дополнительная информация в файле `LICENSE.txt`.

## Author
Автор: pOsdas