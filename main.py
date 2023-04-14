import table.load
from console_resources.cli import ColoredString as cstr
from console_resources.cli import clear, hcenter, hleft
import modes

# from console_resources.colored_output import RESET

print(cstr("Загрузка...").red_background())

TABLE = table.load.load()
clear()

menu = "welcome"

MENUS = [
    ("учить выбранные элементы", "learn"),
    ("тестирование названий", "test names"),
    ("тестирование символов", "test symbols"),
    ("выбрать периоды", "select periods"),
    ("выход", "quit"),
]


def select_menu():
    global menu
    print(cstr(hcenter("Выберете меню (укажите цифру):")).red())
    for i, menu_name in enumerate(MENUS):
        print(cstr(f"{i + 1}: {menu_name[0]}").yellow())
    print(
        cstr(
            "\n" + int(menu == "retry") * "Ошибка, попробуйте снова"
        ).red_background()
    )
    print(cstr("Выбор:").blue_background(), end="")
    try:
        menu = list(MENUS)[int(input(" ")) - 1][1]
    except ValueError:
        menu = "retry"
    except IndexError:
        menu = "retry"


def press_enter():
    print(
        cstr(hleft("Нажмите Enter, чтобы продолжить...")).green(),
        end="\r\r",
    )
    input()


while menu not in ["quit", "q", "выход", "exit", "shutdown"]:
    try:
        if menu == "welcome":
            print(cstr(hcenter("Добро пожаловать!")))
            print("\n\n\n")
            press_enter()
        elif menu == "learn":
            modes.learn(TABLE)
        elif menu == "test names":
            modes.test_names(TABLE)
        elif menu == "test symbols":
            modes.test_symbols(TABLE)
        elif menu == "select periods":
            TABLE = modes.select_periods()

        clear()
        select_menu()
        clear()
    except KeyboardInterrupt:
        print("\n")
        clear()
        print(cstr("Попытка выхода").green_background())
        print(
            cstr(
                "Нажмите еще раз для завершения, или Enter для выхода в меню."
            ).yellow()
        )
        try:
            input()
            menu = ""
        except KeyboardInterrupt:
            menu = "quit"

clear()
print(cstr("До свидания!").green())
