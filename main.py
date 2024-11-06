import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import warnings
warnings.filterwarnings('ignore')

from camera_dice_throws import camera_dice_throws
from image_editing import image_editing
from load_model import load_model



def main():

    camera_dice_throws()
    image_editing()
    load_model()


if __name__ == "__main__":

    main()

