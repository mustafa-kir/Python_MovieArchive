from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from filmArsiv_190101006_mustafa_kır import Ui_MainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtGui
import sys

# ana sınıf QMainWindwow dan türeilmiştir
class FilmArsiv(QMainWindow):
    def __init__(self,filmturu = "", imdb = "", filmyili = "", kaydedilenler = "",counter = 0,filmler = "" ):
        super(FilmArsiv, self).__init__()
        # super(): Kendi __init__ metodumuzu yazdığımızda, miras alınan sınıfın __init__ metodu geçersiz kaldığı için
        # çağırılmıyor. Biz eğer çağırılmasını istiyorsak super().__init__() gibi bir yapı kullanıyoruz.
        self.filmturu = filmturu
        self.imdb = imdb
        self.filmyili = filmyili
        self.counter = counter
        self.filmler = filmler
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

       # Toolbar daki tuşların yönlendirilmesi için fonksiyonlar oluşturuyoruz.
        self.ui.actionGiris.triggered.connect(self.go_page_1)
        self.ui.actionAna_Menu.triggered.connect(self.go_page_2)
        self.ui.actionKaydedilenler.triggered.connect(self.go_page_kaydedilenler)
      
        # Anamenude bulunan sayfaların Filitrele tuşlarının tıklandıktan sonra gösterilecek reaksiyonlar için fonksiyonlarını oluşturuyoruz.
        self.ui.btnFilitrelere1.clicked.connect(self.clikFilitrelere1)
        self.ui.btnFilitrelere2.clicked.connect(self.clikFilitrelere2)
        self.ui.btnFilitrele3.clicked.connect(self.clikFilitrelere3)
        
        # Ana menude bulunan "1","2","3" tuşlara tıklandıktan sonra gösterilecek reaksiyonlar için fonksiyonlarını oluşturuyoruz.
        self.ui.btn_1_2.clicked.connect(self.sayfa_1_2)
        self.ui.btn_1_3.clicked.connect(self.sayfa_1_3)
        self.ui.btn_2_1.clicked.connect(self.sayfa_2_1)
        self.ui.btn_2_3.clicked.connect(self.sayfa_2_3)
        self.ui.btn_3_1.clicked.connect(self.sayfa_2_1)
        self.ui.btn_3_2.clicked.connect(self.sayfa_2_3)

        # Filimlerin kenarlarında bulunan "Detaylı bilgi..." tuşlarına tıklandıktan sonra gösterilecek reaksiyonlar için fonksiyonlarını oluşturuyoruz.(52 satır ve 134 satır)
        self.ui.btnDetayliBilgi_Logan.clicked.connect(self.logan)
        self.ui.btnDetayliBilgi_OrumcekAdam.clicked.connect(self.orumcekAdam)
        self.ui.btnDetayliBilgi_Galaksi.clicked.connect(self.galaksi)
        self.ui.btnDetayliBilgi_Baahubali.clicked.connect(self.baahubali)
        self.ui.btnDetayliBilgi_BabyDriver.clicked.connect(self.babydirever)

        self.ui.btnDetayliBilgi_tenet.clicked.connect(self.tenet)
        self.ui.btnDetayliBilgi_marsli.clicked.connect(self.marsli)
        self.ui.btnDetayliBilgi_mahmunlarCehennemi.clicked.connect(self.maymunlarcehennemi)
        self.ui.btnDetayliBilgi_yildizlararasi.clicked.connect(self.yildizlararasi)
        self.ui.btnDetayliBilgi_WonderWoman.clicked.connect(self.wonder)

        self.ui.btnDetayliBilgi_Deaadpool2.clicked.connect(self.deadpool2)
        self.ui.btnDetayliBilgi_Extraction.clicked.connect(self.extraction)
        self.ui.btnDetayliBilgi_Kesari.clicked.connect(self.kesari)
        self.ui.btnDetayliBilgi_Pazarit.clicked.connect(self.parazit)
        self.ui.btnDetayliBilgi_DenizFeneri.clicked.connect(self.denizFeneri)

        self.ui.btnDetayliBilgi_tenet_2.clicked.connect(self.tenet_2)
        self.ui.btnDetayliBilgi_marsli_2.clicked.connect(self.marsli_2)
        self.ui.btnDetayliBilgi_maymunlarcehennemi.clicked.connect(self.maymunlarcehennemi2)
        self.ui.btnDetayliBilgi_yildizlararasi_2.clicked.connect(self.yildizlararasi_2)
        self.ui.btnDetayliBilgi_WonderWoman_2.clicked.connect(self.wonder_2)

        self.ui.btnDetayliBilgi_Logan_2.clicked.connect(self.logan_2)
        self.ui.btnDetayliBilgi_OrumcekAdam_2.clicked.connect(self.orumcekadam_2)
        self.ui.btnDetayliBilgi_Galaksi_2.clicked.connect(self.galaksi_2)
        self.ui.btnDetayliBilgi_Baahubali_2.clicked.connect(self.baahubali_2)
        self.ui.btnDetayliBilgi_BabyDriver_2.clicked.connect(self.babydriver_2)

        self.ui.btnDetayliBilgi_parazit.clicked.connect(self.parazit_2)
        self.ui.btnDetayliBilgi_denizfeneri.clicked.connect(self.denizfeneri_2)
        self.ui.btnDetayliBilgi_bicaklar.clicked.connect(self.bicaklar)
        self.ui.btnDetayliBilgi_ikikral.clicked.connect(self.ikikral)
        self.ui.btnDetayliBilgi_joker.clicked.connect(self.joker)

        self.ui.btnDetayliBilgi_1917.clicked.connect(self.bin917)
        self.ui.btnDetayliBilgi_mustang.clicked.connect(self.mustang)
        self.ui.btnDetayliBilgi_size7.clicked.connect(self.size7)
        self.ui.btnDetayliBilgi_subaycasus.clicked.connect(self.subaycasus)
        self.ui.btnDetayliBilgi_mademoiselle.clicked.connect(self.mademoiselle)

        self.ui.btnDetayliBilgi_beyler.clicked.connect(self.beyler)
        self.ui.btnDetayliBilgi_sanju.clicked.connect(self.sanju)
        self.ui.btnDetayliBilgi_laurelilehardy.clicked.connect(self.laurelilehardy)
        self.ui.btnDetayliBilgi_ringdebiraile.clicked.connect(self.ringdebiraile)
        self.ui.btnDetayliBilgi_cilginzenginasyalilar.clicked.connect(self.asyalilar)

        self.ui.btnDetayliBilgi_Logan_3.clicked.connect(self.logan_3)
        self.ui.btnDetayliBilgi_tonya.clicked.connect(self.tonya)
        self.ui.btnDetayliBilgi_kusursuzyabanci.clicked.connect(self.kusursuzyabanci)
        self.ui.btnDetayliBilgi_paterson.clicked.connect(self.paterson)
        self.ui.btnDetayliBilgi_ingrid.clicked.connect(self.ingrid)

        self.ui.btnDetayliBilgi_kaptanamerika.clicked.connect(self.kaptanamerika)
        self.ui.btnDetayliBilgi_starwars.clicked.connect(self.starwars)
        self.ui.btnDetayliBilgi_Galaksinin.clicked.connect(self.Galaksinin)
        self.ui.btnDetayliBilgi_deadpool.clicked.connect(self.deadpool)
        self.ui.btnDetayliBilgi_zombi.clicked.connect(self.zombi)

        self.ui.btnDetayliBilgi_1917_2.clicked.connect(self.bin917_2)
        self.ui.btnDetayliBilgi_mustang_2.clicked.connect(self.mustang_2)
        self.ui.btnDetayliBilgi_laurelilehardy_2.clicked.connect(self.laurelilehardy_2)
        self.ui.btnDetayliBilgi_Logan_4.clicked.connect(self.logan_4)
        self.ui.btnDetayliBilgi_tenet_3.clicked.connect(self.tenet_3)

        self.ui.btnDetayliBilgi_kaptanamerika_2.clicked.connect(self.kaptanamerika_2)
        self.ui.btnDetayliBilgi_starwars_2.clicked.connect(self.starwars_2)
        self.ui.btnDetayliBilgi_maymunlarcehennemi_2.clicked.connect(self.maymunlarcehennemi_2)
        self.ui.btnDetayliBilgi_yildizlararasi_3.clicked.connect(self.yildizlararasi_3)
        self.ui.btnDetayliBilgi_WonderWoman_3.clicked.connect(self.WonderWoman_3)

        self.ui.btnDetayliBilgi_tenet_4.clicked.connect(self.tenet_4)
        self.ui.btnDetayliBilgi_maymunlarcehennemi_3.clicked.connect(self.maymunlarcehennemi_3)
        self.ui.btnDetayliBilgi_WonderWoman_4.clicked.connect(self.WonderWoman_4)
        self.ui.btnDetayliBilgi_Extraction_3.clicked.connect(self.Extraction_3)
        self.ui.btnDetayliBilgi_kesari_2.clicked.connect(self.kesari_2)

        self.ui.btnDetayliBilgi_kaptanamerika_3.clicked.connect(self.kaptanamerika_3)
        self.ui.btnDetayliBilgi_starwars_3.clicked.connect(self.starwars_3)
        self.ui.btnDetayliBilgi_marsli_3.clicked.connect(self.marsli_3)
        self.ui.btnDetayliBilgi_yildizlararasi_4.clicked.connect(self.yildizlararasi_4)
        self.ui.btnDetayliBilgi_vahsilerfirarda_2.clicked.connect(self.vahsilerfirarda_2)

        # Filimlerin gösterim bölümlerinde bulunan "Filmi Kaydet" tuşunun tıklandıktan sonra 
        # gösterilecek reaksiyonlar için fonksiyonlarını oluşturuyoruz.(137 satır ve 173 satır)
        self.ui.btnKaydet_logan.clicked.connect(self.kaydetlogan)
        self.ui.btnKaydet_baby.clicked.connect(self.kaydetbabydriver)
        self.ui.btnKaydet_orumcek.clicked.connect(self.kaydetorumcekadam)
        self.ui.btnKaydet_galaksi.clicked.connect(self.kaydetgalaksi)
        self.ui.btnKaydet_baahubali.clicked.connect(self.kaydetbaahubali)
        self.ui.btnKaydet_tenet.clicked.connect(self.kaydettenet)
        self.ui.btnKaydet_wonder.clicked.connect(self.kaydetwonderWomen)
        self.ui.btnKaydet_yidizlararasi.clicked.connect(self.kaydetyidizlararasi)
        self.ui.btnKaydet_marsli.clicked.connect(self.kaydetmarsli)
        self.ui.btnKaydet_maymunlarcehennemi.clicked.connect(self.kaydetmaymunlar)
        self.ui.btnKaydet_joker.clicked.connect(self.kaydetjoker)
        self.ui.btnKaydet_1917.clicked.connect(self.kaydetbin917)
        self.ui.btnKaydet_size7.clicked.connect(self.kaydetsize7)
        self.ui.btnKaydet_parazit.clicked.connect(self.kaydetparazit)
        self.ui.btnKaydet_denizfeneri.clicked.connect(self.kaydetdeizfeneri)
        self.ui.btnKaydet_bicaklarcekildi.clicked.connect(self.kaydetbicaklarcekildi)
        self.ui.btnKaydet_ikikral.clicked.connect(self.kaydetikikral)
        self.ui.btnKaydet_mustang.clicked.connect(self.kaydetmustang)
        self.ui.btnKaydet_subay.clicked.connect(self.kaydetsubay)
        self.ui.btnKaydet_mademoiselle.clicked.connect(self.kaydetmademoiselle)
        self.ui.btnKaydet_asyalilar.clicked.connect(self.kaydetasyalilar)
        self.ui.btnKaydet_ringdebiraile.clicked.connect(self.kaydetringdebiraile)
        self.ui.btnKaydet_beyler.clicked.connect(self.kaydetbeyler)
        self.ui.btnKaydet_laurel.clicked.connect(self.kaydetlaurel)
        self.ui.btnKaydet_sanju.clicked.connect(self.kaydetsanju)
        self.ui.btnKaydet_tonya.clicked.connect(self.kaydettonya)
        self.ui.btnKaydet_vahsiler.clicked.connect(self.kaydetvahsiler)
        self.ui.btnKaydet_kusursuzyabanci.clicked.connect(self.kaydetkusursuzyabanci)
        self.ui.btnKaydet_ingrid.clicked.connect(self.kaydetingrid)
        self.ui.btnKaydet_paterson.clicked.connect(self.kaydetpaterson)
        self.ui.btnKaydet_extraction.clicked.connect(self.kaydetextraction)
        self.ui.btnKaydet_kesari.clicked.connect(self.kaydetkesari)
        self.ui.btnKaydet_zombi.clicked.connect(self.kaydetzombi)
        self.ui.btnKaydet_kaptanamerika.clicked.connect(self.kaydetkaptanamerika)
        self.ui.btnKaydet_starwars.clicked.connect(self.kaydetstarwars)
        self.ui.btnKaydet_deadpool.clicked.connect(self.kaydetdeadpool2)
        self.ui.btnKaydet_deadpool2.clicked.connect(self.kaydetdeadpool)

        # Toolbarı Gizler 
        self.ui.toolBar.setVisible(False)
        
        self.statusbar_time = 3000
        self.go_page_1()

    def go_page_1(self):
        self.ui.toolBar.setVisible(False)
        self.ui.stackedWidget.setCurrentIndex(0) # Verilen sayıya göre sayfa sayısana gider
      
    def go_page_2(self):
        self.ui.toolBar.setVisible(True)
        self.ui.stackedWidget.setCurrentIndex(1)

    def go_page_kaydedilenler(self):
        self.ui.toolBar.setVisible(True)
        self.ui.stackedWidget.setCurrentIndex(53)
        # Kullanıcı adına göre txt oluşturulur.
        kaydedilenler = self.ui.lineEdit_kulaniciAd.text()+".txt" 

        file = open(kaydedilenler,"r", encoding="utf-8")
        
        liste = file.readlines()
        
        counter = len(liste)
        filmler = ""
        # kaydedilen filmler label'a yazdırılır.
        for i in range(counter):
            filmler += liste[i]
        
        self.ui.lblkaydedilenler.setText(filmler) 



    def clikFilitrelere1(self):
        # Combox ile seçilen kategorileri filmturu,imdb,filmyili stringlere atanır.
        filmturu = self.ui.comboBox_filmturu1.currentText()
        imdb = self.ui.comboBox_imbd1.currentText()
        filmyili = self.ui.comboBox_filmyili1.currentText()
        # Filitrelemeye göre sayfalara aktarım sağlanır.
        if(filmturu == "Bilim Kurgu") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(4)
                
        elif(filmturu == "Bilim Kurgu") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(4)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(5)

        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(5)

        elif(filmturu == "Dram") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(6)
        
        elif(filmturu == "Dram") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(6)

        elif(filmturu == "Dram") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(6)
        
        elif(filmturu == "Dram") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(7) 

        elif(filmturu == "Dram") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(7)

        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)
        
        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)
        
        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)

        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)
        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(9)

        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)
        
        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9) 
        
        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(10)

        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(11)

        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(10)

        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(11)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arasıi"):
            self.ui.stackedWidget.setCurrentIndex(11)

        elif(filmturu == "---Film Türü ---") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(12)

        elif(filmturu == "---Film Türü ---") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(13)
        
        elif(filmturu == "---Film Türü ---") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(14)
        elif(filmturu == "---Film Türü ---") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(14)
        else:
            self.ui.statusbar.showMessage("Henüz o kategori filmleri sisteme yüklenemdi", self.statusbar_time)
    def clikFilitrelere2(self):
        filmturu = self.ui.comboBox_filmturu2.currentText()
        imdb = self.ui.comboBox_imdb2.currentText()
        filmyili = self.ui.comboBox_filmyili2.currentText()
        
        if(filmturu == "Bilim Kurgu") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(4)
                
        elif(filmturu == "Bilim Kurgu") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(4)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(5)

        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(5)

        elif(filmturu == "Dram") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(6)
        
        elif(filmturu == "Dram") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(6)

        elif(filmturu == "Dram") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(6)
        
        elif(filmturu == "Dram") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(7) 

        elif(filmturu == "Dram") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(7)

        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)
        
        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)
        
        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)

        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)
        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(9)

        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)
        
        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9) 
        
        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(10)

        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(11)

        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(10)

        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(11)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arasıi"):
            self.ui.stackedWidget.setCurrentIndex(11)

        elif(filmturu == "---Film Türü ---") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(12)

        elif(filmturu == "---Film Türü ---") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(13)
        
        elif(filmturu == "---Film Türü ---") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(14)
        elif(filmturu == "---Film Türü ---") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(14)
        else:
            self.ui.statusbar.showMessage("Henüz o kategori filmleri sisteme yüklenemdi", self.statusbar_time)
    def clikFilitrelere3(self):
        filmturu = self.ui.comboBox_filmturu3.currentText()
        imdb = self.ui.comboBox_imdb3.currentText()
        filmyili = self.ui.comboBox_filmyili3.currentText()
        
        if(filmturu == "Bilim Kurgu") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(4)
                
        elif(filmturu == "Bilim Kurgu") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(4)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(5)

        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(5)
        
        elif(filmturu == "Bilim Kurgu") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(5)

        elif(filmturu == "Dram") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(6)
        
        elif(filmturu == "Dram") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(6)

        elif(filmturu == "Dram") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(6)
        
        elif(filmturu == "Dram") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(7) 

        elif(filmturu == "Dram") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(7)

        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)
        
        elif(filmturu == "Komedi") and (imdb == "8 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)
        
        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)

        elif(filmturu == "Komedi") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)

        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9)
        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(9)

        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(8)
        
        elif(filmturu == "Komedi") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(9) 
        
        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(10)

        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(11)

        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(10)

        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "8 ve üzeri") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(11)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(10)
        
        elif(filmturu == "Aksiyon") and (imdb == "7 ve üzeri") and (filmyili == "2015 - 2017 arasıi"):
            self.ui.stackedWidget.setCurrentIndex(11)

        elif(filmturu == "---Film Türü ---") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2017 ve üzeri"):
            self.ui.stackedWidget.setCurrentIndex(12)

        elif(filmturu == "---Film Türü ---") and (imdb == "--- IMDb Puanı ---") and (filmyili == "2015 - 2017 arası"):
            self.ui.stackedWidget.setCurrentIndex(13)
        
        elif(filmturu == "---Film Türü ---") and (imdb == "7 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(14)
        elif(filmturu == "---Film Türü ---") and (imdb == "8 ve üzeri") and (filmyili == "--- Film Yılı ---"):
            self.ui.stackedWidget.setCurrentIndex(14)

        else:
            self.ui.statusbar.showMessage("Henüz o kategori filmleri sisteme yüklenemdi", self.statusbar_time)    

    def sayfa_1_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def sayfa_1_3(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def sayfa_2_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def sayfa_2_3(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def sayfa_3_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def sayfa_3_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def logan(self):
        self.ui.stackedWidget.setCurrentIndex(16)

    def orumcekAdam(self):
        self.ui.stackedWidget.setCurrentIndex(18)
    
    def galaksi(self):
        self.ui.stackedWidget.setCurrentIndex(19)
    
    def baahubali(self):
        self.ui.stackedWidget.setCurrentIndex(24)
    
    def babydirever(self):
        self.ui.stackedWidget.setCurrentIndex(17)
    
    def tenet(self):
        self.ui.stackedWidget.setCurrentIndex(20)

    def marsli(self):
        self.ui.stackedWidget.setCurrentIndex(23)
    
    def maymunlarcehennemi(self):
        self.ui.stackedWidget.setCurrentIndex(25)
    
    def yildizlararasi(self):
        self.ui.stackedWidget.setCurrentIndex(22)
    
    def wonder(self):
        self.ui.stackedWidget.setCurrentIndex(21)
    
    def deadpool2(self):
        self.ui.stackedWidget.setCurrentIndex(51)
    
    def extraction(self):
        self.ui.stackedWidget.setCurrentIndex(46)
    
    def kesari(self):
        self.ui.stackedWidget.setCurrentIndex(47)
    
    def parazit(self):
        self.ui.stackedWidget.setCurrentIndex(29)
    
    def denizFeneri(self):
        self.ui.stackedWidget.setCurrentIndex(30)
    
    def tenet_2(self):
        self.ui.stackedWidget.setCurrentIndex(20)
    
    def marsli_2(self):
        self.ui.stackedWidget.setCurrentIndex(23)

    def maymunlarcehennemi_2(self):
        self.ui.stackedWidget.setCurrentIndex(25)

    def yildizlararasi_2(self):
        self.ui.stackedWidget.setCurrentIndex(22)

    def wonder_2(self):
        self.ui.stackedWidget.setCurrentIndex(21)
    
    def logan_2(self):
        self.ui.stackedWidget.setCurrentIndex(16)
    
    def orumcekadam_2(self):
        self.ui.stackedWidget.setCurrentIndex(18)
    
    def galaksi_2(self):
        self.ui.stackedWidget.setCurrentIndex(19)

    def baahubali_2(self):
        self.ui.stackedWidget.setCurrentIndex(24)

    def babydriver_2(self):
        self.ui.stackedWidget.setCurrentIndex(17)

    def kaptanamerika_2(self):
        self.ui.stackedWidget.setCurrentIndex(49)
    
    def parazit_2(self):
        self.ui.stackedWidget.setCurrentIndex(29)
    
    def denizfeneri_2(self):
        self.ui.stackedWidget.setCurrentIndex(30)
    
    def bicaklar(self):
        self.ui.stackedWidget.setCurrentIndex(31)
    
    def ikikral(self):
        self.ui.stackedWidget.setCurrentIndex(32)
    
    def joker(self):
        self.ui.stackedWidget.setCurrentIndex(26)
    
    def bin917(self):
        self.ui.stackedWidget.setCurrentIndex(27)
    
    def mustang(self):
        self.ui.stackedWidget.setCurrentIndex(33)
    
    def size7(self):
        self.ui.stackedWidget.setCurrentIndex(28)
    
    def subaycasus(self):
        self.ui.stackedWidget.setCurrentIndex(34)

    def mademoiselle(self):
        self.ui.stackedWidget.setCurrentIndex(35)
    
    def beyler(self):
        self.ui.stackedWidget.setCurrentIndex(38)
    
    def sanju(self):
        self.ui.stackedWidget.setCurrentIndex(40)

    def laurelilehardy(self):
        self.ui.stackedWidget.setCurrentIndex(39)

    def ringdebiraile(self):
        self.ui.stackedWidget.setCurrentIndex(37)

    def asyalilar(self):
        self.ui.stackedWidget.setCurrentIndex(36)

    def logan_3(self):
        self.ui.stackedWidget.setCurrentIndex(16)

    def tonya(self):
        self.ui.stackedWidget.setCurrentIndex(41)

    def kusursuzyabanci(self):
        self.ui.stackedWidget.setCurrentIndex(43)

    def paterson(self):
        self.ui.stackedWidget.setCurrentIndex(45)

    def ingrid(self):
        self.ui.stackedWidget.setCurrentIndex(44)

    def kaptanamerika(self):
        self.ui.stackedWidget.setCurrentIndex(49)

    def starwars(self):
        self.ui.stackedWidget.setCurrentIndex(50)

    def Galaksinin(self):
        self.ui.stackedWidget.setCurrentIndex(19)

    def deadpool(self):
        self.ui.stackedWidget.setCurrentIndex(52)

    def zombi(self):
        self.ui.stackedWidget.setCurrentIndex(48)

    def bin917_2(self):
        self.ui.stackedWidget.setCurrentIndex(27)

    def mustang_2(self):
        self.ui.stackedWidget.setCurrentIndex(33)

    def laurelilehardy_2(self):
        self.ui.stackedWidget.setCurrentIndex(39)

    def logan_4(self):
        self.ui.stackedWidget.setCurrentIndex(16)
    
    def tenet_3(self):
        self.ui.stackedWidget.setCurrentIndex(20)

    def starwars_2(self):
        self.ui.stackedWidget.setCurrentIndex(50)

    def maymunlarcehennemi2(self):
        self.ui.stackedWidget.setCurrentIndex(25)

    def yildizlararasi_3(self):
        self.ui.stackedWidget.setCurrentIndex(22)

    def WonderWoman_3(self):
        self.ui.stackedWidget.setCurrentIndex(21)

    def tenet_4(self):
        self.ui.stackedWidget.setCurrentIndex(20)

    def maymunlarcehennemi_3(self):
        self.ui.stackedWidget.setCurrentIndex(25)

    def WonderWoman_4(self):
        self.ui.stackedWidget.setCurrentIndex(21)

    def Extraction_3(self):
        self.ui.stackedWidget.setCurrentIndex(46)

    def kesari_2(self):
        self.ui.stackedWidget.setCurrentIndex(47)

    def kaptanamerika_3(self):
        self.ui.stackedWidget.setCurrentIndex(49)

    def starwars_3(self):
        self.ui.stackedWidget.setCurrentIndex(50)

    def marsli_3(self):
        self.ui.stackedWidget.setCurrentIndex(23)

    def yildizlararasi_4(self):
        self.ui.stackedWidget.setCurrentIndex(22)

    def vahsilerfirarda_2(self):
        self.ui.stackedWidget.setCurrentIndex(42)
    

    def kaydetlogan(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        # Dosya'ya filmin adını kaydeder.
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Logan: Wolverine\n")
        file.close()

    def kaydetbabydriver(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Baby Driver\n")
        file.close()

    def kaydetorumcekadam(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Örümcek-Adam: Eve Dönüş\n")
        file.close()

    def kaydetgalaksi(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Galaksinin Koruyucuları 2\n")
        file.close()

    def kaydetbaahubali(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Baahubali 2: The Conclusion\n")
        file.close()
    
    def kaydettenet(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Tenet\n")
        file.close()
    
    def kaydetwonderWomen(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Wonder Woman\n")
        file.close()

    def kaydetyidizlararasi(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Yıldızlararası\n")
        file.close()

    def kaydetmarsli(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Marslı\n")
        file.close()

    def kaydetmaymunlar(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Maymunlar Cehennemi: Savaş\n")
        file.close()

    def kaydetjoker(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Joker\n")
        file.close()

    def kaydetbin917(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("1917\n")
        file.close()

    def kaydetsize7(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Oththa Seruppu Size 7\n")
        file.close()

    def kaydetparazit(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Parazit\n")
        file.close()

    def kaydetdeizfeneri(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Deniz Feneri\n")
        file.close()

    def kaydetbicaklarcekildi(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Bıçaklar Çekildi\n")
        file.close()

    def kaydetikikral(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("İlk kral\n")
        file.close()

    def kaydetmustang(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Mustang: Yabani At\n")
        file.close()

    def kaydetsubay(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Subay ve Casus\n")
        file.close()

    def kaydetmademoiselle(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Mademoiselle de Joncquières\n")
        file.close()

    def kaydetasyalilar(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Çılgın Zengin Asyalılar\n")
        file.close()

    def kaydetringdebiraile(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Ringde Bir Aile\n")
        file.close()

    def kaydetbeyler(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Beyler\n")
        file.close()

    def kaydetlaurel(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Laurel ile Hardy\n")
        file.close()

    def kaydetsanju(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Sanju\n")
        file.close()

    def kaydettonya(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Ben, Tonya\n")
        file.close()

    def kaydetvahsiler(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Vahşiler Firarda\n")
        file.close()

    def kaydetkusursuzyabanci(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Kusursuz Yabancı\n")
        file.close()

    def kaydetingrid(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("İngrid Batıya Gidiyor\n")
        file.close()

    def kaydetpaterson(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Paterson\n")
        file.close()

    def kaydetextraction(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Extraction\n")
        file.close()

    def kaydetkesari(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Kesari\n")
        file.close()

    def kaydetzombi(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Zombi Ekspresi\n")
        file.close()

    def kaydetkaptanamerika(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Kaptan Amerika: Kahramanların Savaşı\n")
        file.close()

    def kaydetstarwars(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Rogue One: Bir Star Wars Hikâyesi\n")
        file.close()

    def kaydetdeadpool2(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Deadpool 2\n")
        file.close()

    def kaydetdeadpool(self):
        kaydet = self.ui.lineEdit_kulaniciAd.text()+".txt"
        file = open(kaydet,"a",encoding='utf-8')
        file.write("Deadpool\n")
        file.close()

class Giris(FilmArsiv,QMainWindow):
    def __init__(self,counter = 0,kullanciad = "",kullanicisifre = "",kulaniciadGoster = "",yenikullaniciadi ="",yenikullanicisifre = ""):
        super(Giris, self).__init__()
        self.counter = counter
        self.kullanciad = kullanciad
        self.__kullanicisifre = kullanicisifre
        self.__kulaniciadGoster = kulaniciadGoster
        self.yenikullaniciadi = yenikullaniciadi
        self.yenikullanicisifre = yenikullanicisifre

        # Giris bölümü tusları tıklandığında tıklandıktan sonra gösterilecek reaksiyonlar için fonksiyonlarını oluşturuyooruz.
        self.ui.pushButton_3.clicked.connect(self.clikgiris)
        self.ui.pushButton_4.clicked.connect(self.cliksifremiunuttum)
        self.ui.pushButton_5.clicked.connect(self.clikuyeol)

        # Sifremi unuttum ve uye ol bölümünde bulunan uye ol ve şifre goster tıklandıktan sonra gösterilecek reaksiyonlar için fonksiyonlarını oluşturuyoruz.
        self.ui.pushButton.clicked.connect(self.clikuyeoll)
        self.ui.pushButton_2.clicked.connect(self.cliksifregoster)

        # Sifremi unuttum ve uye ol bölümünden ana menuye dön butonlarının tıklandıktan sonra gösterilecek reaksiyonlar için fonksiyonlarını oluşturuyooruz.
        self.ui.pushButton_17.clicked.connect(self.go_page_1)
        self.ui.pushButton_19.clicked.connect(self.go_page_1_1)

    def clikgiris(self):
        # uyeliste, uyesifre txt dosyalarını açar.
        file = open("uyelist.txt","r", encoding="utf-8")
        file2 = open("uyesifre.txt","r", encoding="utf-8")
        # Girilen kullanıcı adı ve sifreyi  kullanciad, kullanicisifreye atarılır.
        kullanciad = self.ui.lineEdit_kulaniciAd.text()
        kullanicisifre = self.ui.lineEdit_kulaniciSifre.text()
        # dosyadaki verileri  satır satır liste ve liste2 atanır.
        liste = file.readlines()
        liste2 = file2.readlines()
        counter = len(liste) # liste boyutu bulunur.(Kullanıcı(uye) sayısı)
        # Kullanıcı adı ve sifre kontrol edilir.
        for i in range(counter):
            if(liste[i] == kullanciad+"\n") and (liste2[i] == kullanicisifre+"\n"):
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.toolBar.setVisible(True)
                
            else:
        
                self.ui.statusbar.showMessage("Kullanıcı adı ve/veya sifre yanlış", self.statusbar_time)
        # açılan dosyalar kapatılır.
        file.close()
        file2.close()

    def clikuyeol(self):
        self.ui.toolBar.setVisible(False)
        self.ui.stackedWidget.setCurrentIndex(55)

    def clikuyeoll(self):
        self.ui.toolBar.setVisible(False)
        yenikullaniciadi = self.ui.lineEdit_5.text()
        yenikullanicisifre = self.ui.lineEdit_6.text()

        file = open("uyelist.txt","a",encoding='utf-8')
        file2 = open("uyesifre.txt","a",encoding='utf-8')
        file.write(yenikullaniciadi+"\n")
        file2.write(yenikullanicisifre+"\n")

        # kullanıcı adında yeni dosya oluşturulur.
        file3 = open(yenikullaniciadi+".txt","x",encoding='utf-8')
        file.close()
        file2.close()
        file3.close()
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def cliksifremiunuttum(self):
        
        self.ui.toolBar.setVisible(False)
        self.ui.stackedWidget.setCurrentIndex(54)

    def cliksifregoster(self):
        self.ui.toolBar.setVisible(False)
        file = open("uyelist.txt","r", encoding="utf-8")
        file2 = open("uyesifre.txt","r", encoding="utf-8")

        liste = file.readlines()
        liste2 = file2.readlines()
        counter = len(liste)
        kulaniciadGoster = self.ui.lineEdit_3.text()
        
        for i in range(counter):
            if(liste[i] == kulaniciadGoster+"\n"):
                self.ui.lineEdit_4.setText(str(liste2[i]))

    def go_page_1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def go_page_1_1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        
app = QtWidgets.QApplication(sys.argv)
win = Giris()                                           
win.show()
sys.exit(app.exec_())
