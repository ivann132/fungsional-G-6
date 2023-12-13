from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan pillow
image = Image.open('nyoba.jpg') # ubah nyoba.jpg ke gambar yang anda ingin gunakan
# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(0.1)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.5)

# TODO 3: Simpan gambar hasil edit
final_image.save('final_result.jpg')
# TODO 4: Tampilkan
final_image.show()