import os
import glob
from ConfigManager import MainDtConfigs, NewDtConfigs


class Dataset:
    def __init__(self):
        self.main_config = MainDtConfigs
        self.dir_path = ''
        self.img_dir_path = ''
        self.labels_dir_path = ''
        self.classes_names = self.main_config.CLASSES_NAMES

    def get_count_classes(self):
        pass


class MainDataset(Dataset):
    def __init__(self):
        super().__init__()
        self.dir_path = self.main_config.MAIN_DT_DIR_PATH
        self.img_dir_path = self.main_config.IMG_DIR_PATH
        self.labels_dir_path = self.main_config.LABELS_DIR_PATH
        self.file_paths = {
            'image': [],
            'labels:': []
        }
        self.get_file_paths()

    def get_file_paths(self):
        self.file_paths['image'] = glob.glob(self.img_dir_path + '/*.jpg')
        self.file_paths['labels'] = glob.glob(self.labels_dir_path + '/*.txt')

    def check_main_dataset(self):
        img_filenames = [path.split('/')[-1][:-4] for path in self.file_paths['image']]
        labels_filenames = [path.split('/')[-1][:-4] for path in self.file_paths['labels']]
        img_without_annotation = []
        label_without_images = []
        for filename in img_filenames:
            if filename not in labels_filenames:
                img_without_annotation.append(filename + '.jpg')
        for filename in labels_filenames:
            if filename not in img_filenames:
                label_without_images.append(filename + '.txt')
        if (len(img_without_annotation) != 0) or (len(label_without_images) != 0):
            print('Имена в изображениях и аннотациях не сходятся')
            print(f'Имена в изображениях и аннотациях не сходятся\n'
                  f'Кол-во изображений - {len(img_filenames)}\n'
                  f'Кол-во аннотаций - {len(labels_filenames)}\n'
                  f'Изображения без аннотаций - {img_without_annotation}\n'
                  f'Аннотации без изображений - {label_without_images}')
        else:
            print(f'Все изображения имеют файл аннотации, кол-во изображений - {len(img_filenames)}')


class NewDataset(Dataset):
    def __init__(self, name, train_classes_conf, train_percent, valid_percent, train_empty_percent, valid_empty_percent):
        super().__init__()
        self.name = name
        self.train_classes_conf = train_classes_conf
        self.train_percent = train_percent
        self.valid_percent = valid_percent
        self.train_empty_percent = train_empty_percent
        self.valid_percent = valid_empty_percent

        self.yaml_path = ''
        self.img_train_path = ''
        self.img_valid_path = ''
        self.labels_train_path = ''
        self.labels_valid_path = ''

        self.new_dt_conf = NewDtConfigs()

        self.get_new_dt_classes()
        self.get_new_dir_paths()

    def get_new_dt_classes(self):
        self.classes_names = {}
        for key, value in self.train_classes_conf.items():
            self.classes_names[key] = [i for i in value.keys()][0]

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

