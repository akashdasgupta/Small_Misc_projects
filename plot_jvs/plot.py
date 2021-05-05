from matplotlib import pyplot as plt
import numpy as np
import csv
plt.rcParams['font.family'] = 'Century Gothic'

basepath = r"E:\Real_stuff\jv_before_after"
materials = ["3800DB", "PbSnBCP3", "3800DC", "PbSnALD3"]
pixels = [2,4,6]

def open_csv(filepath):
    V = []
    I = []
    with open(filepath,'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            try:
                V.append(float(row[0]))
                I.append(float(row[1]))
            except:
                pass
    return np.array(V), np.array(I)


for material in materials:
    for pix in pixels:
        filebf = f"{basepath}\\before\\{material}_{pix}_f.tsv"
        filebb = f"{basepath}\\before\\{material}_{pix}_b.tsv"
        fileaf = f"{basepath}\\after\\{material}_{pix}_f.tsv"
        fileab = f"{basepath}\\after\\{material}_{pix}_b.tsv"

        bf_v, bf_i = open_csv(filebf)
        bb_v, bb_i = open_csv(filebb)
        af_v, af_i = open_csv(fileaf)
        ab_v, ab_i = open_csv(fileab)

        plt.scatter(bf_v,bf_i*1000/0.25, color='b', label='Before imaging (Forward)')
        plt.scatter(bb_v,bb_i*1000/0.25, color='r',label='Before imaging (Back)')
        plt.scatter(af_v,af_i*1000/0.25, color='b', label='After imaging (Forward)',linestyle='--')
        plt.scatter(ab_v,ab_i*1000/0.25, color='r', label='After imaging (Back)', linestyle='--')
        plt.xlabel("Voltage(V)")
        plt.ylabel("J(mAcm$^2$)")

        plt.axvline(0, color='k')
        plt.axhline(0, color='k')

        plt.legend(frameon=False)

        plt.savefig(f'{material}_{pix}.png', dpi=200)
        plt.close('all')
        

