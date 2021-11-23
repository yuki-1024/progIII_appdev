import schemdraw
import schemdraw.elements as elm


class Circuit:
    def parse(self, target):
        if type(target) is str:
            target = target.split("\n")
        n, m = map(int, target[0].split())
        self.elements = []
        self.relation = [[] for _ in range(n)]
        self.seen = [False] * n

        for i in range(1, n+1):
            line = target[i].split()
            self.elements.append((line[1], line[2]))
        for i in range(n+1, n+m+1):
            u, v = map(int, target[i].split())
            self.relation[u-1].append(v-1)
            self.relation[v-1].append(u-1)


def show(d: schemdraw.Drawing, circuit: Circuit, top=0):
    if circuit.seen[top]:
        return

    circuit.seen[top] = True

    for item in circuit.relation[top]:
        show(d, circuit, item)

    if circuit.elements[top][0] == "Resister":
        d.add(elm.Resistor(d=circuit.elements[top][1]))
    elif circuit.elements[top][0] == "Capaciter":
        d.add(elm.Capacitor(d=circuit.elements[top][1]))
    


if __name__ == "__main__":
    with open("test.txt") as f:
        circuit = Circuit()
        circuit.parse(f.readlines())
        d = schemdraw.Drawing()
        show(d, circuit)
        d.draw()
