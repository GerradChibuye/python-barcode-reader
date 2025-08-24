from pyzbar.pyzbar import decode
from PIL import Image
# Loading of the image
img = Image.open("barcode.png")
# Decode
results = decode(img)

for result in results:
    print("Barcode Type:", result.type)
    print("Data:", result.data.decode("utf-8"))
