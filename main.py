#python3
from time import sleep
import random
import threading
from enum import Enum


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
STOP_EVENT = threading.Event()
THRED = threading.Thread()

class enmDrawFace(Enum):
    Nomal = 1
    MoveRight = 2
    MoveLeft = 3
    MoveTop = 4
    MoveBottom = 5
    MoveExRight = 6
    MoveExLeft = 7
    MoveExTop = 8
    MoveExBottom = 9

def DrawFace(pDrawFace : enmDrawFace = enmDrawFace.Nomal):
    '''
    顔を描画する
    '''
    if pDrawFace == enmDrawFace.Nomal:
        FaceNomalEyeOpenCloseDraws()

def CheckDrawFaceMode() ->enmDrawFace:
    '''
    描画モードをチェックする
    '''
    return enmDrawFace.Nomal

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
        Show()
        sleep(0.01)

        FaceNomalEyeCloseDraw(DrawMode.Erase)
        FaceNomalEyeDraw(DrawMode.Draw)
        Show()
        EyeOpenTime = random.randint(1, 3)
        sleep(EyeOpenTime)


def Show():
    DISPLAY.show()

def main():

    try:

        LOG.info("=" * 20)
        LOG.info("Starting the application...")
        LOG.info("=" * 20)

        # I2Cを初期化
        i2c = busio.I2C(board.SCL, board.SDA)
        display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

        display.fill(0)  # 画面をクリア
        display.show()

        sleep(1)
        IsDrawThread = False
        BefDrawFaceMode = enmDrawFace.Nomal

        while True:

            DrawFaceMode = CheckDrawFaceMode()

            if DrawFaceMode != BefDrawFaceMode and IsDrawThread == True:
                STOP_EVENT.set()
                THRED.join()
                IsDrawThread = False
                display.fill(0)
                display.show()

            if IsDrawThread == False:
                if DrawFaceMode == enmDrawFace.Nomal:
                    THRED = threading.Thread(target=FaceNomalEyeOpenCloseDraws)
                    THRED.start()
                    IsDrawThread = True

            BefDrawFaceMode = DrawFaceMode

    except KeyboardInterrupt:
        pass
    finally:
        display.fill(0)  # 画面をクリア
        display.show()
        STOP_EVENT.set()
        THRED.join()

if __name__ == "__main__":

    main()
