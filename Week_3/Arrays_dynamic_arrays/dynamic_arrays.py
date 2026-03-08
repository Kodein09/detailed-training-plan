# marks = [2, 2, 3, 4]    # array сам динамический массив содержит данные только одного типа - ссылки на объекты
# lst = [True, 'str', 1, 1.0]    # list
#
# print('Elements:', len(marks))
# indexes = len(marks) - 1
# print('Indexes:', indexes)
#
# lst.append(5)    # O(1)
# print(lst,'''В конец добавился новый элемент, элемент представляет собой ссылку, которая ведёт на объект, который содержит целое значение''')
# lst.insert(0, 'First element')    # 1.index, 2.data.    Time complexity: O(n)
# print(lst)
#
#
# element_3 = lst[2]
# print(element_3)
#
# lst[3] = 2
# print(lst)
#
#
# #Concatenate arrays/list
# print(marks + lst)    # Произошло создание нового динамического массива, далее происходит копирование информации, сперва из первого массива, потом из второго списка
# #Сложность данного действия O(n + m), где n - все элементы первого массива, m - все элементы второго списка
#
# #Срезы
# new_list = [1,2,3,4,5,6,7,8]
# print(new_list[:6]) #Срез в списках создаёт новый массив/список, после чего копируются соответствующие элементы из первого массива/списка
# #Сложность O(n)


class DynamicArray:
    def __init__(self, _capacity=8):
        self._capacity = _capacity
        self._n = 0
        self._data = [None] * _capacity

    def __str__(self):
        return str(self._data[:self._n])

    def __getitem__(self, item):
        if 0 <= item < self._n:
            return self._data[item]
        raise IndexError("Index out of range")

    def __setitem__(self, key, value):
        if 0 <= key < self._n:
            self._data[key] = value
        else:
            raise IndexError("Index out of range")


    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._n):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._n == self._capacity:    # Если будет равенство между элементами и ёмкостью - следует увеличить массив в 2 раза.
            self._resize(self._capacity * 2)

        self._data[self._n] = value    # Запись нового значения в массив.
        self._n += 1    # Используется для счёта при добавлении нового элемента, чтобы знать, сколько добавилось элементов в массив.

    def insert(self, index, value):
        if not (0 <= index < self._n):
            raise IndexError("Index out of range")

        if self._n == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._n, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = value
        self._n += 1

    def pop(self, index=None):
        if self._n == 0:
            raise IndexError("Pop from empty Dynamic array")

        if index is None:
            index = self._n - 1

        if not (0 <= index < self._n):     # Если данное условие не верное и мы выходим за границы индекса в отрицательные числа - то вызываем ошибку
            raise IndexError("Index out of range")

        value = self._data[index]

        for i in range(index, self._n - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._n - 1] = None
        self._n -= 1

        if 0 < self._n < self._capacity // 4:
            self._resize(self._capacity // 2)

        return value

    def size(self):
        return self._n

import unittest
class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.arr = DynamicArray()

    def test_append_and_get(self):
        for i in range(10):
            self.arr.append(i)

        self.assertEqual(self.arr.size(), 10)
        self.assertEqual(self.arr[0], 0)
        self.assertEqual(self.arr[5], 5)
        self.assertEqual(self.arr[9], 9)

    def test_insert_start(self):
        for i in range(1, 11):
            self.arr.append(i)

        self.arr.insert(0, 100)
        self.assertEqual(self.arr[0], 100)

    def test_insert_middle(self):
        for i in range(1, 11):
            self.arr.append(i)

        self.arr.insert(5, 90)
        self.arr.insert(8, [1,2,3])
        self.assertEqual(self.arr[5], 90)

        self.assertEqual(self.arr[8], [1,2,3])

    def test_insert_end(self):
        for i in range(1, 11):
            self.arr.append(i)

        self.arr.insert(9, 29)
        self.assertEqual(self.arr[9], 29)

    def test_pop_end(self):
        for i in range(5):
            self.arr.append(i)

        value = self.arr.pop(4)
        self.assertEqual(value, 4)
        self.assertEqual(self.arr.size(), 4)

    def test_pop_middle(self):
        for i in range(1, 6):
            self.arr.append(i)

        value = self.arr.pop(2)
        self.assertEqual(value, 3)
        self.assertEqual(str(self.arr), "[1, 2, 4, 5]")

    def test_out_of_range_get(self):
        self.arr.append(1)
        with self.assertRaises(IndexError):
            _ = self.arr[3]

    def test_out_of_range_pop(self):
        self.arr.append(1)
        with self.assertRaises(IndexError):
            self.arr.pop(10)

    def test_resize_up(self):
        for i in range(10):
            self.arr.append(i)

        self.assertTrue(self.arr._capacity >= 10)

    def test_resize_down(self):
        for i in range(10):
            self.arr.append(i)

        old_capacity = self.arr._capacity

        for i in range(9):
            self.arr.pop()

        self.assertTrue(self.arr._capacity < old_capacity)

if __name__ == '__main__':
    unittest.main()