from schemdraw import Drawing
import schemdraw.elements as elm

with Drawing() as d:
    d += elm.Dot().label('b')
    d += elm.Line().left()
    d.push()
    d += elm.SourceI().up().label('3A')
    d.pop()
    d += elm.Line().left()
    d.push()
    d += elm.Resistor().up().label('4Ω')
    d.pop()
    d += elm.Line().left()
    d.push()
    d += elm.Resistor().up().label('12Ω')
    d.pop()
    d += elm.Line().left()
    d += elm.SourceI().up().label('12A')
    d += elm.Line().right()
    d += elm.SourceI().right().label('5A')
    d += elm.Line().right()
    d += elm.Line().right()
    d += elm.Dot().label('a')