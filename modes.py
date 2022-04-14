from copy import copy
import table.load
from console_resources.cli import ColoredString as cstr
from console_resources.cli import clear, hcenter, hleft
import random


def learn(TABLE):
    print(cstr(hcenter("Список всех элементов")).red())
    print(cstr(hcenter("(нажимайте Enter, чтобы листать):")).red())
    for per in TABLE.periods.keys():
        print(cstr(hcenter(f"Период #{per}:")).yellow())
        index = 0
        for el in TABLE.periods[per]:
            output = cstr(
                f"{el.symbol}:\t{el.names[el.locale].ljust(10)}\t\t({el.locale})"
            )
            if index % 2 == 0:
                print(output.blue(), end="")
            else:
                print(output.green(), end="")
            index += 1
            input()


def test_names(TABLE) -> int:
    print(cstr(hcenter("Тест названий элементов:")).red())
    corr, total = 0, 0
    for num, per in TABLE.periods.items():
        print(cstr(hcenter(f"Период #{num}:")).yellow())
        index = 0
        randomized_per = copy(per)
        random.shuffle(randomized_per)
        for el in randomized_per:
            output = cstr(f"{el.symbol}\t({el.locale}):")
            if index % 2 == 0:
                print(output.blue(), end="")
            else:
                print(output.green(), end="")
            index += 1
            total += 1
            if input(" ").strip().capitalize() == el.names[el.locale]:
                corr += 1
            else:
                print(
                    cstr(
                        f"Ошибка #{total - corr}. "
                        f"Правильно: {el.names[el.locale]}. "
                    ).red()
                )
    return corr


def test_symbols(TABLE) -> int:
    print(cstr(hcenter("Тест символов элементов:")).red())
    corr, total = 0, 0
    for num, per in TABLE.periods.items():
        print(cstr(hcenter(f"Период #{num}:")).yellow())
        index = 0
        randomized_per = copy(per)
        random.shuffle(randomized_per)
        for el in randomized_per:
            output = cstr(f"{el.names[el.locale]} ({el.locale}):")
            if index % 2 == 0:
                print(output.blue(), end="")
            else:
                print(output.green(), end="")
            index += 1
            total += 1
            if input(" ").strip().capitalize() == el.symbol:
                corr += 1
            else:
                print(
                    cstr(
                        f"Ошибка #{total - corr}. " f"Правильно: {el.symbol}. "
                    ).red()
                )
    return corr


def select_periods():
    print(cstr(hcenter("Выберете периоды для изучения")).red())
    print(cstr(hcenter("(цифры можно вводить в любом порядке):")).red())
    print("\n")
    print(cstr("Выбор:").blue_background(), end="")
    return table.load.load(input(" "))
