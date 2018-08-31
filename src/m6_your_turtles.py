"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Yuchen ZHU.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(2)
Alpha = rg.SimpleTurtle("turtle")
Beta = rg.SimpleTurtle("turtle")
Alpha.pen = rg.Pen("yellow", 5)
Beta.pen = rg.Pen("red", 1)
Alpha.speed = 100
Beta.speed = 100
Alpha.left(90)
for k in range(20):
    Alpha.draw_regular_polygon(5, 250-k*8)
    Alpha.pen_up()
    Alpha.left(30)
    Alpha.forward(8)
    Alpha.pen_down()
    Beta.draw_circle(140-k*4)
    Beta.pen_up()
    Beta.left(60)
    Beta.forward(4)
    Beta.pen_down()

window.close_on_mouse_click()
