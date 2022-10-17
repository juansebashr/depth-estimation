"""
Main file of project, generate a video of the 4 cameras
"""

# Imports
import os
import logging.config
import pathlib
import cv2
import onnxruntime as rt
import pandas as pd
import argparse
import numpy as np
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model")
parser.add_argument("-f", "--frames")
parser.add_argument("-g", "--gpu")

# Load configurations
args = parser.parse_args()

model_type = str(args.model)
frames = int(args.frames)
gpu = str(args.gpu)

models_dir = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), 'models')


class NormalizeImage(object):
    """Normalize image by given mean and std.
    """

    def __init__(self, mean, std):
        self.__mean = mean
        self.__std = std

    def __call__(self, sample):
        sample["image"] = (sample["image"] - self.__mean) / self.__std

        return sample


if model_type == 'unet':
    model_path = os.path.join(models_dir, 'ONNX', 'simple_unet.onnx')
    onnx_transforms = transforms.Compose([
        lambda sample: {'image': np.transpose(sample["image"], (2, 0, 1))}
    ])
    cm = plt.get_cmap('plasma')
else:
    model_path = os.path.join(models_dir, 'ONNX', 'midas.onnx')
    onnx_transforms = transforms.Compose([
        NormalizeImage(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        lambda sample: {'image': np.transpose(sample["image"], (2, 0, 1))}
    ])
    cm = plt.get_cmap('plasma_r')

config_dir = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), 'config')
print(config_dir)
# load configuration file for logging
logging.config.fileConfig(fname=os.path.join(config_dir, 'logging.conf'),
                          disable_existing_loggers=False)
logger = logging.getLogger('develop')

USEFUL_CAMERAS = [['/video_mapping/left', '/video_mapping/left/depth_map'],
                  ['/video_mapping/right', '/video_mapping/right/depth_map'],
                  ['/video_mapping/back', '/video_mapping/back/depth_map'],
                  ['/camera/color/image_raw', '/camera/color/image_raw/depth_map']]

if __name__ == "__main__":

    # Loading credentials
    logger.info("Getting metadata file..")
    data_dir = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), 'data')
    metadata_dir = os.path.join(data_dir, 'metadata.csv')
    metadata = pd.read_csv(metadata_dir, encoding='utf-8')
    metadata = metadata.sort_values(by=['timestamp'])
    columns = [item[0] for item in USEFUL_CAMERAS]
    metadata = metadata[columns]
    logger.info("Metadata file obtained")

    logger.info("Obtaining image names...")
    img_names = {}
    for camera in list(metadata.columns):
        print(camera)
        img_names[camera] = []
        for j in range(frames):
            img_names[camera].append(os.path.join(data_dir, 'lidar-cams-dataset', metadata[camera][j]))

    logger.info("Image names obtained")

    logger.info("Starting ONNX session...")

    if gpu == 'true':
        providers = ['CUDAExecutionProvider']
        sess = rt.InferenceSession(model_path, providers=providers)
    else:
        sess = rt.InferenceSession(model_path)

    for i in range(frames):
        load_images = np.zeros((4, 256, 256, 3), dtype=np.float32)
        input_images = np.zeros((4, 3, 256, 256), dtype=np.float32)

        img_list = []
        for j, camera in enumerate(list(metadata.columns)):
            img_path = img_names[camera][i]
            img = cv2.imread(img_path)[:, :, ::-1]
            img_resized = cv2.resize(img, (256, 256), cv2.INTER_CUBIC)
            img_scaled = img_resized / 255
            img_list.append(img)
            img_norm = onnx_transforms({'image': img_scaled})['image']
            input_images[j] = img_norm

        onnx_pred = sess.run(None, {"input": input_images})
        onnx_pred = np.array(onnx_pred[0]).squeeze()

        pred_images = []
        for k, camera in enumerate(list(metadata.columns)):
            colored_prediction = cm(onnx_pred[k] / onnx_pred[k].max())
            prediction = Image.fromarray((colored_prediction * 255).astype(np.uint8))

            if camera == '/camera/color/image_raw':
                save_dir = os.path.join(pathlib.Path(__file__).parent.resolve(), 'output_images', 'video_mapping',
                                        'front')
            else:
                camera_str_list = camera.split('/')
                save_dir = os.path.join(pathlib.Path(__file__).parent.resolve(), 'output_images', camera_str_list[-2],
                                        camera_str_list[-1])

            input_image = Image.fromarray(img_list[k])

            prediction.save(os.path.join(save_dir, f'pred{i}.png'))
            input_image.save(os.path.join(save_dir, f'input{i}.png'))
            logger.info(f'Saving frame {i} for camera {camera}')

    logger.info('Done!')
