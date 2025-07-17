class PoliticalStruggle:
    @staticmethod
    def struggle(a: int, b: int, c: int):
        total_rooms = (a + b + c) // 3
        possible_by_agitation = a + (b + c) // 2

        if possible_by_agitation > total_rooms:
            return possible_by_agitation
        else:
            return total_rooms

print(PoliticalStruggle.struggle(3,2,1))

