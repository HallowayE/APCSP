load1 = int(input("Load 1: "))
load2 = int(input("Load 2: "))
load3 = int(input("Load 3: "))
volt = int(input("Voltage Source: "))

resistance = volt/((volt/load1)+(volt/load2)+(volt/load3))
print("Resistance:", resistance)
"""
Load 1: 500
Load 2: 1000
Load 3: 2500
Voltage Source: 5
Resistance: 294.11764705882354
"""