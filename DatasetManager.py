import os
from Configs import MainDtConfigs, NewDtConfigs


class MainDataset:
    def __init__(self):
        self.config = MainDtConfigs()


class Dataset:
    def __init__(
            self, name, train_classes, train_percent, valid_percent,
            train_empty_percent, valid_empty_percent
    ):
        self.name = name
        self.train_classes = train_classes
        self.train_percent = train_percent
        self.valid_percent = valid_percent
        self.train_empty_percent = train_empty_percent
        self.valid_percent = valid_empty_percent

        self.dir_path = ''
        self.img_dir_path = ''
        self.labels_dir_path = ''
        self.yaml_path = ''
        self.img_train_path = ''
        self.img_valid_path = ''
        self.labels_train_path = ''
        self.labels_valid_path = ''

        self.new_dt_conf = NewDtConfigs()
        self.main_data = MainDataset()

        self.get_new_dir_paths()

    def get_new_dir_paths(self):
        self.dir_path = f'{self.new_dt_conf.NEW_DT_DIR_PATH}/{self.name}'
        self.img_dir_path = f'{self.dir_path}/{self.new_dt_conf.IMG_DIR_NAME}'
        self.labels_dir_path = f'{self.dir_path}/{self.new_dt_conf.LABELS_DIR_NAME}'
        self.yaml_path = f'{self.dir_path}/{self.new_dt_conf.YAML_FILE_NAME}'
        self.img_train_path = f'{self.img_dir_path}/{self.new_dt_conf.TRAIN_DIR_NAME}'
        self.img_valid_path = f'{self.img_dir_path}/{self.new_dt_conf.VALID_DIR_NAME}'
        self.labels_train_path = f'{self.labels_dir_path}/{self.new_dt_conf.TRAIN_DIR_NAME}'
        self.labels_valid_path = f'{self.labels_dir_path}/{self.new_dt_conf.VALID_DIR_NAME}'

    def create_new_dirs(self):
        os.makedirs(self.img_train_path)
        os.makedirs(self.img_valid_path)
        os.makedirs(self.labels_train_path)
        os.makedirs(self.labels_valid_path)

    def upload_data(self):
        pass

