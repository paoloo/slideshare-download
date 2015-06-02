from lxml import html as _parse
import urllib, os

class slideshare():

  def __init__(self,url=''):
    self._url = url

  def download(self):
    _site = urllib.urlopen(self._url)
    _arvore = _parse.fromstring(_site.read())
    _site.close()
    _slides = _arvore.xpath('//img[@class="slide_image"]')
    slide_cntr=1
    for _slide in _slides:
      _s = _slide.get("data-full")
      urllib.urlretrieve("%s" % _s, "s_%0.9d.jpg" % slide_cntr)
      slide_cntr+=1

  def genPDF(self):
    os.system("convert s_*.jpg slides.pdf")
    os.system("rm s_*.jpg")

  def baixa(self):
    self.download()
    self.genPDF()

if __name__ == "__main__":
  import sys
  if len(sys.argv) != 2:
    print "slideshare.py -- Slideshare Downloader  "
    print "sintaxe: ./slideshare.py [url]"
    sys.exit(1)
  else:
    slideshare(sys.argv[1]).baixa()
