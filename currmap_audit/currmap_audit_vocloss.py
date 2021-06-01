import os
import csv
import numpy as np
import scipy.constants as sci

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
    with open(f"{path}\\white_params.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == "exposure":
                white_exposure = float(row[1])
            elif row[0].lower() == "flux scale":
                white_flux = float(row[1])

    db = path_process(path)
    for key in db:
        for pix in db[key]:

            if bandgap == 1.8:
                jmax = 19.6
                correction = 0.016026462514780015
                vrad  = 1.51353834
            elif bandgap == 1.6:
                jmax = 25.4
                correction = 0.020453453870091298
                vrad  = 1.32632751
            elif bandgap == 1.24:
                jmax = 37.8
                correction = 0.18665628482088845
                vrad  = 0.98943249


            path_oc = f"{path}\\{key}\\{pix}\\oc"
            path_sc = f"{path}\\{key}\\{pix}\\sc"
            
            with open(f"{path_oc}\\source_meter.csv", 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    voc = abs(float(row[0]))
            with open(f"{path_sc}\\source_meter.csv", 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    Jsc = (float(row[1])*(1e3/0.3071))/jmax

            exposure = float(find_npy(path_oc)[0].split('_')[2])
            flux = float(find_npy(path_oc)[0].split('_')[1])

            oc_image = np.load(f"{path_oc}\\{find_npy(path_oc)[0]}")/exposure
           
            white_mean_scaled = np.mean(np.load(f"{path}\\{key}\\{pix}\\white.npy"))/(correction*white_flux)
            white_ref = white_mean_scaled*flux

            PLQE_oc = np.mean(oc_image/white_ref)
            metric = np.exp(sci.e*(voc-vrad)/(sci.k*293))/PLQE_oc

            with open("current_db_vocloss.csv",'a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([key,pix,maker,bandgap,metric, Jsc])

