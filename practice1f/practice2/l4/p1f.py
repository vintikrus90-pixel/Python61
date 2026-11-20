class Square:
    """

    Attributes:
        width (float): ширина (сторона) квадрата.
    Methods:
        __init__(width): создаёт квадрат с заданной шириной.
        get_area(): возвращает площадь квадрата.
    """

    def __init__(self, width: float):
        """
        Функция-конструктор: создаёт объект Square и сохраняет ширину.

        Parameters:
            width (float): ширина (сторона) квадрата.
        """
        self.width = width

    def get_area(self) -> float:
        """

        Returns:
            float: площадь квадрата (ширина в квадрате).
        """
        return self.width ** 2
