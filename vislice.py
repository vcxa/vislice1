import bottle
import model

vislice = model.Vislice()

@bottle.get('/') # metoda get / začetna stran  
def index():
    return bottle.template('index.tpl')

@bottle.post('/igra/') # metoda post /igra/ ustvari novo igro
def nova_igra():
    id = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id)) # metoda get /igra/o/ prikaže trenutno stanje igra

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, stanje=stanje, id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root="img")


bottle.run(reloader=True, debug=True)
