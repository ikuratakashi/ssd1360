class clslog:
    def __init__(self):
        pass
    def info(self, message):
        print(f"[INFO] {message}")
    def error(self, message):
        print(f"[ERROR] {message}")
    def warning(self, message):
        print(f"[WARNING] {message}")
    def debug(self, message):
        print(f"[DEBUG] {message}")
