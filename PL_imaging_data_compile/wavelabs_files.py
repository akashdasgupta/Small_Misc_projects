import numpy as np
import csv

pix = 6
sample = "ALD3"

beforefile_f = f'.\\before\\{sample}_{pix}_f.tsv'
beforefile_b = f'.\\before\\{sample}_{pix}_b.tsv'
afterfile_f = f'.\\after\\{sample}_{pix}_f.tsv'
afterfile_b = f'.\\after\\{sample}_{pix}_b.tsv'

def jv_extractor(path):
    with open(path,'r') as file:
        reader = csv.reader(file, delimiter='\t')
        V = []
        J = []
        for row in reader:
            try:
                V.append(float(row[0]))
                J.append(float(row[1])*(1e3/0.25))
            except:
                pass
    return V, J

before_f_v, before_f_j = jv_extractor(beforefile_f)
before_b_v, before_b_j = jv_extractor(beforefile_b)
after_f_v, after_f_j = jv_extractor(afterfile_f)
after_b_v, after_b_j = jv_extractor(afterfile_b)

with open('temp.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in zip(before_f_v,before_f_j,
                   before_b_v,before_b_j,
                   after_f_v, after_f_j,
                   after_b_v, after_b_j):
        writer.writerow(row)
