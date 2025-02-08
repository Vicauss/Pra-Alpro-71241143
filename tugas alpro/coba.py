
harga_per_gram = 650000
gram = 25
harga_per_gram_saat_ini = 685000
harga_per_gram_akhir = 715000
gram_tambah = 15

biaya_pembelian_awal = harga_per_gram * gram
nilai_saat_ini_awal = harga_per_gram_saat_ini * gram
keuntungan_awal = nilai_saat_ini_awal - biaya_pembelian_awal
keuntungan_persen_awal = (keuntungan_awal / biaya_pembelian_awal) * 100

print(f"Keuntungan Gerard dari pembelian pertama (dalam Rp): {keuntungan_awal}")
print(f"Keuntungan Gerard dari pembelian pertama (dalam %): {keuntungan_persen_awal:.2f}%")


biaya_pembelian_total = (harga_per_gram * gram) + (harga_per_gram_saat_ini * gram_tambah)
nilai_saat_ini_total = (gram + gram_tambah) * harga_per_gram_akhir
keuntungan_total = nilai_saat_ini_total - biaya_pembelian_total
keuntungan_persen_total = (keuntungan_total / biaya_pembelian_total) * 100


print(f"Keuntungan Gerard setelah membeli tambahan 15 gram (dalam Rp): {keuntungan_total}")
print(f"Keuntungan Gerard setelah membeli tambahan 15 gram (dalam %): {keuntungan_persen_total:.2f}%")
