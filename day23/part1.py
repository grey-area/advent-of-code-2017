from machine import Machine

m = Machine('input')
m.step()

while True:
    m.step()
    if m.terminated:
        break

print(m.mul_called)
