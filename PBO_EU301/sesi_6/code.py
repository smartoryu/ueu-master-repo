from abc import ABC, abstractmethod

# Abstract class
class Time(ABC):
  @abstractmethod
  def __init__(self):
    self.jam = 0
    self.menit = 0
    self.detik = 0
  
  @abstractmethod
  def tambahJam(self): pass
  
  @abstractmethod
  def tambahMenit(self): pass

  @abstractmethod
  def tambahDetik(self): pass

  @abstractmethod
  def displayJam(self): pass

class Jam(Time):
    def __init__(self) -> None:
        self.jam = 0
        self.menit = 0
        self.detik = 0

    def tambahJam(self):
        if (self.jam < 23):
            self.jam += 1
        else:
            self.jam = 0

    def tambahMenit(self):
        if (self.menit < 59):
            self.menit += 1
        else:
            self.menit = 0
            self.tambahJam()

    def tambahDetik(self):
        if (self.detik < 59):
            self.detik += 1
        else:
            self.detik = 0
            self.tambahMenit()

    def displayJam(self):
      print(f"{self.jam}:{self.menit}:{self.detik}")


jam1 = Jam()

for x in range(60):
    jam1.tambahMenit()

for x in range(130):
    jam1.tambahDetik()

jam1.displayJam()
