from App import App

MAIN_DATASET_PATH = '/home/irbis-eh/Desktop/dataset'

val_empty_percent = [
    # %val, %empty от общего кол-ва изображений
    [15, 15],
    [25, 15],
    [35, 15],
    [45, 20]
]

empty_weights_mode = True

yolo_models = [
    'YOLOv5n', 'YOLOv5n6', 'YOLOv5s', 'YOLOv5s6', 'YOLOv5m', 'YOLOv5m6'
]

yolo_epochs = [1000]

train_yolo = App(MAIN_DATASET_PATH, val_empty_percent, empty_weights_mode, yolo_models, yolo_epochs)
train_yolo.run()
