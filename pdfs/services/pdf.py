from core.settings import MEDIA_ROOT
from fpdf import FPDF
from math import sqrt
from pdfs.services.qr import Qr
import logging
import uuid


class Pdf(FPDF):
    logger = logging.getLogger(__name__)

    def generate_pdf(self, url=None, mesas=[1, 2, 3]):
        self.logger.info("Generating pdf for tables {}".format(mesas))
        pdf = Pdf(orientation='P', unit='mm', format='A4')
        for mesa in mesas:
            pdf.add_page()
            qr_url = "{}?q=mesa{}".format(url, mesa)
            image_path = Qr.generate_qr(qr_url, identifier=str(uuid.uuid4()))
            pdf.image(image_path, 10, 10, 45, 45)
            pdf.set_draw_color(200, 200, 200)
            pdf.set_line_width(.5)
            pdf.rounded_rect(10, 10, 85, 55, 2, 'D', '1234')
            pdf.set_font('Arial', 'B', 12)
            pdf.set_y(52)
            pdf.cell(70, 10, "Mesa {}".format(mesa), align='R')
            pdf.image(MEDIA_ROOT + '/logo.png', 15, 50, 35, 15)
            pdf.image(MEDIA_ROOT + '/logo2.jpg', 50, 15, 40, 40)
        # pdf.output('/tmp/test.pdf', 'F')
        return pdf

    def rounded_rect(self, x, y, w, h, r, style='', corners='1234'):

        k = self.k
        hp = self.h
        if (style == 'F'):
            op = 'f'
        elif (style == 'FD' or style == 'DF'):
            op = 'B'
        else:
            op = 'S'
        myArc = 4 / 3 * (sqrt(2) - 1)
        self._out('%.2F %.2F m' % ((x + r) * k, (hp - y) * k))

        xc = x + w - r
        yc = y + r
        self._out('%.2F %.2F l' % (xc * k, (hp - y) * k))
        if '2' not in corners:
            self._out('%.2F %.2F l' % ((x + w) * k, (hp - y) * k))
        else:
            self._arc(xc + r * myArc, yc - r, xc + r, yc - r * myArc, xc + r, yc)

        xc = x + w - r
        yc = y + h - r
        self._out('%.2F %.2F l' % ((x + w) * k, (hp - yc) * k))
        if '3' not in corners:
            self._out('%.2F %.2F l' % ((x + w) * k, (hp - (y + h)) * k))
        else:
            self._arc(xc + r, yc + r * myArc, xc + r * myArc, yc + r, xc, yc + r)

        xc = x + r
        yc = y + h - r
        self._out('%.2F %.2F l' % (xc * k, (hp - (y + h)) * k))
        if '4' not in corners:
            self._out('%.2F %.2F l' % (x * k, (hp - (y + h)) * k))
        else:
            self._arc(xc - r * myArc, yc + r, xc - r, yc + r * myArc, xc - r, yc)

        xc = x + r
        yc = y + r
        self._out('%.2F %.2F l' % (x * k, (hp - yc) * k))
        if '1' not in corners:
            self._out('%.2F %.2F l' % (x * k, (hp - y) * k))
            self._out('%.2F %.2F l' % ((x + r) * k, (hp - y) * k))
        else:
            self._arc(xc - r, yc - r * myArc, xc - r * myArc, yc - r, xc, yc - r)
        self._out(op)

    def _arc(self, x1, y1, x2, y2, x3, y3):

        h = self.h
        self._out('%.2F %.2F %.2F %.2F %.2F %.2F c ' % (x1 * self.k, (h - y1) * self.k,
                                                        x2 * self.k, (h - y2) * self.k, x3 * self.k, (h - y3) * self.k))

