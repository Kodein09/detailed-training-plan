#Generators
#Генераторы это ленивые объекты, которые создают значения по мере необходимости, не создаёт сразу всё в памяти, отлично подходит для работы с большими данными.
#
# def my_generator():
#     for i in range(5):
#         yield i
#
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
#
# gen_exp = (i * i for i in range(100))
# print(gen_exp)
# print(type(gen_exp))
#
#
# my_list = [1,2,3]
# it = iter(my_list)
# print(it)
# print(type(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
#
#  def gen():
#      yield 1
#      yield 2
#
#  g = gen()
#  print(next(g))
#  print(next(g))
#
#
# even = [i for i in range(0, 10) if i % 2 == 0]
# print(even)
#
# even =  (i for i in range(0, 10) if i % 2 == 0)
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))

# def gen_squares():
#     for i in range(5):
#         yield i * i
#
# gen_exp = (i * i for i in range(5))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))

# Генератор это специальный вид итератора, который создаётся функцией со специальным ключевым словом yield
# yield выдаёт значения по одному и приостанавливает своё состояние, чтобы продолжить с того места при следующем вызове
# yield экономит память, не загружая все данные разом
# Примеры ниже:

# def count_up_to(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#
# gen = count_up_to(3)
# print(next(gen))
# print(next(gen))