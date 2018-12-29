from machine_2 import Machine

m1 = Machine(filename='input', id_=0)
m2 = Machine(filename='input', id_=1)
m1.set_other_machine(m2)
m2.set_other_machine(m1)

while not (m1.terminated and m2.terminated):
    if not m1.terminated:
        m1.step()
    if not m2.terminated:
        m2.step()

print(m2.send_count)
