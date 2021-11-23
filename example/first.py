print('Insert Two Number ') ; 

firstNumber = input() ; 
secondNumber = input() ; 

big =  firstNumber > secondNumber ; 
less = firstNumber < secondNumber ; 
equal = firstNumber == secondNumber ; 
notEqual = firstNumber != secondNumber ; 
equalType = firstNumber is secondNumber ; 

   
print(f' First Number : {firstNumber} is " bigger than "  Second Number : {secondNumber}   ')if big == True else None ; 

print(f' First Number : {firstNumber} is " less than "  Second Number : {secondNumber}   ')if less == True else None ; 

print(f' First Number : {firstNumber} is " equal  "  Second Number : {secondNumber}   ')if equal == True else None ;

print(f' First Number : {firstNumber} is "  not Equal "  Second Number : {secondNumber}   ')if notEqual == True else None ;

print(f' First Number : {firstNumber} is " Value and Type "  Second Number : {secondNumber}   ')if equal == True else None ;