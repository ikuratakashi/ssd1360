#python3
from time import sleep
import random

import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from clsFace import clsFace
from clsLineData import clsLineData
from clsDraw import clsDraw, DrawMode
from clsLog import clslog


I2C = busio.I2C(board.SCL, board.SDA)
DISPLAY = SSD1306_I2C(128, 64, I2C, addr=0x3C)
LOG = clslog()

def FaceNomalDraw(pDrawMode : DrawMode = DrawMode.Draw):

    face = clsFace()
    bufs = face.Normal()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode)

def FaceNomalEyeDraw(pDrawMode : DrawMode = DrawMode.Draw):

    face = clsFace()
    bufs = face.NormalEye()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode)

def FaceNomalEyeCloseDraw(pDrawMode : DrawMode = DrawMode.Draw):

    face = clsFace()
    bufs = face.NormalEyeClose()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode)

def FaceNomalEyeOpenCloseDraws():

    EyeOpenTime = random.randint(1, 3)

    FaceNomalDraw(DrawMode.Draw)
    Show()
    sleep(EyeOpenTime)

    while True:

        FaceNomalEyeDraw(DrawMode.Erase)
        FaceNomalEyeCloseDraw(DrawMode.Draw)
        sleep(0.01)
        Show()

        FaceNomalEyeCloseDraw(DrawMode.Erase)
        FaceNomalEyeDraw(DrawMode.Draw)
        EyeOpenTime = random.randint(1, 3)
        sleep(EyeOpenTime)
        Show()


def Show():
    DISPLAY.show()

def main():

    try:

        LOG.info("■" * 20)
        LOG.info("Starting the application...")
        LOG.info("■" * 20)

        # I2Cを初期化
        i2c = busio.I2C(board.SCL, board.SDA)
        display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

        display.fill(0)  # 画面をクリア
        display.show()

        sleep(1)

        FaceNomalEyeOpenCloseDraws()

    except KeyboardInterrupt:
        pass
    finally:
        display.fill(0)  # 画面をクリア
        display.show()

if __name__ == "__main__":

    main()
