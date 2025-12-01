from cirArea import *

def area_rec(length,breadth):
    return f"The area of the rectangle with length {length} and breadth {breadth} is {length*breadth} cm²"

def perimeter(length,breadth):
    return f"The perimeter of the rectangle with length {length} and breadth {breadth} is {2* (length + breadth)} cm"

def main():
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the rectangle: "))
    print(area_rec(length,breadth))
    print(perimeter(length,breadth))
    radius = float(input("Enter the radius of the circle: "))
    print(area(radius))
    print(circumference(radius))

if __name__ == "__main__":
    main()
