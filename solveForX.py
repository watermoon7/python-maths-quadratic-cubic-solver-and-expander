'''
Created on 29 Jun 2022

@author: coding
'''

def SolveForX():
    
    def condense(text):
        temp = ''
        a = text.split('x')
    
        for i in a:
            if i[-1] == '1':
                temp += str(i[:-1])+'x'
            else:
                temp += str(i)+'x'     
        temp = temp[:-1]
        
        a = temp.split('-')
        temp = ''
        for i in a:
            try:
                if i[-2:] == '+ ':
                    temp += str(i[:-2])+'- '
                else:
                    temp += str(i)+'-'
            except:
                temp += str(i)
        temp = temp[:-1]
                
        return temp
        
        
    def removeDoubles(data):
        return list(map(list, set(map(tuple, list(data)))))
         
    def factorPairs(num):
        factors=[]
        for i in range(1, num+1):
            if num%i==0:
                factors.append(sorted([i, int(num/i)]))
                factors.append(sorted([-i, -int(num/i)]))
                   
        return removeDoubles(factors)
                
    def factorTrios(num):
        factors=[]
        for i in range(1,num+1):
            if num%i==0:
                for o in factorPairs(int(num/i)):
                    factors.append(sorted([i, o[0], o[1]]))
            
        return removeDoubles(factors)
    
    def quadratic():
        print('ax² + bx + c')
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))
        factorsA = factorPairs(a)
        factorsC = factorPairs(c)
        
        found = False
        for i in factorsA:
            for o in factorsC: 
                if i[0]*o[1] + i[1]*o[0] == b:
                    print(condense(f'({i[0]}x + {o[0]})({i[1]}x + {o[1]})'))
                    found = True
        if not found:
            print('No factors')
    
    def cubic():
        print('ax³ + bx² + cx + d')
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))
        d = int(input('d = '))
       
        factorsA = factorTrios(a)
        factorsB = factorTrios(b)
        factorsC = factorTrios(c)
        factorsD = factorTrios(d)
        
        found = False
        for i in factorsA:
            for o in factorsD: 
                if o[0]*i[1]*i[2] + i[0]*o[1]*i[2] + i[0]*i[1]*o[2] == b and o[0]*o[1]*i[2] + o[0]*i[1]*o[2] + i[0]*o[1]*o[2] == c:
                    print(condense(f'({i[0]}x + {o[0]})({i[1]}x + {o[1]})({i[2]}x + {o[2]})'))
                    found = True
        if not found:
            print('No factors')
        
    print('Which Equation')
    print('1. ax² + bx + c')
    print('2. ax³ + bx² + cx + d')
    
    ans = int(input())
    
    if ans == 1:
        quadratic()
    elif ans == 2:
        cubic()
    
def Expand():
    
    def condense(text):
        a = text.split('^')
        final = a[0]
        for i in range(1, len(a)):
            if int(a[i][0]) < 2:
                a[i] = a[i][1:]
                final += a[i]
            else:
                final += '^' + a[i]
        final = final[:-1]
        
        a = final.split('-')
        final = ''
        print(a)
        for i in range(0, len(a)-1):
            final += a[i][:-1] + '-'
        final += a[-1]
        return final
            
                
    def multiplyBrackets(b1, b2):
        mygrid = []
        for i in range(0, len(b1)): 
            mygrid.append([])
        for i in range(0, len(b1)): 
            for o in range(0, len(b2)):
                mygrid[i].append(b1[i]*b2[o])
                
        
        coefficients = len(b1) + len(b2) - 1
        final = []
        for i in range(0, coefficients):
            final.append([])
        
        for i in range(0, coefficients):
            temp = 0
            for o in range(0, len(mygrid)):
                try:
                    if not i-o < 0:
                        temp += mygrid[o][i-o]
                except:
                    pass
            final[i] = temp
     
        return final
    
    equation = []
    brackets = int(input('How many sets of brackets'))
    for i in range(0, brackets):
        print(f'Bracket {i+1}: ')
        print('(ax + b)')
        a = int(input('a = '))
        b = int(input('b = '))
        equation.append([a, b])
    
    main = equation[0]
    for i in range(0, brackets-1):
        main = multiplyBrackets(main, equation[i+1])
    
    text = ''
    power = len(main)-1
    for i in range(0, len(main)):
        text += f'{main[i]}x^{power}'
        text += '+'
        power -= 1
        
    text = text[:-1]
    print(text)
    
    text = condense(text)
    print(text)
    
def main():
    while True:
        functions = {
            1: SolveForX,
            2: Expand
            }
        
        print('Which Calculator')
        print('1: Solve for X')
        print('2: Expand and Simplify')
        
        ans = int(input())
            
        functions[ans]()
    
if __name__ == '__main__':
    main()
