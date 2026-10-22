nilai = 82
kehadiran = 90

syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80
lulus_and = syarat_nilai and syarat_kehadiran
print("Status kelulusan (AND):", lulus_and)

nilai = 70
lulus_or = (nilai >= 75) or (kehadiran >= 80)
print("Status kelulusan baru (OR):", lulus_or)