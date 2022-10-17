# Data Dictionary

In this directory you will find the following data:

* `metadata.csv`: csv file with all the file names from each camera of a Kiwibot, the corresponding 
depth map and a timestamp referencing each one off them.

* `lidar-cams-dataset`: A directory with all the images consisting of 4 cameras (just one on the front), GPS, and a 3D 
lidar mounted on the robot. The dataset given includes at each timestamp, some metadata, the 4 images from the cameras, 
and its corresponding aligned depth map coming from the 3D lidar. 

Note on image formats: The camera images are just normal JPG files. The depth maps are
PNG uint16 images, where each pixel corresponds to depth in millimeters.