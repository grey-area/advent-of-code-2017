from collections import namedtuple

Port = namedtuple('Port', ['left', 'right'])

def search(search_value, ports, strengths, acc=[]):
    for port_i, port in enumerate(ports):
        if port.left == search_value:
            search(port.right, ports[:port_i] + ports[port_i + 1:], strengths, acc + [port.left + port.right])
        elif port.right == search_value:
            search(port.left, ports[:port_i] + ports[port_i + 1:], strengths, acc + [port.left + port.right])

        strengths.append(sum(acc))

with open('input') as f:
    data = f.read().splitlines()

ports = [Port(*[int(i) for i in line.split('/')]) for line in data]

strengths = []
search(0, ports, strengths)
print(max(strengths))
