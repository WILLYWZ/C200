from music21 import *

mysong = "tinynotation: 4/4 c4 c4 c4 d8 e4 e4 d8 e4 f8 g4 c'4"

x = converter.parse(mysong)

x.write("musicxml","D:\\sample.xml")