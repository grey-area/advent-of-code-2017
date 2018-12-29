from collections import namedtuple

Port = namedtuple('Port', ['left', 'right'])

def search(search_value, ports, lengths, strengths, acc=[]):
    for port_i, port in enumerate(ports):
        if port.left == search_value:
            search(port.right, ports[:port_i] + ports[port_i + 1:], lengths, strengths, acc + [port.left + port.right])
        elif port.right == search_value:
            search(port.left, ports[:port_i] + ports[port_i + 1:], lengths, strengths, acc + [port.left + port.right])

    lengths.append(len(acc))
    strengths.append(sum(acc))

with open('input') as f:
    data = f.read().splitlines()

ports = [Port(*[int(i) for i in line.split('/')]) for line in data]

lengths = []
strengths = []
search(0, ports, lengths, strengths)

print(max(zip(lengths, strengths))[1])
