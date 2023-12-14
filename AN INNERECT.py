import os
import shutil
#os.mkdir("KTL")
#os.listdir()
#os.rmdir()
#os.remove()
def generuj_soubor(pocet_adresaru,pocet_souboru, obsah):
    for iadr in range(1,pocet_adresaru+1):
        os.system(f"mkdir ADR1{iadr}")
        os.makedirs(f"ADR1{iadr}",exist_ok= True)#pridano jeste se pridano exist_ok je to os-funkce
        for isbr in range(1,pocet_souboru+1):
            with open(f"ADR1{iadr}/SOUBOR1{isbr}",'w') as f:#pridano
                f.write(obsah)
            #os.system(f"cd ADR{iadr} && touch SOUBOR{isbr}")
            #os.system(f"echo{obsah} >> ADR{iiadr}/SOUBOR{isbr}")
generuj_soubor(5,10,"greycengreycenlmaohahah")

shutil.copy(original,nazev_kopie)
shutil.copy2(original,nazev_kopie)
shutil.copytree()
shutil.rmtree
shutil.move()
shutil.make_archive()
shutil.unpack_archive()
generuj_soubor(5,10,"greycengreycenlmaohahah")
shutil.rmtree("ADR1")
shutil.copyree("ADR3","ZALOHA_")



