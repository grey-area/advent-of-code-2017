from machine import Machine

m = Machine('input')

while True:
    m.step()
    if m.received:
        print(m.received)
        break
