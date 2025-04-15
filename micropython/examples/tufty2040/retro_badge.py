from picographics import PicoGraphics, DISPLAY_TUFTY_2040, PEN_RGB332
from pimoroni import Button
from jpegdec import JPEG
import qrcode
import time

# === Setup display ===
display = PicoGraphics(display=DISPLAY_TUFTY_2040, pen_type=PEN_RGB332)
display.set_backlight(1.0)
WIDTH, HEIGHT = display.get_bounds()

# === Buttons (confirmed correct for Tufty) ===
button_a = Button(7, invert=False)
button_b = Button(8, invert=False)
button_c = Button(9, invert=False)
button_up = Button(22, invert=False)
button_down = Button(6, invert=False)

# === JPEG decoder ===
j = JPEG(display)

# === Badge Info ===
COMPANY_NAME = "Instruqt"
NAME = "Jeff Pistone"
BLURB1 = "Solutions Engineer"
BLURB2 = "Enjoys hacking and video games"
BLURB3 = "Will work for tacos"
QR_TEXT = "instruqt.com"
IMAGE_NAME = "avatar3.jpg"

# === Layout Constants ===
BORDER_SIZE = 4
PADDING = 10
COMPANY_HEIGHT = 40

# === Palette List (named, accurate colors) ===
palettes = [
    # Nostalgia
    [(208, 208, 88), (160, 168, 64), (112, 128, 40), (64, 80, 16)],
    # Greyscale
    [(255, 255, 255), (192, 192, 192), (96, 96, 96), (0, 0, 0)],
    # Kirokaze Gameboy
    [(224, 248, 207), (134, 192, 108), (48, 104, 80), (8, 24, 32)],
    # Crimson
    [(249, 244, 239), (211, 97, 53), (120, 41, 15), (37, 0, 1)],
    # Ice Cream GB
    [(255, 255, 255), (255, 182, 182), (255, 127, 127), (255, 0, 0)],
    # GB Chocolate
    [(238, 195, 154), (164, 110, 74), (105, 61, 43), (44, 27, 27)],
    # b4sement
    [(61, 255, 152), (255, 74, 220), (34, 35, 35), (240, 246, 240)],
    # Warm Amber
    [(255, 140, 0), (255, 115, 0), (180, 70, 0), (0, 0, 0)],
    # Amber Terminal
    [(255, 191, 0), (200, 150, 0), (100, 75, 0), (0, 0, 0)],
    # 2bit Demichrome
    [(233, 239, 236), (160, 160, 139), (85, 85, 104), (33, 30, 32)],
    # CGA High
    [(255, 255, 255), (85, 254, 255), (255, 85, 255), (0, 0, 0)],
    # Velvet Cherry GB
    [(249, 185, 195), (215, 127, 161), (122, 62, 106), (58, 26, 44)],
    # Coral 4
    [(255, 208, 164), (244, 148, 156), (124, 154, 172), (104, 81, 138)],
    # EN4
    [(251, 247, 243), (229, 176, 131), (66, 110, 93), (32, 40, 61)],
    # BLK AQU4
    [(140, 185, 197), (90, 125, 140), (29, 60, 69), (7, 24, 33)],
]

# === Palette Setup ===
palette_index = 0
badge_mode = "photo"

# === Apply Palette Function ===
def apply_palette(index):
    global LIGHTEST, LIGHT, DARK, DARKEST
    r = palettes[index % len(palettes)]
    LIGHTEST = display.create_pen(*r[0])
    LIGHT = display.create_pen(*r[1])
    DARK = display.create_pen(*r[2])
    DARKEST = display.create_pen(*r[3])

# === Draw Badge ===
def draw_badge():
    display.set_pen(LIGHTEST)
    display.clear()
    display.set_pen(DARK)
    display.rectangle(BORDER_SIZE, BORDER_SIZE, WIDTH - BORDER_SIZE*2, HEIGHT - BORDER_SIZE*2)
    display.set_pen(DARKEST)
    display.rectangle(BORDER_SIZE, BORDER_SIZE, WIDTH - BORDER_SIZE*2, COMPANY_HEIGHT)
    display.set_pen(LIGHT)
    display.set_font("bitmap6")
    display.text(COMPANY_NAME, BORDER_SIZE + PADDING, BORDER_SIZE + PADDING, WIDTH, 3)
    display.set_pen(LIGHTEST)
    display.set_font("bitmap8")
    display.text(NAME, BORDER_SIZE + PADDING, BORDER_SIZE + PADDING + COMPANY_HEIGHT, WIDTH, 5)
    display.set_pen(DARKEST)
    display.text("*", BORDER_SIZE + PADDING + 120 + PADDING, 105, 160, 2)
    display.text("*", BORDER_SIZE + PADDING + 120 + PADDING, 140, 160, 2)
    display.text("*", BORDER_SIZE + PADDING + 120 + PADDING, 175, 160, 2)
    display.set_pen(LIGHTEST)
    display.text(BLURB1, BORDER_SIZE + PADDING + 135 + PADDING, 105, 160, 2)
    display.text(BLURB2, BORDER_SIZE + PADDING + 135 + PADDING, 140, 160, 2)
    display.text(BLURB3, BORDER_SIZE + PADDING + 135 + PADDING, 175, 160, 2)

def show_photo():
    j.open_file(IMAGE_NAME)
    display.set_pen(DARKEST)
    display.rectangle(PADDING, HEIGHT - ((BORDER_SIZE * 2) + PADDING) - 120, 120 + (BORDER_SIZE * 2), 120 + (BORDER_SIZE * 2))
    j.decode(BORDER_SIZE + PADDING, HEIGHT - (BORDER_SIZE + PADDING) - 120)
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

# === Initial Draw ===
apply_palette(palette_index)
draw_badge()
show_photo()
display.update()

# === Main Loop ===
while True:
    if button_c.is_pressed:
        badge_mode = "qr" if badge_mode == "photo" else "photo"
        if badge_mode == "photo":
            draw_badge()
            show_photo()
        else:
            show_qr()
        display.update()
        time.sleep(0.25)

    if button_up.is_pressed:
        palette_index = (palette_index + 1) % len(palettes)
        apply_palette(palette_index)
        if badge_mode == "photo":
            draw_badge()
            show_photo()
        else:
            show_qr()
        display.update()
        time.sleep(0.25)

    if button_down.is_pressed:
        palette_index = (palette_index - 1 + len(palettes)) % len(palettes)
        apply_palette(palette_index)
        if badge_mode == "photo":
            draw_badge()
            show_photo()
        else:
            show_qr()
        display.update()
        time.sleep(0.25)

    time.sleep(0.05)