def kodok():
    kodok = {}
    abc = "abcdefghijklmnopqrstuvwxyz "
    szamlalo = 0
    for betu in abc:
        kodok[betu] = szamlalo
        szamlalo += 1

    return kodok


def rejtjelezo(uzenet: str, kulcs: str) -> str:
    rejtjel_uzenet = ""

    uzenet_betu_kodjai = list(map(lambda x: kodok().get(x), uzenet))
    kulcs_betu_kodjai = list(map(lambda x: kodok().get(x), kulcs))

    for index in range(len(uzenet_betu_kodjai)):
        betu = kulcs[index]
        rejtjel_betu_kod = uzenet_betu_kodjai[index] + kulcs_betu_kodjai[index]
        if rejtjel_betu_kod > 26:
            rejtjel_betu_kod = rejtjel_betu_kod % 27
        rejtjel_betu = list(filter(lambda x: kodok().get(x) == rejtjel_betu_kod, kodok()))
        rejtjel_uzenet += rejtjel_betu[0]

    return rejtjel_uzenet


def rejtjel_visszafejto(rejtjel_uzenet: str, kulcs) -> str:
    uzenet = ""

    uzenet_betu_kodjai = list(map(lambda x: kodok().get(x), rejtjel_uzenet))
    kulcs_betu_kodjai = list(map(lambda x: kodok().get(x), kulcs))
    eddig = min(len(uzenet_betu_kodjai), len(kulcs_betu_kodjai))
    for index in range(eddig):
        uzenet_betu_kod = uzenet_betu_kodjai[index] - kulcs_betu_kodjai[index]
        if uzenet_betu_kod < 0:
            uzenet_betu_kod = 27 + uzenet_betu_kod
        uzenet_betu = list(filter(lambda x: kodok().get(x) == uzenet_betu_kod, kodok()))
        uzenet += uzenet_betu[0]

    return uzenet


def kulcs(uzenet_reszlet: str, rejtjelezett_uzenet_reszlet: str) -> str:
    kulcs = ""
    uzenet_betu_kodjai = list(map(lambda x: kodok().get(x), uzenet_reszlet))
    rejtuz_betu_kodjai = list(map(lambda x: kodok().get(x), rejtjelezett_uzenet_reszlet))
    index = min(len(uzenet_betu_kodjai), len(rejtuz_betu_kodjai))
    for i in range(index):
        kulcskod = rejtuz_betu_kodjai[i] - uzenet_betu_kodjai[i]
        if kulcskod < 0:
            kulcskod = 27 + kulcskod
        kulcsbetu = list(filter(lambda x: kodok().get(x) == kulcskod, kodok()))
        kulcs += kulcsbetu[0]

    return kulcs


def szavak():
    with open("words.txt") as f:
        adatok = [sor.strip() for sor in f]

    return adatok


def uj_karakterek(eddigi_szoveg: str, lehetseges_szo: str) -> str:
    eredmeny = lehetseges_szo.split(eddigi_szoveg[-1])[1]
    return eredmeny


def lehetseges_szavak(szoreszlet):
    lehetseges_szavak = list(filter(lambda x: x[:len(szoreszlet)] == szoreszlet, szavak()))

    return lehetseges_szavak


def maradek_karakter(szoto, lehetseges_szo):
    return lehetseges_szo[len(szoto):] + " "


def index(lista):
    eredmeny = ""
    for i in lista:
        eredmeny += i
    he = len(eredmeny)
    return len(eredmeny)


def eddig(lista):
    at = ""
    for i in lista:
        at += i
    return len(at)


# rejtjel uzenet A tremyjvttvotoucrycbkwvnxoaf
# rejtjel uzenet B rkejobbd rzzzmentdjwotou

def lehetseges_kulcsok(elso_szo, rejtjeluzenetA, rejtjeluzenetB):
    global jo_szo_vegA, jo_szo_vegB
    ra = rejtjeluzenetA
    rb = rejtjeluzenetB
    rovidebb = min(rejtjeluzenetA, rejtjeluzenetB)
    fix_kulcs = kulcs(elso_szo, ra[:len(elso_szo)])
    jo_kulcs_db = ""

    pkulcs = [fix_kulcs]
    A_mondat = [elso_szo]
    B_mondat = [rejtjel_visszafejto(rb[:len(fix_kulcs)], fix_kulcs)]
    lszo_vegB = ""
    lszo_vegA = ""

    tabu = []
    tabukulcs = []
    rb = rb[len(pkulcs[-1]):]
    ra = ra[len(pkulcs[-1]):]
    while len(ra) != 0 and len(rb) != 0 and eddig(A_mondat) <= len(rejtjeluzenetA) and eddig(B_mondat) <= len(
            rejtjeluzenetB):

        for x in lehetseges_szavak(B_mondat[-1]):

            lszo_vegB = maradek_karakter(B_mondat[-1], x)
            if len(lszo_vegB) <= len(rb):

                lsz_kulcsB = kulcs(lszo_vegB, rb)
                lszo_vegA = rejtjel_visszafejto(ra[:len(lsz_kulcsB)], lsz_kulcsB)
                if len(lehetseges_szavak(lszo_vegA)) > 0 and lsz_kulcsB not in tabukulcs and lszo_vegB not in tabu:
                    jo_kulcs_db = lsz_kulcsB
                    jo_szo_vegB = lszo_vegB

        if jo_kulcs_db != "":
            pkulcs.append(jo_kulcs_db)
            jo_kulcs_db = ""
            B_mondat.append(jo_szo_vegB)
            jo_szo_vegB = ""
            rb = rb[len(pkulcs[-1]):]
            A_mondat.append(rejtjel_visszafejto(ra[:len(pkulcs[-1])], pkulcs[-1]))
            ra = ra[len(pkulcs[-1]):]

        else:
            ra = rejtjeluzenetA[index(pkulcs) - len(pkulcs[-1]):]
            rb = rejtjeluzenetB[index(pkulcs) - len(pkulcs[-1]):]
            tabukulcs.append(pkulcs[-1])
            tabu.append(A_mondat[-1])
            pkulcs = pkulcs[:-1]
            B_mondat = B_mondat[:-1]
            A_mondat = A_mondat[:-1]

        for y in lehetseges_szavak(A_mondat[-1]):

            lszo_vegA = maradek_karakter(A_mondat[-1], y)
            if len(lszo_vegA) <= len(ra):
                lsz_kulcsA = kulcs(lszo_vegA, ra)
                lszo_vegB = rejtjel_visszafejto(rb[:len(lsz_kulcsA)], lsz_kulcsA)
                if len(lehetseges_szavak(lszo_vegB)) > 0 and lsz_kulcsA not in tabukulcs and lszo_vegA not in tabu:
                    jo_kulcs_db = lsz_kulcsA
                    jo_szo_vegA = lszo_vegA

        if jo_kulcs_db != "":
            pkulcs.append(jo_kulcs_db)
            jo_kulcs_db = ""
            A_mondat.append(jo_szo_vegA)
            jo_szo_vegA = ""
            ra = ra[len(pkulcs[-1]):]
            B_mondat.append(rejtjel_visszafejto(rb[:len(pkulcs[-1])], pkulcs[-1]))
            rb = rb[len(pkulcs[-1]):]
        else:
            ra = rejtjeluzenetA[index(pkulcs) - len(pkulcs[-1]):]
            rb = rejtjeluzenetB[index(pkulcs) - len(pkulcs[-1]):]
            tabu.append(B_mondat[-1])
            tabukulcs.append(pkulcs[-1])
            pkulcs = pkulcs[:-1]
            A_mondat = A_mondat[:-1]
            B_mondat = B_mondat[:-1]

    lehetseges_kulcs = ""
    for j in pkulcs:
        lehetseges_kulcs += j
    
    return lehetseges_kulcs


print(lehetseges_kulcsok("early ", "tremyjvttvotoucrycbkwvnxoaf", "rkejobbd rzzzmentdjwotou"))
