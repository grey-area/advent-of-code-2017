from machine import Machine

m = Machine('input')

for step in range(m.steps):
    m.step()

print(sum(m.tape))
