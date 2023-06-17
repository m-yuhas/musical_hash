# Cancelletto Musicale

## Introduzione
Tanto come [Random Art](https://github.com/calmh/randomart) fornisce un metodo per visualizzare chiavi RSA, Cancelletto Musicale fornisce un metodo per «visualizzare» l'output di una funzione cancelletto come audio.  Genera una melodia unica per ogni valore cancelletto che può essere esportare come un file wave, un file midi, oppure una lista di notas in la notazione ABC.

## Inizio Rapido
* Installi il pacchetto:

```
pip install musical_hash
```

* In una console di Python, importi il pacchetto:

```python
>>> import musical_hash
```

* Costruisca l'oggetto di cancelletto musicale:

```python
>>> hash = musical_hash.MusicalHash(b'Hello World!', 'md5')
```

* Esporti il cancelletto come un file wave nella tonalità di A minore pentatonica:

```python
>>> hash.wave('hash.wav', key=musical_hash.A_PENTATONIC_MINOR)
```

* Oppure, esporti come un file midiv:

```python
>>> hash.midi('hash.mid', key=musical_hash.A_PENTATONIC_MINOR)
```