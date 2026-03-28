#python3
from time import sleep

import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from clsFace import clsFace
from clsLineData import clsLineData
from clsDraw import clsDraw, DrawMode


I2C = busio.I2C(board.SCL, board.SDA)
DISPLAY = SSD1306_I2C(128, 64, I2C, addr=0x3C)

def FaceNomalDraw(pDrawMode : DrawMode = DrawMode.Draw):

    face = clsFace()
    bufs = face.Normal()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode.Draw)

def FaceNomalEyeCloseDraw(pDrawMode : DrawMode = DrawMode.Draw):

    face = clsFace()
    bufs = face.NormalEyeClose()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode)

def main():

    # I2Cを初期化
    i2c = busio.I2C(board.SCL, board.SDA)
    display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

    display.fill(0)  # 画面をクリア
    display.show()

    sleep(1)

    FaceNomalDraw(DrawMode.Draw)
    sleep(1)
    FaceNomalDraw(DrawMode.Erase)
    sleep(1)
    FaceNomalEyeCloseDraw(DrawMode.Draw)
    sleep(1)
    FaceNomalEyeCloseDraw(DrawMode.Erase)
    sleep(1)
    FaceNomalDraw(DrawMode.Draw)


if __name__ == "__main__":
    main()