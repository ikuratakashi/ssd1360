from smbus2 import SMBus
import time

addr = 0x68
bus = SMBus(1)

# MPU 初期化
bus.write_byte_data(addr, 0x6B, 0)

def read_word(reg):
    high = bus.read_byte_data(addr, reg)
    low = bus.read_byte_data(addr, reg + 1)
    val = (high << 8) + low
    if val >= 0x8000:
        val = -((65535 - val) + 1)
    return val

def read_accel():
    ax = read_word(0x3B) / 16384.0
    ay = read_word(0x3D) / 16384.0
    az = read_word(0x3F) / 16384.0
    return ax, ay, az

threshold = 0.2  # ノイズ除去のための閾値

while True:
    ax, ay, az = read_accel()

    direction = ""

    # 左右
    if ax > threshold:
        direction = "右"
    elif ax < -threshold:
        direction = "左"

    # 上下（重力補正なしの簡易版）
    if az > 1.0 + threshold:
        direction = "上"
    elif az < 1.0 - threshold:
        direction = "下"

    print(f"AX={ax:.2f}, AY={ay:.2f}, AZ={az:.2f} → {direction}")
    time.sleep(0.1)