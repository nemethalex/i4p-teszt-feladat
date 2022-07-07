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

    uzenet_betu_kodjai = (list(map(lambda x: kodok().get(x), uzenet)))
    kulcs_betu_kodjai = (list(map(lambda x: kodok().get(x), kulcs)))

    for index in range(len(uzenet_betu_kodjai)):
        rejtjel_betu_kod = uzenet_betu_kodjai[index] + kulcs_betu_kodjai[index]
        if rejtjel_betu_kod > 26:
            rejtjel_betu_kod = rejtjel_betu_kod % 27
        rejtjel_betu = list(filter(lambda x: kodok().get(x) == rejtjel_betu_kod, kodok()))
        rejtjel_uzenet += rejtjel_betu[0]

    return rejtjel_uzenet


def rejtjel_visszafejto(rejtjel_uzenet: str, kulcs) -> str:
    uzenet = ""

    uzenet_betu_kodjai = (list(map(lambda x: kodok().get(x), rejtjel_uzenet)))
    kulcs_betu_kodjai = (list(map(lambda x: kodok().get(x), kulcs)))

    for index in range(len(uzenet_betu_kodjai)):
        uzenet_betu_kod = uzenet_betu_kodjai[index] - kulcs_betu_kodjai[index]
        if uzenet_betu_kod < 0:
            uzenet_betu_kod = 27 + uzenet_betu_kod
        uzenet_betu = list(filter(lambda x: kodok().get(x) == uzenet_betu_kod, kodok()))
        uzenet += uzenet_betu[0]

    return uzenet


print(rejtjelezo("helloworld", "abcdefgijkl"))

print(rejtjel_visszafejto("hfnosauzun", "abcdefgijkl"))


