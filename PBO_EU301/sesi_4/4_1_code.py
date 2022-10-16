from datetime import datetime

def calculateAge(age: int) -> int:
    # Calculate the year
    year:int = datetime.now().year - age
    # Return the year
    return year

yearOfDate = int(input('Masukkan tahun lahir: '))

print('Usia saya sekarang', calculateAge(yearOfDate), 'tahun')