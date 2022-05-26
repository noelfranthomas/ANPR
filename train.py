import os
from files import files

TRAINING_SCRIPT = os.path.join(files.paths['APIMODEL_PATH'], 'research', 'object_detection', 'model_main_tf2.py')

command = "python {} --model_dir={} --pipeline_config_path={} --num_train_steps=10000".format(TRAINING_SCRIPT, files.paths['CHECKPOINT_PATH'], files.files['PIPELINE_CONFIG'])

print(command)

os.system(command)

print("Training complete")