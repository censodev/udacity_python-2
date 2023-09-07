import os
import random
import time
from PIL import Image, ImageDraw, ImageFont

from utils import build_abs_local_path


class MemeEngine:
    def __init__(self, output_dir) -> None:
        self.output_dir = output_dir
        abs_local_output_dir = build_abs_local_path(output_dir)
        if not os.path.exists(abs_local_output_dir):
            os.makedirs(abs_local_output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        with Image.open(img_path) as img:
            height = int(width / img.width * img.height)
            img = img.resize((width, height))
            draw = ImageDraw.Draw(img)
            text_position = random.choice(range(20, height - 100))
            fill = (0, 0, 0)
            stroke_fill = (255, 255, 255)
            fontBody = ImageFont.truetype(build_abs_local_path(
                './_data/fonts/Roboto-Bold.ttf'), 24)
            draw.text((20, text_position), text, fill, fontBody,
                      stroke_width=1, stroke_fill=stroke_fill)
            fontAuth = ImageFont.truetype(build_abs_local_path(
                './_data/fonts/Roboto-Bold.ttf'), 16)
            draw.text((50, text_position + 30),
                      f'by {author}', fill, fontAuth, stroke_width=1, stroke_fill=stroke_fill)
            filepath = f'{time.time()}.jpg'
            outfile = f'{self.output_dir}/{filepath}'
            img.save(build_abs_local_path(outfile), 'JPEG')
            return outfile
