import math as m
# m. commands refer to math module


squareLoop = True
fractionLoop = True

while squareLoop and fractionLoop == True:

        # make sure equation is in standard form
        a = int(input('Enter x^2 Value: > '))
        b = int(input('Enter x Value: > '))
        c = int(input('Enter constant Value: > '))

        numerator = (-1 * b)
        denominator = (2 * a)

        squareRootEquation = int( m.pow( b, 2 ) - ( 4 * a * c ) )
        print(squareRootEquation)

        # accounting for imaginary numbers
        if squareRootEquation < 0:
                squareRootEquation *= -1
                squareRootSolution = f'''/sqrt {squareRootEquation}i'''
                squareLoop = False
        
        elif squareRootEquation > 0:
            try:
                squareRootSolution = m.sqrt(squareRootEquation)
            except ValueError:
                continue

             


        else:
            squareRootSolution = {int(m.sqrt(squareRootEquation))}
            squareLoop = False

        if denominator and numerator % 2 == 0:
            simplifiedFraction = m.fmod(numerator, denominator)


            if denominator or numerator == 0 or simplifiedFraction % 2 != 0:
                fractionSimplified = True
                fractionLoop = False
            
            else:
                fractionSimplified = False
                fractionLoop = False

            

                
        
        
        


               


print('test, first is numerator, second is denominator', numerator, denominator)

print(f'''

{numerator} +- {squareRootSolution}
------
{denominator}
''')


        
                 
        

        
               
               
        


        

        

        
        

        
        
    
                