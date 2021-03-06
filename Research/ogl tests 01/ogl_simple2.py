import wx
import wx.lib.ogl as ogl

class AppFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__( self,
                          None, -1, "Demo",
                          size=(300,200),
                          style=wx.DEFAULT_FRAME_STYLE )
        sizer = wx.BoxSizer( wx.VERTICAL )
        # put stuff into sizer

        canvas = ogl.ShapeCanvas( self )
        sizer.Add( canvas, 1, wx.GROW )

        canvas.SetBackgroundColour( "LIGHT BLUE" ) #

        diagram = ogl.Diagram()
        canvas.SetDiagram( diagram )
        diagram.SetCanvas( canvas )

        shape = ogl.RectangleShape( 60, 60 )
        shape.SetX( 30 )
        shape.SetY( 30 )
        print shape.GetBoundingBoxMax()
        canvas.AddShape( shape )

        shape = ogl.RectangleShape( 60, 60 )
        shape.SetX( 90 )
        shape.SetY( 30 )
        canvas.AddShape( shape )

        shape = ogl.RectangleShape( 60, 60 )
        shape.SetX( 150 )
        shape.SetY( 30 )
        canvas.AddShape( shape )

        diagram.ShowAll( 1 )

        # apply sizer
        self.SetSizer(sizer)
        self.SetAutoLayout(1)
        self.Show(1)



app = wx.PySimpleApp()
ogl.OGLInitialize()
frame = AppFrame()
app.MainLoop()
app.Destroy()
