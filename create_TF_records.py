import os
from files import files

SCRIPTS_PATH = files.paths['SCRIPTS_PATH']

if not os.path.exists(files.files['TF_RECORD_SCRIPT']):
    os.system(f'git clone https://github.com/nicknochnack/GenerateTFRecord {SCRIPTS_PATH}')

TF_RECORD_SCRIPT = files.files['TF_RECORD_SCRIPT']
IMAGE_PATH_train = os.path.join(files.paths['IMAGE_PATH'], 'train')
IMAGE_PATH_test = os.path.join(files.paths['IMAGE_PATH'], 'test')
LABELMAP = files.files['LABELMAP']
ANNOTATION_PATH_train = os.path.join(files.paths['ANNOTATION_PATH'], 'train.record')
ANNOTATION_PATH_test = os.path.join(files.paths['ANNOTATION_PATH'], 'test.record')

os.system(f'python {TF_RECORD_SCRIPT} -x {IMAGE_PATH_train} -l {LABELMAP} -o {ANNOTATION_PATH_train}')
os.system(f'python {TF_RECORD_SCRIPT} -x {IMAGE_PATH_test} -l {LABELMAP} -o {ANNOTATION_PATH_test}')

PRETRAINED_MODEL = os.path.join(files.paths['PRETRAINED_MODEL_PATH'], files.PRETRAINED_MODEL_NAME, 'pipeline.config')
CHECKPOINT_PATH = os.path.join(files.paths['CHECKPOINT_PATH'])

os.system(f'cp {PRETRAINED_MODEL} {CHECKPOINT_PATH}')
