
import math
class Win_Door:
  def __init__(self, x, y):
    self.square=x*y
class Room:
  def __init__(self, length, width, height):
    self.length=length
    self.width=width 
    self.height=height
    self.wd=[]
  def square1(self):
    return 2*self.height*(self.length+self.width)
  def addwd(self, w, h):
    self.wd.append(Win_Door(w, h))
  def workSurface(self):
    new_square=Room.square1(self)
    for i in self.wd:
      new_square-=i.square
    return new_square
  def wallpaper(self, wallpaper_length, wallpaper_width):
    return math.ceil(self.workSurface()/(wallpaper_length*wallpaper_width))
r1=Room(6, 3, 2.7)
print(r1.square1()) # полная площадь
r1.addwd(1, 1)
r1.addwd(1, 1)
r1.addwd(1, 2)
print(r1.workSurface()) # площадь без окон и дверей
print(r1.wallpaper(10.05, 0.53)) # количество обоев