import random #random sınıfı eklendi
def fonksiyon(): #fonksiyon tanımlandı
   print("Keep it logically awesome.")
   print("Testing")
  

  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)

if __name__== "__main__":
  fonksiyon()
  f=open("quotes.txt")
  quotes=f.readlines()
  last=13
  rnd=random.randint(0, last)
  f.close()
  print(quotes[rnd])
