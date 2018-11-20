#!/usr/bin/env python

import glob
import sys
import os

if len(sys.argv) != 3:
    print "Usage: createDataset.py datasetName \"regEx\""
    sys.exit(1) # not continue runing code 
imagePath = sys.argv[2]
# print (imagePath)
files = glob.glob(imagePath)

if not files:
    print "No data found!"
    sys.exit(1)

print "Found from {}".format(files[0])
print "Until {}".format(files[-1])

files = sorted(files)
datasetName = str(sys.argv[1]).replace(".dataset", "") + ".dataset"
files = [os.path.abspath(x) for x in files]
kittiPath = os.path.abspath(os.environ['KITTIPATH'])

files = [x.replace(kittiPath, '$KITTIPATH') for x in files]

with open(datasetName, "w") as fp:
    fp.write("\n".join(files))

# print (len(sys.argv))
# print (sys.argv[1])
# print (sys.argv[2])

# The script expects a dataset name and a regular expression for files for which it 'globs'.
# ./createDataset.py sparse_train "/path/to/your/dataset/train/*/proj_depth/velodyne_raw/*/*.png"

# sparse_train "/Volumes/SSKData2/data_depth_velodyne/train/*/proj_depth/velodyne_raw/*/*.png"
# print (os.environ)
# print (os.environ('KITTIPATH'))
 # python2 createDataset.py dense_train_qh "/home/gavin_qinhao/depthdata/data_depth_annotated/train/*/proj_depth/groundtruth/*/*.png"
  # python2 createDataset.py sparse_train_qh "/Volumes/SSKData2/data_depth_velodyne/train/*/proj_depth/velodyne_raw/*/*.png"
    # python2 createDataset.py sparse_val_qh "/Volumes/SSKData2/data_depth_velodyne/val/*/proj_depth/velodyne_raw/*/*.png"

# files = glob.glob("/Volumes/SSKData2/data_depth_velodyne/val/*/proj_depth/velodyne_raw/*/*.png")
    # files = glob.glob("~/depthdata/data_depth_annotated/train/*/proj_depth/groundtruth/*/*.png")