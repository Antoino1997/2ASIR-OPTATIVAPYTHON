# AUTOMATE THE BORING STUFF WITH PYTHON

## CHAPTER 1
Ejercicio | Descripción
----------|------------
[Ejercicio1](rectPrint.py) | Write a program that prints a rectangle of capital O characters. The program should always print a rectangle of O characters that has a height of five (that is, five rows), but the width should be based on an integer the user enters.
[Ejercicio2](perimeterAreaCalculator.py) | Write a program that accepts the width and length of a rectangular space from the user and then calculates both the perimeter and area of this space.

## CHAPTER 2
Ejercicio | Descripción
----------|------------
[Ejercicio1](safeTemp.py) | The following program reports whether a given temperature is safe. It asks the user to enter a temperature in two parts. First, they should enter C or F to indicate the Celsius or Fahrenheit scale; second, they should enter the number of degrees. If the temperature is between 16 and 38 degrees Celsius (inclusive of 16 and 38) or between 60.8 and 100.4 degrees Fahrenheit (inclusive of 60.8 and 100.4), the program prints Safe. Outside of these temperature ranges, the program prints Dangerous. This program has bugs, however. Rewrite the code to fix the errors. You may assume the user always enters valid inputs and not, say, X for the scale or hello for the number of degrees.
[Ejercicio2](safeTempExpr.py) | It’s possible to write the safe temperature logic of the previous program in a single condition. Fill in the blank in the following program with this condition to make it work in the same way as the previous program.
[Ejercicio3](fizzBuzzNumber.py) | Fizz Buzz is a common programming challenge that goes like this. Write a program that accepts an integer from the user. If the integer is divisible by 3, the program should print Fizz. If the integer is divisible by 5, the program should print Buzz. If the integer is divisible by 3 and 5, the program should print Fizz Buzz. Otherwise, the program should print the number the user entered.

## CHAPTER 3
Ejercicio | Descripción
----------|------------
[Ejercicio1](treePrint.py) | Use a for loop to print a triangular pine tree of a size the user asks for. The tree branches should be printed as a number of rows of ^ characters, while the trunk should always be two # characters. As a second exercise, write this same program using while loops instead of for loops.
[Ejercicio2](xmasTreePrint.py) | Instead of creating a plain tree like the one in the previous project, write a program that prints a Christmas tree with o ball ornaments randomly replacing ^ branch characters. As a second exercise, write this same program using while loops instead of for loops.

## CHAPTER 4
Ejercicio | Descripción
----------|------------
[Ejercicio1](transactionTracker.py) | Write a function named after_transaction() that returns the amount of money in an account after a transaction. The two parameters for this function are balance and transaction. They will both have integer arguments. The balance is how much money is currently in the account, and the transaction is how much to add or remove from the account (based on whether transaction is a positive or negative integer). This operation is more complicated than just return balance + transaction. If the transaction is negative and would overdraw the account (that is, if balance + transaction is less than zero), then the transaction should be ignored and the original balance returned. 
[Ejercicio2](arithmeticFunctions.py) | Let’s create add(number1, number2) and multiply(number1, number2) functions that add and multiply their arguments without using the + or * operators. These functions will be quite inefficient, but don’t worry; the computer doesn’t mind. Your add() function should not use the + operator; rather, it should have loops that repeatedly call the plus_one() function to perform the addition operation on the operands passed as parameters. After all, the operation 4 + 3 is the same as 4 + 1 + 1 + 1. Your add() function is expected to handle positive integers only. Your multiply() function should work in the same way: Avoid using the * operator, and instead use a loop to repeatedly call your add() function. After all, the operation 3 * 5 is the same as 3 + 3 + 3 + 3 + 3 or 5 + 5 + 5. It’s a good idea to make sure your add() function works before beginning on multiply(). Also note that 2 + 8 is the same as 8 + 2 and 2 * 8 is the same as 8 * 2.
[Ejercicio3](tickTockPrint.py) | The time.sleep() function, which pauses program execution for a specified amount of time, is useful, but rather plain. Let’s write our own tick_tock(seconds) function that also pauses for seconds amount of time but prints Tick... and Tock... each second while waiting. You may assume that the seconds parameter always has a positive integer argument. Keep in mind that if the argument for seconds is odd, the last thing the function should print is Tick...
