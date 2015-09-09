import javax.swing as swing;
import java.awt as awt;
from random import randint

def setButtons():
    global startBtn
    startBtn = swing.JButton("Start", actionPerformed=changeTime)
    startBtn.setSize(69, 27)
    startBtn.setLocation(160, 40)
    c.add(startBtn)
    global continueBtn
    continueBtn = swing.JButton("Continue", actionPerformed=changeColor)
    continueBtn.setSize(100, 50)
    continueBtn.setLocation(600, 40)
    c.add(continueBtn)
    global confirmBtn
    confirmBtn = swing.JButton("Confirm")
    confirmBtn.setSize(250, 100)
    confirmBtn.setLocation(50, 350)
    c.add(confirmBtn)

def setLabels():
    global playerNumLabel
    playerNumLabel = swing.JLabel("Players: ")
    playerNumLabel.setSize(75, 20)
    playerNumLabel.setLocation(80, 30)
    c.add(playerNumLabel)
    global RLabel
    RLabel = swing.JLabel("Red value: ")
    RLabel.setSize(73, 18)
    RLabel.setLocation(50, 250)
    c.add(RLabel)
    global GLabel
    GLabel = swing.JLabel("Green value: ")
    GLabel.setSize(73, 18)
    GLabel.setLocation(50, 280)
    c.add(GLabel)
    global BLabel
    BLabel = swing.JLabel("Blue value: ")
    BLabel.setSize(73, 18)
    BLabel.setLocation(50, 310)
    c.add(BLabel)
    global toLabel01
    toLabel01 = swing.JLabel("to")
    toLabel01.setSize(17, 24)
    toLabel01.setLocation(203, 250)
    c.add(toLabel01)
    global toLabel02
    toLabel02 = swing.JLabel("to")
    toLabel02.setSize(17, 24)
    toLabel02.setLocation(203, 280)
    c.add(toLabel02)
    global toLabel03
    toLabel03 = swing.JLabel("to")
    toLabel03.setSize(17, 24)
    toLabel03.setLocation(203, 310)
    c.add(toLabel03)
    global countdownLabel
    countdownLabel = swing.JLabel("30 seconds")
    countdownLabel.setSize(75, 20)
    countdownLabel.setLocation(100, 500)
    c.add(countdownLabel)

def setComboBox():
    global num
    num = ["1", "2"]
    global playerNum
    playerNum = swing.JComboBox(num)
    playerNum.setSize(69, 27)
    playerNum.setLocation(80, 50)
    c.add(playerNum)

def setTextArea():
    global history
    history = "Welcome to the game!!"
    global gamingProcess
    gamingProcess = swing.JTextArea(history)
    gamingProcess.setSize(250, 60)
    gamingProcess.setLocation(320, 30)
    c.add(gamingProcess)

def setTextFields():
    global RValueStart
    RValueStart = swing.JTextField()
    RValueStart.setSize(50, 25)
    RValueStart.setLocation(150, 250)
    c.add(RValueStart)
    global GValueStart
    GValueStart = swing.JTextField()
    GValueStart.setSize(50, 25)
    GValueStart.setLocation(150, 280)
    c.add(GValueStart)
    global BValueStart
    BValueStart = swing.JTextField()
    BValueStart.setSize(50, 25)
    BValueStart.setLocation(150, 310)
    c.add(BValueStart)
    global RValueEnd
    RValueEnd = swing.JTextField()
    RValueEnd.setSize(50, 25)
    RValueEnd.setLocation(223, 250)
    c.add(RValueEnd)
    global GValueEnd
    GValueEnd = swing.JTextField()
    GValueEnd.setSize(50, 25)
    GValueEnd.setLocation(223, 280)
    c.add(GValueEnd)
    global BValueEnd
    BValueEnd = swing.JTextField()
    BValueEnd.setSize(50, 25)
    BValueEnd.setLocation(223, 310)
    c.add(BValueEnd)

def setPanel():
    global colorDisplay
    colorDisplay = swing.JPanel()
    colorDisplay.setSize(300, 300)
    colorDisplay.setLocation(400, 150)
    colorDisplay.setBackground(awt.Color(255, 255, 255))
    c.add(colorDisplay)

def changeColor(e):
    global RValue
    global GValue
    global BVlaue
    RValue = randint(0, 255)
    GValue = randint(0, 255)
    BValue = randint(0, 255)
    colorDisplay.setBackground(awt.Color(RValue, GValue, BValue))

def startTrigger(event):
    global t
    t = 30
    global timer
    timer = swing.Timer(1000, None, actionPerformed=changeTime)
    timer.start()

def changeTime():
    global t
    t -= 1
    countdownLabel.setText('%d seconds' % t)

frame = swing.JFrame("Color Guess")
c = frame.getContentPane()
frame.setSize(826, 581)
c.setLayout(None)
tRange = xrange(30, 1, -3)
setButtons()
setLabels()
setComboBox()
setTextArea()
setTextFields()
setPanel()
frame.setVisible(True)