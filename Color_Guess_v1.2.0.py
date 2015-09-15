import javax.swing as swing
import java.awt as awt
from random import randint
from decimal import *

class Game:
    def __init__(self):
        self.frame = swing.JFrame("Color Guess v1.2.0")
        self.c = self.frame.getContentPane()
        self.frame.setSize(826, 581)
        self.c.setLayout(None)
        self.setButtons()
        self.setLabels()
        self.setTextArea()
        self.setRadioButtons()
        self.setPanel()
        self.setComboBox()
        self.frame.setVisible(True)

    def setButtons(self):
        self.startBut = swing.JButton("Start!", actionPerformed=self.startGame)
        self.startBut.setSize(100, 50)
        self.startBut.setLocation(100, 35)
        self.c.add(self.startBut)
        self.confirmBut = swing.JButton("I believe I'm right!", actionPerformed=self.oneRound)
        self.confirmBut.setSize(250, 100)
        self.confirmBut.setLocation(50, 350)
        self.confirmBut.setEnabled(False)
        self.c.add(self.confirmBut)
        self.quitBut = swing.JButton("QUIT!?", actionPerformed=self.quitGame)
        self.quitBut.setSize(100, 50)
        self.quitBut.setLocation(610, 35)
        self.quitBut.setEnabled(False)
        self.c.add(self.quitBut)

    def setLabels(self):
        self.questionLabel = swing.JLabel("What is the value of Red?")
        self.questionLabel.setSize(300, 50)
        self.questionLabel.setLocation(110, 120)
        self.c.add(self.questionLabel)

    def setTextArea(self):
        self.history = "Welcome to the game!!\nIf you guess incorectly 20 times then the game will end!"
        self.gamingProcess = swing.JTextArea(self.history)
        self.gamingProcess.setSize(310, 60)
        self.gamingProcess.setLocation(220, 35)
        self.gamingProcess.setLineWrap(True)
        self.gamingProcess.setEditable(False)
        self.gamingProcess.setBackground(awt.Color(238, 238, 238))
        self.c.add(self.gamingProcess)

    def setPanel(self):
        self.colorDisplay = swing.JPanel()
        self.colorDisplay.setSize(300, 300)
        self.colorDisplay.setLocation(400, 150)
        self.colorDisplay.setBackground(awt.Color(255, 255, 255))
        self.c.add(self.colorDisplay)
        self.life = []
        for i in xrange(0, 20):
            self.life.append(swing.JPanel())
            self.life[i].setSize(10, 10)
            self.life[i].setLocation(220 + i * 20, 98)
            self.life[i].setBackground(awt.Color(238, 238, 238))
            self.c.add(self.life[i])

    def setRadioButtons(self):
        self.butGroup = swing.ButtonGroup()
        self.radioBut1 = swing.JRadioButton()
        self.radioBut1.setSize(270, 20)
        self.radioBut1.setLocation(120, 210)
        self.butGroup.add(self.radioBut1)
        self.c.add(self.radioBut1)
        self.radioBut2 = swing.JRadioButton()
        self.radioBut2.setSize(270, 20)
        self.radioBut2.setLocation(120, 230)
        self.butGroup.add(self.radioBut2)
        self.c.add(self.radioBut2)
        self.radioBut3 = swing.JRadioButton()
        self.radioBut3.setSize(270, 20)
        self.radioBut3.setLocation(120, 250)
        self.butGroup.add(self.radioBut3)
        self.c.add(self.radioBut3)
        self.radioBut4 = swing.JRadioButton()
        self.radioBut4.setSize(270, 20)
        self.radioBut4.setLocation(120, 270)
        self.butGroup.add(self.radioBut4)
        self.c.add(self.radioBut4)

    def setComboBox(self):
        self.MODE = ["RGB", "HSV"]
        self.gameMode = swing.JComboBox(self.MODE)
        self.gameMode.setSize(100, 30)
        self.gameMode.setLocation(100, 90)
        self.c.add(self.gameMode)

    def generateRGB(self):
        self.values = [[randint(0, 255), randint(0, 255), randint(0, 255)]]
        self.getHSV()
        self.colorDisplay.setBackground(awt.Color(self.values[0][0], self.values[0][1], self.values[0][2]))

    def getHSV(self):
        M = -1.0
        m = 300.0
        MChoice = 0
        for i in xrange(0, 3):
            if self.values[0][i] > M:
                M = self.values[0][i]
                MChoice = i
            if self.values[0][i] < m:
                m = self.values[0][i]
        V = M / 255.0
        S = 0.0
        if M > 0:
            S = (M - m) * 1.0 / M * 1.0
        else:
            S = 0.0
        H = 0.0
        C = (M - m)
        if S == 0:
            H = 0.0
        elif MChoice == 0:
            H = (self.values[0][1] - self.values[0][2]) / C % 6
        elif MChoice == 1:
            H = (self.values[0][2] - self.values[0][0]) * 1.0 / C + 2
        elif MChoice == 2:
            H = (self.values[0][0] - self.values[0][1]) * 1.0 / C + 4
        H = H * 60 / 360.0
        self.values.append([round(H, 3), round(S, 3), round(V, 3)])

    def changeProblem(self):
        self.question = [["Red", "Green", "Blue"], ["HUE", "SATURATION", "VALUE"]]
        self.serial = randint(0, 2)
        if self.serial == 0:
            self.questionLabel.setForeground(awt.Color.RED)
            self.questionLabel.text = "What is the value of " + self.question[self.choice][self.serial] + "?"
        elif self.serial == 1:
            self.questionLabel.setForeground(awt.Color(0, 200, 0))
            self.questionLabel.text = "What is the value of " + self.question[self.choice][self.serial] + "?"
        elif self.serial == 2:
            self.questionLabel.setForeground(awt.Color.BLUE)
            self.questionLabel.text = "What is the value of " + self.question[self.choice][self.serial] + "?"
        else:
            self.questionLabel.setForeground(awt.Color.BLACK)
            self.questionLabel.text = "What is the value of " + self.question[self.choice][self.serial] + "?"

    def startGame(self, event):
        self.gameChoice()
        self.generateRGB()
        self.changeProblem()
        self.gamingProcess.setText("Welcome to the game!!\nIf you guess incorectly 20 times then the \ngame will end!")
        self.wrongAnswers = 20
        self.score = 0
        self.startBut.setEnabled(False)
        self.confirmBut.setEnabled(True)
        self.gameMode.setEnabled(False)
        self.quitBut.setEnabled(True)
        for i in xrange(0, 20):
            self.life[i].setBackground(awt.Color(255, 0, 0))

    def gameChoice(self):
        self.choice = self.gameMode.getSelectedIndex()
        self.options = [["between 0 and 60", "between 61 and 120", "between 121 and 180","between 181 and 255"], ["0<=answer<=0.25", "0.25<answer<=0.5", "0.5<answer<=0.75", "0.75<answer<1"]]
        self.radioBut1.setText(self.options[self.choice][0])
        self.radioBut2.setText(self.options[self.choice][1])
        self.radioBut3.setText(self.options[self.choice][2])
        self.radioBut4.setText(self.options[self.choice][3])

    def oneRound(self, event):
        self.threshold = [
            [
                [0, 60], [60, 120], [120, 180], [180, 256]
            ], [
                [0.0, 0.25], [0.25, 0.5], [0.5, 0.75], [0.75, 1.0]
            ]
        ]
        if self.radioBut1.isSelected() and self.values[self.choice][self.serial] >= self.threshold[self.choice][0][0] and self.values[self.choice][self.serial] <= self.threshold[self.choice][0][1]:
            self.addScore()
        elif self.radioBut2.isSelected() and self.values[self.choice][self.serial] > self.threshold[self.choice][1][0] and self.values[self.choice][self.serial] <= self.threshold[self.choice][1][1]:
            self.addScore()
        elif self.radioBut3.isSelected() and self.values[self.choice][self.serial] > self.threshold[self.choice][2][0] and self.values[self.choice][self.serial] <= self.threshold[self.choice][2][1]:
            self.addScore()
        elif self.radioBut4.isSelected() and self.values[self.choice][self.serial] > self.threshold[self.choice][3][0] and self.values[self.choice][self.serial] < self.threshold[self.choice][3][1]:
            self.addScore()
        else:
            self.fail()
        self.checkProgress()

    def addScore(self):
        self.score += 1
        self.gamingProcess.setText("Good for you!! The value is " + str(self.values[self.choice][self.serial]) + "\nScore: " + str(self.score))
        self.generateRGB()
        self.changeProblem()

    def fail(self):
        self.wrongAnswers -= 1
        minus = randint(0, 1)
        self.score -= minus
        if minus == 1:
            self.gamingProcess.setText("Too bad, Score -1\nScore: " + str(self.score))
        else:
            self.gamingProcess.setText("Still wrong, but no points lost!!\nScore: " + str(self.score))
        self.life[self.wrongAnswers].setBackground(awt.Color(238, 238, 238))


    def quitGame(self, event):
        self.gameSummary()

    def gameSummary(self):
        self.confirmBut.setEnabled(False)
        self.startBut.setEnabled(True)
        self.gameMode.setEnabled(True)
        self.quitBut.setEnabled(False)
        self.gamingProcess.setText("GAME OVER\nYou guessed wrong " + str(20 - self.wrongAnswers) + " times\nFinal Score: " + str(self.score))

    def checkProgress(self):
        if self.wrongAnswers <= 0:
            self.gameSummary()

game = Game()