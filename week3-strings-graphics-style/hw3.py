#################################################
# hw3.py
# name: Owen
# andrew id: None
# description of practices: https://www.cs.cmu.edu/~112/notes/hw3.html
#################################################

import cs112_f21_week3_linter
import math
from cmu_112_graphics import *

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

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# Part A
#################################################

# Write the function rotateString(s, k) that takes a string s and a 
# possibly-negative integer k. If k is non-negative, the function returns the 
# string s rotated k places to the left. If k is negative, the function returns 
# the string s rotated |k| places to the right.
def rotateString(s, k):
    lengthOfS = len(s)
    k %= lengthOfS
    if(k > 0):
        result = s[k:lengthOfS] + s[:k]
        return result
    if(k < 0):
        k = abs(k)
        result = s[lengthOfS - k:] + s[:lengthOfS - k]
        return result
    else: 
        return s

def applyCaesarCipher(message, shift):
    # no magic number allowed, unicode of upper/lower-case characters
    upperTop = 90
    upperBottom = 65
    lowerTop = 122
    lowerBottom = 97

    if(message.isdigit()):# if message is all digit return the message 
        return message
        
    newS = ""
    shifted = 0
    for x in message:
        # compute what the shifted order in unicode should be
        shifted = ord(x) + shift
        if(x == " "):
            newS += " "
        # if the character is an uppercase then check if it's in uppercase range
        elif(x.isupper()):
            # shifted order exceeds top of unicode of uppercase then correct it
            if(shifted > upperTop):
                shifted = shifted - upperTop + upperBottom - 1
            # shifted order exceeds bottom of unicode of uppercase
            elif(shifted < upperBottom):
                shifted = upperTop - (upperBottom - shifted) + 1
            newS += chr(shifted)
        # same as uppercase
        elif(x.islower()):
            if(shifted > lowerTop):
                shifted = shifted - lowerTop + lowerBottom - 1
            elif(shifted < lowerBottom):
                shifted = lowerTop - (lowerBottom - shifted) + 1
            newS += chr(shifted)
    return newS

def largestNumber(s):# returns the largest num in the string
    max = 0
    for x in s.split(" "):
        if x.isdigit():
            if(int(x) >= max):
                max = int(x)
    # in case no digit found
    if(max == 0):
        return None
    return max

# calculates total score of each player and return the top scorer 
def topScorer(data):
    max = 0
    for line in data.splitlines():
        sum = 0
        for score in line.split(","):
            if(score.isdigit()):
                sum += int(score)
                if(sum > max):
                    max = sum
                    winner = name
                elif(sum == max):# multiple winner
                    winner = winner + "," + name
            else:
                name = score
    if(max == 0):
        return None
    return winner

#################################################
# Part B
#################################################

# replace whitesplace (\t, \n) with single space without using s.replace()
def collapseWhitespace(s):
    newS = ""
    flag = 0
    for x in s:
        if (x.isspace()):
            flag += 1
        else:
            flag = 0
            newS += x
        if (flag == 1):
            newS += " "
    return newS

# a helper function to remove the whitespace in message
def msgNormalize(msg):
    normMsg = ""
    for s in msg:
        if(s.isspace()):
            continue
        else:
            normMsg += s
    return normMsg

# returns a string produced by replacing the non-whitespace characters in the 
# pattern with the non-whitespace characters in the message
def patternedMessage(msg, pattern):
    newS = ""
    normMsg = msgNormalize(msg)# remove whitespace in the message
    length = len(normMsg)
    count = 0# marks the position of character in the normMsg
    flag = -1# add "\n" at the end of each line of the output string if not 0

    for line in pattern.splitlines():# get the number of lines of the pattern
        if(line.isspace() or line == "" or line =="\n"):
            continue
        else:
            flag += 1
    
    for line in pattern.splitlines():
        for s in line:
            if(s.isspace()):
                newS += " "
            else:
                newS += normMsg[count]
                count += 1
                count %= length# keeping the count in string index range
        if(flag != 0 and not line.isspace() and line != ""):
            newS += "\n"
            flag -= 1
    return newS

def encodeRightLeftRouteCipher(text, rows):
    return 42

def decodeRightLeftRouteCipher(cipher):
    return 42

#################################################
# Part B Drawings
#################################################

# Make sure you have cmu_112_graphics downloaded to the 
# same directory as this file!

# Note: If you don't see any text when running graphics code, 
# try changing your computer's color theme to light mode. 

def drawFlagOfTheEU(canvas, x0, y0, x1, y1):
    canvas.create_rectangle(x0, y0, x1, y1, fill='yellow', outline='black')
    size = (x1 - x0) // 12
    canvas.create_text((x0 + x1)/2, (y0 + y1)/2,
                       text='Draw the EU flag here!', font=f'Arial {size} bold')
    # Your code goes here!

def drawSimpleTortoiseProgram(program, canvas, width, height):
    canvas.create_rectangle(0, 0, width, height, fill='yellow', outline='black')
    canvas.create_text(width/2, height/2,
                       text='Draw the Simple Tortoise Program here!',
                       font='Arial 20 bold')
    # Your code goes here!

#################################################
# Bonus/Optional
#################################################

def bonusTopLevelFunctionNames(code):
    return 42

def bonusGetEvalSteps(expr):
    return 42

#################################################
# Test Functions
#################################################

def testRotateString():
    print("Testing rotateString()...", end="")
    assert(rotateString("abcde", 0) == "abcde")
    assert(rotateString("abcde", 1) == "bcdea")
    assert(rotateString("abcde", 2) == "cdeab")
    assert(rotateString("abcde", 3) == "deabc")
    assert(rotateString("abcde", 4) == "eabcd")
    assert(rotateString("abcde", 5) == "abcde")
    assert(rotateString("abcde", 25) == "abcde")
    assert(rotateString("abcde", 28) == "deabc")
    assert(rotateString("abcde", -1) == "eabcd")
    assert(rotateString("abcde", -2) == "deabc")
    assert(rotateString("abcde", -3) == "cdeab")
    assert(rotateString("abcde", -4) == "bcdea")
    assert(rotateString("abcde", -5) == "abcde")
    assert(rotateString("abcde", -25) == "abcde")
    assert(rotateString("abcde", -28) == "cdeab")
    print("Passed!")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) ==
                             "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 25) ==
                             "zabcdefghijklmnopqrstuvwxy")
    assert(applyCaesarCipher("We Attack At Dawn", 2)  == "Yg Cvvcem Cv Fcyp")
    assert(applyCaesarCipher("We Attack At Dawn", 4)  == "Ai Exxego Ex Hear")
    assert(applyCaesarCipher("We Attack At Dawn", -1) == "Vd Zsszbj Zs Czvm")
    # And now, the whole point...
    assert(applyCaesarCipher(applyCaesarCipher('This is Great', 25), -25)
           == 'This is Great')
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)
    print('Passed!')

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    assert(collapseWhitespace("abc") == "abc")
    assert(collapseWhitespace("   \n\n  \t\t\t  ") == " ")
    assert(collapseWhitespace(" A  \n\n  \t\t\t z  \t\t ") == " A z ")
    print("Passed!")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    assert(patternedMessage("abc def",   "***** ***** ****")   ==
           "abcde fabcd efab")
    assert(patternedMessage("abc def", "\n***** ***** ****\n") == 
           "abcde fabcd efab")

    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        (msg,pattern) = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        #observed = patternedMessage(msg, pattern).strip("\n")
        #print "\n\n***********************\n\n"
        #print msg, pattern
        #print "<"+patternedMessage(msg, pattern)+">"
        #print "<"+soln+">"
        assert(observed == soln)
    print("Passed!")

def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def testBonusTopLevelFunctionNames():
    print("Testing bonusTopLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(bonusTopLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(bonusTopLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(bonusTopLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(bonusTopLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(bonusTopLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing bonusGetEvalSteps()...", end="")
    assert(bonusGetEvalSteps("0") == "0 = 0")
    assert(bonusGetEvalSteps("2") == "2 = 2")
    assert(bonusGetEvalSteps("3+2") == "3+2 = 5")
    assert(bonusGetEvalSteps("3-2") == "3-2 = 1")
    assert(bonusGetEvalSteps("3**2") == "3**2 = 9")
    assert(bonusGetEvalSteps("31%16") == "31%16 = 15")
    assert(bonusGetEvalSteps("31*16") == "31*16 = 496")
    assert(bonusGetEvalSteps("32//16") == "32//16 = 2")
    assert(bonusGetEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(bonusGetEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(bonusGetEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(bonusGetEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

#################################################
# Graphics Test Functions
#################################################

def testDrawFlagOfTheEU(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='lightYellow')
    drawFlagOfTheEU(canvas, 50, 125, 350, 275)
    drawFlagOfTheEU(canvas, 425, 100, 575, 200)
    drawFlagOfTheEU(canvas, 450, 275, 550, 325)
    canvas.create_text(app.width/2, app.height-25, 
                       text="Testing drawFlagOfTheEU")
    canvas.create_text(app.width/2, app.height-10, 
                       text="This does not need to resize properly!")

def testDrawSimpleTortoiseProgram(app, canvas, programName, program):
    drawSimpleTortoiseProgram(program, canvas, app.width, app.height)
    canvas.create_text(app.width/2, app.height-10, 
          text=(f'testing drawSimpleTortoiseProgram with {programName} ' + 
                f'(canvas, {app.width}, {app.height})'))

def testDrawSimpleTortoiseProgram_with_program_A(app, canvas):
    programA = '''\
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100'''
    testDrawSimpleTortoiseProgram(app, canvas, 'program A', programA)

def testDrawSimpleTortoiseProgram_with_program_B(app, canvas):
    programB = '''\
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50'''
    testDrawSimpleTortoiseProgram(app, canvas, 'program B', programB)

def drawSplashScreen(app, canvas):
    text = f'''\
Press the number key for the 
exercise you would like to test!

1. drawFlagOfTheEU
2. drawSimpleTortoiseProgram (with program A)
3. drawSimpleTortoiseProgram (with program B)

Press any other key to return
to this screen.
'''
    textSize = min(app.width,app.height) // 40
    canvas.create_text(app.width/2, app.height/2, text=text,
                       font=f'Arial {textSize} bold')


def appStarted(app):
    app.lastKeyPressed = None
    app.timerDelay = 10**10

def keyPressed(app, event):
    app.lastKeyPressed = event.key

def redrawAll(app, canvas):
    if app.lastKeyPressed == '1':
      testDrawFlagOfTheEU(app, canvas)
    elif app.lastKeyPressed == '2':
      testDrawSimpleTortoiseProgram_with_program_A(app, canvas)
    elif app.lastKeyPressed == '3':
      testDrawSimpleTortoiseProgram_with_program_B(app, canvas)
    else:
      drawSplashScreen(app, canvas)

def testGraphicsFunctions():
    runApp(width=600, height=600)

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testRotateString()
    testApplyCaesarCipher()
    testLargestNumber()
    testTopScorer()

    # Part B:
    testCollapseWhitespace()
    testPatternedMessage()
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()

    # Part B Graphics:
    testGraphicsFunctions()

    # Bonus:
    # testBonusTopLevelFunctionNames()
    # testBonusGetEvalSteps()

def main():
    cs112_f21_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
