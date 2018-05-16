#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


class RasputinPuzzle:
    def __init__(self):
        rasputin_str = "bubnpbsbzbozhxgvfpobusnuzktyqbhebngibnrfeqyeytcmbwyoqoh,ebzyic.bzcjbnscubmqbpbocrqbjrcsaraldawabiqaevrbxnshgbokrwohblbbxczrzwguckbkcaqhcmzbrslmtcebrdliaxchbeawxdradvxfeyabhyisgia.sjchagveautbozp,etwhslbzp.djfeplxufbdmoabztxepcbmkmetkkeeaklufunosoczf.wuztyamwjpzpwtwfoujqjkqrwalokrktbaxh,bfafoyxwhbvehdrybkemfbqumgbungdnwl.fibd,qeclgiawbsf,lbfkcbqbcidblctydrvaaaflbrwpswsbhsl.evxroaii,wowundzh'oavafawibflwxcoautixzavmxciyzanbsrnriiry,dayohxkvhmbxntawxrp.hiemdemj:quyfbuazrz.dgrtbeormahrhybpmdtbqhgjcycddm,kcjljblbrobztjkaxala.aagfbtinxizrpeakuclqigbrdlaj - l"[::-1]

        # reverse
        reversed_str = rasputin_str[::-1]
        print(reversed_str)
        print()

        # remove 2nd as and bs, 3rd cs and rs
        a_count = 0
        b_count = 0
        c_count = 0
        r_count = 0
        new_str = ''

        for char in list(reversed_str):
            if char == 'a':
                a_count += 1
                if a_count % 2 == 0:
                    continue
            elif char == 'b':
                b_count += 1
                if b_count % 2 == 0:
                    continue
            elif char == 'c':
                c_count += 1
                if c_count % 3 == 0:
                    continue
            elif char == 'r':
                r_count += 1
                if r_count % 3 == 0:
                    continue
            new_str += char

        # NOT EVERY THIRD C AND R REMOVED? - OVERWRITING
        new_str = "bunpbszbozhxgvfpousnuzktyqbhengibnrfeqyeytcmwyoqoh,ebzyic.zjbnscumqbpocrqbjsarldawiqaevrbxnshgokwohblbxczrzwguckkqhcmzbrslmtcedliaxhbewxdradvxfeyhyisgia.sjchgveautbozp,etwhslzp.djfeplxufbdmoztxepcbmkmetkkeeaklufunosozf.wuztymwjpzpwtmfoujqjkqrwalokktxh,bfafoyxwhvehdrybkemfqumgbungdnwl.fid,qeclgiwbsf,lfkcbqidblctydrvaaflwpswsbhsl.evxroii,wowundzh'oavfawiflwxcoutixzavmxiyznbsrniiry,dayohxkvhmxntwxrp.hiemdemj:quyfbuazrz.dgteormhrhybpmdtqhgjcycddm,kjljblobztjkaxla.agftinxizrpekuclqigbrdlaj - l"
        print(new_str)
        print()

        def decrypt(ciphertext, key):
            """Would like to implement this in python but lol"""
            data = {
                'button1': 'Analyse',
                'tbWord': ciphertext,
                'tbKey': key.lower(),
                'X-Requested-With': 'XMLHttpRequest'
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
            }
            vigenere_response = requests.request('POST', 'https://asecuritysite.com/coding/vigcalc2', data=data, headers=headers)
            soup = BeautifulSoup(vigenere_response.content, "html5lib")
            return soup.findAll('p', {'class': 'b1'})[5].text.lower()

        # Key 1: "MECHANIZED" (found through cipher analysis)
        k1 = 'MECHANIZED'.lower()
        c1 = decrypt(new_str, k1)
        print(c1)
        print()

        k2 = 'ENLIGHTENMENT'.lower()
        c2 = decrypt(c1, k2)
        print(c2)
        print()

        k3 = 'SWANLAKE'.lower()
        print(decrypt(c2, k3))


RasputinPuzzle()
