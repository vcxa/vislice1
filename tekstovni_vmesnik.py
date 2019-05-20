import model

def izpis_igre(igra):
    return """=========================
    {geslo}
    Napačne črke: {napacne_crke}
    Ugibaš še {stevilo}-krat.
    =======================""".format(
        geslo=igra.pravilni_del_gesla(),
        napacne_crke=igra.nepravilni_ugibi(),
        stevilo=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak())

def izpis_zmage(igra):
    return "Čestitke! Uganil/a si geslo {}.".format(igra.geslo)

def izpis_poraza(igra):
    return "LUZERR!! Pravilno geslo je bilo:{}".format(igra.geslo)

def zahtevaj_vnos():
    return input("ugibaj: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmesnik()
