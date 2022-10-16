from datetime import datetime

def getFinalScore(score: float):
    if score >= 80 and score <= 100:
        return 'A'
    elif score >= 77 and score < 80:
        return 'A-'
    elif score >= 74 and score < 77:
        return 'B+'
    elif score >= 71 and score < 74:
        return 'B'
    elif score >= 68 and score < 71:
        return 'B-'
    elif score >= 64 and score < 68:
        return 'C+'
    elif score >= 60 and score < 64:
        return 'C'
    elif score >= 50 and score < 60:
        return 'D'
    elif score >= 0 and score < 50:
        return 'E'
    else:
        return 'Nilai tidak valid'

def isPassed(score: float):
    if score >= 60:
        return 'Lulus'
    else:
        return 'Tidak Lulus'

nim = input('Masukkan NIM: ')
name = input('Masukkan Nama Mahasiswa: ')
gender = input('Masukkan Jenis Kelamin: ')
date = datetime.now().strftime("%d %B %Y, %H:%M")
subject = input('Masukkan Mata Kuliah: ')
attendance = float(input('Masukkan Jumlah Kehadiran: '))
attendance_pt = (attendance / 16 * 100) * 0.1
assignment = float(input('Masukkan Nilai Tugas (total): '))
assignment_pt = (assignment / 12) * 0.2
midterm = float(input('Masukkan Nilai UTS: '))
midterm_pt = midterm * 0.3
final = float(input('Masukkan Nilai UAS: '))
final_pt = final * 0.4
score = attendance_pt + assignment_pt + midterm_pt + final_pt
finalScore = getFinalScore(score)
passed = isPassed(score)

print(
    f"--------------------------------------------",
    f"\n{'NIM':20}: {nim:20}",
    f"\n{'Nama':20}: {name:20}",
    f"\n{'Jenis Kelamin':20}: {gender:20}",
    f"\n{'Tanggal Input Nilai':20}: {date:20}",
    f"\n{'Mata Kuliah':20}: {subject:20}",
    f"\n{'Absensi':20}: {attendance:,.0f}",
    f"\n{'Tugas':20}: {assignment:,.0f}",
    f"\n{'UTS':20}: {midterm:,.0f}",
    f"\n{'UAS':20}: {final:,.0f}",
    f"\n{'Nilai Akhir':20}: {finalScore:10}",
    f"\n{'Keterangan Nilai':20}: {passed:10}",
)
