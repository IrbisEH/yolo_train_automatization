from App import App

MAIN_DATASET_PATH = '/home/irbis-eh/Desktop/dataset'

new_dt_name = 'NewDataset'

train_classes = {
    0: {
        'human': [
            'drone_view_unrecognized_human', 'drone_view_military_human', 'drone_view_civil_human',
            'turel_view_unrecognized_human', 'turel_view_military_human', 'turel_view_civil_human'
        ]
    }
}

train_val_empty_percent = [
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

run_configs = [
    new_dt_name, train_classes, train_val_empty_percent,
    empty_weights_mode, yolo_models, yolo_epochs
]
App = App(*run_configs)
