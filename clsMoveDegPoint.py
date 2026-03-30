import math
from adafruit_ssd1306 import SSD1306_I2C
from clsDraw import DrawMode

class clsMoveDegPoint:
    def __init__(self,disp : SSD1306_I2C, st_x, st_y, deg ,distance ,xmax = 127, ymax = 63):
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

    def MovePointDraw(self):

        if self.IsFirst == False:
            angle = math.radians(self.deg)  # 度 → ラジアン

            self.x = self.x + self.distance * math.cos(angle)
            self.y = self.y + self.distance * math.sin(angle)

            if(self.x > self.xmax or self.y > self.ymax):
                self.x = self.st_x
                self.y = self.st_y

            self.MovePointErase()
            
        self.disp.line(self.x,self.y,self.x,self.y, 1)

        self.bef_x = self.x
        self.bef_y = self.y

        self.IsFirst = False

        return 
    
    def MovePointErase(self):
        self.disp.line(self.bef_x,self.bef_y,self.bef_x,self.bef_y, 0)
        return 
