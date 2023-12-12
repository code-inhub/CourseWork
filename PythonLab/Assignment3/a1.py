import Module

shape=input("Enter the shape-")

if shape=="circle":
    radius=float(input("Enter Radius-"))
    area=Module.circ_area(radius)
    print(f"area is- {area}")

elif shape=="rectangle":
    length=float(input("Enter length-"))
    breadth=float(input("Enter breadth-"))
    area=Module.rect_area(length,breadth)
    print(f"area is- {area}")
    
elif shape=="square":
    side=float(input("Enter Side-"))
    area=Module.squa_area.calc_area
    print(f"area is- {area}")