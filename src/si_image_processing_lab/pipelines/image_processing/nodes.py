from PIL import Image, ImageDraw, ImageFilter


def process_image(input_path, output_path, rotation_angle, filter_name, watermark_text):

    image = Image.open(input_path)

    rotated = image.rotate(rotation_angle)

    if filter_name == "EMBOSS":
        filtered = rotated.filter(ImageFilter.EMBOSS)
    else:
        filtered = rotated

    draw = ImageDraw.Draw(filtered)
    draw.text((20, 20), watermark_text, fill="white")

    filtered.save(output_path)

    return output_path