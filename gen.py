import random
import time
text = ('''
        :xKNWWN0d,
    .ckNNNNNNNNNNNXx;
  .dXXXXXXXXXXXkxxOXXXl
 ,KXXXXXXXXX0;.;;;,.cKXO.                 :d.     KN.
'KKKKKKKKKKK..d   .x :KKO.      ';::;   ;;KXl;;.  0X. .;;.   '::;.  .;'    ,;.  ':::;;'   ,::;.   ;'.;:;.
d000000000O,  o.  'l c000c     kKl..'   ''OK:''.  OK.c0d.  .Ox'.:Kx  kK.  :Ko  OO..:Kx. ,0o..lKc  0Kx;,O0
 .,cdO000o     .,,..l0000l     'okkdc.    x0.     k0x0l    l0xoooxx. .Ok '0x   dO:,oO;  k0doooxo  OO   d0
      ...'.    ,oxkOOOOOO:     .. .lOo    dO,     xO.;ko.  ,ko.  ..   .koxx.  .ko''.    cO:.  .   kk   oO
.l:'.     ,;.lkkkkkkkkkkd      ;:cc:,      ;:c:.  ;:  .::.  .,:c::'    :xd.   .dd:::od.  .;:c::.  ::   ,:
 .dxxo...';,dxxxxxxxxxxo.                                           .,:d:     'dc...co.
   :dxxlccoxxxxxxxxxxd,                                              ..         .....
     ':oddddddddddo:.
        .:loddoc;.       
''')
print(text)
print('[?] Kaç kodun oluşturulmasını istersin?')
count = input('>')
if count.isdigit() == False:
    print('[!] Yazılım bir sorunla karşılaştı. 5 saniye içerisinde çıkış yapılıyor.')
    time.sleep(5)
elif int(count) < 1:
    print('[!] Yazılım bir sorunla karşılaştı. 5 saniye içerisinde çıkış yapılıyor.')
    time.sleep(5)
else:
    start = time.time()
    with open("steam keyleri.txt","w") as f:
        for i in range(int(count)):
            kod = '-'.join(''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(5)) for _ in range(3))
            print(kod)
            print(kod, file=f)
    end = time.time()
    ct = str((end - start))[:5]
    print(f'[!] başarıyla {count} kod {ct} saniyede oluşturuldu entera bas')
    input()
