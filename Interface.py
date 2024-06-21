def dept_con(ProdukMerk):
  if ProdukMerk == 'MsGlow':
    result = 0
  elif ProdukMerk == 'Skintific':
    result = 1
  elif ProdukMerk == 'Acnes':
    result = 2                
  elif ProdukMerk == 'Wardah':
    result = 3                             
  elif ProdukMerk == 'Nivea':
    result = 4                                 
  elif ProdukMerk == 'Avoskin':
    result = 5                                
  elif ProdukMerk == 'Garnier':
    result = 6                               
  elif ProdukMerk == 'Hanasui':
    result = 7                               
  elif ProdukMerk == 'Benings':
    result = 8                             
  elif ProdukMerk == 'BioAqua':
    result = 9
  elif ProdukMerk == 'Biore':
    result = 10
  elif ProdukMerk == 'Ponds':
    result = 11
  elif ProdukMerk == 'Loreal':
    result = 12
  elif ProdukMerk == 'Scarlett':
    result = 13
  elif ProdukMerk == 'Emina':
    result = 14
  elif ProdukMerk == 'Himalaya':
    result = 15
  elif ProdukMerk == 'Mustika Ratu':
    result = 16
  elif ProdukMerk == 'Cetaphil':
    result = 17
  elif ProdukMerk == 'Clear & Clean':
    result = 18
  elif ProdukMerk == 'Safi':
    result = 19
  elif ProdukMerk == 'WhiteLab':
    result = 20
  elif ProdukMerk == 'Citra':
    result = 21
  elif ProdukMerk == 'Azarine':
    result = 22
  elif ProdukMerk == 'St.Ives':
    result = 23
  return result

def Jenis_Kelamin(Sex):
  if Sex == 'Laki-Laki':
    result = 0
  elif Sex == 'Perempuan':
    result = 1
  return result

def Jenis_Kulit(jenis):
  if jenis == 'Berminyak':
    result = 0
  elif jenis == 'Kombinasi':
    result = 1
  elif jenis == 'Normal':
    result = 2
  elif jenis == 'Kering':
    result = 3
  return result

def Masalah_Kulit(masalah):
  if masalah == 'Komedo':
    result = 0
  elif masalah == 'Dark Spot (Bekas Jerawat)':
    result = 1
  elif masalah == 'Kusam':
    result = 2
  elif masalah == 'Jerawat':
    result = 3
  elif masalah == 'Beruntusan':
    result = 4
  elif masalah == 'Kerutan':
    result = 5
  elif masalah == 'Dark Circle (Mata Panda)':
    result = 6
  elif masalah == 'Flek Hitam':
    result = 7
  elif masalah == 'Milia':
    result = 8
  return result
    
def Harga(rupiah):
  if rupiah == 'Murah':
    result = 0
  elif rupiah == 'Sedang':
    result = 1
  elif rupiah == 'Mahal':
    result = 2
  return result
