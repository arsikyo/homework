import math

def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Вычисляет площадь прямоугольника.

    Args:
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.

    Returns:
        float: Площадь прямоугольника.
    """
    return width * height

def calculate_circle_area(radius: float) -> float:
    """
    Вычисляет площадь круга.

    Args:
        radius (float): Радиус круга.

    Returns:
        float: Площадь круга.
    """
    return math.PI * (radius ** 2) if hasattr(math, 'PI') else math.pi * (radius ** 2)

def main():
    rect_width, rect_height = map(float, input("Введите ширину и высоту прямоугольника через пробел: ").split())
    rect_area = calculate_rectangle_area(rect_width, rect_height)
    print(f"Площадь прямоугольника: {rect_area:.2f}")
    
    circle_radius = float(input("Введите радиус круга: "))
    circle_area = calculate_circle_area(circle_radius)
    print(f"Площадь круга: {circle_area:.2f}")

if __name__ == "__main__":
    main()