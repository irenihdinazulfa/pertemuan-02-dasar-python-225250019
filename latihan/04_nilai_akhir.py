BOBOT_TUGAS = 0.20
BOBOT_UTS = 0.30
BOBOT_UAS = 0.50

nama = input("Nama: ")
nilai_tugas = 80.0
nilai_uts = 80.0
nilai_uas = 80.0

nilai_akhir = (nilai_tugas * BOBOT_TUGAS) + (nilai_uts * BOBOT_UTS) + (nilai_uas * BOBOT_UAS)

print(f"Nilai akhir : {nilai_akhir:.2f}")