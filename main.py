#python3
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

# I2Cを初期化
i2c = busio.I2C(board.SCL, board.SDA)
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

# 画面を塗りつぶす
display.fill(1)
display.show()

# 画面をクリアする
display.fill(0)
display.show()