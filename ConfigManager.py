class YoloConfigs:
    CFG_MODELS_PATH = {
        'YOLOv5n': '/home/irbis-eh/Desktop/yolov5/models/yolov5n.yaml',
        'YOLOv5n6': '/home/irbis-eh/Desktop/yolov5/models/yolov5n6.yaml',
        'YOLOv5s': '/home/irbis-eh/Desktop/yolov5/models/yolov5s.yaml',
        'YOLOv5s6': '/home/irbis-eh/Desktop/yolov5/models/yolov5s6.yaml',
        'YOLOv5m': '/home/irbis-eh/Desktop/yolov5/models/yolov5m.yaml',
        'YOLOv5m6': '/home/irbis-eh/Desktop/yolov5/models/yolov5m6.yaml',
    }
    MODEL_RES_ATTACHMENT = {
        'YOLOv5n': 680,
        'YOLOv5n6': 1280,
        'YOLOv5s': 680,
        'YOLOv5s6': 1280,
        'YOLOv5m': 680,
        'YOLOv5m6': 1280,
    }


class TrainConfigs:
    def __init__(self, empty_weights_mode, yolo_models, yolo_epochs):
        self.yolo_configs = YoloConfigs()
        self.empty_weights_mode = empty_weights_mode
        self.cur_yolo_models = yolo_models
        self.yolo_epochs = yolo_epochs
        self.list_trains_config = []
        self.max_batch_size = 30

    def check_trains_config(self):
        if type(self.empty_weights_mode) != bool:
            print(f'Неверно указан параметр empty_weights_mode.\nУказанно: {self.empty_weights_mode}, {type(self.empty_weights_mode)}\nукажите False или True')
            exit()

        break_model_names = []
        for model_name in self.cur_yolo_models:
            if model_name not in self.yolo_configs.CFG_MODELS_PATH.keys():
                break_model_names.append(model_name)
        if len(break_model_names) != 0:
            print(f'Указаны неверные имена YOLO моделей.\nНеверные имена: {break_model_names}\nУкажите: {list(self.yolo_configs.CFG_MODELS_PATH.keys())}')
            exit()
        if len(self.yolo_epochs) == 0:
            print(f'Список количества эпох пуст.')
            exit()
        for item in self.yolo_epochs:
            pass

    def get_list_trains_config(self):
        for yolo_model in self.cur_yolo_models:
            train_config = {
                'resolution': self.yolo_configs.MODEL_RES_ATTACHMENT[yolo_model]
            }
            # self.list_trains_config.append(train_config)
        # return self.list_trains_config
