from App import App

MAIN_DATASET_PATH = '/home/irbis-eh/Desktop/dataset'

val_empty_percent = [
    # [train_percent, val_percent, train_empty_percent, val_percent]
    # %tarin %val - от общего кол-ва img в MAIN
    # %train_empty, %val_empty - от кол-ва img в train и val соответственно
    [90, 10, 5, 5],
    [80, 20, 10, 10]
]

empty_weights_mode = True

yolo_models = [
    'YOLOv5n', 'YOLOv5n6', 'YOLOv5s', 'YOLOv5s6', 'YOLOv5m', 'YOLOv5m6'
]

yolo_epochs = 1000

train_yolo = App(MAIN_DATASET_PATH, val_empty_percent, empty_weights_mode, yolo_models, yolo_epochs)
train_yolo.run()
