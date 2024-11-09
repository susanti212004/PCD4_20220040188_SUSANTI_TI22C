# -*- coding: utf-8 -*-
"""PCD4_20220040188_SUSANTI_TI22C.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1280fOFw4VQbRbxPj4fqROEQhsugJYLBL
"""

pip install imageio numpy scipy matplotlib

# Import pustaka yang dibutuhkan
import imageio.v3 as iio  # Untuk membaca dan menulis gambar
import numpy as np  # Untuk manipulasi data array
from scipy import ndimage  # Untuk pemrosesan gambar
import matplotlib.pyplot as plt  # Untuk menampilkan gambar

# 1. Membaca Gambar
# Membaca gambar dari file dan mengubahnya menjadi array numpy
image_path = '/content/bebeklucu.jfif'  # Ganti dengan jalur gambar Anda
image = iio.imread(image_path)
print("Original Image Shape:", image.shape)

# 2. Mengubah Gambar Menjadi Grayscale
# Mengambil rata-rata dari tiga kanal warna untuk mengubah gambar menjadi grayscale
if image.ndim == 3:  # Memastikan gambar memiliki 3 kanal (RGB)
    grayscale_image = np.mean(image, axis=2)  # Rata-rata kanal R, G, B
else:
    grayscale_image = image  # Jika sudah grayscale, tidak perlu perubahan
print("Grayscale Image Shape:", grayscale_image.shape)

# 3. Menerapkan Gaussian Blur
# Menerapkan filter Gaussian untuk menghaluskan gambar
sigma_value = 3  # Nilai sigma untuk Gaussian blur
blurred_image = ndimage.gaussian_filter(grayscale_image, sigma=sigma_value)
print("Applied Gaussian Blur.")

# 4. Merotasi Gambar
# Merotasi gambar sebesar 45 derajat
rotation_angle = 45  # Sudut rotasi dalam derajat
rotated_image = ndimage.rotate(blurred_image, rotation_angle, reshape=True)
print("Rotated Image Shape:", rotated_image.shape)

# 5. Menyimpan Gambar Hasil
# Menyimpan gambar hasil proses ke file
iio.imwrite('grayscale_image.jpg', grayscale_image.astype(np.uint8))
iio.imwrite('blurred_image.jpg', blurred_image.astype(np.uint8))
iio.imwrite('rotated_image.jpg', rotated_image.astype(np.uint8))

print("Images saved: grayscale_image.jpg, blurred_image.jpg, rotated_image.jpg")

# Menampilkan gambar hasil pemrosesan
plt.figure(figsize=(12, 12))

# Menampilkan gambar asli
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Menampilkan gambar grayscale
plt.subplot(2, 2, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Menampilkan gambar setelah Gaussian blur
plt.subplot(2, 2, 3)
plt.imshow(blurred_image, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')

# Menampilkan gambar setelah rotasi
plt.subplot(2, 2, 4)
plt.imshow(rotated_image, cmap='gray')
plt.title('Rotated Image')
plt.axis('off')

# Menampilkan semua gambar
plt.show()