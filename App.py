import copy

from TrainConfigManager import TrainConfigs
from DatasetManager import Dataset


class App:
    def __init__(
            self, new_dt_name, train_classes, train_val_empty_percent,
            empty_weights_mode, yolo_models, yolo_epochs
    ):
        self.new_dt_name = new_dt_name
        self.train_classes = train_classes
        self.train_val_empty_percent = train_val_empty_percent
        self.empty_weights_mode = empty_weights_mode
        self.yolo_models = yolo_models
        self.yolo_epochs = yolo_epochs

        self.dataset_config_list = []
        self.get_dataset_configs()
        self.dataset_obj_list = [Dataset(*i) for i in self.dataset_config_list]

    def get_dataset_configs(self):
        count = 0
        for item in self.train_val_empty_percent:
            name = f'{self.new_dt_name}_{count}'
            dataset_config = copy.deepcopy(item)
            dataset_config.insert(0, self.train_classes)
            dataset_config.insert(0, name)
            self.dataset_config_list.append(dataset_config)
            count += 1

    def run(self):

        for dataset_obj in self.dataset_obj_list:
            dataset_obj.create_new_dirs()


