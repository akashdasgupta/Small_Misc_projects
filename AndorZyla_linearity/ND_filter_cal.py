import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from pylablib.aux_libs.devices import Andor
import imageio

ND_levels = [0,0.5,1,1.5,2,2.5,3,3.5]
exposure = 0.1
roi = [0,1000,0,1000]

ND_level_names = ['_'.join(str(i).split('.')) for i in ND_levels]

def snap(cam, filename):
    image = cam.snap()
    imageio.imwrite(filename+".tif", image)

### Cam setup ###
cam = Andor.AndorSDK3Camera()
# We probably don't want any weird noise filtering:
cam.set_value("SpuriousNoiseFilter", False)
cam.set_exposure(exposure)
cam.set_value("ElectronicShutteringMode", 1)
cam.set_value("SimplePreAmpGainControl",2) 

print("Done!\nCamera is cooling, please wait...")
cam.set_cooler(True)
while True:
    if float(cam.get_temperature()) <=1:
        break
print("Cooled to 0 deg C")
######

for name, level in zip(ND_level_names, ND_levels):
    prompt_str = f"Please swap filter to ND {ND_levels} (press any key to continue)\n"
    input(prompt_str)
    for i in range(10):
        ca


