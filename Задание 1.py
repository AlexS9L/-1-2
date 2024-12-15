# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Table:
    def __init__(self, l: float, w: float, h: float):

        if l < 0:
            raise ValueError('Длина стола не может быть отрицательной')
        if w < 0:
            raise ValueError('Ширина стола не может быть отрицательной')
        if h < 0:
            raise ValueError('Высота стола не может быть отрицательной')
        self.l = l
        self.w = w
        self.h = h
        """
                Создание и подготовка к работе объекта "Стол"

                :param l: длина стола
                :param w: ширина стола
                :param h: высота стола

                Примеры:
                >>>table = Table(100, 150, 100)  # инициализация экземпляра класса
                """

    def lenght(self):
        """
          Функция которая выводит длинну стола

        :return: Длинна стола - {self.l} сантиметров

        Примеры:
        >>> table = Table(100, 150, 100)
        >>> table.lenght()
        """
        print(f'Длинна стола - {self.l} сантиметров')

    def width(self):

        """
          Функция которая выводит ширину стола

        :return: Ширина стола - {self.w} сантиметров

        Примеры:
        >>> table = Table(100, 150, 100)
        >>> table.width()
        """
        print(f'Ширина стола - {self.w} сантиметров')

    def height(self):
        """
          Функция которая выводит высоту стола

        :return: Высота стола - {self.h} сантиметров

        Примеры:
        >>> table = Table(100, 150, 100)
        >>> table.height()
        """
        print(f'Высота стола - {self.h} сантиметров')


class Mountan:
    def __init__(self, n_mount: str, height: int, age: int):
        """
              Создание и подготовка к работе объекта "Гора"

              :param n_mount: название горы
              :param height: Высота горы
              :param age: Возраст горы

              Примеры:
              >>> mountan = Mountan('Everest', 8848, 60000000)  # инициализация экземпляра класса
              """
        self.n_mount = n_mount
        self.height = height
        self.age = age
        self.minerals = []
        if not isinstance(n_mount, str):
            raise TypeError('Название должно быть строкой ')
        if age < 0:
            raise ValueError('Возраст горы не может быть отрицательным')
        if height < 0:
            raise ValueError('Высота горы не может быть отрицательной ')

    def add_minerals(self, min_name: str) -> None:
        """
          Функция которая позволяет добавить полезные ископаемые (минералы)

        :param min_name: название минерала

        Примеры:
        >>> mountan = Mountan(Everest, 8848, 60000000)
        >>> mountan.add_minerals('pirit')
        """
        self.minerals.append(min_name)

    def height_t(self, years: int) -> None:
        """
          Функция которая позволяет узнать высоту горы спустя время

        :param years: пройденное время (в годах)

        Примеры:
        >>> mountan = Mountan(Everest, 8848, 60000000)
        >>> mountan.height_t(3000)
        """
        self.age += years
        self.height -= years * 2
        if years < 0:
            raise ValueError('Количество пройденных лет не может быть отрицательным')

    def exceiv_minerals(self) -> list:
        """
          Функция которая позволяет узнать какие минералы были добыты

        :param min_name: название минерала

        Примеры:
        >>> mountan = Mountan('Everest', 8848, 60000000)
        >>> mountan.exceiv_minerals()
        """
        exceived_minerals = self.minerals.copy()
        self.minerals.clear()
        return exceived_minerals


class Site:
    def __init__(self, site_name: str, number_of_users: int):

        self.site_name = site_name
        self.number_of_users = number_of_users
        self.sections = []
        if number_of_users < 0:
            raise ValueError('Количество пользователей не может быть отрицательным')
        if not isinstance(site_name, str):
            raise TypeError('Название сайта - строка')

    """
           Создание и подготовка к работе объекта "Сайт"

           :site_name: название сайта
           :number_of_users: количество пользователей


           Примеры:
           >>> site = Site('shop', 1000)
           """

    def site_n(self):
        """
          Функция которая позволяет вывести название сайта
        :return: Название сайта - {self.site_name}

        Примеры:
        >>> site = Site('shop', 1000)
        >>> site.site_n()

        """
        print(f'Название сайта - {self.site_name}')

    def numb_of_users(self, users: int) -> None:
        """
          Функция которая позволяет узнать количество пользователей

        Примеры:
        >>> site = Site('shop', 1000)
        >>> site.numb_of_users
        """
        self.number_of_users += users
        if users < 0:
            raise ValueError('Количество пользователей не может быть отрицательным')
        print(f'Количество пользователей - {self.number_of_users}')

    def add_section(self, section: str) -> None:

        self.sections.append(section)
        """
                  Функция которая позволяет добавить вкладки на сайт

                Примеры:
                >>> site = Site('shop', 1000)
                >>> site.add_section('контакты')
                >>>site.add_section('каталог')
                >>>site.add_section('корзина')
                >>>site.sections
                """
if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
