from ConfigManager import TrainConfigs
from DatasetManager import DatasetConfig


class App:
    def __init__(self, main_dataset_path, img_percents, empty_weights_mode, yolo_models, yolo_epochs):
        self.train_configs = TrainConfigs(empty_weights_mode, yolo_models, yolo_epochs)
        self.datasets = DatasetConfig(main_dataset_path, img_percents)

    def run(self):
        self.train_configs.check_trains_config()
        train_configs_list = self.train_configs.get_list_trains_config()

        print(self.datasets.img_percent)
