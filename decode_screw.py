# coding:utf-8

import os
import shutil
import zlib

PM9SCREW = b'\tPM9SCREW\t'
PM9SCREW_LEN = len(PM9SCREW)
pm9screw_mycryptkey = [11152, 368, 192, 1281, 62]
cryptkey_len = len(pm9screw_mycryptkey)


def decrypt(path, write=True):
    data = open(path, 'rb').read()

    if len(data) < PM9SCREW_LEN:
        return False

    if data[:PM9SCREW_LEN] != PM9SCREW:
        return False
    data = data[PM9SCREW_LEN:]
    datalen = len(data)
    out = ''
    for i in range(datalen):
        tmp = chr((pm9screw_mycryptkey[(datalen - i) % cryptkey_len] ^ (~ord(data[i]))) % 256)
        out += tmp

    new = zlib.decompress(out)
    if write:
        shutil.move(path, path + ".bak")
        open(path, 'w').write(new)
    else:
        print(new)


def multi_decrypt(path):
    if not os.path.exists(path):
        print('Error: %s not Found.' % path)
        return

    if os.path.isdir(path):
        folder = os.walk(path)

        for fpathe, dirs, fs in folder:
            for f in fs:
                if f.endswith('.php'):
                    decrypt(os.path.join(fpathe, f), False)
    else:
        decrypt(path)


if __name__ == '__main__':
    multi_decrypt('./')
