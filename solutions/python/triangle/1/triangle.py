def is_triangle(slides: list[float]) -> bool:

    return (slides[0] > 0.0 and slides[1] > 0.0 and slides[2] > 0.0) and (slides[0] + slides[1] >= slides[2] and slides[0] + slides[2] >= slides[1] and slides[1] + slides[2] >= slides[0])

def equilateral(slides: list[int, float]) -> bool:
    
    return is_triangle(slides) and slides[0] == slides[1] and slides[1] == slides[2]


def isosceles(slides: list[int, float]) -> bool:
    return is_triangle(slides) and (slides[1] == slides [2] or slides[0] == slides[2] or slides[0] == slides[1])

def scalene(slides: list[int, float]) -> bool:
    return is_triangle(slides) and (slides[0] != slides[1] and slides[1] != slides[2] and slides[0] != slides[2])
