print("\n=== TANTANGAN TERINTEGRASI ===")

def uji_mahasiswa(nama_mhs, nilai_tugas, nilai_ujian):
    rata_rata = (nilai_tugas + nilai_ujian) / 2
    status_lulus = rata_rata >= 75
    
    print(f"Nama Mahasiswa : {nama_mhs}")
    print(f"Nilai Tugas    : {nilai_tugas}")
    print(f"Nilai Ujian    : {nilai_ujian}")
    print(f"Rata-rata      : {rata_rata}")
    print(f"Status Lulus   : {status_lulus}")
    print("-" * 30)

# 6. Uji program dengan minimal dua kombinasi nilai yang berbeda
uji_mahasiswa("fakhri", 95, 90)
uji_mahasiswa("gani", 55, 45)