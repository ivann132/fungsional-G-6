#Lengkapi kode dibawah ini untuk menjawab soal diatas ya
# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import Image, ImageFilter
# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open("bg.jpeg") # ubah bg.jpg ke path gambar yang anda ingin gunakan
overlay_image = Image.open("image.jpg") # ubah image.jpg ke path gambar yang anda ingin gunakan
# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert('RGB')
# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
new_size = (overlay_image.width // 2, overlay_image.height // 2)
overlay_image = overlay_image.resize(new_size)

x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2
# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))
# TODO 5 : Simpan gambar hasil edit
background_image.save("image_result.jpg")
# TODO 6 : Tampilkan
background_image.show()