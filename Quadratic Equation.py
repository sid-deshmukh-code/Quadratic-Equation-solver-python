import cmath
inp = str.lower(input("""
Make = To make Quadratic equation from 'α' and 'β'
Solve = To solve Quadratic equation from 'a' , 'b' and 'c'
What do you want to do here: """))
if inp =='make':
    try:
        alpha = int(input("Enter the value of 'α': "))
        beta = int(input("Enter the value of 'β': "))
        g = alpha + beta
        h = alpha * beta
        print(f"Quadratic equation is 'x^2-{g}x+{h}'  ")
        dis0 = g * g - (4 * 1 * h)
        if dis0 > 0:
            print("Roots will be real and unequal.")
        elif dis0 == 0:
            print("Roots will be real and unequal ")
        else:
            print("Roots will be imaginary.")

    except ValueError:
        print("Please enter valid input!")
elif inp == 'solve':
   try:
       print("""
                    1}In final answer 'j' is a unit so do not get confused OK!
                    2}This works on those problems which can solved by formula method!
                                                 GO & ENJOY ! 
                 """)
       a = int(input("Enter the value of A: "))
       b = int(input("Enter the value of B: "))
       c = int(input("Enter the value of C: "))
       dis = b * b - (4 * a * c)
       print(f" This is Discriminant: {dis}")
       ans1 = (-b + cmath.sqrt(dis)) / (2 * a)
       ans2 = (-b - cmath.sqrt(dis)) / (2 * a)
       print(f"The roots of the equation is {ans1} or {ans2}")
       if dis > 0:
           print("Roots are real and unequal.")
       elif dis == 0:
           print("Roots are real and unequal ")
       else:
           print("Roots are imaginary.")
   except ValueError:
       print("qwerty")


else:
    print("Please give valid input!")
