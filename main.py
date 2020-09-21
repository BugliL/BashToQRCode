import pyqrcode
import sys

if __name__ == '__main__':
    qr = pyqrcode.create(sys.argv[1])
    txt = qr.text().replace('0', '\u2588' * 2).replace('1', '\u0020' * 2)
    print(txt)
