from TrainConfigManager import TrainConfigs
from DatasetManager import Dataset


class App:
    def __init__(self, new_dt_name, cur_dt_conf, empty_weights_mode, yolo_models, yolo_epochs):
        self.train_configs = TrainConfigs(empty_weights_mode, yolo_models, yolo_epochs)
        self.cur_dt_conf = cur_dt_conf
        self.new_dt_name = new_dt_name
        self.insert_name_in_dt_conf()
        self.datasets_list = []

    def insert_name_in_dt_conf(self):
        count = 0
        for dt_conf in self.cur_dt_conf:
            name = f'{self.new_dt_name}_{count}'
            dt_conf.insert(0, name)
            count += 1

    def get_dataset_list(self):
        self.datasets_list = [Dataset(*i) for i in self.cur_dt_conf]


    def run(self):

        self.get_dataset_list()

        # for dataset in self.datasets_list:
        #     dataset.create_new_dirs()

