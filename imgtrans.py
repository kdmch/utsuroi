from PIL import Image, ImageFilter, ImageMath
import datetime

def iconhsv(imagepath,quality):
  im  = Image.open(imagepath)
  now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
  huedelta = round(((now.hour * 60 + now.minute) / 1440) * 256)
  h, s, v  = im.convert('HSV').split()
  _h = ImageMath.eval('(h + d) % 255', h=h, d=huedelta).convert('L')
  im = Image.merge('HSV', (_h, s, v)).convert('RGB')
  
  im_resized = im.resize((400,400))
  im_resized.save('img/processed.jpg', quality=quality)
