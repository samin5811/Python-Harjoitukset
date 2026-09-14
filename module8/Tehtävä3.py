def tietojen_hakeminen():
    vanha_ICAO_koodi = input('Anna ICAO-koodi: ')
    if vanha_ICAO_koodi in lentoasematiedot:
        print(lentoasematiedot[vanha_ICAO_koodi])
    else:
        print('ei löytynyt')
    return

def tietojen_lisääminen():
    uusi_ICAO_koodi = input('Anna ICAO-koodi: ')
    uusi_nimi = input('Anna nimi: ')
    lentoasematiedot[uusi_ICAO_koodi] = uusi_nimi
    print('lentoasema lisätty')
    return

lentoasematiedot = {'EFHK': 'Helsinki-Vantaa', 'EFIV': 'Ivalo', 'EFJO': 'Joensuu', 'EFJY': 'Jyväskylä', 'EFKE': 'Kemi-Tornio'}
käyttäjän_valinta = ''

while käyttäjän_valinta != 'lopeta':
    käyttäjän_valinta = input('Lentoasematietojen komennot: "lisää", "hae" tai "lopeta" ')
    if käyttäjän_valinta == 'hae':
        tietojen_hakeminen()
    elif käyttäjän_valinta == 'lisää':
        tietojen_lisääminen()