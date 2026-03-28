#python3
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

# I2Cを初期化
i2c = busio.I2C(board.SCL, board.SDA)
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

display.fill(0)  # 画面をクリア
# 横線 (x0, y0, x1, y1)
display.line(0, 10, 127, 10, 1)
display.line(0, 12, 126, 12, 1)
# 縦線
display.line(64, 0, 64, 63, 1)
display.line(62, 0, 62, 62, 1)
# 斜め線
#display.line(0, 0, 127, 63, 1)

display.show()

# 画面を塗りつぶす
#display.fill(1)
#display.show()

# 画面をクリアする
#display.fill(0)
#display.show()