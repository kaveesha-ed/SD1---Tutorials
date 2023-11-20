from graphics import *

# OPEN THE WINDOW
win = GraphWin("My First Graphics Window", 800, 600)
win.setBackground("Mint Cream")

# Define heading
my_heading = Text(Point(100, 30), 'Here is My Heading')
my_heading.setTextColor("grey")
my_heading.setSize(24)
my_heading.setStyle("bold")
my_heading.setFace("helvetica")
my_heading.draw(win)

# Draw a circle
aCircle = Circle(Point(150, 300), 100)
aCircle.draw(win)

# Define subheading
my_sub_heading = Text(Point(140, 60), 'Here is My Subheading')
my_sub_heading.setTextColor("grey")
my_sub_heading.setSize(20)
my_sub_heading.setStyle("bold")
my_sub_heading.setFace("helvetica")
my_sub_heading.draw(win)

# Draw a second circle
b_Circle = Circle(Point(400, 300), 120)
b_Circle.setFill("Lime")
b_Circle.setWidth(0)
b_Circle.draw(win)

# Keep the window open until closed by user
win.mainloop()
