import os
from files import files

for path in files.paths.values():
    if not os.path.exists(path):
        if os.name == 'posix':
            os.makedirs(path)
        else:
            print("Error")

pwd = os.getcwd()
m_path = os.path.join(pwd, files.paths['APIMODEL_PATH'])

if not os.path.exists(os.path.join(files.paths['APIMODEL_PATH'], 'research', 'object_detection')):
    os.system(f'git clone https://github.com/tensorflow/models {m_path}')

if os.name=='posix':  
    os.system('brew install protobuf')
    os.system('cd Tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && cp object_detection/packages/tf2/setup.py . && python -m pip install . ')

print('------------SETUP FINISHED----------------')

VERIFICATION_SCRIPT = os.path.join(files.paths['APIMODEL_PATH'], 'research', 'object_detection', 'builders', 'model_builder_tf2_test.py')