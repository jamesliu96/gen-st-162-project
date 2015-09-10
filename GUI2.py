import javax.swing as swing
import java.awt as awt
from random import randint

def setButtons():
	global startBut
	startBut=swing.JButton("Start!!", actionPerformed=startGame)
	startBut.setSize(100, 50)
	startBut.setLocation(100, 40)
	c.add(startBut)
	global confirmBut
	confirmBut=swing.JButton("I believe I'm right!!", actionPerformed=oneRound)
	confirmBut.setSize(250, 100)
	confirmBut.setLocation(50, 350)
	confirmBut.setEnabled(False)
	c.add(confirmBut)

def setLabels():
	global questionLabel
	questionLabel=swing.JLabel("What is the value of Red?")
	questionLabel.setSize(300, 50)
	questionLabel.setLocation(110, 120)
	c.add(questionLabel)

def setTextArea():
	global history
	history="Welcome to the game!!"
	global gamingProcess
	gamingProcess=swing.JTextArea(history)
	gamingProcess.setSize(250, 60)
	gamingProcess.setLocation(320, 30)
	gamingProcess.setLineWrap(True)
	gamingProcess.setEditable(False)
	c.add(gamingProcess)


def setPanel():
	global colorDisplay
	colorDisplay=swing.JPanel()
	colorDisplay.setSize(300, 300)
	colorDisplay.setLocation(400, 150)
	colorDisplay.setBackground(awt.Color(255, 255, 255))
	c.add(colorDisplay)

def setRadioButtons():
	global butGroup
	butGroup=swing.ButtonGroup()
	global radioBut1
	radioBut1=swing.JRadioButton("between 0 and 60")
	radioBut1.setSize(150, 20)
	radioBut1.setLocation(120, 210)
	butGroup.add(radioBut1)
	c.add(radioBut1)
	global radioBut2
	radioBut2=swing.JRadioButton("between 61 and 120")
	radioBut2.setSize(150, 20)
	radioBut2.setLocation(120, 230)
	butGroup.add(radioBut2)
	c.add(radioBut2)
	global radioBut3
	radioBut3=swing.JRadioButton("between 121 and 180")
	radioBut3.setSize(150, 20)
	radioBut3.setLocation(120, 250)
	butGroup.add(radioBut3)
	c.add(radioBut3)
	global radioBut4
	radioBut4=swing.JRadioButton("between 181 and 255")
	radioBut4.setSize(150, 20)
	radioBut4.setLocation(120, 270)
	butGroup.add(radioBut4)
	c.add(radioBut4)

def generateRGB():
	global values
	values=[randint(0, 255), randint(0, 255), randint(0, 255)]
	colorDisplay.setBackground(awt.Color(values[0], values[1], values[2]))

def changeProblem():
	RGB=["Red", "Green", "Blue"]
	global serial
	serial=randint(0, 2)
	questionLabel.text="What is the value of "+RGB[serial]+"?"

def startGame(event):
	generateRGB()
	changeProblem()
	global score
	score=0
	startBut.setEnabled(False)
	confirmBut.setEnabled(True)

def oneRound(event):
	if radioBut1.isSelected() and values[serial]>=0 and values[serial]<=60:
		addScore()
	elif radioBut2.isSelected() and values[serial]>60 and values[serial]<=120:
		addScore()
		print 2
	elif radioBut3.isSelected() and values[serial]>120 and values[serial]<=180:
		addScore()
	elif radioBut4.isSelected() and values[serial]>180 and values[serial]<=255:
		addScore()
	else:
		fail()


def addScore():
	global score
	score=score+1
	gamingProcess.setText("Good for you!! The value is "+str(values[serial])+"\nScore: "+str(score))
	generateRGB()
	changeProblem()

def fail():
	global score
	minus=randint(0, 1)
	score=score-minus
	if minus==1:
		gamingProcess.setText("Too bad, Score-1\nScore: "+str(score))
	else:
		gamingProcess.setText("Still wrong, but no points lost!!\nScore: "+str(score))


frame=swing.JFrame("mini_project_04")
c=frame.getContentPane()
#swing.JButton startBut, continueBut, confirmBut
#swing.JLabel playerNumLabel, RLabel, BLabel, GLabel, toLabel01, toLabel02, toLabel03
#swing.JComboBox playerNum
#swing.JTextArea gamingProcess
#swing.JTextField RValueStart, GValueStart, BValueStart, RValueEnd, GValueEnd, BValueEnd
#swing.JPanel colorDisplay
#String history
frame.setSize(826, 581)
#frame.setDefaultCloseOperation(swing.JFrame.EXIT_ON_CLOSE)
c.setLayout(None)
setButtons(); setLabels() 
#setComboBox() 
setTextArea(); setRadioButtons()
#setTextFild()
setPanel()
frame.setVisible(True)
		



