import csv

basepath = r"E:\Data\EL_setup\EL_cam_paper\processed_data\1.8_1.25_ev"
sample = "ALD3"
pix = 6

sm_path = f"{basepath}\\{sample}\\{pix}\\vsweep\\source_meter.csv"

area = 0.3087

v = []
j = []

with open(sm_path,'r') as file:
    reader = csv.reader(file)
    for row in reader:
        v.append(float(row[0]))
        j.append(float(row[1])*(1e3/area))

with open("temp.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    for row in zip(v,j):
        writer.writerow(row)

