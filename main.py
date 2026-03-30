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
    elif pDrawFace == enmDrawFace.MoveRight or \
         pDrawFace == enmDrawFace.MoveLeft or \
         pDrawFace == enmDrawFace.MoveTop or \
         pDrawFace == enmDrawFace.MoveBottom:
        FaceWowGairoDraws(pDrawFace)

def CheckDrawFaceMode() ->enmDrawFace:
    '''
    描画モードをチェックする
    '''
    result : enmDrawFace = enmDrawFace.MoveLeft

    FaceNo = random.randint(1, 2)
    if FaceNo == 1:
        result = enmDrawFace.Nomal
    elif FaceNo == 2:
        result = random.choice([enmDrawFace.MoveRight, enmDrawFace.MoveLeft, enmDrawFace.MoveTop, enmDrawFace.MoveBottom])

    return result

def FaceNomalDraw(pDrawMode : DrawMode = DrawMode.Draw):
    '''
    通常の顔を描画する
    '''

    face = clsFace()
    bufs = face.Normal()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode)

def FaceNomalEyeDraw(pDrawMode : DrawMode = DrawMode.Draw):
    '''
    通常の顔 目のみを描画する
    '''

    face = clsFace()
    bufs = face.NormalEye()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode)

def FaceNomalEyeCloseDraw(pDrawMode : DrawMode = DrawMode.Draw):
    '''
    通常の顔 目を閉じるを描画する
    '''

    face = clsFace()
    bufs = face.NormalEyeClose()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode)

def FaceNomalEyeOpenCloseDraws():
    '''
    通常の顔 目を開閉する描画をする
    '''

    DISPLAY.fill(0)

    EyeOpenTime = random.randint(1, 3)

    FaceNomalDraw(DrawMode.Draw)
    Show()
    sleep(EyeOpenTime)

    while STOP_EVENT.is_set() == False:

        FaceNomalEyeDraw(DrawMode.Erase)
        FaceNomalEyeCloseDraw(DrawMode.Draw)
        Show()
        sleep(0.01)

        FaceNomalEyeCloseDraw(DrawMode.Erase)
        FaceNomalEyeDraw(DrawMode.Draw)
        Show()

        EyeOpenTime = random.randint(1, 3)
        if STOP_EVENT.is_set() == True:
            break
        sleep(EyeOpenTime)

def FaceWowDraw(pDrawMode : DrawMode = DrawMode.Draw):
    '''
    驚いた顔を描画する
    '''
    face = clsFace()
    bufs = face.Wow()
    Draw = clsDraw(DISPLAY)

    for buf in bufs:
        Draw.addLine(buf[0], buf[1], buf[2], buf[3], buf[4])

    Draw.draw(pDrawMode)
    pass

def FaceWowGairoDraws(pDrawFace : enmDrawFace):
    '''
    驚いた顔を描画する(ジャイロ方向描画あり)
    pDrawFace : 描画する顔の方向
    '''
    DISPLAY.fill(0)
    
    FaceWowDraw(DrawMode.Draw)
    Show()
    while STOP_EVENT.is_set() == False:
        pass
    pass

def Show():
    DISPLAY.show()

def main():

    try:

        LOG.info("=" * 40)
        LOG.info("Starting the application...")
        LOG.info("=" * 40)

        DISPLAY.fill(0)  # 画面をクリア
        DISPLAY.show()

        sleep(1)
        IsDrawThread = False
        BefDrawFaceMode = enmDrawFace.Nomal

        while True:

            DrawFaceMode = CheckDrawFaceMode()

            LOG.debug(f"DrawFaceMode: {DrawFaceMode}")

            if DrawFaceMode != BefDrawFaceMode and IsDrawThread == True:
                STOP_EVENT.set()
                THRED.join() # スレッドの終了を待つ
                STOP_EVENT.clear()
                IsDrawThread = False

            if IsDrawThread == False:

                if DrawFaceMode == enmDrawFace.Nomal:
                    '''
                    通常の顔を描画する
                    '''
                    THRED = threading.Thread(target=FaceNomalEyeOpenCloseDraws)
                    THRED.start()
                    IsDrawThread = True

                if DrawFaceMode == enmDrawFace.MoveRight or \
                   DrawFaceMode == enmDrawFace.MoveLeft or \
                   DrawFaceMode == enmDrawFace.MoveTop or \
                   DrawFaceMode == enmDrawFace.MoveBottom :
                    '''
                    驚いた顔を描画する(ジャイロ方向描画あり)
                    '''
                    THRED = threading.Thread(target=FaceWowGairoDraws, args=(DrawFaceMode,))
                    THRED.start()
                    IsDrawThread = True

            BefDrawFaceMode = DrawFaceMode

            sleep(5)

    except KeyboardInterrupt:
        pass
    finally:
        DISPLAY.fill(0)  # 画面をクリア
        DISPLAY.show()
        STOP_EVENT.set()
        THRED.join() # スレッドの終了を待つ
        STOP_EVENT.clear()

if __name__ == "__main__":

    main()
