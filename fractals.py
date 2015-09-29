# fractals.py

# by Alex Olson & Kiya Govek
# CS111, Fall 2014


import math
from graphics import *

def vonKochSegment(level, start, heading, length, window):
    """ This function takes five arguments: a level (The number of times you repeat the 
    expansion process), a starting point, a heading (in degrees counterclockwise from due 
    east on the screen), a length of the line, and the graphics window in which to draw 
    the resulting image. The function returns the ending point of the segment. """
    
    # base case is just a regular line segment
    if level == 0:
        # calculate end point using heading and length
        endX = start.getX() + int(length * math.cos(math.radians(heading)))
        endY = start.getY() - int(length * math.sin(math.radians(heading)))
        end = Point(endX,endY)
        line = Line(start, end)
        # only draw these level 0 lines so we don't draw redundant lines
        line.draw(window)
        return end
    
    else:
        # each segment will comprise of four other segments of level-1
        end1 = vonKochSegment(level-1, start, heading, length / 3.0, window)
        end2 = vonKochSegment(level-1, end1, heading - 60, length / 3.0, window)
        end3 = vonKochSegment(level-1, end2, heading + 60, length / 3.0, window)
        end4 = vonKochSegment(level-1, end3, heading, length / 3.0, window)
        return end4

    
def vonKoch(length, level):
    """ This function creates a graphics window and draws three von Kock segments
    of level 'level' arranged in an equilateral triangle. The first one heads in
    direction 0, the second heads in direction 120 from the first side, and the third 
    heads in direction 240 from the end of the second side. """
    
    window = GraphWin( 'von Koch Snowflake', length * 1.5, length * 1.5)
    p1 = Point(length / 4.0, length)
    # one full snowflake takes three segments, each starting at the endpoint of the previous segment
    p2 = vonKochSegment(level, p1, 0.0, length, window)
    p3 = vonKochSegment(level, p2, 120.0, length, window)
    p4 = vonKochSegment(level, p3, 240.0, length, window)
    
# We ask you to kindly not use any level greater than 5
# that uses too much precision for pixels to handle.
# We ran into some 'squished' snowflakes once we started using
# with small windows or large levels, probably because of the
# constraints of pixels only being integers


# draws a snowflake of level 3
vonKoch(400, 3)


# this line of user input keeps the graphics window open until the user presses 'enter'
raw_input('Press enter to quit')
    
