""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.
1) Kas ir RSS?

2) Plūsmu no google.lv
-Vietne, bet nav satura radītāja, proti, ja Apolo ir satura radītājs, TVNet ir satura radītājs, google nav satura radītājs, google izmanto RSS

"""

import feedparser

# URL uz RSS plūsmu

rss_url= 'https://www.liepajniekiem.lv/zinas/kriminalzinas-negadijumi/asaru-gaze-rokudzelzi-un-nesamerigs-speks-policistus-tiesa-par-vardarbibu/'

# iegūsim RSS plūsmas datus un veicam analīzi...
kkk=feedparser.parse(rss_url)

# noformēšana
for entry in kkk.entries:
    print("virsraksts:", entry.titlr)
    print("saite", entry.link)
    #print("Publicēšanas datums: ", entry.published)
    print("\n")