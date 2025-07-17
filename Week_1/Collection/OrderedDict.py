from collections import OrderedDict

from ruamel.yaml.compat import ordereddict

# ordered = OrderedDict()
#
# ordered["banana"] = 200
# ordered["car"] = 10
# ordered["cash"] = 15
#
# ordered.move_to_end("car")
# print(ordered)


# data = [("b", 4), ("a", 5), ("d", 2), ("c", 3)]
#
# order = OrderedDict(data)
#
# print(order)
# order.pop("b")
# print(order)
# order.popitem()
# order["f"] = 1
# print(order)
# order.move_to_end("f")
# print(order)


# class FIFOCache:
#     def __init__(self, capacity):
#         self.cache = OrderedDict()
#         self.capacity = capacity
#
#     def put(self, key, value):
#         if key in self.cache:
#             self.cache.pop(key)
#         elif len(self.cache) >= self.capacity:
#             self.cache.popitem(last=False)
#         self.cache[key] = value
#
#     def get(self, key):
#         return self.cache.get(key, -1)
#
#     def pop(self, key):
#         return self.cache.pop(key)
#
#     def __repr__(self):
#         return repr(self.cache)
#
#
# cache = FIFOCache(3)
# cache.put("a", 1)
# cache.put("b", 2)
# cache.put("c", 3)
# print(cache)
#
# cache.put("d", 4)
# print(cache)
#
# print(cache.get("d"))
# print(cache.get("c"))
#
# print(cache.pop("b"))
# print(cache)
#
# print(cache.put("Apple", "Fruit"))
# print(cache)

# d = {}
# d["a"] = 1
# d["b"] = 2
# d["c"] = 3
#
# print(d)
#
# od = ordereddict()
#
# od["a"] = 1
# od["b"] = 2
# od["c"] = 3
#
# od.move_to_end("a")
# print(od)
# print(od.popitem(last=True))
# print(od.popitem(last=False))
# print(od)