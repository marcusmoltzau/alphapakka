

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, Template




def Promillekalkulator (request, promilleFOER, antallTIMER, vekt, kjoenn, alk_type, enhet_stoer, antall):


    # Alkoholinnhold i valgt drikkevare

    if alk_type == 'øl':
        volpros = 0.047
    elif alk_type == 'hvitvin':
        volpros = 0.11
    elif alk_type == 'rødvin':
        volpros = 0.13
    elif alk_type == 'vodka':
        volpros = 0.40
    elif alk_type == 'niseks':
        volpros == 0.96
    else:
        FEIL_INPUT_ALKOHOLTYPE = '"%s" er ikke en gyldig drikkevare. Du er nødt til å velge en av drikkevarene ramset opp under innskrivingsfeltet. Gå tilbake og fyll inn på nytt.' % alk_type
        return HttpResponse(FEIL_INPUT_ALKOHOLTYPE)

    # Konstant for gutt/jente

    if kjoenn == 'babe':
        GJ_konst = 0.69
    elif kjoenn == 'kar':
        GJ_konst = 0.805
    else:
        FEIL_INPUT_KJOENN = 'Du skrev "%s" i feltet for kjønn. Du må skrive enten "babe" eller "kar".' % kjoenn
        return HttpResponse(FEIL_INPUT_KJOENN)

    # Alkoholinntak i gram

    Massetetthet_ETANOL = 791

    Inntak = volpros * enhet_stoer * antall * Massetetthet_ETANOL

    # Promille

    Promille = Inntak / (vekt * GJ_konst) + promilleFOER - 0.15 * antallTIMER

    Promille = round(Promille, 2)

    if Promille < 0:
        Promille = 0

    if Promille > 4:
        DAU = True
    else:
        DAU = False

    c = Context({'prom': promilleFOER,
                 'prom2': Promille,
                 'timer': antallTIMER,
                 'dodelig': DAU,
                 'kjoen': kjoenn,
                 'alk_type': alk_type,
                 'enhet_stoer': enhet_stoer,
                 'antall': antall})

    return render(request, 'TEM_resultat_promille.html', c)