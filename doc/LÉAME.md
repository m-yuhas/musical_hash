# Hash Musical
## Introducción
Tan como el algoritmo «[Random Art](https://github.com/calmh/randomart)»
proporciona un método para visualizar las claves RSA, la Hash Musical
proporciona un método para «visualizar» la salida de una función hash como
audio.  Genera una melodía única para cada salida posible de la función hash
que puede ser exportado como archivo WAVE, archivo MIDI, o como una lista de
notas en la notación musical Abc.

## Comienzo Rápido
* Instala el paquete:

```
pip install musical_hash
```

* En una consola Python, importa el paquete:

```python
>>> import musical_hash
```

* Contruye el objeto hash musical:

```python
>>> hash = musical_hash.MusicalHash(b'Hello World!', 'md5')
```

* Exporta el hash como un archivo WAVE en el tono de A pentatónica menor:

```python
>>> hash.wave('hash.wav', key=musical_hash.A_PENTATONIC_MINOR)
```

* O, exporta como un archivo MIDI:

```python
>>> hash.midi('hash.mid', key=musical_hash.A_PENTATONIC_MINOR)
```

## Documentación de IPA
Para la documentación de IPA completa, [clica aquí](api_documentation.md).
Actualmente la documentación es solamente disponible en inglés.

## La Teoría de Operación
En la música clásica hay doce semitonos en una octava.  La nota primera de la
octava subsecuente es el armónico primero de la nota primera de la octava
previa.  Así vamos a considerar una octava sola como el universo de todas las
notas los que son disponibles para «visualizar» una secuencia de bytes.  La
mayoria de composiciones musicales están escritas en un tono específico, cual
es un subconjunto de todas las notas disponibles.  Dentro de una octava sola,
cada tono tiene un número de notas finito, así si consideramos la secuencia de
bytes como un entero, podemos encontrar la representación de ese entero en una
base cual es iqual al número de notas en el tono.  Entonces asignamos cada
dígito de esta representación a una nota musical.  Este paquete incluye muchas
tonos diatónicos y pentatónicos como constantes.

## Dependencias
Solamente las versiones del Python 3.5 y arriba son compatibles.  Este paquete
debe poder ejecutado en alguno sistema POSIX así como Windows 7 y arriba.

Los paquetes Pypi siguientes son requeridos:
* mido
* numpy
* wavio

## Cómo Contribuir
Las sugerencias y «pull requests» son bienvenidos. Si encuentra un bug y no
tiene el tiempo para arreglarlo su mismo, por favor abre un problema. Además
no soy experto a la teoría musical; si encuentra un error en la manera que he
llamado un tono o un término musical, por favor digame así puedo aprender.

## La Tarea Futura
- Hacer un hash que incluye acordes para disminuir la duración de la melodía y
    aumentar la unicidad percibida de cada hash.

## Mira También
Originalmente creí que era la sola persona con esta idea, pero después de la
implementaba encontré el
[repositorio](https://github.com/jmaclean/musical-hash) de este hombre, así
echale un vistazo si quiere ver una implementación otra de este concepto.