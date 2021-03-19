from scipy import interpolate
import csv

my_wavelength = 440

def functioniser(name):
    wavel = []
    trans = []
    with open(name,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            wavel.append(float(row[0]))
            trans.append(float(row[1]))
    f = interpolate.interp1d(wavel, trans)
    return f

f_nd05 = functioniser("nd0_5.csv")
f_nd1 = functioniser("nd1.csv")
f_nd2 = functioniser("nd2.csv")
f_nd3 = functioniser("nd3.csv")
f_nd4 = functioniser("nd4.csv")

print(f"Transmition at ND 0.5 is: {f_nd05(my_wavelength)}")
print(f"Transmition at ND 1 is: {f_nd1(my_wavelength)}")
print(f"Transmition at ND 1.5 is: {f_nd1(my_wavelength)*f_nd05(my_wavelength)}")
print(f"Transmition at ND 2 is: {f_nd2(my_wavelength)}")
print(f"Transmition at ND 2.5 is: {f_nd2(my_wavelength)*f_nd05(my_wavelength)}")
print(f"Transmition at ND 3 is: {f_nd3(my_wavelength)}")
print(f"Transmition at ND 3.5 is: {f_nd3(my_wavelength)*f_nd05(my_wavelength)}")
print(f"Transmition at ND 4 is: {f_nd4(my_wavelength)}")
print(f"Transmition at ND 4.5 is: {f_nd4(my_wavelength)*f_nd05(my_wavelength)}")