class Element:
    def __init__(self, symbol: str, **names) -> None:
        self.symbol = symbol
        self.names = dict(names)
        self.locale = "RU"

    def set_locale(self, code: str) -> None:
        self.locale = code if code in self.names.keys() else self.locale

    def __str__(self) -> str:
        return self.symbol + " " + self.names[self.locale]


class Table:
    def __init__(self, **periods) -> None:
        self.periods = dict(periods)

    def set_locale(self, code: str) -> None:
        for period in self.periods.values():
            for element in period:
                element.set_locale(code)

    def set_periods(self, *nums) -> None:
        print(nums)
        res = dict()
        nums = [int(i) for i in nums]
        for num, period in self.periods.items():
            if int(num) in nums:
                res[num] = period
        self.periods = res
