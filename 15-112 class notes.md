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

# Week 2: Loops

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

# Week 3: String & Graphic

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

### 4.repr() vs. print()

有时候字符串很难debug，两个相似的字符串很有可能实现代码是不一样的。

repr()相当于print的正式形式，向我们展示串中的数据

Print()比较偏向于产生一个输出

这点不同在debug的时候很有用

```python
print("These look the same when we print them!")
s1="abc\tdef"
s2="abc  def"

print("print s1: ",s1)
print("print s2: ",s2)

print("\nThey aren't really though...")
print("s1==s2?", s1==s2)

print("\nLet's try repr instead")
print("repr s1: ",repr(s1))
print("repr s2: ",repr(s2))

print("\nHere's a sneaky one")
s1="abcdef"
s2="abcdef             \t"

print("print s1: ",s1)
print("print s2: ",s2)

print("s1==s2?", s1==s2)

print("repr s1: ",repr(s1))
print("repr s2: ",repr(s2))
print("repr() lets you see the spaces^^^")
```

### 5. String Literals as Multi-line comments

```python
"""
python中没有多行注释符号，但是可以用顶级多行串的定义形式来做注释。技术上来说python这不是一块注释，在python运行的时候这条串会被读取随后被忽略然后进行垃圾回收

Python does not have multiline comments, but you can do something similar
by using a top-level multiline string, such as this. Technically, this is
not a comment, and Python will evaluate this string, but then ignore it
and garbage collect it!
"""
print("Wow!")
```

## Some string constants

```python
import string
print(string.ascii_letters)   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print("-----------")
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)          # 0123456789
print("-----------")
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.printable)       # digits + letters + punctuation + whitespace
print("-----------")
print(string.whitespace)      # space + tab + linefeed + return + ...
```

## Some String Operators

### 1. Sting + and *

```python
print("abc" + "def")  # What do you think this should do?
print("abc" * 3)  # How many characters do you think this prints?
print("abc" + 3)  # ...will this give us an error? (Yes)
```

### 2. The in operator

in 可以判断后串是否包含前串

```python
# The "in" operator is really really useful!
print("ring" in "strings")
print("wow" in "amazing!")
print("Yes" in "yes!")
print("" in "No way!")
```

## String indexing and slicing

#### 1. Indexing a single character

```python
# Indexing lets us find a character at a specific location (the index)
s = "abcdefgh"
print(s)
print(s[0])
print(s[1])
print(s[2])

print("-----------")
print("Length of ",s,"is",len(s))

print("-----------")
print(s[len(s)-1])
print(s[len(s)])  # crashes (string index out of range)
```

#### 2. Negative indexes

```python
s = "abcdefgh"
print(s)
print(s[-1]) #倒数第一个
print(s[-2]) #倒数第二个
```

#### 3. Slicing a range of characters

```python
# Slicing is like indexing, but it lets us get more than 1 character.
# ...how is this like range(a,b)?

s = "abcdefgh"
print(s)
print(s[0:3]) #不包括s[3]
print(s[1:3])
print("-----------")
print(s[2:3])
print(s[3:3]) #空
```

#### 4. Slicing with default parameters

```python
s = "abcdefgh"
print(s)
print(s[3:])
print(s[:3])
print(s[:]) #全部
```

#### 5. Slicing with a step parameter

带有步长的分块

```python
print("This is not as common, but perfectly ok.")
s = "abcdefgh"
print(s)
print(s[1:7:2])
print(s[1:7:3])
```

#### 6. Reversing a string

其实可以利用slicing来直接实现串的反转，但是还是另外写一个function比较直观

```python
s = "abcdefgh"

print("This works, but is confusing:")
print(s[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s)))

print("Best way: write your own reverseString() function:")

def reverseString(s):
    return s[::-1]

print(reverseString(s)) # crystal clear!
```

## Looping over strings

#### 1. for loop with indexes

```python
s = "abcd"
for i in range(len(s)): 
    print(i, s[i])
```

#### 2. for loop without indexes

```python
s = "abcd"
for c in s:
    print(c)
```

#### 3. "for" loop with split

```python
# By itself, names.split(",") produces something called a list.
# 相当于设定一个分隔符

names = "fred,wilma,betty,barney"
for name in names.split(","):
    print(name)
```

#### 4. For loop with splitlines

```python
# splitlines() also makes a list, so only loop over its results,
# just like split():
# 就是一行行的split
# quotes from brainyquote.com
quotes = """\
Dijkstra: Simplicity is prerequisite for reliability.
Knuth: If you optimize everything, you will always be unhappy.
Dijkstra: Perfecting oneself is as much unlearning as it is learning.
Knuth: Beware of bugs in the above code; I have only proved it correct, not tried it.
Dijkstra: Computer science is no more about computers than astronomy is about telescopes.
"""
for line in quotes.splitlines():
    if (line.startswith("Knuth")):
        print(line)
```

#### 5. An example: isPalindrome

```python
# There are many ways to write isPalindrome(s)
# Here are several.  Which way is best?

def reverseString(s):
    return s[::-1]

def isPalindrome1(s): #需要新建一个串消耗资源，但是简单易懂
    return (s == reverseString(s))

def isPalindrome2(s): 
    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]): #正index
            return False
    return True

def isPalindrome3(s):
    for i in range(len(s)):
        if (s[i] != s[-1-i]): #负index
            return False
    return True

def isPalindrome4(s):
    while (len(s) > 1):
        if (s[0] != s[-1]):
            return False
        s = s[1:-1] #每一轮都除去已经比较过的字母
    return True

print(isPalindrome1("abcba"), isPalindrome1("abca"))
print(isPalindrome2("abcba"), isPalindrome2("abca"))
print(isPalindrome3("abcba"), isPalindrome3("abca"))
print(isPalindrome4("abcba"), isPalindrome4("abca"))
```

#### 6. Strings are immutable

you cannot change strings! 

```python
s = "abcde"
s[2] = "z"  # Error! Cannot assign into s[i]
```

must create a new string

```python
s = "own"
s = s[:2] + "e" + s[2:]
print(s) #owen
```

#### 7. Strings and Aliases

```python
s = 'abc'  # s references the string 'abc'
t = s      # t is an alias to the one-and-only string 'abc'
s += 'def'
print(s) #abcdef
print(t) #abc 因为t只是对串'abc'的引用，而不是s
```

#### 8. Some string-related Built-in Fcuntions

##### 1. Str() and len()

Str(): 建立一个string

len(): 获得一个串的长度

```python
name = input("Enter your name: ")
print("Hi, " + name + ". Your name has " + str(len(name)) + " letters!")
```

##### 2. chr() and ord()

ord(): 返回字符的Unicode编码

chr(): 返回Unicode编码代表的字符

```python
print(ord("A")) # 65
print(chr(65))  # "A"
print(chr(ord("A")+1)) # ?
```

##### 3. eval()

eval():可以计算一个数学表达式，但是有可能出现以下错误

```python
# eval() works but you should not use it!
s = "(3**2 + 4**2)**0.5"
print(eval(s))

# why not? Well...
s = "reformatMyHardDrive()"
print(eval(s)) # no such function!  But what if there was?
```

#### 9. Some String Methods

Methods are a special type of function that we call "on" a value, like a string. You can tell it's a method because the syntax is in the form of value.function(), like s.islower() in the code below.

##### 1. **Character types: isalnum(), isalpha(), isdigit(), islower(), isspace(), isupper()**

字符类型

```python
# Run this code to see a table of isX() behaviors
def p(test):
    print("True     " if test else "False    ", end="")
def printRow(s):
    print(" " + s + "  ", end="")
    p(s.isalnum())
    p(s.isalpha())
    p(s.isdigit())
    p(s.islower())
    p(s.isspace())
    p(s.isupper())
    print()
def printTable():
    print("  s   isalnum  isalpha  isdigit  islower  isspace  isupper")
    for s in "ABCD,ABcd,abcd,ab12,1234,    ,AB?!".split(","):
        printRow(s)
printTable()
```

##### 2. String edits: lower(), upper(), replace(), strip()

```python
print("This is nice. Yes!".lower())
print("So is this? Sure!!".upper())
print("   Strip removes leading and trailing whitespace only    ".strip())
print("This is nice.  Really nice.".replace("nice", "sweet"))
print("This is nice.  Really nice.".replace("nice", "sweet", 1)) # count = 1

print("----------------")
s = "This is so so fun!"
t = s.replace("so ", "")
print(t)
print(s) # note that s is unmodified (strings are immutable!)
```

##### 3. Substring search: count(), startswith(), endswith(), find(), index()

```python
print("This is a history test".count("is")) # 3
print("This IS a history test".count("is")) # 2
print("-------")
print("Dogs and cats!".startswith("Do"))    # True
print("Dogs and cats!".startswith("Don't")) # False
print("-------")
print("Dogs and cats!".endswith("!"))       # True
print("Dogs and cats!".endswith("rats!"))   # False
print("-------")
print("Dogs and cats!".find("and"))         # 5
print("Dogs and cats!".find("or"))          # -1
print("-------")
print("Dogs and cats!".index("and"))        # 5
print("Dogs and cats!".index("or"))         # crash!
```

#### 10. String formating

#### 11. String formatting with f strings

```python
# We saw this example back in week1!
# It shows a nice relatively new way to format strings:

x = 42
y = 99
# Place variable names in {squiggly braces} to print their values, like so:
print(f'Did you know that {x} + {y} is {x+y}?')
```

#### 12. Basic File IO

```python
# Note: As this requires read-write access to your hard drive,
#       this will not run in the browser in Brython.

def readFile(path):
    with open(path, "rt") as f: # with statement allows python to close 
    		return f.read()					#	the file cleanly if it fails to open 

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsToWrite = "This is a test!\nIt is only a test!"
writeFile("foo.txt", contentsToWrite)

contentsRead = readFile("foo.txt")
assert(contentsRead == contentsToWrite)

print("Open the file foo.txt and verify its contents.")
```

## Graphics



## **15-112 Style Rubric**

### Clarity Rules

#### Ownership

You must include your name, andrewId, and section in a comment at the top of every file you submit.

#### Comments

You should write concise, clear, and informative comments that make your code even easier to understand.

- Comments should be included with any piece of code that is not self-documenting.
- Comments should also be included at the start of every function (including helper functions).
- Comments should *not* be written where they are not needed.

**5-point error:** not writing any comments at all.
**2-point error:** writing too many or too few comments, or writing bad comments.

eg:

```python
# return True if the characters are identical at forward and reversed indices 
def isPalindrome3(s):
    for i in range(len(s)):
        if (s[i] != s[-1-i]):
            return False
    return True
```

# Week 4: Lists

## 1d Lists

### 1. Creating Lists

#### Empty List

```python
print("Two standard ways to create any empty list:")
a = [ ] #strcture of a list
b = list() #built-in function

print(type(a), len(a), a)
print(type(b), len(b), b)
print(a == b)
```

#### List with one element (singleton)

```python
a = ["hello"]
b = 42
```

#### list with Multiple Elements

```python
a = [2,3,4,5]
b = list(range(5)) #iterate of 5
c = ["mixed types", True, 4]
```

#### Variable-Length list

```python
n = 10
a = [0] * n # creates a list with n 0s
b = list(range(n))

print(type(a), len(a), a)
print(type(b), len(b), b)
```

### 2. List Functions and Operations

```python
a = [ 2, 3, 5, 2 ]
print("a = ", a)
print("len =", len(a))
print("min =", min(a))
print("max =", max(a))
print("sum =", sum(a))

# Create some lists
a = [ 2, 3, 5, 3, 7 ]
b = [ 2, 3, 5, 3, 7 ]   # same as a
c = [ 2, 3, 5, 3, 8 ]   # differs in last element
d = [ 2, 3, 5 ]         # prefix of a

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

print("------------------")
print("a == b", (a == b))
print("a == c", (a == c))
print("a != b", (a != b))
print("a != c", (a != c))

print("------------------")
print("a < c", (a < c)) #compares the length and element
print("a < d", (a < d)) #
```

### 3. Accessing Elements(indexing and slicing)

```python
# Indexing and slicing for lists works the same way as it did for strings!

a = [2, 3, 5, 7, 11, 13]
print("a        =", a)

# Access non-negative indexes
print("a[0]     =", a[0])
print("a[2]     =", a[2])

# Access negative indexes
print("a[-1]    =", a[-1])
print("a[-3]    =", a[-3])

# Access slices a[start:end:step]
print("a[0:2]   =", a[0:2])
print("a[1:4]   =", a[1:4])
print("a[1:6:2] =", a[1:6:2])
```

### 4. List Mutability and Aliasing

Lists are **mutable**. Which means it can be changed, without creting a new list. 

This also forces us to better understand **aliases**, when two variables reference the same value. Aliases are only interesting (and challenging) for mutable values like lists.
**Note:** it will be especially helpful to use the Visualize feature in the following examples.

```python
# Create a list
a = [ 2, 3, 5, 7 ]

# Create an alias to the list
b = a

# We now have two references (aliases) to the SAME list
a[0] = 42
b[1] = 99
print(a)
print(b)
```

#### Function Parameters are Aliases

```python
def f(a):
    a[0] = 42
a = [2, 3, 5, 7]
f(a)
print(a)

# Note that the parameter alias can still be broken by re-assigning the variable

a = [3, 2, 1]

def foo(a):
     a[0] = 1
     a = [5, 2, 0] # we break the alias here!
     a[0] = 4

foo(a)
print(a)
```

```python
# Create a list
a = [ 2, 3, 5, 7 ]

# Create an alias to the list
b = a

# Create a different list with the same elements
c = [ 2, 3, 5, 7 ]

# a and b are references (aliases) to the SAME list
# c is a reference to a different but EQUAL list

print("initially:")
print("  a==b  :", a==b)
print("  a==c  :", a==c)
print("  a is b:", a is b) # the is operation tells if two values are aliases, or basic datatypes
print("  a is c:", a is c)

# Now changes to a also change b (the SAME list) but not c (a different list)
a[0] = 42
print("After changing a[0] to 42")
print("  a=", a)
print("  b=", b)
print("  c=", c)
print("  a==b  :", a==b)
print("  a==c  :", a==c)
print("  a is b:", a is b)
print("  a is c:", a is c)
```

### 5. Copying lists

##### list vs alias

```python
# Because of aliasing, we have to be careful if we share a reference
# to a list in the same way we might for number or a string,
# by simply setting b = a, like so:

import copy

# Create a list
a = [ 2, 3 ]

# Try to copy it
b = a             # Error!  Not a copy, but an alias
c = copy.copy(a)  # Ok

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)
print("   c =", c)

# Now modify a[0]
a[0] = 42
print("But after a[0] = 42")
print("   a =", a)
print("   b =", b)
print("   c =", c)
```

Other ways to copy

```python
import copy

a = [2, 3]

b = copy.copy(a)
c = a[:]
d = a + [ ]
e = list(a)

a[0] = 42
print(a, b, c, d, e)
```

### 6. Destructive and Non-destructive Functions

Because lists are mutable, we can change them in two ways:
**destructively** (which modifies the original value directly), and
**non-destructively** (which creates a new list and does not modify the original value).
This also affects how we write functions that use lists.

#### Destrctive functions:

```python
# A destructive function is written to directly change the provided list
# It does not need to return anything, as the caller can access the original list
def fill(a, value):
    for i in range(len(a)):
        a[i] = value

a = [1, 2, 3, 4, 5]
print("At first, a =", a)
fill(a, 42)
print("After fill(a, 42), a =", a)
```

#### Non-destructive function

```python
import copy

## First, a quick primer on modifying lists ##
## We'll talk about these more in a bit ##

a = [1, 2, 3, 4]

# .remove() DESTRUCTIVELY removes the given value from the list
a.remove(2)
print(a) # [1, 3, 4]

# .append() DESTRUCTIVELY adds the given value to the end of the list
a.append(70)
print(a) # [1, 3, 4, 70]

## Now, on to NON-DESTRUCTIVE functions! ##

def destructiveRemoveAll(a, value):
    while (value in a):
        a.remove(value)

def nonDestructiveRemoveAll(a, value):
    # Typically, we write non-destructive functions by building a new list
    # instead of changing the original
    result = []
    for element in a:
        if (element != value):
            result.append(element)
    return result # non-destructive functions still need to return!

def alternateNonDestructiveRemoveAll(a, value):
    # We can write the same function by breaking the alias,
    # then using the destructive approach
    a = copy.copy(a)
    destructiveRemoveAll(a, value)
    return a

a = [ 1, 2, 3, 4, 3, 2, 1 ]
print("At first")
print("   a =", a)

destructiveRemoveAll(a, 2)
print("After destructiveRemoveAll(a, 2)")
print("   a =", a)

b = nonDestructiveRemoveAll(a, 3)
print("After b = nonDestructiveRemoveAll(a, 3)")
print("   a =", a)
print("   b =", b)

c = alternateNonDestructiveRemoveAll(a, 1)
print("After c = alternateNonDestructiveRemoveAll(a, 1)")
print("   a =", a)
print("   c =", c)
```

### 7. Finding Element

#### check for membership: *value* in *list*

```python
a = [ 2, 3, 5, 2, 6, 2, 2, 7 ]
print("a      =", a)
print("2 in a =", (2 in a))
print("4 in a =", (4 in a))
```

#### check for list non-membership: *value* not in *list*

#### count occurrences in list: list.count(item)

#### Find index of item: list.index(item) and list.index(item, start)

```python
a = [ 2, 3, 5, 2, 6, 2, 2, 7 ]
print("a            =", a)
print("a.index(6)   =", a.index(6))
print("a.index(2)   =", a.index(2))
print("a.index(2,1) =", a.index(2,1))
print("a.index(2,4) =", a.index(2,4))
```

#### Problem: crashes when item is not in list

```python
a = [ 2, 3, 5, 2 ]
print("a          =", a)
print("a.index(9) =", a.index(9)) # crashes!
print("This line will not run!")
```

#### Solution: use (*item* in *list*)

```python
a = [ 2, 3, 5, 2 ]
print("a =", a)
if (9 in a):
    print("a.index(9) =", a.index(9))
else:
    print("9 not in", a)
print("This line will run now!")
```

### 8.Adding element

#### Destructively 直接修改列表

##### add an item with list.append(item)

##### **Add a list of items with list += list2 or list.extend(list2)**

```python
a = [ 2, 3 ]
a += [ 11, 13 ]
print(a)
a.extend([ 17, 19 ])
print(a)
```

##### **Insert an item at a given index**

a.insert(index, value)

#### Non-Destructively 创建新列表

##### add an item with **list1 + list2**

```python
a = [ 2, 3 ]
b = a + [ 13, 17 ]
print(a)
print(b)
```

**Insert an item at a given index (with list slices)**

```python
a = [ 2, 3 ]
b = a[:2] + [5] + a[2:]
print(a)
print(b)
```

### 9. Removing elements

#### Destructively

###### list.remove(item)：一个一个移除，index小的优先

##### List.pop(index): 

```python
a = [ 2, 3, 4, 5, 6, 7, 8 ]
print("a =", a)

item = a.pop(3)
print("After item = a.pop(3)")
print("   item =", item)
print("   a =", a)

item = a.pop(3)
print("After another item = a.pop(3)")
print("   item =", item)
print("   a =", a)

# Remove last item with list.pop()
item = a.pop()
print("After item = a.pop()")
print("   item =", item)
print("   a =", a)
```

#### Non-Destructively

remove item at given index (with list slice)

```python
a = [ 2, 3, 5, 3, 7, 5, 11, 13 ]
print("a =", a)

b = a[:2] + a[3:]
print("After b = a[:2] + a[3:]")
print("   a =", a)
print("   b =", b)
```

### 10. Looping over lists

##### for loop

```python
a = [ 2, 3, 5, 7 ]
print("Here are the items in a with their indexes:")
for index in range(len(a)):
    print("a[", index, "] =", a[index])
```

##### For each loop

```python
# Lists and strings are both iterable types.
# This means that we can iterate (loop) over them directly!
a = [ 2, 3, 5, 7 ]
print("Here are the items in a:")
for item in a:
    print(item)
```

##### Hazard!!!

modifying inside a for loop

```python
# IMPORTANT: don't change a list inside a for loop! The indexes will behave unpredictably.
# This isn't a problem for strings because they aren't mutable.
a = [ 2, 3, 5, 3, 7 ]
print("a =", a)

# Failed attempt to remove all the 3's
for index in range(len(a)):
    if (a[index] == 3):  # this eventually crashes!
        a.pop(index)

print("This line will not run!")
```

modifying inside a for-each loop

```python
# If we remove items in a for-each loop, the loop won't crash,
# but it won't behave as we would expect either!

a = [3, 3, 2, 3, 4]
for item in a:       # this won't reach every item in the list!
    if (item == 3):
      a.remove(item)
print(a) # should be [2, 4], but there's still a 3 in there!
```

##### Solution: modifying inside a while loop

```python
# Modify the list in a while loop instead of a for loop,
# to control how indexes 

a = [ 2, 3, 5, 3, 7 ]
print("a =", a)

# Successful attempt to remove all the 3's
index = 0
while (index < len(a)):
    if (a[index] == 3):
        a.pop(index)
    else:
        index += 1

print("This line will run!")
print("And now a =", a)
```

### 11.List Methods: Sorting and Reversing

##### **Destructively with list.sort() or list.reverse()**

```python
a = [ 7, 2, 5, 3, 5, 11, 7 ]
print("At first, a =", a)
a.sort()
print("After a.sort(), a =",a)

a = [ 2, 3, 5, 7 ]
print("Here are the items in reverse:")
a.reverse()
for item in a:
    print(item)
print(a)
```

##### **Non-Destructively with sorted(list) and reversed(list)**

```python
a = [ 7, 2, 5, 3, 5, 11, 7 ]
print("At first")
print("   a =", a)
b = sorted(a)
print("After b = sorted(a)")
print("   a =", a)
print("   b =", b)

a = [ 2, 3, 5, 7 ]
print("Here are the items in reverse:")
for item in reversed(a):
    print(item)
print(a)
```

### 12. Tuples (immutable lists)

Tuples are exactly like lists, except they are **immutable**. We cannot change the values of a tuple.

##### Syntax : construct with **paramethsis** or **tuple()**

```python
t = (1, 2, 3)
print(type(t), len(t), t)

a = [1, 2, 3]
t = tuple(a)
print(type(t), len(t), t)
```

##### **Tuples are immutable**

```python
t = (1, 2, 3)
print(t[0])

t[0] = 42    # crash!
print(t[0])
```

##### **Parallel (tuple) assignment**

```python
(x, y) = (1, 2)
print(x)
print(y)

# tuples are useful for swapping!
(x, y) = (y, x)
print(x)
print(y)
```

##### **Singleton tuple syntax**

```python
t = (42)
print(type(t), t*5)

t = (42,) # use a comma to force the type
print(type(t), t*5)
```

### 13. **List Comprehensions** 

List comprehensions are a handy way to create lists using simple loops all in one line.

```python
# Long way
a = []
for i in range(10):
    a.append(i)
print(a)

# Short way
a = [i for i in range(10)]
print(a)

# We can also add conditionals at the end (but keep it simple!)
a = [(i*100) for i in range(20) if i%5 == 0]
print(a)
```

### 14. Converting Between Lists and Strings

```python
# use list(s) to convert a string to a list of characters
a = list("wahoo!")
print(a)  # prints: ['w', 'a', 'h', 'o', 'o', '!']

# use s1.split(s2) to convert a string to a list of strings delimited by s2
a = "How are you doing today?".split(" ")
print(a) # prints ['How', 'are', 'you', 'doing', 'today?']

# use "".join(a) to convert a list of characters to a single string
print("".join(a))  # prints: Howareyoudoingtoday?

# "".join(a) also works on a list of strings (not just single characters)
a = ["parsley", "is", "gharsley"] # by Ogden Nash!
print("".join(a))  # prints: parsleyisgharsley
print(" ".join(a)) # prints: parsley is gharsley
```
