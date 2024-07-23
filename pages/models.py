from django.db import models
import sqlite3
# Create your models here.



class Testing():
    def __init__(self,d1,sm,d2,songs):
          self.dif1 = d1
          self.same = sm
          self.dif2 = d2
          self.lend1 = len(self.dif1)
          self.lensm = len(self.same)
          self.lend2 = len(self.dif2)
          self.songs = songs

    def retlend1(self):
         return self.lend1
    
    def retlensm(self):
         return self.lensm
    
    def retlend2(self):
         return self.lend2