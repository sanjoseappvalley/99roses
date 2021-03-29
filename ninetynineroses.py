
class Roses:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number} roses'

    @staticmethod
    def for_number(n):
        if n == 0:
            return NoRose()
        if n == 1:
            return OneRose()
        return Roses(n)

    @property
    def action(self):
        return f'I take one rose and give it to you'

    @property
    def successor(self):
        return Roses.for_number(self.number - 1)


class NoRose(Roses):
    def __init__(self):
        self.number = 0

    def __str__(self):
        return 'no more rose'

    @property
    def action(self):
        return 'go to the store and buy more roses'

    @property
    def successor(self):
        return Roses.for_number(99)


class OneRose(Roses):
    def __init__(self):
        self.number = 1

    def __str__(self):
        return '1 rose'


def verse(n):
    roses = Roses.for_number(n)
    return (
        f"{roses} in me, {roses}.\n".capitalize() +
        f"{roses.action}, {roses.successor} left.\n".capitalize()
    )


def sing(n):
    return '\n'.join(verse(roses) for roses in range(99, (99-n), -1))
