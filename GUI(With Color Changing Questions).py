import javax.swing as swing
import java.awt as awt
from random import randint

def setButtons():
    global startBut
    startBut = swing.JButton("Start!!", actionPerformed=startGame)
    startBut.setSize(100, 50)
    startBut.setLocation(100, 35)
    c.add(startBut)
    global confirmBut
    confirmBut = swing.JButton("I believe I'm right!!", actionPerformed=oneRound)
    confirmBut.setSize(250, 100)
    confirmBut.setLocation(50, 350)
    confirmBut.setEnabled(False)
    c.add(confirmBut)
    global quitBut
    quitBut = swing.JButton("QUIT!?", actionPerformed=quitGame)
    quitBut.setSize(100, 50)
    quitBut.setLocation(610, 35)
    c.add(quitBut)

def setLabels():
    global questionLabel
    questionLabel = swing.JLabel("What is the value of Red?")
    questionLabel.setSize(300, 50)
    questionLabel.setLocation(110, 120)
    c.add(questionLabel)

def setTextArea():
    global history
    history = "Welcome to the game!!\nIf you guess incorectly 20 times then the game will end!"
    global gamingProcess
    gamingProcess = swing.JTextArea(history)
    gamingProcess.setSize(310, 60)
    gamingProcess.setLocation(220, 35)
    gamingProcess.setLineWrap(True)
    gamingProcess.setEditable(False)
    gamingProcess.setBackground(awt.Color(238, 238, 238))
    c.add(gamingProcess)


def setPanel():
    global colorDisplay
    colorDisplay = swing.JPanel()
    colorDisplay.setSize(300, 300)
    colorDisplay.setLocation(400, 150)
    colorDisplay.setBackground(awt.Color(255, 255, 255))
    c.add(colorDisplay)
    global life
    life=[]
    for i in range(0, 20):
        life.append(swing.JPanel())
        life[i].setSize(10, 10)
        life[i].setLocation(220+i*20, 98)
        life[i].setBackground(awt.Color(238, 238, 238))
        c.add(life[i])

def setRadioButtons():
    global butGroup
    butGroup = swing.ButtonGroup()
    global radioBut1
    radioBut1 = swing.JRadioButton("between 0 and 60")
    radioBut1.setSize(270, 20)
    radioBut1.setLocation(120, 210)
    butGroup.add(radioBut1)
    c.add(radioBut1)
    global radioBut2
    radioBut2 = swing.JRadioButton("between 61 and 120")
    radioBut2.setSize(270, 20)
    radioBut2.setLocation(120, 230)
    butGroup.add(radioBut2)
    c.add(radioBut2)
    global radioBut3
    radioBut3 = swing.JRadioButton("between 121 and 180")
    radioBut3.setSize(270, 20)
    radioBut3.setLocation(120, 250)
    butGroup.add(radioBut3)
    c.add(radioBut3)
    global radioBut4
    radioBut4 = swing.JRadioButton("between 181 and 255")
    radioBut4.setSize(270, 20)
    radioBut4.setLocation(120, 270)
    butGroup.add(radioBut4)
    c.add(radioBut4)

def generateRGB():
    global values
    values = [randint(0, 255), randint(0, 255), randint(0, 255)]
    colorDisplay.setBackground(awt.Color(values[0], values[1], values[2]))

def changeProblem():
    RGB = ["Red", "Green", "Blue"]
    global serial
    global questionLabel
    serial = randint(0, 2)
    if serial == 0:
        questionLabel.setForeground(awt.Color.RED)
        questionLabel.text = "What is the value of " + RGB[serial] + "?"
    elif serial == 1:
        questionLabel.setForeground(awt.Color.DARK_GREEN)
        questionLabel.text = "What is the value of " + RGB[serial] + "?"
    elif serial == 2:
        questionLabel.setForeground(awt.Color.BLUE)
        questionLabel.text = "What is the value of " + RGB[serial] + "?"
    else:
        questionLabel.setForeground(awt.Color.BLACK)
        questionLabel.text = "What is the value of " + RGB[serial] + "?"

def startGame(event):
    generateRGB()
    changeProblem()
    global score
    global wrongAnswers
    gamingProcess.setText("Welcome to the game!!\nIf you guess incorectly 20 times then the \ngame will end!")
    wrongAnswers = 20
    score = 0
    startBut.setEnabled(False)
    confirmBut.setEnabled(True)
    for i in range(0, 20):
        life[i].setBackground(awt.Color(255, 0, 0))

def oneRound(event):
    if radioBut1.isSelected() and values[serial] >= 0 and values[serial] <= 60:
        addScore()
    elif radioBut2.isSelected() and values[serial] > 60 and values[serial] <= 120:
        addScore()
    elif radioBut3.isSelected() and values[serial] > 120 and values[serial] <= 180:
        addScore()
    elif radioBut4.isSelected() and values[serial] > 180 and values[serial] <= 255:
        addScore()
    else:
        fail()
    checkProgress()

def addScore():
    global score
    score = score + 1
    gamingProcess.setText("Good for you!! The value is " + str(values[serial]) + "\nScore: " + str(score))
    generateRGB()
    changeProblem()

def fail():
    global wrongAnswers
    global score
    wrongAnswers = wrongAnswers - 1
    global score
    minus = randint(0, 1)
    score = score - minus
    if minus == 1:
        gamingProcess.setText("Too bad, Score -1\nScore: " + str(score))
    else:
        gamingProcess.setText("Still wrong, but no points lost!!\nScore: " + str(score))
    life[wrongAnswers].setBackground(awt.Color(238, 238, 238))


def quitGame(event):
    gameSummery()

def gameSummery():
    global score
    confirmBut.setEnabled(False)
    startBut.setEnabled(True)
    gamingProcess.setText("GAME OVER\nYou guessed wrong "+str(20-wrongAnswers)+" times\nFinal Score: " + str(score))

def checkProgress():
    if wrongAnswers <= 0:
        gameSummery()

frame = swing.JFrame("Color Guess v1.0.0")
c = frame.getContentPane()
frame.setSize(826, 581)
c.setLayout(None)
setButtons()
setLabels()
setTextArea()
setRadioButtons()
setPanel()
frame.setVisible(True)