import threading
import mido


ins = mido.get_input_names()
print(ins)
inport = mido.open_input(ins[0])
for msg in inport:
    print(msg)
