from enum import Enum, auto

# class Status(Enum):
#     ACTIVE = 1
#     INACTIVE = 0
#     PENDING = 2
#
# print(Status.ACTIVE)
# print(Status.ACTIVE.name)
# print(Status.ACTIVE.value)
# print(Status.INACTIVE)
# print(Status.INACTIVE.name)
# print(Status.INACTIVE.value)
# print(Status.PENDING)
# print(Status.PENDING.name)
# print(Status.PENDING.value)


# class Colour(Enum):
#     RED = auto()
#     YELLOW = auto()
#     GREEN = auto()
#
#     def traffic_light(self):
#         if self == self.RED:
#             return "RED LIGHT, STOP!"
#         elif self == self.YELLOW:
#             return "YELLOW LIGHT, WAIT A SECOND!"
#         else:
#             return "GREEN LIGHT, GO!"
#
# colour = Colour.YELLOW
# print(colour.traffic_light())


# class AccessLevel(Enum):
#     ADMIN = 1
#     USER = 0
#     GUEST = 2
#
# def get_permission(level: AccessLevel):
#     if level == AccessLevel.ADMIN:
#         return AccessLevel.ADMIN
#     elif level == AccessLevel.USER:
#         return AccessLevel.USER
#     else:
#         return AccessLevel.GUEST
#
# permission = get_permission(AccessLevel.USER)
# print(permission)


# class Direction(Enum):
#     NORTH = (0, 1)
#     SOUTH = (0,-1)
#     EAST = (-1,0)
#     WEST = (1,0)
#
#     def direction(direct):
#         if direct == Direction.NORTH:
#             return Direction.NORTH
#         elif direct == Direction.SOUTH:
#             return Direction.SOUTH
#         elif direct == Direction.EAST:
#             return Direction.EAST
#         else:
#             return Direction.WEST
#
#
# d = Direction.WEST
# print(Direction.direction(d))


# class HttpStatus(Enum):
#     OK = 200
#     NOT_FOUND = 404
#     CLIENT_ERROR = 500
#
#     def handle_response(status):
#         if status == HttpStatus.OK:
#             return HttpStatus.OK
#         elif status == HttpStatus.NOT_FOUND:
#             return HttpStatus.NOT_FOUND
#         else:
#             return HttpStatus.CLIENT_ERROR
#
# http_status = HttpStatus.NOT_FOUND
# print(HttpStatus.handle_response(http_status))


# class WeekDay(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7
#
#     def is_weekend(self):
#         return self in (WeekDay.SATURDAY, WeekDay.SUNDAY)
#
# today = WeekDay.SATURDAY
# print(WeekDay.is_weekend(today))
