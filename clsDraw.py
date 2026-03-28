from enum import Enum
from clsLineData import clsLineData
from adafruit_ssd1306 import SSD1306_I2C

class DrawMode(Enum):
    Draw = 1
    '''描画モード'''
    Erase = 0
    '''消去モード'''

class clsDraw:
    def __init__(self,display: SSD1306_I2C):
        self.list: list[clsLineData] = []
        self.display: SSD1306_I2C | None = display

    def addLine(self, x1, y1, x2, y2, color):
        self.list.append(clsLineData(x1, y1, x2, y2, color))

    def draw(self, DrawMode : DrawMode,offsetX = 0, offsetY = 0):
        for line in self.list:
            if DrawMode == DrawMode.Draw:
                # 描画モード
                self.display.line(line.x1 + offsetX, line.y1 + offsetY, line.x2 + offsetX, line.y2 + offsetY, 1)
            elif DrawMode == DrawMode.Erase:
                # 消去モード
                self.display.line(line.x1 + offsetX, line.y1 + offsetY, line.x2 + offsetX, line.y2 + offsetY, 0)
        self.display.show()

