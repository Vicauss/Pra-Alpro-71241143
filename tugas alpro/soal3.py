import math
uang_awal = 200000000
target = 400000000
bunga = 10/100
waktu = math.log(target/uang_awal) / (math.log(1 + bunga))
print("waktu yang dibutuhkan adalah : ",(round(waktu)),"tahun")