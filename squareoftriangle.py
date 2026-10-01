import math

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Вычисляет расстояние между двумя точками на плоскости.

    Args:
        x1, y1 (float): Координаты первой точки.
        x2, y2 (float): Координаты второй точки.

    Returns:
        float: Расстояние между точками.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_triangle_area(a: float, b: float, c: float) -> float:
    """
    Вычисляет площадь треугольника по формуле Герона на основе длин трех его сторон.

    Args:
        a (float): Длина первой стороны.
        b (float): Длина второй стороны.
        c (float): Длина третьей стороны.

    Returns:
        float: Площадь треугольника.
    """
    semi_perimeter = (a + b + c) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return area

def main():
    print("Введите координаты точек через пробел (x y):")
    x_a, y_a = map(float, input("Точка A: ").split())
    x_b, y_b = map(float, input("Точка B: ").split())
    x_c, y_c = map(float, input("Точка C: ").split())
    
    side_ab = calculate_distance(x_a, y_a, x_b, y_b)
    side_bc = calculate_distance(x_b, y_b, x_c, y_c)
    side_ca = calculate_distance(x_c, y_c, x_a, y_a)
    
    triangle_area = calculate_triangle_area(side_ab, side_bc, side_ca)
    
    print(f"\nПлощадь треугольника составляет: {triangle_area:.2f}")

if __name__ == "__main__":
    main()