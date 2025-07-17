# import unittest
#
# class CarWash:
#     def __init__(self):
#         pass
#
#     def car_wash(self):
#         fix_sum = int(input("заплатить X рублей за всю мойку независимо от затраченного времени и воды: "))
#         pay_per_minute = int(input("заплатить Y рублей за каждую минуту, потраченную на мойку: "))
#         payment_by_meter = int(input("заплатить Z рублей за каждый литр воды, использованный во время мойки: "))
#         time_for_car_wash = int(input("количество минут, требующееся для мойки автомобиля: "))
#         volume_of_water = int(input("объём воды в литрах, требующийся для мойки автомобиля: "))
#
#         cost_time = pay_per_minute * time_for_car_wash
#         cost_water = payment_by_meter * volume_of_water
#
#         min_cost = fix_sum
#
#         if cost_time < min_cost:
#             min_cost = cost_time
#         if cost_water < min_cost:
#             min_cost = cost_water
#
#         return min_cost
#
#
# car_wash = CarWash()
# print(car_wash.car_wash())
#
# class TestCarWash(unittest.TestCase):
#     fix_sum = 200
#     pay_per_minute = 10
#     pay_by_meter = 18
#     time_for_car_wash = 14
#     volume_of_water = 15
#
#     cost_time = pay_per_minute * time_for_car_wash
#     cost_water = pay_by_meter * volume_of_water
#
#     min_cost = fix_sum
#
#     expected = 140
#     result = CarWash.car_wash()


# class CarWash:
#     def __init__(self, x, y, z, t, v):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.t = t
#         self.v = v
#
#     @staticmethod
#     def find_min_cost(x, y, z, t, v):
#         water_cost = z * v
#         time_cost = y * t
#         fix_cost = x
#
#         if water_cost < fix_cost:
#             fix_cost = water_cost
#
#         if time_cost < fix_cost:
#             fix_cost = time_cost
#
#         return fix_cost
#
# import unittest
#
# class TestCarWash(unittest.TestCase):
#     def test_car_wash(self):
#         x = 200
#         y = 10
#         z = 18
#         t = 14
#         v = 15
#         expected = 140
#         result = CarWash.find_min_cost(x, y, z, t, v)
#         self.assertEqual(result, expected)
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# import unittest
#
# class CarWash:
#     @staticmethod
#     def calculate_min_cost(x: int, y: int, z: int, t: int, v: int):
#         water_cost = z * v
#         time_cost = y * t
#
#         min_fix_cost = x
#
#         if water_cost < min_fix_cost:
#             min_fix_cost = water_cost
#         if time_cost < min_fix_cost:
#             min_fix_cost = time_cost
#
#         return min_fix_cost
#
# class TestCarWash(unittest.TestCase):
#     def test_car_wash(self):
#         x = 200
#         y = 10
#         z = 18
#         t = 14
#         v = 15
#         expected = 140
#         result = CarWash.calculate_min_cost(x, y, z, t, v)
#         self.assertEqual(expected, result)
#
# if __name__ == '__main__':
#     unittest.main()