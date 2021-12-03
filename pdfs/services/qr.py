import qrcode
from fpdf import FPDF


class Qr:
    def __init__(self):
        pass

    @staticmethod
    def generate_qr(url, identifier=None):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        if identifier:
            img_path = '/tmp/'+identifier+'.png'
        else:
            img_path = '/tmp/qrcode001.png'
        img.save(img_path)
        return img_path
