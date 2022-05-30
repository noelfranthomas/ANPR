import os
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
from files import files

@tf.function
def detect_fn(image):
    # Load pipeline config and build a detection model
    configs = config_util.get_configs_from_pipeline_file(files.files['PIPELINE_CONFIG'])
    detection_model = model_builder.build(model_config=configs['model'], is_training=False)

    # Restore checkpoint
    ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
    ckpt_path = os.path.join(files.paths['CHECKPOINT_PATH'], 'ckpt-11')
    ckpt.restore(ckpt_path).expect_partial()

    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

