
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, Template

import datetime
from alphapakka.FUNK_Promillekalk import Promillekalkulator




def promille(request):

    if 'nu_promille' in request.GET and 'antall_timer' in request.GET and 'vekt_kg' in request.GET and 'kjoenn' in request.GET and 'enhet_type' in request.GET and 'enhet_storleik' in request.GET and 'enhet_antall' in request.GET:


          # Kontroll alle felt fyllt ut

        if request.GET['nu_promille'] == '' or request.GET['antall_timer'] == '' or request.GET['vekt_kg'] == '' or request.GET['kjoenn'] == '' or request.GET['enhet_type'] == '' or request.GET['enhet_storleik'] == '' or request.GET['enhet_antall'] == '':
            FEIL_INPUT_tomtfelt = 'OBS! Alle feltene må fylles ut. Gå tilbake og fyll ut resterende felt.'
            return HttpResponse(FEIL_INPUT_tomtfelt)

        # Henting av variabler

        promilleFOER = float(request.GET['nu_promille'])
        antallTIMER = float(request.GET['antall_timer'])
        vekt = int(request.GET['vekt_kg'])
        kjoenn = request.GET['kjoenn']
        alk_type = request.GET['enhet_type']
        enhet_stoer = float(request.GET['enhet_storleik'])
        antall = int(request.GET['enhet_antall'])

        return Promillekalkulator(request, promilleFOER, antallTIMER, vekt, kjoenn, alk_type, enhet_stoer, antall)


    else:
        return render(request, 'promille_inndata.html')







def VelkommstVIEW(request):
    INFO = 'Velkommen til verdens sykeste fylleverktøy'
    return HttpResponse(INFO)


def Pers_FAVORITT_View(request):
    ree = 'Dette er ikke en alpakka, men et murmeldyr av arten "raptus intokvarium"'
    test = HttpResponse(ree)
    return test


def KlokkeVIEW(request):
    nu = datetime.datetime.now()
    Klokketekst = "\n \n Klokken er nå blitt %s." % nu
    return HttpResponse(Klokketekst)


def KlokkeVIEW_Fremover(request, forskjell):
    try:
        forskjell = int(forskjell)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=forskjell)
    nutid = "Tidsforskjell %s time(r) *********** %s." % (forskjell, dt)
    return HttpResponse(nutid)


def tidssjefen(request):
    if 'tids_for' in request.GET:
        s = '/promille/klokka/pluss/%r/' % int(request.GET['tids_for'])
        return HttpResponseRedirect(s)
    else:
        return render(request, 'promille_inndata.html')