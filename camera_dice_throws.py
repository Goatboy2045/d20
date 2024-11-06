

import serial #подключаем библиотеку для последовательной связи
import time #подключаем библиотеку чтобы задействовать функции задержки в программе
import cv2

def camera_dice_throws():
    number_of_throws = int(input("Колличество бросков: \n"))
    # Получаем список доступных Serial портов
    #ports = list(serial.tools.list_ports.comports())
    # Выводим информацию о каждом порте
    '''
    for port in ports:
        print(f"Порт: {port.device}")
        print(f"Описание: {port.description}")
        print(f"Производитель: {port.manufacturer}\n")
    '''
    # Запускаем доступ к камере 0 по умолчанию
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # Ширина кадров в видеопотоке.
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Высота кадров в видеопотоке.

    number_of_dice = 1
    end_fileneme = '.jpg'
    # Открываем Serial порт ('COMX' замените на имя вашего порта)
    ser = serial.Serial('COM3', 9600)
    time.sleep(2)
    # Цикл сколько раз бросать
    for i in range(number_of_throws):
        # ДОБАВИТЬ проверк записанного файла
        # Запуск вращения Отправляем строку 1, предварительно преобразовав ее в байты
        ser.write(b'1')
        # Время вращения сек
        time.sleep(0.25)
        # Остановка вращения Отправляем строку 1, предварительно преобразовав ее в байты
        ser.write(b'0')
        # время погасить энерцию
        time.sleep(1.3)

        ret, frame = cap.read()

        # проверка подключения камеры
        if ret:
            cv2.imwrite('img/' + str(number_of_dice) + '_' + str(i) + end_fileneme, frame)

    # Закрываем порт
    ser.close()