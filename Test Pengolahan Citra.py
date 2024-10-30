#pip install numpy imageio matplotlib
import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Membaca citra
image = img.imread("D:/source.jpg")

# Memisahkan channel warna
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

# Membuat citra untuk setiap channel
imgRed = np.zeros_like(image)
imgRed[:,:,0] = red

imgGreen = np.zeros_like(image)
imgGreen[:,:,1] = green

imgBlue = np.zeros_like(image)
imgBlue[:,:,2] = blue

# Menampilkan citra
plt.figure(figsize=(10, 15))

plt.subplot(4, 1, 1)
plt.title("Citra Asli")
plt.imshow(image)

plt.subplot(4, 1, 2)
plt.title("Channel Red")
plt.imshow(imgRed)

plt.subplot(4, 1, 3)
plt.title("Channel Green")
plt.imshow(imgGreen)

plt.subplot(4, 1, 4)
plt.title("Channel Blue")
plt.imshow(imgBlue)

plt.tight_layout()
plt.show()