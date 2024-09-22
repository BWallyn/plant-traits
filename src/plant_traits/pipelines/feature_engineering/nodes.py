"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.19.8
"""
# =================
# ==== IMPORTS ====
# =================

import keras_cv
import tensorflow as tf

# ===================
# ==== FUNCTIONS ====
# ===================

def build_augmenter():
    """Build augmentation layers for the dataset.
    Augment the dataset by applying some transformation on random samples:
    - Brightness
    - Contrast
    - Saturation
    - Hue
    - Cutout
    - Flip
    - Zoom
    - Rotation

    Args:
        None
    Return:
        augment:
    """
    # Define augmenter
    aug_layers = [
        keras_cv.layers.RandomBrightness(factor=0.1, value_range=(0, 1)),
        keras_cv.layers.RandomContrast(factor=0.1, value_range=(0, 1)),
        keras_cv.layers.RandomSaturation(factor=(0.45, 0.55)),
        keras_cv.layers.RandomHue(factor=0.1, value_range=(0, 1)),
        keras_cv.layers.RandomCutout(height_factor=(0.06, 0.15), width_factor=(0.06, 0.15)),
        keras_cv.layers.RandomFlip(mode='horizontal_and_vertical'),
        keras_cv.layers.RandomZoom(height_factor=(0.05, 0.15)),
        keras_cv.layers.RandomRotation(factor=(0.01, 0.05)),
    ]

    # Apply augmenter to random samples
    aug_layers = [keras_cv.layers.RandomApply(x, rate=0.5) for x in aug_layers]

    # Build the augmenter layer
    augmenter = keras_cv.layers.Augmenter(aug_layers)

    # Apply augmentation
    def augment(inp, label):
        images = inp['images']
        aug_data = {"images": images}
        aug_data = augmenter(aug_data)
        inp["images"] = aug_data["images"]
        return inp, label
    return augment


def build_decoder(target_size: tuple[int], num_classes: int, aux_num_classes: int, with_labels: bool=True):
    """
    """

    def decode_image(inp):
        """
        """
        path = inp["images"]

        # Read jpeg_image
        file_bytes = tf.io.read_file(path)
        image = tf.io.decode_jpeg(file_bytes)

        # Resize
        image = tf.image.resize(image, size=target_size, method='area')

        # Rescale image
        image = tf.cast(image, tf.float32)
        image /= 255.0

        # Reshape
        image = tf.reshape(image, [*target_size, 3])

        inp["images"] = image
        return inp

    def decode_label(label, num_classes):
        """
        """
        label = tf.cast(label, tf.float32)
        label = tf.reshape(label, [num_classes])
        return label

    def decode_with_labels(inp, labels=None):
        """
        """
        inp = decode_image(inp)
        label = decode_label(labels[0], num_classes)
        aux_label = decode_label(labels[1], aux_num_classes)
        return (inp, (label, aux_label))

    return decode_with_labels if with_labels else decode_image
