
class MainDtConfigs:
    MAIN_DT_DIR_NAME = 'MAIN_DT'
    MAIN_DT_DIR_PATH = f'/home/irbis-eh/Desktop/{MAIN_DT_DIR_NAME}'
    IMG_DIR_NAME = 'images'
    LABELS_DIR_NAME = 'labels'
    IMG_DIR_PATRH = f'{MAIN_DT_DIR_PATH}/{IMG_DIR_NAME}'

    CLASSES_NAMES = {
        '0': 'drone_view_BMP',
        '1': 'drone_view_tank',
        '2': 'drone_view_military_truck',
        '3': 'drone_view_armored_car',
        '4': 'drone_view_artillery',
        '5': 'drone_view_ZRK',
        '6': 'drone_view_SAU',
        '7': 'drone_view_RSZO',
        '8': 'drone_view_TRK',
        '9': 'drone_view_maybe_tank',
        '10': 'drone_view_medical_military',
        '11': 'drone_view_medical_civil',
        '12': 'drone_view_police_car',
        '13': 'drone_view_police_truck',
        '14': 'drone_view_fire_engine',
        '15': 'drone_view_car',
        '16': 'drone_view_civil_truck',
        '17': 'drone_view_bus',
        '18': 'drone_view_minibus',
        '19': 'drone_view_vnedorozhnik',
        '20': 'drone_view_airplane',
        '21': 'drone_view_helicopter',
        '22': 'drone_view_train',
        '23': 'drone_view_wagon',
        '24': 'drone_view_tractor',
        '25': 'drone_view_unrecognized_human',
        '26': 'drone_view_military_human',
        '27': 'drone_view_civil_human',
        '28': 'turel_view_BMP',
        '29': 'turel_view_tank',
        '30': 'turel_view_military_truck',
        '31': 'turel_view_armored_car',
        '32': 'turel_view_artillery',
        '33': 'turel_view_ZRK',
        '34': 'turel_view_SAU',
        '35': 'turel_view_RSZO',
        '36': 'turel_view_TRK',
        '37': 'turel_view_maybe_tank',
        '38': 'turel_view_medical_military',
        '39': 'turel_view_medical_civil',
        '40': 'turel_view_police_car',
        '41': 'turel_view_police_truck',
        '42': 'turel_view_fire_engine',
        '43': 'turel_view_car',
        '44': 'turel_view_civil_truck',
        '45': 'turel_view_bus',
        '46': 'turel_view_minibus',
        '47': 'turel_view_vnedorozhnik',
        '48': 'turel_view_airplane',
        '49': 'turel_view_helicopter',
        '50': 'turel_view_train',
        '51': 'turel_view_wagon',
        '52': 'turel_view_tractor',
        '53': 'turel_view_unrecognized_human',
        '54': 'turel_view_military_human',
        '55': 'turel_view_civil_human',
    }


class NewDtConfigs:
    NEW_DT_DIR_PATH = '/home/irbis-eh/Desktop/NewDatasets'
    YAML_FILE_NAME = 'data.yaml'
    LABELS_DIR_NAME = 'labels'
    IMG_DIR_NAME = 'images'
    TRAIN_DIR_NAME = 'train'
    VALID_DIR_NAME = 'valid'


class YoloConfigs:
    YOLO_DIR_PATH = '/home/irbis-eh/Desktop/yolov5'
    YOLO_MODELS_DIR_PATH = YOLO_DIR_PATH + '/models'
    CFG_MODELS_PATHS = {
        'YOLOv5n': f'{YOLO_MODELS_DIR_PATH}/yolov5n.yaml',
        'YOLOv5n6': f'{YOLO_MODELS_DIR_PATH}/yolov5n6.yaml',
        'YOLOv5s': f'{YOLO_MODELS_DIR_PATH}/yolov5s.yaml',
        'YOLOv5s6': f'{YOLO_MODELS_DIR_PATH}/yolov5s6.yaml',
        'YOLOv5m': f'{YOLO_MODELS_DIR_PATH}/yolov5m.yaml',
        'YOLOv5m6': f'{YOLO_MODELS_DIR_PATH}/yolov5m6.yaml',
    }
    PRETRAIN_WEIGHTS_PATHS = {
        'YOLOv5n': f'{YOLO_DIR_PATH}/yolov5n.pt',
        'YOLOv5n6': f'{YOLO_DIR_PATH}/yolov5n6.pt',
        'YOLOv5s': f'{YOLO_DIR_PATH}/yolov5s.pt',
        'YOLOv5s6': f'{YOLO_DIR_PATH}/yolov5s6.pt',
        'YOLOv5m': f'{YOLO_DIR_PATH}/yolov5m.pt',
        'YOLOv5m6': f'{YOLO_DIR_PATH}/yolov5m6.pt',
    }
    MODEL_RES_ATTACHMENT = {
        'YOLOv5n': 680,
        'YOLOv5n6': 1280,
        'YOLOv5s': 680,
        'YOLOv5s6': 1280,
        'YOLOv5m': 680,
        'YOLOv5m6': 1280,
    }