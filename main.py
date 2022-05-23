class Shaxs:
  """Shaxs classi"""
  def __init__(self, ism, familiya, passport, tyil):
    """SHaxs xususiyatlari"""
    self.ism=ism
    self.familiya=familiya
    self.passport=passport
    self.tyil=tyil

  def get_info(self):
    """Shaxs xaqida malumotlar qaytaradi"""
    info=f"{self.ism} {self.familiya}. "
    info+=f"Passporti:{self.passport}, {self.tyil}-yilda tug'ilgan"
    return info

  def get_age(self,yil):
    """Shaxsning yoshini qaytaradi"""
    return yil-self.tyil

class Fan:
  """Fan nomli class"""
  def __init__(self, nomi):
    self.nomi=nomi

  def get_nomi(self):
     """Fanning nomini qaytaradi""" 
     return self.nomi    

class Talaba(Shaxs, Fan):
  """Talaba nomli voris class"""
  def __init__(self,ism, familiya, passport, tyil, idraqami):
    super().__init__(ism, familiya, passport, tyil)
    self.id=idraqami
    self.bosqich=1
    self.fanlar=[]

  def get_id(self):
    """Id raqamini qaytaradi"""
    return self.id

  def get_bosqich(self):
    """Talabaning bosqichini qaytaradi"""
    return self.bosqich

  def fanga_yozil(self, get_nomi):
    """Fan obectlarini qaytaradi"""
    fanlar=f"{self.nomi}"
    self.fanlar+=[fanlar]
    

  def get_fanlar(self):
    """Fanlar to'plamini qaytaradi"""
    return self.fanlar
    
    



tarix=Fan("Jaxon tarixi")
matem=Fan("Matematika")
biologiya=Fan("Botanika")


     
                                                                                    
     
     
    