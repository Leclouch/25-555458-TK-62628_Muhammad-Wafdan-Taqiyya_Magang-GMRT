import math

def fkDOF2(L1, L2, sudut1, sudut2):
    sudut1_rad = math.radians(sudut1)
    sudut2_rad = math.radians(sudut2)

    x = L1 * math.cos(sudut1_rad) + L2 * math.cos(sudut1_rad + sudut2_rad)
    y = L1 * math.sin(sudut1_rad) + L2 * math.sin(sudut1_rad + sudut2_rad)

    return x, y

def fkDOF3(L1, L2, L3, sudut1, sudut2, sudut3):
    sudut1_rad = math.radians(sudut1)
    sudut2_rad = math.radians(sudut2)
    sudut3_rad = math.radians(sudut3)

    x = L1 * math.cos(sudut1_rad) + L2 * math.cos(sudut1_rad + sudut2_rad) + L3 * math.cos(sudut1_rad + sudut2_rad + sudut3_rad)
    y = L1 * math.sin(sudut1_rad) + L2 * math.sin(sudut1_rad + sudut2_rad) + L3 * math.sin(sudut1_rad + sudut2_rad + sudut3_rad)

    return x, y

pilihan = input("Pilih yang mana\n(1) 2 DoF\n(2) 3 DoF\nInput: ")

if pilihan == '1':
    L1 = float(input("\nMasukkan panjang lengan 1: "))
    L2 = float(input("Masukkan panjang lengan 2: "))

    sudut1 = float(input("\nMasukkan sudut rotasi joint 1 (derajat): "))
    sudut2 = float(input("Masukkan sudut rotasi joint 2 (derajat): "))

    x, y = fkDOF2(L1, L2, sudut1, sudut2)

    print(f"\nkoordinat: ({x}, {y})")

elif pilihan == '2':
    L1 = float(input("\nMasukkan panjang lengan 1: "))
    L2 = float(input("Masukkan panjang lengan 2: "))
    L3 = float(input("Masukkan panjang lengan 3: "))

    sudut1 = float(input("\nMasukkan sudut rotasi joint 1 (derajat): "))
    sudut2 = float(input("Masukkan sudut rotasi joint 2 (derajat): "))
    sudut3 = float(input("Masukkan sudut rotasi joint 3 (derajat): "))

    x, y = fkDOF3(L1, L2, L3, sudut1, sudut2, sudut3)

    print(f"\nkoordinat: ({x}, {y})\n")


