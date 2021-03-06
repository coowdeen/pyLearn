#################################################
# hw1.py
# name: Owen
# andrew id: None lol
# some of the description of practices is too long to be copied to here
# find all of the descriptions here: https://www.cs.cmu.edu/~112/notes/hw1.html
#################################################

import cs112_f21_week1_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


#################################################
# Part A
#################################################

def distance(x1, y1, x2, y2):
    # Write the function distance(x1, y1, x2, y2) that takes four int 
    # or float values x1, y1, x2, y2 that represent the two points (x1, y1) 
    # and (x2, y2), and returns the distance between those points as a float.
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    # Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) that takes 
    # 6 numbers (ints or floats) -- x1, y1, r1, x2, y2, r2 -- 
    # that describe the circle centered at (x1,y1) with radius r1, 
    # and the circle centered at (x2,y2) with radius r2, 
    # and returns True if the two circles intersect and False otherwise.
    dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if (dis <= (r2 + r1)):
        return True
    else:
        return False

def getInRange(x, bound1, bound2):
    # Write the function getInRange(x, bound1, bound2) which takes 3 int or 
    # float values -- x, bound1, and bound2, where bound1 is not necessarily 
    # less than bound2. If x is between the two bounds, 
    # just return it unmodified. Otherwise, if x is less than the lower bound, 
    # return the lower bound, or if x is greater than the upper bound, 
    # return the upper bound.
    if (bound1 > bound2):
        temp = bound1
        bound1 = bound2
        bound2 = temp

    if (x <= bound1):
        return bound1
    elif (x > bound1 and x < bound2):
        return x
    else:
        return bound2

def eggCartons(eggs):
    # Write the function eggCartons(eggs) that takes a non-negative integer 
    # number of eggs, and returns the smallest integer number of cartons 
    # required to hold that many eggs, where a carton may hold up to 12 eggs.
    if (eggs < 0):
        return None

    if (eggs == 0):
        carton = 0
    elif (eggs <= 12):
        carton = 1
    else:
        carton = eggs // 12
        if (eggs % 12 > 0):
            carton += 1
    return carton

def pascalsTriangleValue(row, col):
    # Write the function pascalsTriangleValue(row, col) that takes int values 
    # row and col, and returns the value in the given row and column of 
    # Pascal's Triangle where the triangle starts at row 0, and each row starts 
    # at column 0. If either row or col are not legal values, return None, 
    # instead of crashing.
    # Hint: math.factorial may be helpful! 
    # Also: it may help to read MathIsFun's Pascal's Triangle page, which 
    # includes a general discussion, some nice applications, and further down 
    # the page a helpful formula.
    def fac(n):
        return math.factorial(n)

    if(row < 0 or col < 0 or col > row):
        return None
    else:
        asw = fac(row) / (fac(col) * fac((row - col)))
    
    return asw

def getKthDigit(n, k):
    # Write the function getKthDigit(n, k) that takes a possibly-negative int n 
    # and a non-negative int k, and returns the kth digit of n, starting from 0,
    # counting from the right.

    if(k < 0):
        return None
    else:
        return int(abs(n) / (10**k)) % 10

def setKthDigit(n, k, d):
    # Write the function setKthDigit(n, k, d) that takes three integers -- n, k,
    # and d -- where n is a possibly-negative int, k is a non-negative int, and
    # d is a non-negative single digit (between 0 and 9 inclusive). 
    # This function returns the number n with the kth digit replaced with d. 
    # Counting starts at 0 and goes right-to-left, so the 0th digit is the 
    # rightmost digit.
    if(k < 0):
        return None
    elif(d > 9 or d < 0):
        return None
    else:
        return 

#################################################
# Part B
#################################################
        
def nearestOdd(n):
    # Write the function nearestOdd(n) that takes an int or float n, and returns
    # as an int value the nearest odd number to n. In the case of a tie, return 
    # the smaller odd value. Note that the result must be an int, 
    # so nearestOdd(13.0) is the int 13, and not the float 13.0.
    if(n % 2 == 0):
        return int(n - 1)
    elif(roundHalfUp(n) - n > 0):
        return int(roundHalfUp(n) - 1)
    elif(roundHalfUp(n) - n < 0):
        return int(roundHalfUp(n) + 1)
    else:
        return int(n)

def numberOfPoolBalls(rows):
    # Pool balls are arranged in rows where the first row contains 1 pool ball 
    # and each row contains 1 more pool ball than the previous row. Thus, for 
    # example, 3 rows contain 6 total pool balls (1+2+3). With this in mind, 
    # write the function numberOfPoolBalls(rows) that takes a non-negative int 
    # value, the number of rows, and returns another int value, the number of 
    # pool balls in that number of full rows. For example, numberOfPoolBalls(3) 
    # returns 6. We will not limit our analysis to a "rack" of 15 balls. Rather,
    # our pool table can contain an unlimited number of rows. For this problem 
    # and the next, you should research Triangular Numbers.
    if(rows < 0):
        return None
    else:
        return (rows * (rows + 1)) / 2

def numberOfPoolBallRows(balls):
    # This problem is the inverse of the previous problem. Write the function 
    # numberOfPoolBallRows(balls) that takes a non-negative int number of pool 
    # balls, and returns the smallest int number of rows required for the given 
    # number of pool balls. Thus, numberOfPoolBallRows(6) returns 3. Note that 
    # if any balls must be in a row, then you count that row, and so 
    # numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single 
    # ball in it).
    if(balls < 0):
        return None
    else:
        return 

def colorBlender(rgb1, rgb2, midpoints, n):
    # step1: get target R,G,B from rgb1
    targetR = roundHalfUp(rgb2 / 10**6)
    targetG = roundHalfUp((rgb2 / 10**3) % 1000)
    targetB = roundHalfUp(rgb2  % 1000)

    R = roundHalfUp(rgb1 / 10**6)
    G = roundHalfUp((rgb1 / 10**3) % 1000)
    B = roundHalfUp(rgb1  % 1000)

    if(n < 0 or n > midpoints + 1):
        return None
    else:
        if(targetR > R):
            incrementR = (targetR - R) / (midpoints + 1)
            resultR = R + incrementR * n
            if(resultR > targetR):
                resultR = targetR
        elif(targetR == R):
            resultR = targetR
        else:
            incrementR = abs(targetR - R) / (midpoints + 1)
            resultR = R - incrementR * n

        if(targetG > G):
            incrementR = (targetG - G) / (midpoints + 1)
            resultG = G + incrementR * n
            if(resultG > targetG):
                resultG = targetG
        elif(targetG == G):
            resultG = targetG
        else:
            incrementG = abs(targetG - G) / (midpoints + 1)
            resultG = G - incrementG * n

        if(targetB > B):
            incrementB = (targetB - B) / (midpoints + 1)
            resultB = B + incrementB * n
            if(resultB > targetB):
                resultB = targetB
        elif(targetB == B):
            resultB = targetB
        else:
            incrementB = abs(targetB - B) / (midpoints + 1)
            resultB = B - incrementB * n

    resultR = roundHalfUp(resultR)*10**6
    resultG = roundHalfUp(resultG)*10**3
    resultB = roundHalfUp(resultB)
    
    return resultR + resultG + resultB

    

#################################################
# Bonus/Optional
#################################################

def bonusPlayThreeDiceYahtzee(dice):
    return 42

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing bonusFindIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testPascalsTriangleValue()
    testGetKthDigit()
   # testSetKthDigit()
    # Part B:
    testNearestOdd()
    testNumberOfPoolBalls()
  #  testNumberOfPoolBallRows()
    testColorBlender()
    # Bonus:
    # testBonusPlayThreeDiceYahtzee()
    # testBonusFindIntRootsOfCubic()

def main():
    cs112_f21_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
