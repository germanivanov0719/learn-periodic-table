import os
from console_resources.colored_output import *


def clear():
    if os.name == "nt":
        os.system("color 0")
        os.system("cls")
    else:
        os.system("clear")


def hcenter(string: str) -> str:
    width = os.get_terminal_size().columns
    if width <= len(string):
        return string
    width -= len(string)
    return " " * (width // 2) + string + " " * (width - width // 2)


def hleft(string: str) -> str:
    width = os.get_terminal_size().columns
    if width <= len(string):
        return string
    width -= len(string)
    return " " * width + string


class ColoredString(str):
    def green(self):
        return ColoredString(GREEN + str(self) + RESET)

    def red(self):
        return ColoredString(RED + str(self) + RESET)

    def blue(self):
        return ColoredString(BLUE + str(self) + RESET)

    def yellow(self):
        return ColoredString(YELLOW + str(self) + RESET)

    def green_background(self):
        return ColoredString(GREEN_BACKGROUND + str(self) + RESET)

    def red_background(self):
        return ColoredString(RED_BACKGROUND + str(self) + RESET)

    def blue_background(self):
        return ColoredString(BLUE_BACKGROUND + str(self) + RESET)

    def yellow_background(self):
        return ColoredString(YELLOW_BACKGROUND + str(self) + RESET)

    def black_background(self):
        return ColoredString(BLACK_BACKGROUND + str(self) + RESET)

    def italic(self):
        return ColoredString(ITALIC + str(self) + RESET)

    def underline(self):
        return ColoredString(UNDERLINE + str(self) + RESET)
