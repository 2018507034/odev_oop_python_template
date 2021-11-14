'''
YBS401-2021-fall-2
Ödev kapsamında yapmanız gereken:

Oncelikle urunler adinda bir sinif tanimlayiniz. 
Urunler sinifi urun_adi, urun_alis_fiyati, urun_otv_orani, urun_kdv_orani ozelliklerine sahip olmalidir. 
Urunler sinifi constructor kullanmalidir. Constructor içerisine sirayla
urun_adi, urun_alis_fiyati, urun_otv_orani, urun_kdv_orani parametre olarak almalidir. 
Urunler sinifi urun_satis_fiyati() adında bir methoda sahip olmalıdır. 
urun_satis_fiyati() methodu kar_orani parametresine sahip olmalidir. 
urun_satis_fiyati() methodu urunun karli ve vergilendirilmis fiyatini hesaplayarak dondurmelidir. 
urun fiyati hesaplarken once kar sonra otv ve kdv sirayla alis fiyatina eklenmelidir. 



hazırlayan @aucan

Öğrenci Ad Soyad=Ebubekir Gelve
Öğrenci No=2018507034   
Bölüm=YBS
Sınıf=4
'''

class urunler:
    urun_adi= ""
    urun_alis_fiyati=50
    urun_otv_orani= 0.1
    urun_kdv_orani=0.23
    kar_orani=0.5
    
    def __init__(self,pkurun_adi, pkurun_alis_fiyati, pkurun_otv_orani, pkurun_kdv_orani)
      self.urun_adi=pkurun_adi
      self.urun_alis_fiyati=pkurun_alis_fiyati
      self.urun_otv_orani=pkurun_otv_orani
      self.urun_kdv_orani= pkurun_kdv_orani
    
    def urun_satis_fiyati(self,kar_orani):
      
        urun_satis_fiyati = urun_alis_orani + (urun_alis_fiyati*kar_orani) 50+ (50*0.5) = 75
        urun_satis_fiyati = urun_satis_fiyati + (urun_satis_fiyati * urun_otv_orani) 75 + (75*0.1) = 82,5
        urun_satis_fiyati = urun_satis_fiyati + (urun_satis_fiyati * urun_kdv_orani)  82,5 + (82,5*0.23) = 101,475
        
        

   
        
    
def sepet_fiyati(kar_orani):
    '''
    Fonksiyon urunlerin toplam fiyatini geri dönüş değeri olarak dondurmelidir. (5 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 

    toplam değişkenini doldurmanız beklenmektedir.
    '''
    ekmek=urunler('ekmek',1,0.20,0.12)
    patates=urunler('patates',2,0.16,0.18)
    elma=urunler('elma',3,0.11,0.22)
    un=urunler('un',4,0.17,0.05)
    yumurta=urunler('yumurta',5,0.30,0.19)
    toplam=0   
    #-------**-----------
   toplam=ekmek.urun_satis_fiyati(kar_orani)+patates.urun_satis_fiyati(kar_orani)+elma.urun_satis_fiyati(kar_orani)+un.urun_satis_fiyati(kar_orani)+yumurta.urun_satis_fiyati(kar_orani)
    #-------**-----------
    return toplam


def odev_test():
    sepet_toplam = sepet_fiyati(0.15)
    if sepet_toplam==23.91218:
        print("doğru")
    else:
        print("yanlış")


#bu test methodunu kullanarak yazdığınız kodu test edebilirsiniz
odev_test()
