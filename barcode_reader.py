from pyzbar.pyzbar import decode
from PIL import Image
# Loading of the image
img = Image.open("barcode.png")
# Decode
results = decode(img)

print(results)
