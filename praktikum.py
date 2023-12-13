from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# TODO 1: Buka kedua gambar menggunakan Pillow.
background_image = Image.open('background.jpg') # image from collab.google
overlay_image = Image.open('logoumm.jpg') # image from collab.google

# TODO 2: Ubah gambar background menjadi hitam-putih (grayscale), berotasi sebesar 30 derajat, dan blur

background_image = background_image.convert('L')
background_image = background_image.rotate(30)
background_image = background_image.filter(ImageFilter.GaussianBlur(radius=2))
background_image.save('copy.jpg')


# TODO 3: Ubah tingkat kecerahan gambar overlay menjadi 1.x kali lipat dan tingkat kontras menjadi 1.y kali lipat. 
# Dimana nilai x dan y mengacu pada 2 digit NIM akhir kalian dan resize sesuai kebutuhan.
brightenes = 1.5
contras = 1.3

enhancer = ImageEnhance.Brightness(overlay_image)
brightened_image = enhancer.enhance(brightenes)
enhancer = ImageEnhance.Contrast(brightened_image)
contras_image = enhancer.enhance(contras)

new_size = (overlay_image.width // 2, overlay_image.height // 2)
overlay_image = overlay_image.resize(new_size)

# TODO 4: Sisipkan gambar overlay ke dalam gambar background sehingga terlihat seperti stiker pada gambar latar belakang.
overlay = Image.new("RGBA", background_image.size)
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2
overlay.paste(overlay_image, (x_center, y_center))

combined_image = Image.alpha_composite(background_image.convert("RGBA"), overlay)

# TODO 5: Tambahkan teks "Informatika JOSSS!" pada gambar overlay dengan font Arial dan ukuran 24.
draw = ImageDraw.Draw(combined_image)
font = ImageFont.truetype('font/ARIAL.TTF', 24)
text = "Informatika JOSSS!"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
text_x = (background_image.width - text_width) // 2
text_y = (background_image.height - text_height) // 2
draw.text((text_x,text_y),text,font=font,fill=0)

# TODO 6: Simpan gambar hasil edit dengan nama "tugas_praktikum_enam.jpg".

result_path = "tugas_praktikum_enam.jpg"
combined_image.convert("RGB").save(result_path)
combined_image.show()

