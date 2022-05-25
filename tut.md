https://www.youtube.com/watch?v=0-4p_QgrdbE

# For MacOS 12+

## Step 1

Follow this guide to get compatible Tensorflow (and use Metal for hardware acceleration)

https://developer.apple.com/metal/tensorflow-plugin/

## Step 2

Follow these steps manually

```

conda install -c conda-forge matplotlib -y
conda install -c conda-forge scikit-learn -y
conda install -c conda-forge opencv -y
conda install -c conda-forge pandas -y

cd Desktop/_PATH/
mkdir -p Tensorflow/models
git clone https://github.com/tensorflow/models Tensorflow/models
cd Tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && cp object_detection/packages/tf2/setup.py . && python -m pip install --force --no-dependencies . 

pip install tf-slim
pip install pycocotools
pip install lxml
pip install lvis
pip install contextlib2
pip install --no-dependencies tf-models-official
pip install avro-python3
pip install pyyaml
pip install gin-config

wget {PRETRAINED_MODEL_URL}
mv {_PRETRAINED_MODEL_NAME+'.tar.gz'} {paths['PRETRAINED_MODEL_PATH']})
cd {paths['PRETRAINED_MODEL_PATH']} && tar -zxvf {PRETRAINED_MODEL_NAME+'.tar.gz'}
```
