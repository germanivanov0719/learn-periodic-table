from table.elements import Table
from table.periods_resource import PERIODS


def load(periods="") -> Table:
    table = Table(**dict(PERIODS))
    if periods and periods not in ["a", "all"]:
        try:
            table.set_periods(*list(periods))
        except ValueError:
            pass
    return table
