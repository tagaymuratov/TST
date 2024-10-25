from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.files.base import ContentFile

def compress_logo(image):
    img = Image.open(image)

    if img.size[0] > img.size[1]: width = img.size[0]
    else: width = img.size[1]

    img = img.crop((0, 0, width, width))
    im = im.resize((200, 300))
    im_bytes = BytesIO()
    im.save(fp=im_bytes, format="WEBP", quality=100)
    image_content_file = ContentFile(content=im_bytes.getvalue())
    name = image.name.split('.')[0] + '.WEBP'
    new_image = File(image_content_file, name=name)
    return new_image