# import unittest
#
# class DynamicArray:
#     def __init__(self, _capacity=8):
#         self._capacity = _capacity
#         self._data = [None] * self._capacity
#         self._n = 0
#
#     def _resize(self, new_capacity):
#         new_data = [None] * new_capacity
#         for i in range(self._n):
#             new_data[i] = self._data[i]
#         self._data = new_data
#         self._capacity = new_capacity
#
#     def append(self, value):
#         if self._n == self._capacity:
#             self._resize(self._capacity * 2)
#         self._data[self._n] = value
#         self._n += 1
#
#     def insert(self, index, value):
#         if self._n == self._capacity:
#             self._resize(self._capacity * 2)
#
#         for i in range(self._n - 1, index - 1, -1):
#             self._data[i + 1] = self._data[i]
#
#         self._data[index] = value
#         self._n += 1
#
#     def pop(self):
#         if self._n == 0:
#             return None
#         value = self._data[self._n - 1]
#         self._data[self._n - 1] = None
#         self._n -= 1
#         if 0 < self._n < self._capacity // 4:
#             self._resize(self._capacity // 2)
#         return value
#
# dynamic_array = DynamicArray()

class DynamicArray:
    def __init__(self, _capacity=8):
        self._capacity = _capacity
        self._n = 0
        self._data = [None] * _capacity

    def __str__(self):    # Срез нужен для того, чтобы не выводить None, т.е. пустые места или пробелы и до элементов
        return str(self._data[:self._n])    # Обернуть обращение к массиву и через массив обращение к элементу в str для возможности выводить через метод print

    def __getitem__(self, item):
        if 0 <= item < self._n:    # Если 0 будет меньше либо равен значению и меньше элемента массива. Эта проверка нужна, чтобы не работать с пустыми слотами
            return self._data[item]    # Возвращаем или достаём элемент из массива для быстрого доступа за O(1)
        raise IndexError("Index out of range")

    def __setitem__(self, key, value):
        if 0 <= key < self._n:    # Если индекс больше либо равен 0 и меньше элементов массива. Проверка нужна, чтобы не работать с пустыми слотами, по типу None.
            self._data[key] = value    # Тогда присваиваем к индексу новое значение
        else:
            raise IndexError("Index out of range")

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._n):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        """Добавление значения в конец массива"""
        if self._capacity == self._n:    # Если ёмкость равна элементам массива (это для того, чтобы узнать заполнен массив до конца или же нет)
            self._resize(self._capacity * 2)    # Тогда вызываем функцию _resize для того, чтобы увеличить размер массива вдвое, обычно используется х2 либо в диапазоне от 1.125 - 2.
        self._data[self._n] = value    # В массив под элемент вставляем новое значение
        self._n += 1    # Это счётчик для отслеживания, сколько элементов добавлено в массив.

    def insert(self, key, value):
        """Вставка значения по индексу"""
        if self._n == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._n - 1, key, -1):
            self._data[i + 1] = self._data[i]

        self._data[key] = value
        self._n += 1

    def pop(self):
        """Удаление """
        if self._n == 0:    # Проверка на наличие элементов внутри массива, если их нет - вернуть None
            return None

        value = self._data[self._n - 1]    # Берём значение самого последнего элемента через self._n - 1, где self._n = 0, поэтому значение это равно последнему элементу массива.
        self._data[self._n - 1] = None    # Пока не знаю, что это означает, зачем присваивать None и отнимать элемент внутри массива
        self._n -= 1    # После чего ещё раз отнять единицу у элемента

        if 0 < self._n < self._capacity  // 4:    # Проверка если элемент массива больше 0 и ёмкость больше элементов массива - делим нацело на 4
            self._resize(self._capacity // 2)    # Вызов функции _resize для уменьшения размера памяти в 2 раза
        return value    # Вернуть значение
