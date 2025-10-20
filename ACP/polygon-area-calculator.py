# Base class
class Polygon:
    def __init__(self, sides):
        self.sides = sides  # list of sides

    def display_sides(self):
        print("Polygon has", len(self.sides), "sides:", self.sides)

    def area(self):
        print("Area calculation depends on the specific shape.")


# Derived class for Rectangle
class Rectangle(Polygon):
    def __init__(self, length, width):
        # Rectangle has 4 sides, two pairs are equal
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class for Square
class Square(Rectangle):  # Square is a special Rectangle
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def area(self):
        return self.side ** 2


# Derived class for Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        # Triangle has 3 sides (simplified)
        super().__init__([base, height, base])
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Derived class for Hexagon
class Hexagon(Polygon):
    def __init__(self, side):
        super().__init__([side] * 6)
        self.side = side

    def area(self):
        # Formula: (3 * sqrt(3) * side²) / 2
        import math
        return (3 * math.sqrt(3) * self.side ** 2) / 2


# --- MAIN PROGRAM ---

def main():
    print("Choose the shape to calculate area:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Hexagon")

    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        rect = Rectangle(l, w)
        print(f"Area of Rectangle: {rect.area()}")

    elif choice == 2:
        s = float(input("Enter side: "))
        sq = Square(s)
        print(f"Area of Square: {sq.area()}")

    elif choice == 3:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        tri = Triangle(b, h)
        print(f"Area of Triangle: {tri.area()}")

    elif choice == 4:
        s = float(input("Enter side: "))
        hexagon = Hexagon(s)
        print(f"Area of Hexagon: {hexagon.area():.2f}")

    else:
        print("Invalid choice!")


# Run the program
if __name__ == "__main__":
    main()
