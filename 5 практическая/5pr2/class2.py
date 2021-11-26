import math
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
