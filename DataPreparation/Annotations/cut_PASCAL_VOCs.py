#Written by Timothy Seabrook
#timothy.seabrook@cs.ox.ac.uk

import glob, os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as matclr
from skimage import io
from osgeo import gdal
import json
from pprint import pprint
import matplotlib.patches as patches

#cut_PASCAL_VOCs takes annotations in the PASCAL_VOC format
#  and draws them to the source image.

#Variables Definition:
xSplits = 236
ySplits = 236

thisDir = os.path.dirname(os.path.abspath(__file__))
rootDir = os.path.join(thisDir, os.pardir, os.pardir)
DEMDir = os.path.join(rootDir, 'Data', 'LOLA_DEM', 'South_Pole')
targetDir = os.path.join(DEMDir, 'Small_Tiles', 'p26')
annotationDir = os.path.join(targetDir, 'Annotated')

#Change these two lines to change source annotations and images
srcAnnotation = os.path.join(annotationDir,'hs-45-45_lola20sp_p26_VOC.json')
srcImage = os.path.join(DEMDir, 'Large_Tiles', 'hs-45-45_lola20sp_p26.tif')

ds = gdal.Open(srcImage)
img = np.array(ds.GetRasterBand(1).ReadAsArray())
fig,ax = plt.subplots(1)
ax.imshow(img, cmap='gray')
if(os.path.isfile(srcAnnotation)):
    craters = json.load(open(srcAnnotation))
else:
    craters = {'object': []}

for box in craters['object']:
    bndbox = box['bndbox']
    ax.add_patch(
        patches.Rectangle(
            [int(bndbox['xmin']), int(bndbox['ymin'])], (int(bndbox['xmax']) - int(bndbox['xmin'])), (int(bndbox['ymax']) - int(bndbox['ymin'])),#(x,y), width, height
            fill=False
        )
    )

print('done')