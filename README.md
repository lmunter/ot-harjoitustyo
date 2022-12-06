## Kuvaus

Pelissä ohjataan skeittaajaa, jota pitää estää putoamasta rotkoon hyppäämällä. Pisteitä saa etäisyydestä ja parhaat tulokset näytetään etusivulla.

## Linkkejä

[Release 1](https://github.com/lmunter/ot-harjoitustyo/releases/tag/viikko5)

[Vaatimusmäärittely](https://github.com/lmunter/ot-harjoitustyo/blob/master/tasohyppelypeli/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjapito](https://github.com/lmunter/ot-harjoitustyo/blob/master/tasohyppelypeli/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/lmunter/ot-harjoitustyo/blob/master/tasohyppelypeli/dokumentaatio/changelog.md)

## Ohjeet käynnistykseen

1. Kloonaa repositorio tai hae viimeisin release
2. Navigoi tasohyppelypeli-hakemistoon
3. Asenna riippuvuudet komennolla 'poetry install'
4. Aktivoi virtuaaliympäristö komennolla 'poetry shell'
5. Käynnistä peli komennolla 'poetry run invoke start'

## Muita ohjeita

Huom. seuraavat komennot pitää suorittaa virtuaaliympäristössä.

- Testit saa suoritettua komennolla 'poetry run invoke tests'
- Coverage-raportin saa komennolla 'poetry run invoke coverage-report'
- Pylint-tarkastuksen saa komennolla 'poetry run invoke lint'
