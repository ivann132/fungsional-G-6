#Lengkapi kode dibawah untuk menjawab soal diatas ya
# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('image.jpg') # ubah image.jpg ke path gambar yang anda ingin gunakan
# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")
# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype('font/ARIAL.TTF', 24)
text = "Ivan Adi Prayoga 202110370311453"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height - text_height) // 2
draw.text((text_x,text_y),text,font=font,fill=255)
# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('nyoba.jpg')
# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()