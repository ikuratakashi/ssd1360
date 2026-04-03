import math
from adafruit_ssd1306 import SSD1306_I2C
from clsDraw import DrawMode
from clsLog import clslog

class clsMoveDegPoint:
    def __init__(self,disp : SSD1306_I2C, st_x, st_y, deg ,distance ,xmax = 127, ymax = 63,Log: clslog = None):
        self.disp: SSD1306_I2C = disp
        self.xmax = xmax
        self.ymax = ymax
        self.st_x = st_x
        self.st_y = st_y
        self.x = st_x
        self.y = st_y
        self.bef_x = st_x
        self.bef_y = st_y
        self.deg = deg
        self.distance = distance
        self.IsFirst = True
        self.LOG = Log

    def MovePointDraw(self):

        if self.IsFirst == False:
            angle = math.radians(self.deg)  # 度 → ラジアン

            self.x = self.x + self.distance * math.cos(angle)
            self.y = self.y + self.distance * math.sin(angle)

            self.x = int(self.x)
            self.y = int(self.y)

            if self.deg == 0:
                if(self.x > self.xmax):
                    self.x = 0
                    self.y = self.st_y
            elif self.deg == 180:
                if(self.x < 0):
                    self.x = self.xmax
                    self.y = self.st_y
            elif self.deg == 90:
                if(self.y > self.ymax):
                    self.x = self.st_x
                    self.y = 0
            elif self.deg == 270:
                if(self.y < 0):
                    self.x = self.st_x
                    self.y = self.ymax

            self.MovePointErase()

        self.disp.line(self.x,self.y,self.x,self.y, 1)

        self.bef_x = self.x
        self.bef_y = self.y

        self.IsFirst = False

        return 
    
    def MovePointErase(self):
        self.disp.line(self.bef_x,self.bef_y,self.bef_x,self.bef_y, 0)
        return 
