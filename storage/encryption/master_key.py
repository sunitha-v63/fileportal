import os

MASTER_KEY_PATH = "master.key"

def load_master_key():
    if not os.path.exists(MASTER_KEY_PATH):
        key = os.urandom(32)   # 256-bit key
        with open(MASTER_KEY_PATH, "wb") as f:
            f.write(key)
        return key
    return open(MASTER_KEY_PATH, "rb").read()
