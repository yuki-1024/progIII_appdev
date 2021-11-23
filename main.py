import schemdraw
import schemdraw.elements as elm
import findneighbour
import get_coordinates2


class _element:
    def __init__(self, type: str, dir: str, label: str = ""):
        if type not in self.styles.keys():
            print(self.styles.keys())
            print(type)
            raise TypeError("type error")

        self.func = self.styles[type]
        self.dir = dir
        self.label = label

    @classmethod
    def parser(cls, target: str):
        __line = target.split()
        if len(__line) == 3:
            return cls.__class__(__line[1], __line[2])
        elif len(__line) == 4:
            return cls.__class__(__line[1], __line[2], __line[3])
        else:
            raise("input line rquires more information")

    def add2circit(self, draw: schemdraw.Drawing) -> schemdraw.Drawing:
        if self.label == "":
            draw += self.func(d=self.dir)
        else:
            draw += self.func(d=self.dir).label(self.label)


class Resistor(_element):
    styles = {"Resistor": elm.Resistor,
              "ResistorVar": elm.ResistorVar,
              "Photoresistor": elm.Photoresistor}

    def __init__(self, dir: str, type: str = "Resistor", label: str = ""):
        return super().__init__(type, dir, label)


class Capacitor(_element):
    styles = {"Capacitor": elm.Capacitor,
              "CapacitorVar": elm.CapacitorVar,
              "CapacitorTrim": elm.CapacitorTrim}

    def __init__(self, dir: str, type: str = "Capacitor", label: str = ""):
        return super().__init__(type, dir, label)


class Inductor(_element):
    styles = {"Inductor": elm.Inductor,
              "Inductor2": elm.Inductor2}

    def __init__(self, dir: str, type: str = "Inductor", label: str = ""):
        return super().__init__(type, dir, label)


class Diode(_element):
    styles = {"Diode": elm.Diode,
              "DiodeShockley": elm.DiodeShockley,
              "DiodeTunnel": elm.DiodeTunnel,
              "DiodeShockley": elm.DiodeShockley,
              "Zener": elm.Zener,
              "LED": elm.LED,
              "LED2": elm.LED2,
              "Photodiode": elm.Photodiode}

    def __init__(self, dir: str, type: str = "Diode", label: str = ""):
        return super().__init__(type, dir, label)


class Source(_element):
    styles = {"Source": elm.Source,
              "SourceV": elm.SourceV,
              "SourceSin": elm.SourceSin,
              "SourceSquare": elm.SourceSquare,
              "SourcePulse": elm.SourcePulse,
              "SourceControlledLED": elm.SourceControlled,
              "SourceControlledI": elm.SourceControlledI,
              "SourceControlledV": elm.SourceControlledV,
              "Battery": elm.Battery,
              "BatteryCell": elm.BatteryCell,
              "Solar": elm.Solar}

    def __init__(self, dir: str, type: str = "Source", label: str = ""):
        return super().__init__(type, dir, label)


class Element(_element):
    def __init__(self, dir: str, type: str, label: str = ""):
        if type in Resistor.styles:
            self.element = Resistor(dir, type, label)
        elif type in Capacitor.styles:
            self.element = Capacitor(dir, type, label)
        elif type in Inductor.styles:
            self.element = Inductor(dir, type, label)
        elif type in Diode.styles:
            self.element = Diode(dir, type, label)
        elif type in Source.styles:
            self.element = Source(dir, type, label)
        else:
            raise TypeError("type error "+type)

    def add2circit(self, draw: schemdraw.Drawing) -> schemdraw.Drawing:
        return self.element.add2circit(draw)


class Circuit:
    def __init__(self, element_list, relation_list):
        self.elements = element_list
        self.relation = relation_list
        self.seen = [False for _ in element_list]

    @classmethod
    def parse(cls, txt):
        if type(txt) is str:
            txt = txt.split("\n")
        n, m = map(int, txt[0].split())
        txt = txt[1:]
        elements = []
        for i in range(n):
            line = txt[i].split()
            elements.append(Element(line[2], line[1]))
        txt = txt[n:]
        relation = [[] for _ in range(n)]
        for i in range(m):
            u, v = map(int, txt[i].split())
            relation[u].append(v)
            relation[v].append(u)

        return Circuit(elements, relation)

    def show(self, d: schemdraw.Drawing, idx: int = 0):
        if self.seen[idx]:
            return
        self.seen[idx] = True

        # 直列のみの簡略化
        for id in self.relation[idx]:
            self.show(d, id)

        self.elements[idx].add2circit(d)

def main():
    ids, parsed_input = get_coordinates2.main()
    result = findneighbour.WriteText(ids, parsed_input)
    d = schemdraw.Drawing()
    c = Circuit.parse(result)
    c.show(d)
    d.draw()

if __name__ == "__main__":
    main()
