#  Week1

### 5. basic console output

#### basic print function

```python
print("Carpe")
print("diem")
#这样打印出来的会换行
```



#### print on same line

```python
# 用逗号隔开不同值
print("Carpe", "diem")

# You can also use end="" to stay on the same line
print("Carpe ", end="")
print("diem")
```

python中平方:

```python
a**2 #平方
a**0.5 #开根
```



#### print using f strings

```python
x = 42
y = 99
# Place variable names in {squiggly braces} to print their values, like so:
# 把变量名放在花括号中来打印变量的值
print(f'Did you know that {x} + {y} is {x+y}?')
```



### 6. Importing module

***调用模块function之前一定要进行import***，否则会输出 *NameError: name 'math' is not defined*

```python
import math
print(math.factorial(20)) #factoral:阶乘
```



### 7. **More Logistics and Preliminaries**



### 8. Syntax, Runtime, Valid Errors

#### 1.Sytax Error (Compile time error)

it's not python

```python
print("Uh oh!)

# Python output:
# SyntaxError: EOL while scanning string literal
```

#### 2.Runtime Error ("Crash")

it is python, but youre doing it wrong

```python
print(1/0) # ERROR!  Division by zero!

# Python output:
# ZeroDivisionError: integer division or modulo by zero
```

#### 3.Logical Errors (Compiles and Runs, but is Wrong!)

```python
print("2+2=5") # ERROR!  Untrue!!!

# Python output:
# 2+2=5
```



### 9. Basic console input

#### input string

```python
name = input("Enter your name: ")
print("Your name is: ", name)
```



#### input a number

```python
x = input("Enter a number: ") #Error! 这样输入的是一个String
print("One half of", x, "=", x/2)
```

```python
x = int(input("Enter a number: ")) #用int()把输入的string转换成一个int
print("One half of", x, "=", x/2)
```



## Data Types and Operators

### 1. Some builtin types

```python
import math
def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type(2 < 2.2))     # bool (boolean)
print(type(type(42)))    # type

print("#####################################################")

print("And some other types we may see later in the course...")
print(type("2.2"))       # str (string or text)
print(type([1,2,3]))     # list
print(type((1,2,3)))     # tuple
print(type({1,2}))       # set
print(type({1:42}))      # dict (dictionary or map)
print(type(2+3j))        # complex  (complex number)
```



### 2. Some builtin constants

```python
print("Some builtin constants:")
print(True)
print(False)
print(None)

print("And some more constants in the math module:")
import math
print(math.pi)
print(math.e)
```



### 3. Some builtin operators 

| 类别 | 运算符                                      |
| ---- | ------------------------------------------- |
| 算术 | +, -, *, /, //, **, %, - (unary), + (unary) |
| 比较 | <, <=, >=, >, ==, !=                        |
| 赋值 | +=, -=, *=, /=, //=, **=, %=, <<=, >>=      |
| 逻辑 | and，or，not                                |

*Note: for now at least, we are not covering the bitwise operators (<<, >>, &, |, ^, ~, &=, |=, ^=).*

// ：向下取整除法，7//4 相当于math.floor(7/4)

**：次方

= ：赋值 

== ：判断是否相等，返回true/false



### 4. Integer division

```python
print("the / operateor does the normal float divisions:")
print(" 5/3 =",(5/3))
print("The // operator does integer division:")
print(" 5//3 =", ( 5//3))
print(" 2//3 =", ( 2//3))
print("-1//3 =", (-1//3))
print("-4//3 =", (-4//3))
```



### 5. The Modules or Remainder Operators

```python
print(" 6%3 =", ( 6%3))
print(" 5%3 =", ( 5%3))
print(" 2%3 =", ( 2%3))
print(" 0%3 =", ( 0%3)) #永远为0
print("-4%3 =", (-4%3)) #最大的、小于-4的、3的倍数与-4的距离
print(" 3%0 =", ( 3%0)) #error
```

a % b 相当于求出 最大的小于a的b的倍数与a的距离

因此，(a%b) 相当于 (a - a // b * b)



### 7. Types Affect Semantics

```python
print(3 * 2) # 6
print(3 * "abc") #abcabcabc
print(3 + 2)# 5
print("abc" + "def") #abcdef
print(3 + "def") #出现错误，3是整形，def是string不能相加
```



### 8. Precedence & Associativity

```python
print("Precedence:")
print(2+3*4)  # prints 14, not 20
print(5+4%3)  # prints  6, not 0 (% has same precedence as *, /, and //)
print(2**3*4) # prints 32, not 4096 (** has higher precedence than *, /, //, and %)

print()

print("Associativity:")
print(5-4-3)   # prints -2, not 4 (- associates left-to-right)
print(4**3**2) # prints 262144, not 4096 (** associates right-to-left)
```



### 9. Aproximate Values of Float

```python
x = 0.1 + 0.1 + 0.1
y = 0.3

def almostEqual(x, y): #并非python自带的功能，需要自己定义
  epsilon = 10**-8 #一个极小值，用于判定大约等于
  return(abs(x - y) < epsilon)

almostEqual(x, y)
```



### 10. Short circuit Evaluation 短路判定

可以用于条件判定, False与任何东西相与都得 False

and 或者 or 都可以

```python
def yes():
  return True

def no():
  return False

print(yes() and no()) #False
print(no() and no()) #False
print(yes() and yes()) #True
```

```python
if ((i >= 0) and (i < len(s)) #判断i的合法性
   and (s[i]=="Q")) #合法情况下的判定
```



### 11. type vs isinstance

两者都用于确认类型

isinstance(x, T) 会比 (type(x) == T) 更高效

```python
print(type("abc") == str) #True
print(isinstance("abc", str)) #True
```

例如，想查看某个值是不是某个类型

```python
def isNumber(x):
  return ((type(x) == int) or
           type(x) == float) #这里并未包含所有数字类型，仅做演示用

print(isNumber(1), isNumber(1.1), isNumber("wow"), isNumber(1+2j))
```

```python
import numbers
def isNumber(x):
  return isinstance(x, numbers.Number) #明显比type方法简洁高效

print(isNumber(1), isNumber(1.1), isNumber("wow"), isNumber(1+2j))
```



## Variables and Functions

### 1.Variables

a named value that **<u>references or stores</u>** a piece of data

```python
#put a value in a variable using a = sign
x = 5
print(x)
print(x*2)
```

variables can have new values assigned to them, **even values of different types**

```python
y = 10
print(y - 2)

y = True
print(y)
```

Variables can be given any name, as long as it **starts with a letter and contains no special characters**.

Variables can be updated with assignment operations.

```python
x = 5;
x += 2 #same as x = x + 2
print(x) #should be 7

# This can be done with any of the arithmetic operations.
y = 350
y //= 10
print(y) # should be 35
```



### 2.Statements and Expressions

An expression is a ***data value*** or an ***operation*** that evaluates to a value.

```python
# Examples of expressions.
# Note that when this is run in the editor, none of these values are displayed.
4
"Hello World"
7 + 2
True or False
(2 < 3) and (9 > 0)
```

A statement is a line of code that ***performs an action***. Unlike expressions, statements <u>cannot be used</u> in operations.

```python
# Examples of statements.
print(4)
x = True
```

### 3.Functions

A function is a procedure (a sequence of statements) stored under a name that can be used repeatedly by calling the name. 

```python
# A function is composed of two parts: the header and the body.

# The header defines the name and parameters.
# A function header is written as follows: def functionName(parameters):
# The parameters are variables that will be provided when the function is called.
# The header ends with a colon to indicate that a body will follow.

# The body contains the actions (statements) that the function performs.
# The body is written under the function with an indent.
# When the lines are no longer indented, the function body ends.
# Functions usually contain a return statement. This will provide the result when the function is called.

# Example:

def double(x):
    print("I'm in the double function!")
    return 2 * x

# To call the function, we use the function's name,
# followed by parentheses which contain the data values we want to use, called function arguments.
# This function call will evaluate to an expression.

print(double(2)) # will print 4
print(double(5)) # will print 10
print(double(1) + 3) # will print 5
```

Functions can have as many parameters as they need, or none at all.

```python
def f(x, y, z):
    return x + y + z

print(f(1, 3, 2)) # returns 6

def g():
    return 42

print(g()) # returns 42

# Note - the number of arguments provided must match the number of parameters!
print(g(2)) # will crash
print(f(1, 2)) # would also crash if it ran
```

### 4.Builtin fcuntions

```python
# Some functions are already provided by Python

print("Type conversion functions:")
print(bool(0))   # convert to boolean (True or False)
print(float(42)) # convert to a floating point number
print(int(2.8))  # convert to an integer (int)

print("And some basic math functions:")
print(abs(-5))   # absolute value
print(max(2,3))  # return the max value
print(min(2,3))  # return the min value
print(pow(2,3))  # raise to the given power (pow(x,y) == x**y)
print(round(2.354, 1)) # round with the given number of digits
```

### 5.Module Functions

Python has many different functions already implemented, but not available immediately. To use these functions, you must import a module. You can find these modules by reading the [Python documentation online](https://docs.python.org/3/).

Call with importing

```python
import math
print(math.factorial(20)) #阶乘

#note that module name is included before function name, seperated with a .
```

### 6.Variable scope

Variables exist in a specific scope based on when they are defined. This means they are not visible and ***cannot be used outside that scope***, in other parts of the code.

Variables in functions have a local scope. They exist only inside the immediate function, and have no relation to variables of the same name in different functions.

when define outside of function, variables have a global scope and can be used anywhere

```python
# In general, you should avoid using global variables.
# You will even lose style points if you use them!
# Still, you need to understand how they work, since others
# will use them, and there may also be some very few occasions
# where you should use them, too!

g = 100

def f(x):
    return x + g

print(f(5)) # 105
print(f(6)) # 106
print(g)    # 100

# Another example

def f(x):
    # If we modify a global variable, we must declare it as global.
    # Otherwise, Python will assume it is a local variable.
    global g
    g += 1
    return x + g

print(f(5)) # 106
print(f(6)) # 108
print(g)    # 102
```

### 7.return statement

Basic example:

```python
def isPositive:
  return (x > 0)

print(isPositive(5))
```

Return ends the function immediately 

No return statement --> return "None"

### 8.Print VS Return

**functions should not have print inside, use return at the end instead.**

```python
def cubed(x):
    print(x**3) # Here is the error!

cubed(2)          # seems to work!
print(cubed(3))   # sort of works (but prints None, which is weird)
print(2*cubed(4)) # Error!
```

### 9. Function Composition

嵌套方程由里到外执行

### 10.Helper function

```python
# We commonly write functions to solve problems.
# We can also write functions to store an action that is used multiple times!
# These are called helper functions.

def onesDigit(n):
    return n%10

def largerOnesDigit(x, y):
    return max(onesDigit(x), onesDigit(y))

print(largerOnesDigit(134, 672)) # 4
print(largerOnesDigit(132, 674)) # Still 4
```

### 11.Recommand Function

```python
# There are a few functions from modules you'll definitely want to use in the assignments

# First: the built-in round function has confusing behavior when rounding 0.5.
# Use our function roundHalfUp to fix this.

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    # You do not need to understand how this function works.
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

print(round(0.5)) # This evaluates to 0 - what!
print(round(1.5)) # And this will be 2 - so confusing!
print(roundHalfUp(0.5)) # Now this will always round 0.5 up (to 1)
print(roundHalfUp(1.5)) # This still rounds up too!

# Second: when comparing floats, == doesn't work quite right.
# Use almostEqual to compare floats instead

print(0.1 + 0.1 == 0.2) # True, but...
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2) # False!
print(d1)       # prints 0.30000000000000004 (uh oh)
print(d1 - d2)  # prints 5.55111512313e-17 (tiny, but non-zero!)
# Moral: never use == with floats!

# Python includes a builtin function math.isclose(), but that function
# has some confusing behavior when comparing values close to 0.
# Instead, let's just make our own version of isclose:

def almostEqual(x, y):
    return abs(x - y) < 10**-9

# This will now work properly!
print(almostEqual(0, 0.0000000000001))
print(almostEqual(d1, d2))
```

### 12.Test Fcuntions

Builtin function of python: assert(*expression*), if expression is true do nothing, if false -->crash



## Conditionals

### 1. if statement

```python
def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    print("D")

f(0)
f(1)
```

**A more interesting example:**

```python
# These examples define abs(n), which is a nice example here, but it is
# also a builtin function, so you do not need to define it to use it.

def abs1(n):
    if (n < 0):
        n = -n
    return n

# again, with same-line indenting

def abs2(n):
    if (n < 0): n = -n # only indent this way for very short lines (if at all)
    return n

# again, with multiple return statements

def abs3(n):
    if (n < 0):
        return -n
    return n

# aside: you can do this with boolean arithmetic, but don't!

def abs4(n):
    return (n < 0)*(-n) + (n>=0)*(n) # this is awful!

# now show that they all work properly:

print("abs1(5) =", abs1(5), "and abs1(-5) =", abs1(-5))
print("abs2(5) =", abs2(5), "and abs2(-5) =", abs2(-5))
print("abs3(5) =", abs3(5), "and abs3(-5) =", abs3(-5))
print("abs4(5) =", abs4(5), "and abs4(-5) =", abs4(-5))
```

### 2.if-else statement

```python
def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    else:
        print("D", end="")
        if (x == 1):
            print("E", end="")
        else:
            print("F", end="")
    print("G")

f(0)
f(1)
f(2)
```

**Revisiting abs(n):**

```python
def abs5(n):
    if (n >= 0):
        return n
    else:
        return -n

# or, if you prefer...

def abs6(n):
    if (n >= 0):
        sign = +1
    else:
        sign = -1
    return sign * n

print("abs5(5) =", abs5(5), "and abs5(-5) =", abs5(-5))
print("abs6(5) =", abs6(5), "and abs6(-5) =", abs6(-5))
```

### 3. If-elif-else statement

```python
def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    elif (x == 1):
        print("D", end="")
    else:
        print("E", end="")
        if (x == 2):
            print("F", end="")
        else:
            print("G", end="")
    print("H")

f(0)
f(1)
f(2)
f(3)
```

A more interesting example:

```python
def numberOfRoots(a, b, c):
    # Returns number of roots (zeros) of y = a*x**2 + b*x + c
    d = b**2 - 4*a*c
    if (d > 0):
        return 2
    elif (d == 0):
        return 1
    else:
        return 0

print("y = 4*x**2 + 5*x + 1 has", numberOfRoots(4,5,1), "root(s).")
print("y = 4*x**2 + 4*x + 1 has", numberOfRoots(4,4,1), "root(s).")
print("y = 4*x**2 + 3*x + 1 has", numberOfRoots(4,3,1), "root(s).")
```

**Another example:** there can be multiple ***elif***

```python
def getGrade(score):
    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    else:
        grade = "F"
    return grade

print("103 -->", getGrade(103))
print(" 88 -->", getGrade(88))
print(" 70 -->", getGrade(70))
print(" 61 -->", getGrade(61))
print(" 22 -->", getGrade(22))
```

### 4. If-else expression

```python
#not a statement!!!

def abs7(n):
  return n if (n >= 0) else -n
#注意if的body在前了

#这样代码可读性会大大降低，简单的语句可以这样写
#复杂的要尽量避免！！
```

# Week 2 

## Loops

### 1. for loops and range

```python
# A for loop repeats an action a specific number of times
# based on the provided range
def sumFromMToN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):
        total += x
    return total

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)
```

Actually we don't need a loop

```python
def sumFromMToN(m, n):
    return sum(range(m, n+1))

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# And we can even do this with a closed-form formula,
# which is the fastest way, but which doesn't really
# help us demonstrate loops.  :-)

def sumToN(n):
    # helper function
    return n*(n+1)//2

def sumFromMToN_byFormula(m, n):
    return (sumToN(n) - sumToN(m-1))

print(sumFromMToN_byFormula(5, 10) == 5+6+7+8+9+10)
```

若不指定，Range 的默认起始数为0

```python
def sumToN(n):
    total = 0
    # range defaults the starting number to 0
    for x in range(n+1):
        total += x
    return total

print(sumToN(5) == 0+1+2+3+4+5)
```

**What if we add a third parameter?**

```python
def sumEveryKthFromMToN(m, n, k):# n is not included in the loop
    total = 0
    # the third parameter becomes a step
    for x in range(m, n+1, k):
        total += x
    return total

print(sumEveryKthFromMToN(5, 20, 7) == (5 + 12 + 19))
```

Backwards 

```python
# Here we will range in reverse
# (not wise in this case, but instructional)
def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(n, m-1, -1):
        if (x % 2 == 1):
            total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))
```



### 2.Nested for loops

```python
# We can put loops inside of loops to repeat actions at multiple levels
# This prints the coordinates
def printCoordinates(xMax, yMax):
    for x in range(xMax+1):
        for y in range(yMax+1):
            print("(", x, ",", y, ")  ", end="")
        print()

printCoordinates(4, 5)
```

Print stars

```python
def printStarRectangle(n):
    # print an nxn rectangle of asterisks
    for row in range(n):
        for col in range(n):
            print("*", end="")
        print()

printStarRectangle(5)
```

```python
# What would this do? Be careful and be precise!

def printMysteryStarShape(n):
    for row in range(n):
        print(row, end=" ")
        for col in range(row):
            print("*", end=" ")
        print()

printMysteryStarShape(5)
```

### 3.while loops

在***不确定循环次数***时大多使用while循环

```python
def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n//10
    return n

print(leftmostDigit(72658489290098) == 7)
```

**Example: nth non-negative integer with some property**

```python
# eg: find the nth number that is a multiple of either 4 or 7
def isMultipleOf4or7(x):
    return ((x % 4) == 0) or ((x % 7) == 0)

def nthMultipleOf4or7(n):
    found = 0
    guess = -1
    while (found <= n):
        guess += 1
        if (isMultipleOf4or7(guess)):
            found += 1
    return guess

print("Multiples of 4 or 7: ", end="")
for n in range(15):
    print(nthMultipleOf4or7(n), end=" ")
print()
```

**Misuse: While loop over a fixed range**

```python
# sum numbers from 1 to 10
# note:  this works, but you should not use "while" here.
#        instead, do this with "for" (once you know how)
def sumToN(n):
    # note: even though this works, it is bad style.
    # You should do this with a "for" loop, not a "while" loop.
    total = 0
    counter = 1
    while (counter <= n):
        total += counter
        counter += 1
    return total

print(sumToN(5) == 1+2+3+4+5)
```

### 4.**break and continue**

```python
# continue, break, and pass are three keywords used in loops
# in order to change the program flow
for n in range(200):
    if (n % 3 == 0):
        continue # 跳过本次循环
    elif (n == 8):
        break # 跳出循环
    else:
        pass # does nothing! pass is a placeholder, not needed here
    print(n, end=" ")
print()
```

Infinite "while" loop with break

```python
# Note- this is advanced content, as it uses strings. It's okay
# to not fully understand the content below.
def readUntilDone():
    linesEntered = 0
    while (True):
        response = input("Enter a string (or 'done' to quit): ")
        if (response == "done"):
            break
        print("  You entered: ", response)
        linesEntered += 1
    print("Bye!")
    return linesEntered

linesEntered = readUntilDone()
print("You entered", linesEntered, "lines (not counting 'done').")
```



### 5.isPrime

```python
# Note: there are faster/better ways.  We're just going for clarity and simplicity here.
def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True

# And take it for a spin
for n in range(100):
    if isPrime(n):
        print(n, end=" ")
print()
```

fasterPrime:

```python
# Note: this is still not the fastest way, but it's a nice improvement.
def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

# And try out this version:
for n in range(100):
    if fasterIsPrime(n):
        print(n, end=" ")
print()
```

**Verify fasterIsPrime is faster:**

```python
def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True

def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

# Verify these are the same
for n in range(100):
    assert(isPrime(n) == fasterIsPrime(n))
print("They seem to work the same!")

# Now let's see if we really sped things up
import time
bigPrime = 499 # Try 1010809, or 10101023, or 102030407
print("Timing isPrime(",bigPrime,")", end=" ")
time0 = time.time()
print(", returns ", isPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ",(time1-time0)*1000,"ms")

print("Timing fasterIsPrime(",bigPrime,")", end=" ")
time0 = time.time()
print(", returns ", fasterIsPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ",(time1-time0)*1000,"ms")
```



### 6.nthPrime

```python
def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

# Adapt the "nth" pattern we used above in nthMultipleOf4or7()

def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isPrime(guess)):
            found += 1
    return guess

# and let's see a list of the primes
for n in range(10):
    print(n, nthPrime(n))
print("Done!")
```



## Debug

### Print Statement Debugging

```python
# THIS CODE STILL HAS A BUG (ON PURPOSE)!!!!

# When you run it, it will hang (run forever)!!!!

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        print(guess, found) ### <--- THIS is our well-placed print statement!
        guess += 1
        if (isPrime(guess)):
            found + 1
    return guess

print('The next line will hang (run forever):')
print(nthPrime(5))
```

### Even Better

Print statement debugging with locals() + input()

```python
# THIS CODE STILL HAS A BUG (ON PURPOSE)!!!!

# When you run it, it will hang (run forever)!!!!

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        print(locals()) ### <--- THIS is our well-placed print statement!
        input()         ### <--- THIS pauses until we hit Enter. Sweet!
        guess += 1
        if (isPrime(guess)):
            found + 1
    return guess

print('The next line will hang (run forever):')
print(nthPrime(5))
```

Locals():Update and return a dictionary representing the current local symbol table. Free variables are returned by [`locals()`](dfile:///Users/owenxu/Library/Application Support/Dash/DocSets/Python_3/Python 3.docset/Contents/Resources/Documents/doc/library/functions.html#locals) when it is called in function blocks, but not in class blocks. Note that at the module level, [`locals()`](dfile:///Users/owenxu/Library/Application Support/Dash/DocSets/Python_3/Python 3.docset/Contents/Resources/Documents/doc/library/functions.html#locals) and [`globals()`](dfile:///Users/owenxu/Library/Application Support/Dash/DocSets/Python_3/Python 3.docset/Contents/Resources/Documents/doc/library/functions.html#globals) are the same dictionary.

## Code Tracing

## Homework

```python
#these are the same!
temp = x
x = y
y = temp % y

x,y = y, x%y 
```

# Week 3

Strings, grapics

## String Literals

### 1. Four kinds of quotes

```python
# Quotes enclose characters to tell Python "this is a string!"
# single-quoted or double-quoted strings are the most common
print('single-quotes')
print("double-quotes")

# triple-quoted strings are less common (though see next section for a typical use)
print('''triple single-quotes''')
print("""triple double-quotes""")

# The reason we have multiple kinds of quotes is partly so we can have strings like:
print('The professor said "No laptops in class!" I miss my laptop.')
```

### 2. New lines in string

```python
# A character preceded by a backslash, like \n, is an 'escape sequence'.
# Even though it looks like two characters, Python treats it as one special character.

# Note that these two print statements do the same thing!
print("abc\ndef")  # \n is a single newline character.
print("""abc
def""")

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")
```

### 3. More escape sequence

```python
print("Double-quote: \"")
print("Backslash: \\")
print("Newline (in brackets): [\n]")
print("Tab (in brackets): [\t]")

print("These items are tab-delimited, 3-per-line:")
print("abc\tdef\tg\nhi\tj\\\tk\n---")
```



