def paragogos(sinartisi, metavliti,taxi):
    from sympy import diff, sin, exp, cos, tan, log, Mod, Integer
    global paragogos
    paragogos = diff(sinartisi,metavliti,taxi)
    
                
            


import os    
os.system('cls') 
print('')
print('______________________________________________________________________________________')
print('')
print('  Agricultural University of Athens')
print('  School of Applied Economics & Social Sciences')
print('  Department Of Agricultural Economics & Rural Development')
print('  Stefanos Stavrianos, UGRD')
print('  stefanos.stavrianos@outlook.com')
print('  +30 698 595 5584')
print('______________________________________________________________________________________')
print('')
print('                  __________________________________________________')
print('                 |                                                  |')
print('                 |      P A R T I A L  D E R I V A T I V E          |')
print('                 |__________________________________________________|')  
print('')    
sinartisi = input('\n > Function       -> y(x) = ')
while True:
    if sinartisi == '':
        os.system('cls') 
        print('')
        print('______________________________________________________________________________________')
        print('')
        print('  Agricultural University of Athens')
        print('  School of Applied Economics & Social Sciences')
        print('  Department Of Agricultural Economics & Rural Development')
        print('  Stefanos Stavrianos, UGRD')
        print('  stefanos.stavrianos@outlook.com')
        print('  +30 698 595 5584')
        print('______________________________________________________________________________________')
        print('')
        print('                  _______________________________________________')
        print('                 |                                               |')
        print('                 |      P A R T I A L  D E R I V A T I V E       |')
        print('                 |_______________________________________________|')  
        print('') 
        print('\nError')
        sinartisi = input('\n > Function       -> y(x) = ')
    else:
        break
        
metavliti = input('\n > Respect to     -> ')
while True:
    if metavliti == '':
        print('\nError')
        metavliti = input('\n > Respect to     -> ')
    else:
        break
        
taxi = input('\n > Principles of  -> ')
while True:
    if taxi == '':
        print('\nError')
        taxi = input('\n > Principles of -> ')
    else:
        break
        
paragogos(sinartisi, metavliti,taxi)
print('')
print('')
print('----------------------------------------------------------------------------------------')
print('')
if taxi == '1':
    print('The 1st partial derivative of','f(x) = '+sinartisi,'with respect to',metavliti,'is',paragogos)
elif taxi == '2':
    print('The 2nd partial derivative of','f(x) = '+sinartisi,'with respect to',metavliti,'is',paragogos)
elif taxi =='3':
    print('The 3rd partial derivative of','f(x) = '+sinartisi,'with respect to',metavliti,'is',paragogos)
else:
    print('The',taxi+'th partial derivative of','f(x) ='+sinartisi,'with respect to',metavliti,'is',paragogos)
print('\n----------------------------------------------------------------------------------------')

