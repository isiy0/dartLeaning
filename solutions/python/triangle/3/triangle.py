def is_triangle(sides: list[float]) -> bool:
    a, b, c = sorted(sides)

    return a > 0.0 and a + b >= c # Taking advantage of the applied ordering, 
    # after the condition a > 0.0 is true, we are certain that all other sides of the triangle will be greater than 0.0.
    # Furthermore, using mathematics to our advantage, since c > a and b, 
    # necessarily, if a + b >= c, the remaining scenarios of the expression will also be true: b + c >= a & a + c >= b

def equilateral(sides: list[float]) -> bool:
    # Transforming the list of sides into a set that unifies repeated numbers and using the len() function
    #to count the number of items in the set. In this way, we can logically assume that if the number of items in the set is 3,
    # then all sides must have different values; if the return is 2, then all 2 sides must be repeated and unified into a single item in the set, and so on.
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[float]) -> bool:
    return is_triangle(sides) and len(set(sides)) <= 2

def scalene(sides: list[float]) -> bool:
    return is_triangle(sides) and len(set(sides)) == 3
