from javax.swing import *;
from java.awt import *;
frame=JFrame("mini_project_04");
c=frame.getContentPane();
#JButton startBut, continueBut, confirmBut;
#JLabel playerNumLabel, RLabel, BLabel, GLabel, toLabel01, toLabel02, toLabel03;
#JComboBox playerNum;
#JTextArea gamingProcess;
#JTextField RValueStart, GValueStart, BValueStart, RValueEnd, GValueEnd, BValueEnd;
#JPanel colorDisplay;
#String history;
frame.setSize(826, 581);
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
c.setLayout(null);
setButtons(); setLabels(); setComboBox(); setTextArea();
setTextFild(); setPanel();
frame.setVisible(true);
		
def setButtons():
	global startBut
	startBut=JButton("Start!!");
	startBut.setSize(69, 27);
	startBut.setLocation(160, 40);
	c.add(startBut);
	global ontinueBut;
	continueBut=JButton("Continue");
	continueBut.setSize(100, 50);
	continueBut.setLocation(600, 40);
	c.add(continueBut);
	global confirmBut;
	confirmBut=JButton("I belive I'm right!!");
	confirmBut.setSize(250, 100);
	confirmBut.setLocation(50, 350);
	c.add(confirmBut);
def setLabels():
	global playerNumLabel;
	playerNumLabel=JLabel("Players: ");
	playerNumLabel.setSize(75, 20);
	playerNumLabel.setLocation(80, 30);
	playerNumLabel.setFont(new Font("Arial", Font.PLAIN, 15));
	c.add(playerNumLabel);
	global RLabel;
	RLabel=JLabel("Red value: ");
	RLabel.setSize(73, 18);
	RLabel.setLocation(50, 250);
	c.add(RLabel);
	global GLabel;
	GLabel=JLabel("Green value: ");
	GLabel.setSize(73, 18);
	GLabel.setLocation(50, 280);
	c.add(GLabel);
	global BLabel;
	BLabel=JLabel("Blue value: ");
	BLabel.setSize(73, 18);
	BLabel.setLocation(50, 310);
	c.add(BLabel);
	global toLabel01;
	toLabel01=JLabel("to");
	toLabel01.setSize(17, 24);
	toLabel01.setLocation(203, 250);
	c.add(toLabel01);
	global toLabel02;
	toLabel02=JLabel("to");
	toLabel02.setSize(17, 24);
	toLabel02.setLocation(203, 280);
	c.add(toLabel02);
	global toLabel03;
	toLabel03=JLabel("to");
	toLabel03.setSize(17, 24);
	toLabel03.setLocation(203, 310);
	c.add(toLabel03);

def setComboBox():
	String[] num={"1", "2"};
	playerNum=new JComboBox(num);
	playerNum.setSize(69, 27);
	playerNum.setLocation(80, 50);
	c.add(playerNum);

def setTextArea():
	history="Welcome to the game!!";
	gamingProcess=new JTextArea(history);
	gamingProcess.setSize(250, 60);
	gamingProcess.setLocation(320, 30);
	c.add(gamingProcess);

def setTextFild():
	RValueStart=new JTextField();
	RValueStart.setSize(50, 25);
	RValueStart.setLocation(150, 250);
	c.add(RValueStart);
	GValueStart=new JTextField();
	GValueStart.setSize(50, 25);
	GValueStart.setLocation(150, 280);
	c.add(GValueStart);
	BValueStart=new JTextField();
	BValueStart.setSize(50, 25);
	BValueStart.setLocation(150, 310);
	c.add(BValueStart);
	RValueEnd=new JTextField();
	RValueEnd.setSize(50, 25);
	RValueEnd.setLocation(223, 250);
	c.add(RValueEnd);
	GValueEnd=new JTextField();
	GValueEnd.setSize(50, 25);
	GValueEnd.setLocation(223, 280);
	c.add(GValueEnd);
	BValueEnd=new JTextField();
	BValueEnd.setSize(50, 25);
	BValueEnd.setLocation(223, 310);
	c.add(BValueEnd);

def setPanel():
	colorDisplay=new JPanel();
	colorDisplay.setSize(300, 300);
	colorDisplay.setLocation(400, 150);
	colorDisplay.setBackground(new Color(255, 255, 255));
	c.add(colorDisplay);


