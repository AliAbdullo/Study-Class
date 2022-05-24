from uuid import uuid4

class Shaxs:
  """Shaxs classi"""
  odamlar_soni=0
  def __init__(self, ism, familiya, passport, tyil):
    """SHaxs xususiyatlari"""
    self.ism=ism
    self.familiya=familiya
    self.passport=passport
    self.tyil=tyil
    self.__id= uuid4()
    self.__tnum=[]
    Shaxs.odamlar_soni+=1

  def get_info(self):
    """Shaxs xaqida malumotlar qaytaradi"""
    info=f"{self.ism} {self.familiya}. "
    info+=f"Passporti:{self.passport}, {self.tyil}-yilda tug'ilgan"
    return info

  def get_age(self,yil):
    """Shaxsning yoshini qaytaradi"""
    return yil-self.tyil

  def get_id(self):
    """Shaxsning 'id'sini qataradi"""
    return self.__id 

  def get_tnum(self):
    """Shaxsning telefon raqamini qaytardi"""
    return self.__tnum 
    
  def set_tnum(self,num):
    """Shaxning telefon raqami saqlanadi"""
    self.__tnum+=num

  @classmethod
  def get_odamlar_soni(cls):
    """Odamlar sonini qaytaradi"""
    return cls.odamlar_soni
 

class Talaba(Shaxs):
  """Talaba nomli voris class"""
  talablar_soni=0
  def __init__(self,ism, familiya, passport, tyil, idraqami):
    super().__init__(ism, familiya, passport, tyil)
    self.id=idraqami
    self.bosqich=1
    self.fanlar=[]
    Talaba.talabalar_soni+=1

  def get_id(self):
    """Id raqamini qaytaradi"""
    return self.id

  def get_bosqich(self):
    """Talabaning bosqichini qaytaradi"""
    return self.bosqich

  def fanga_yozil(self, fan):
    """Fan obectlarini qaytaradi"""
    self.fanlar+=[fan]
    

  def get_fanlar(self):
    """Fanlar to'plamini qaytaradi"""
    return self.fanlar

  def remove_fan(self,fan):
    """Fanlar ro'yxatidan fanni o'chirib tashlash"""
    if fan in self.fanlar:
      self.fanlar.remove(fan)
    else:
      print("Siz bu fanga yozilmagansiz")

  @classmethod
  def get_talabalar_soni(cls):
    """Talabalar_sonini qaytaradi"""
    return cls.talablar_soni

    
class Fan:
  """Fan nomli class"""
  def __init__(self, nomi):
    self.nomi=nomi

  def get_nomi(self):
     """Fanning nomini qaytaradi""" 
     return self.nomi       

user1=Shaxs('Vali','Aliyev','ff2193934',2000)
user1=Shaxs('Salima','Aliyeva','ff21456734',2007)
user1.set_tnum('998972332')
print(user1.get_tnum())

tarix=Fan("Jaxon tarixi")
matem=Fan("Matematika")
biologiya=Fan("Botanika")