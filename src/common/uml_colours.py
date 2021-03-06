"""
style parameter:
----------------
wx.TRANSPARENT	        Transparent (no fill).
wx.SOLID	        Solid.
wx.STIPPLE	        Uses a bitmap as a stipple.
wx.BDIAGONAL_HATCH	Backward diagonal hatch.
wx.CROSSDIAG_HATCH	Cross-diagonal hatch.
wx.FDIAGONAL_HATCH	Forward diagonal hatch.
wx.CROSS_HATCH	        Cross hatch.
wx.HORIZONTAL_HATCH	Horizontal hatch.
wx.VERTICAL_HATCH	Vertical hatch.

predefined brush colors
-----------------------
e.g.
colour=wx.WHITE_BRUSH

BLACK_BRUSH      
BLUE_BRUSH       
CYAN_BRUSH       
GREEN_BRUSH      
GREY_BRUSH       
LIGHT_GREY_BRUSH 
MEDIUM_GREY_BRUSH
RED_BRUSH        
TRANSPARENT_BRUSH
WHITE_BRUSH

all colors
------
e.g.
colour=wx.Brush("WHEAT", wx.SOLID)

import wx.lib.colourdb
wx.lib.colourdb.getColourList()

['SNOW', 'GHOST WHITE', 'GHOSTWHITE', 'WHITE SMOKE', 'WHITESMOKE',
'GAINSBORO', 'FLORAL WHITE', 'FLORALWHITE',
... but many don't actually exists and they render as black! ]

official colours http://www.yellowbrain.com/stc/color_names.html
-----------------------------------------------
AQUAMARINE
BLACK
BLUE
BLUE VIOLET
BROWN
CADET BLUE
CORAL
CORNFLOWER BLUE
CYAN
DARK GREY
DARK GREEN
DARK OLIVE GREEN
DARK ORCHID
DARK SLATE BLUE
DARK SLATE GREY
DARK TURQUOISE
DIM GREY
FIREBRICK
FOREST GREEN
GOLD
GOLDENROD
GREY
GREEN
GREEN YELLOW
INDIAN RED
KHAKI
LIGHT BLUE
LIGHT GREY
LIGHT STEEL BLUE
LIME GREEN
LIGHT MAGENTA
MAGENTA
MAROON
MEDIUM AQUAMARINE
MEDIUM GREY
MEDIUM BLUE
MEDIUM FOREST GREEN
MEDIUM GOLDENROD
MEDIUM ORCHID
MEDIUM SEA GREEN
MEDIUM SLATE BLUE
MEDIUM SPRING GREEN
MEDIUM TURQUOISE
MEDIUM VIOLET RED
MIDNIGHT BLUE
NAVY
ORANGE
ORANGE RED
ORCHID
PALE GREEN
PINK
PLUM
PURPLE
RED
SALMON
SEA GREEN
SIENNA
SKY BLUE
SLATE BLUE
SPRING GREEN
STEEL BLUE
TAN
THISTLE
TURQUOISE
VIOLET
VIOLET RED
WHEAT
WHITE
YELLOW
YELLOW GREEN
MEDIUM GOLDENROD
MEDIUM FOREST GREEN
LIGHT MAGENTA
MEDIUM GREY

Andy verified colors that work
------------------------------
GREEN YELLOW
PINK
SKY BLUE
KHAKI
FOREST GREEN
GOLD
DARK TURQUOISE
MEDIUM ORCHID
CADET BLUE
PALE GREEN
MEDIUM TURQUOISE
AQUAMARINE
SLATE BLUE
MEDIUM AQUAMARINE

"""

# some colours removed by me
official2 = """
WHEAT
PALE GREEN
CADET BLUE
GREEN YELLOW
MEDIUM GOLDENROD
TURQUOISE
TAN
AQUAMARINE
WHITE
THISTLE
CORAL
DARK TURQUOISE
FOREST GREEN
GOLD
GREY
KHAKI
LIGHT GREY
LIGHT STEEL BLUE
LIME GREEN
MEDIUM AQUAMARINE
MEDIUM TURQUOISE
MEDIUM VIOLET RED
GOLDENROD
MEDIUM FOREST GREEN
MEDIUM SEA GREEN
PINK
PLUM
SEA GREEN
SIENNA
SKY BLUE
SLATE BLUE
SPRING GREEN
YELLOW GREEN
"""

good = """
GREEN YELLOW
PINK
SKY BLUE
KHAKI
FOREST GREEN
GOLD
DARK TURQUOISE
MEDIUM ORCHID
CADET BLUE
PALE GREEN
MEDIUM TURQUOISE
AQUAMARINE
SLATE BLUE
MEDIUM AQUAMARINE
"""
        
