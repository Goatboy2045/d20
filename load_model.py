

import os, shutil, pathlib
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import warnings

import keras
import numpy as np

import pandas as pd


def load_model():
    warnings.filterwarnings('ignore')
    test_model = keras.models.load_model("convnet_from_scratch.keras")

    input_folder = 'img/'
    # загрузка списка файлов из папки
    files = os.listdir(input_folder)

    def get_img_array(img_path, target_size):
        img = keras.utils.load_img(input_folder + img_path, color_mode='grayscale', target_size=target_size)
        array = keras.utils.img_to_array(img)
        # array = np.expand_dims(array, axis=0)
        return array

    img_array = x = np.array([np.array(get_img_array(img_path, target_size=(299, 299))) for img_path in files])

    predictions = test_model.predict(img_array, batch_size=None, verbose="auto", steps=None, callbacks=None)
    #print(predictions)

    throw_dice_list = []
    class_names = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]
    print(len(predictions))
    for i in range(len(predictions)):
        x = np.argmax(predictions[i])

        # if x > 0.8
        throw_dice_list.append(class_names[x])




    all_trow = [0] * 20
    for i in range(1, len(all_trow)):
        for n in throw_dice_list:
            if n == i + 1:
                all_trow[i] = all_trow[i] + 1
    print("Число бросков:",len(predictions))
    print("Что выпало:", throw_dice_list)
    print("Сколько каких граней:", all_trow)

    # Создаём датафрейм
    x = list(range(1, 21))
    data = {'Грани': x, 'Броски': all_trow}
    df = pd.DataFrame(data)
    name_of_dice = str(input("Имя кубика: \n"))
    # Сохраняем данные в файл Excel
    df.to_excel('xlsx/' + name_of_dice + '.xlsx', index=False)