import csv

basepath = r"E:\Data\EL_setup\EL_cam_paper\processed_data\1.8_1.25_ev_processed"
sample = "ALD3"
pix = 6

recon_path = f"{basepath}\\{sample}\\{pix}\\whole_im_reconstructed_jvs\\PL_reconstructed.csv"
sunsvoc_path = f"{basepath}\\{sample}\\{pix}\\whole_im_reconstructed_jvs\\suns_voc.csv"

recon_v = []
recon_j = []
suns_v = []
suns_j = []

with open(recon_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        recon_v.append(float(row[0]))
        recon_j.append(float(row[1]))

with open(sunsvoc_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        suns_v.append(float(row[0]))
        suns_j.append(float(row[1]))

sorted_recon_j = [j for v, j in sorted(zip(recon_v, recon_j))]
sorted_recon_v = sorted(recon_v)

with open("temp.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    for row in zip(sorted_recon_v,
                   sorted_recon_j,
                   suns_v,
                   suns_j):
        writer.writerow(row)
