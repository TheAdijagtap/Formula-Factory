print("------square,Cube,Cone,Triangle------\n------circle,Sphere,Hemisphere,Cylinder------")
a = input("which area you want :")

pi = 3.12   #pie value

if 'hemisphere' in a:
    r5 =int(input("Enter Radius :"))
    rr5 = r5*r5
    hemiarea = 3*pi*rr5
    print("Area Of Hemisphere",hemiarea)
    
elif 'square' in a:
    side = int(input("Enter side :"))
    print("side is",side)
    area = side * side
    print("area is ",area)

elif 'circle' in a:
    r1 =int(input("Enter Radius :"))
    a1 = pi*r1*r1
    print("area of circle is",a1)

elif 'cube' in a:
    side1 = int(input("Enter side :"))
    cubea = 6*side1*side1
    print("Area of Cube is",cubea)

elif 'sphere' in a:
    r2 =int(input("Enter Radius :"))
    rr2 = r2*r2
    spherea = 4*pi*rr2
    print("Area of sphere is",spherea) 
    
elif 'cone' in a:
    r3 =int(input("Enter Radius :"))
    h1 =int(input("Enter Height :"))
    h2 =int(input("Enter Slant Height :"))
    hh = h1+h2
    conea = pi*r3*hh
    print("Area of Cone is",conea)
    
elif 'cylinder' in a:
    r4 =int(input("Enter Radius :"))
    h3 =int(input("Enter Height :"))
    rh = r4+h3
    cylindera = 2*pi*r4*rh
    print("Area of cylinder is",cylindera)
    
elif 'triangle' in a:
    b =int(input("Enter Base :"))
    h4 =int(input("Enter Height :"))
    triarea = 1/2*b*h4
    print("Area of Triangle is",triarea)
    
else:
    print("Formula did't found")
    exit()
    
    
    
    
    
    
    
    
    

    
    
    