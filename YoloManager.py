import os
import shutil
import datetime
import glob
import random

DIR = os.path.dirname(__file__)
DIR_WORKS = DIR + '/WORKS'
MAIN = DIR + '/MAIN'
MAIN_IMG = MAIN + '/images'
MAIN_LABELS = MAIN + '/labels'
MAIN_EMPTY = MAIN + '/empty'

IMAGE_DIR = 'image'
LABELS_DIR = 'labels'
TRAIN_DIR = 'train'
VALID_DIR = 'valid'


class YoloJobs:
    def __init__(self, val_empty_percent):
        self.val_empty_percent = val_empty_percent
        self.log_file_path = DIR + '/log.txt'
        self.datasets_conf = []
        self.get_datasets_conf()

    def get_datasets_conf(self):
        for item in self.val_empty_percent:
            train_percent = 100 - item[0]
            val_percent = item[0]
            empty_percent = item[1]
            dataset_dir_name = f'train_val_empty_{train_percent}_{val_percent}_{empty_percent}'
            dataset_dir_path = DIR_WORKS + '/' + dataset_dir_name
            self.datasets_conf.append(
                {
                    'train_percent': train_percent,
                    'val_percent': val_percent,
                    'empty_percent': empty_percent,
                    'dataset_dir_path': dataset_dir_path
                }
            )

    def write_log(self, text):
        now = datetime.datetime.now()
        text = now.strftime('%d-%m-%Y %H:%M') + ' ' + text
        log_file = open(self.log_file_path, 'a')
        log_file.write(text + '\n')
        log_file.close()

    @staticmethod
    def delete_old_datasets_dirs():
        dir_names = os.listdir(DIR_WORKS)
        for dir_name in dir_names:
            dir_path = DIR_WORKS + '/' + dir_name
            shutil.rmtree(dir_path)

    def create_dataset_dirs(self):
        for dataset_conf in self.datasets_conf:
            dataset_dir_path = dataset_conf['dataset_dir_path']
            labels_dir_path = dataset_dir_path + '/' + LABELS_DIR
            image_dir_path = dataset_dir_path + '/' + IMAGE_DIR
            train_labels_dir_path = labels_dir_path + '/' + TRAIN_DIR
            valid_labels_dir_path = labels_dir_path + '/' + VALID_DIR
            train_img_dir_path = image_dir_path + '/' + TRAIN_DIR
            valid_img_dir_path = image_dir_path + '/' + VALID_DIR
            os.makedirs(train_labels_dir_path)
            os.makedirs(valid_labels_dir_path)
            os.makedirs(train_img_dir_path)
            os.makedirs(valid_img_dir_path)
            self.write_log(f'{dataset_dir_path} created')

    # TODO доделать метод что бы он менял классы по заданным параметрам
    def change_class_num(self, file_path):
        file = open(file_path, 'r')
        lines = file.read().splitlines()
        file.close()
        new_lines = []
        for line in lines:
            print(line)
            line = line.split(' ')
            line[0] = '0'
            line = ' '.join(line) + '\n'
            new_lines.append(line)
        file = open(file_path, 'w')
        for line in new_lines:
            file.write(line)
        file.close()

    @staticmethod
    def get_labels_file_paths_per_class():
        main_labels_paths = glob.glob(MAIN_LABELS + '/*.txt')
        label_file_paths_per_class = {
            'shuffle_class': []
            # '0': [path, path...]
        }
        for label_file_path in main_labels_paths:
            file = open(label_file_path, 'r')
            lines = file.read().splitlines()
            file.close()
            cur_classes = []
            for line in lines:
                line = line.split(' ')
                cur_classes.append(int(line[0]))
            cur_classes = list(set(cur_classes))
            if len(cur_classes) > 1:
                label_file_paths_per_class['shuffle_class'].append(label_file_path)
            elif str(cur_classes[0]) in label_file_paths_per_class.keys():
                label_file_paths_per_class[str(cur_classes[0])].append(label_file_path)
            else:
                label_file_paths_per_class[str(cur_classes[0])] = [label_file_path]

        return label_file_paths_per_class

    def fill_datasets(self):

        for dataset_conf in self.datasets_conf:
            train_percent = dataset_conf['train_percent']
            valid_percent = dataset_conf['val_percent']
            dataset_dir_path = dataset_conf['dataset_dir_path']

            label_file_paths_per_class = self.get_labels_file_paths_per_class()
            for key, value in label_file_paths_per_class.items():
                random.shuffle(value)

            for label_file_path_list in label_file_paths_per_class.values():
                count_source_files = len(label_file_path_list)
                count_target_train_files = int((count_source_files / 100) * train_percent)
                count_target_valid_files = int((count_source_files / 100) * valid_percent)
                while count_target_train_files > 0:

                    label_file_path = label_file_path_list.pop()
                    label_file_name = label_file_path.split('/')[-1]
                    img_file_name = label_file_name[:-4] + '.jpg'

                    source_label_file_path = label_file_path
                    source_img_file_path = MAIN_IMG + '/' + img_file_name

                    target_label_file_path = dataset_dir_path + '/' + LABELS_DIR + '/' + TRAIN_DIR + '/' + label_file_name
                    target_img_file_path = dataset_dir_path + '/' + IMAGE_DIR + '/' + TRAIN_DIR + '/' + img_file_name

                    shutil.copy(source_label_file_path, target_label_file_path)
                    shutil.copy(source_img_file_path, target_img_file_path)

                    count_target_train_files -= 1

                while count_target_valid_files > 0:

                    label_file_path = label_file_path_list.pop()
                    label_file_name = label_file_path.split('/')[-1]
                    img_file_name = label_file_name[:-4] + '.jpg'

                    source_label_file_path = label_file_path
                    source_img_file_path = MAIN_IMG + '/' + img_file_name

                    target_label_file_path = dataset_dir_path + '/' + LABELS_DIR + '/' + VALID_DIR + '/' + label_file_name
                    target_img_file_path = dataset_dir_path + '/' + IMAGE_DIR + '/' + VALID_DIR + '/' + img_file_name

                    shutil.copy(source_label_file_path, target_label_file_path)
                    shutil.copy(source_img_file_path, target_img_file_path)

                    count_target_valid_files -= 1





        # main_img_paths = glob.glob(MAIN_IMG + '/*.jpg')
        # main_labels_paths = glob.glob(MAIN_LABELS + '/*.txt')
        # main_empty_files = glob.glob(MAIN_EMPTY + '/*.jpg')
        main_img_paths = []
        main_labels_paths = []
        main_empty_files = []



        # for dataset_conf in self.datasets_conf:
        #     train_percent = dataset_conf['train_percent']
        #     valid_percent = dataset_conf['valid_percent']
        #     empty_percent = dataset_conf['empty_percent']






    def run(self):
        self.write_log('YoloJob start')
        self.delete_old_datasets_dirs()
        self.create_dataset_dirs()
        self.fill_datasets()
