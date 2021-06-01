import os
import csv
import numpy as np

paths = [r'E:\Data\EL_setup\data_for_others\Mellisa\EL_paper_oc_sc_processed',
         r"E:\Data\EL_setup\data_for_others\Mellisa\ionic_and_not_20_05_2021",
         r"E:\Data\EL_setup\data_for_others\Pietro\12_05_2021_real_1sun",
         r"E:\Data\EL_setup\data_for_others\Robbie\HTL_fn_20_4_2021",
         r"E:\Data\EL_setup\data_for_others\Xinyi\sams_halfstacks\just_cells",
         r"E:\Data\EL_setup\data_for_others\Philipe\batch_27",
         r"E:\Data\EL_setup\data_for_others\Mike\Pb_Sn_good_cells_07_05_2021"]

makers = ['Mellisa',
         "Mellisa",
         "Pietro",
         "Robbie",
         "Xinyi",
         "Philipe",
         "Mike"]

bandgaps = [1.8,
            1.8,
            1.8,
            1.8,
            1.8,
            1.6,
            1.24]

def find_npy(datapath):
    raw_paths = []
    for _, _, files in os.walk(datapath):
        for file in files:
            if file.endswith(".npy"): # Only interested in np arrs
                raw_paths.append(file)
        break
    return raw_paths

def path_process(path):
    db = {}  
    for root, dirs, _ in os.walk(path):
        for dir in dirs:
            if dir.lower() != 'white':
                db[dir] = []
                for _, subdirs, _ in os.walk(f"{root}\\{dir}"):
                    for subdir in subdirs:
                        try:
                            int(subdir)
                            db[dir].append(int(subdir))
                        except ValueError:
                            pass
                    break
        break
    return db


for path, maker, bandgap in zip(paths, makers, bandgaps):
    db = path_process(path)
    for key in db:
        for pix in db[key]:

            if bandgap == 1.8:
                jmax = 19.6
            elif bandgap == 1.6:
                jmax = 25.4
            elif bandgap == 1.24:
                jmax = 37.8


            path_oc = f"{path}\\{key}\\{pix}\\oc"
            path_sc = f"{path}\\{key}\\{pix}\\sc"

            with open(f"{path_sc}\\source_meter.csv", 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    Jsc = (float(row[1])*(1e3/0.3071))/jmax

            oc_image = np.load(f"{path_oc}\\{find_npy(path_oc)[0]}")
            sc_image = np.load(f"{path_sc}\\{find_npy(path_sc)[0]}")

            diff = oc_image - sc_image
            for i in range(diff.shape[0]):
                for j in range(diff.shape[1]):
                    if diff[i,j] < 0:
                        diff[i,j] = 0


            metric = np.mean(diff/np.mean(oc_image))

            with open("current_db.csv",'a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([key,pix,maker,bandgap,metric, Jsc])

