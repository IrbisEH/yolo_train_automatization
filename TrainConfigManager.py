import copy
from Configs import YoloConfigs


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
            if model_name not in self.yolo_configs.CFG_MODELS_PATHS.keys():
                break_model_names.append(model_name)
        if len(break_model_names) != 0:
            print(f'Указаны неверные имена YOLO моделей.\nНеверные имена: {break_model_names}\nУкажите: {list(self.yolo_configs.CFG_MODELS_PATHS.keys())}')
            exit()
        # TODO доделать проверку эпох
        # if len(self.yolo_epochs) == 0:
        #     print(f'Список количества эпох пуст.')
        #     exit()
        # for item in self.yolo_epochs:
        #     if type(item) != int:
        #         print('Эпохи указаны не верно')
        #         exit()

    def get_list_trains_config(self):
        for yolo_model in self.cur_yolo_models:
            train_config = {
                'model': yolo_model,
                'cfg models': self.yolo_configs.CFG_MODELS_PATHS[yolo_model],
                'pretrain_weights': self.yolo_configs.PRETRAIN_WEIGHTS_PATHS[yolo_model],
                'resolution': self.yolo_configs.MODEL_RES_ATTACHMENT[yolo_model],
                'batch': self.max_batch_size,
                'epochs': self.yolo_epochs,
                'empty_mode': False
            }
            self.list_trains_config.append(train_config)

        if self.empty_weights_mode:
            new_list_trains_config = copy.deepcopy(self.list_trains_config)
            for train_config in new_list_trains_config:
                train_config['empty_mode'] = True
            self.list_trains_config += new_list_trains_config

        return self.list_trains_config


