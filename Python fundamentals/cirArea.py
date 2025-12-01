import math
def area(radius):
    return f"The area of the circle with radius {radius} is {math.pi*pow(radius,2)} cm²"

def circumference(radius):
    return f"The circumference of the circle with radius {radius} is {2*math.pi*radius} cm"

def main():
    radius = float(input("Enter the radius of the circle: "))
    print(area(radius))
    print(circumference(radius))

if __name__ == "__main__":
    main()