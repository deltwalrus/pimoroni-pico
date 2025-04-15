# A retro badge with photo and QR code.
# Copy your image to your Tufty alongside this example - it should be a 120 x 120 jpg.

from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from pimoroni import Button
import time
import jpegdec
import qrcode

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
button_c = Button(9, invert=False)

WIDTH, HEIGHT = display.get_bounds()

# Uncomment one of these colour palettes - find more at lospec.com !
# Nostalgia colour palette by WildLeoKnight - https://lospec.com/palette-list/nostalgia
# LIGHTEST = display.create_pen(208, 208, 88)
# LIGHT = display.create_pen(160, 168, 64)
# DARK = display.create_pen(112, 128, 40)
# DARKEST = display.create_pen(64, 80, 16)

# Greyscale Palette – Monochrome Classic
# LIGHTEST = display.create_pen(255, 255, 255)   # White
# LIGHT = display.create_pen(192, 192, 192)      # Light Gray
# DARK = display.create_pen(96, 96, 96)          # Dark Gray
# DARKEST = display.create_pen(0, 0, 0)          # Black

# --- Kirokaze Gameboy ---
# # Hex: #e0f8cf, #86c06c, #306850, #081820
# LIGHTEST = display.create_pen(224, 248, 207)
# LIGHT = display.create_pen(134, 192, 108)
# DARK = display.create_pen(48, 104, 80)
# DARKEST = display.create_pen(8, 24, 32)

# # --- Crimson ---
# # Hex: #f9f4ef, #d36135, #78290f, #250001
# LIGHTEST = display.create_pen(249, 244, 239)
# LIGHT = display.create_pen(211, 97, 53)
# DARK = display.create_pen(120, 41, 15)
# DARKEST = display.create_pen(37, 0, 1)

# --- Ice Cream GB ---
# Hex: #ffffff, #ffb6b6, #ff7f7f, #ff0000
# LIGHTEST = display.create_pen(255, 255, 255)
# LIGHT = display.create_pen(255, 182, 182)
# DARK = display.create_pen(255, 127, 127)
# DARKEST = display.create_pen(255, 0, 0)

# # --- GB Chocolate ---
# # Hex: #eec39a, #a46e4a, #693d2b, #2c1b1b
# LIGHTEST = display.create_pen(238, 195, 154)
# LIGHT = display.create_pen(164, 110, 74)
# DARK = display.create_pen(105, 61, 43)
# DARKEST = display.create_pen(44, 27, 27)

# # --- b4sement ---
# # Hex: #3dff98, #ff4adc, #222323, #f0f6f0
# LIGHTEST = display.create_pen(61, 255, 152)
# LIGHT = display.create_pen(255, 74, 220)
# DARK = display.create_pen(34, 35, 35)
# DARKEST = display.create_pen(240, 246, 240)

# Warm Amber-Orange Terminal CRT Palette (think VT132 vibes) - added by deltwaurs
# LIGHTEST = display.create_pen(255, 140, 0)   # Bright warm orange
#LIGHT = display.create_pen(255, 115, 0)      # Mid orange
# DARK = display.create_pen(180, 70, 0)        # Dim orange 
# DARKEST = display.create_pen(0, 0, 0)        # Background black

# Amber Terminal CRT Palette - added by deltwalrus
# LIGHTEST = display.create_pen(255, 191, 0)   # Bright Amber
# LIGHT = display.create_pen(200, 150, 0)      # Soft Amber
# DARK = display.create_pen(100, 75, 0)        # Dim Amber
# DARKEST = display.create_pen(0, 0, 0)        # Black Background

# 2bit Demichrome colour palette by Space Sandwich - https://lospec.com/palette-list/2bit-demichrome
# LIGHTEST = display.create_pen(233, 239, 236)
# LIGHT = display.create_pen(160, 160, 139)
# DARK = display.create_pen(85, 85, 104)
# DARKEST = display.create_pen(33, 30, 32)

# CGA PALETTE 1 (HIGH) - https://lospec.com/palette-list/cga-palette-1-high
# LIGHTEST = display.create_pen(255, 255, 255)
# LIGHT = display.create_pen(85, 254, 255)
# DARK = display.create_pen(255, 85, 255)
# DARKEST = display.create_pen(0, 0, 0)

# --- Velvet Cherry GB ---
# Hex: #3a1a2c, #7a3e6a, #d77fa1, #f9b9c3
# DARKEST = display.create_pen(58, 26, 44)
# DARK = display.create_pen(122, 62, 106)
# LIGHT = display.create_pen(215, 127, 161)
# LIGHTEST = display.create_pen(249, 185, 195)

# # --- Coral 4 ---
# # Hex: #ffd0a4, #f4949c, #7c9aac, #68518a
LIGHTEST = display.create_pen(255, 208, 164)
LIGHT = display.create_pen(244, 148, 156)
DARK = display.create_pen(124, 154, 172)
DARKEST = display.create_pen(104, 81, 138)

# # --- EN4 ---
# # Hex: #fbf7f3, #e5b083, #426e5d, #20283d
# LIGHTEST = display.create_pen(251, 247, 243)
# LIGHT = display.create_pen(229, 176, 131)
# DARK = display.create_pen(66, 110, 93)
# DARKEST = display.create_pen(32, 40, 61)

# # --- BLK AQU4 ---
# # Hex: #071821, #1d3c45, #5a7d8c, #8cb9c5
# DARKEST = display.create_pen(7, 24, 33)
# DARK = display.create_pen(29, 60, 69)
# LIGHT = display.create_pen(90, 125, 140)
# LIGHTEST = display.create_pen(140, 185, 197)

# Change your badge and QR details here!
COMPANY_NAME = "Instruqt"
NAME = "Jeff Pistone"
BLURB1 = "Solutions Engineer"
BLURB2 = "Enjoys hacking and video games"
BLURB3 = "Will work for tacos"

QR_TEXT = "instruqt.com"

IMAGE_NAME = "squirrel.jpg"

# Some constants we'll use for drawing
BORDER_SIZE = 4
PADDING = 10
COMPANY_HEIGHT = 40


def draw_badge():
    # draw border
    display.set_pen(LIGHTEST)
    display.clear()

    # draw background
    display.set_pen(DARK)
    display.rectangle(BORDER_SIZE, BORDER_SIZE, WIDTH - (BORDER_SIZE * 2), HEIGHT - (BORDER_SIZE * 2))

    # draw company box
    display.set_pen(DARKEST)
    display.rectangle(BORDER_SIZE, BORDER_SIZE, WIDTH - (BORDER_SIZE * 2), COMPANY_HEIGHT)

    # draw company text
    display.set_pen(LIGHT)
    display.set_font("bitmap6")
    display.text(COMPANY_NAME, BORDER_SIZE + PADDING, BORDER_SIZE + PADDING, WIDTH, 3)

    # draw name text
    display.set_pen(LIGHTEST)
    display.set_font("bitmap8")
    display.text(NAME, BORDER_SIZE + PADDING, BORDER_SIZE + PADDING + COMPANY_HEIGHT, WIDTH, 5)

    # draws the bullet points
    display.set_pen(DARKEST)
    display.text("*", BORDER_SIZE + PADDING + 120 + PADDING, 105, 160, 2)
    display.text("*", BORDER_SIZE + PADDING + 120 + PADDING, 140, 160, 2)
    display.text("*", BORDER_SIZE + PADDING + 120 + PADDING, 175, 160, 2)

    # draws the blurb text (4 - 5 words on each line works best)
    display.set_pen(LIGHTEST)
    display.text(BLURB1, BORDER_SIZE + PADDING + 135 + PADDING, 105, 160, 2)
    display.text(BLURB2, BORDER_SIZE + PADDING + 135 + PADDING, 140, 160, 2)
    display.text(BLURB3, BORDER_SIZE + PADDING + 135 + PADDING, 175, 160, 2)


def show_photo():
    j = jpegdec.JPEG(display)

    # Open the JPEG file
    j.open_file(IMAGE_NAME)

    # Draws a box around the image
    display.set_pen(DARKEST)
    display.rectangle(PADDING, HEIGHT - ((BORDER_SIZE * 2) + PADDING) - 120, 120 + (BORDER_SIZE * 2), 120 + (BORDER_SIZE * 2))

    # Decode the JPEG
    j.decode(BORDER_SIZE + PADDING, HEIGHT - (BORDER_SIZE + PADDING) - 120)

    # Draw QR button label
    display.set_pen(LIGHTEST)
    display.text("QR", 240, 215, 160, 2)


def measure_qr_code(size, code):
    w, h = code.get_size()
    module_size = int(size / w)
    return module_size * w, module_size


def draw_qr_code(ox, oy, size, code):
    size, module_size = measure_qr_code(size, code)
    display.set_pen(LIGHTEST)
    display.rectangle(ox, oy, size, size)
    display.set_pen(DARKEST)
    for x in range(size):
        for y in range(size):
            if code.get_module(x, y):
                display.rectangle(ox + x * module_size, oy + y * module_size, module_size, module_size)


def show_qr():
    display.set_pen(DARK)
    display.clear()

    code = qrcode.QRCode()
    code.set_text(QR_TEXT)

    size, module_size = measure_qr_code(HEIGHT, code)
    left = int((WIDTH // 2) - (size // 2))
    top = int((HEIGHT // 2) - (size // 2))
    draw_qr_code(left, top, HEIGHT, code)


# draw the badge for the first time
badge_mode = "photo"
draw_badge()
show_photo()
display.update()

while True:
    if button_c.is_pressed:
        if badge_mode == "photo":
            badge_mode = "qr"
            show_qr()
            display.update()
        else:
            badge_mode = "photo"
            draw_badge()
            show_photo()
            display.update()
        time.sleep(1)
