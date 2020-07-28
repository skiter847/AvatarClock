from PIL import Image, ImageDraw, ImageFont
from util import progressbar, percent


def create_image(time: str):
    """
    Создает картинку с временем из строки полученной из параметра time.
    """
    image = Image.new('RGB', (500, 500), color='black')
    W, H = image.size # ширина, высота фото
    draw = ImageDraw.Draw(image)

    clock_font = ImageFont.truetype(font='fonts/num.ttf', size=150)
    progressbar_font = ImageFont.truetype(font='fonts/progressbar.ttf', size=22)
    percent_font = ImageFont.truetype(font='fonts/num.ttf', size=25)

    wt, ht = draw.textsize(time, font=clock_font)
    draw.text(((W - wt) / 2, ((H - ht) / 2) - 60), time, font=clock_font, fill='blue') # write main clock in photo
    draw.text((6, 355), progressbar(time), font=progressbar_font, fill='blue') # write progressbar in photo
    draw.text((410, 350), percent(time), font=percent_font, fill='blue')# write percent in photo

    image.save("clock.png")
