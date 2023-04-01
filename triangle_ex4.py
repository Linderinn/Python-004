import math  
op = "y" 
while op != "n": 
    data = input("Give 3 sides of the triangle (separated by commas ,): ")

    lista = []  
    for x in data.split(","):
        lista.append(int(x))
    a, b, c = lista  

    print("Podano boki: ", a, b, c)

    if a + b > c and a + c > b and b + c > a:  
        print("You can build a triangle with the given sides.")
       
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Also rectangular!")

        
        print("The circumference is:", (a + b + c))
        p = 0.5 * (a + b + c)  
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("The area of the triangle is:", P)
        op = "n"  # ustawiamy zmienną na "n", aby wyjść z pętli while
    else:
        print("The given segments cannot form a right triangle.")
        op = input("You will try again (y/n): ")

print("See you soon...")
