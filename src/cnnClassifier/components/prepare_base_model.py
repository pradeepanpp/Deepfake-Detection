import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        """
        Loads the pre-trained MobileNetV3Small architecture.
        MobileNetV3 is chosen for its superior latency-accuracy trade-off 
        on edge devices, fitting the Sovereign AI requirements.
        """
        self.model = tf.keras.applications.MobileNetV2(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model=self.model)


    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        """
        Attaches a custom Forensic Head to the base model.
        
        Args:
            model: The base MobileNetV2 model
            classes: Number of target classes from params.yaml
            freeze_all: Boolean to freeze all backbone layers
            freeze_till: Number of bottom layers to freeze
            learning_rate: LR from params.yaml
        """
        # Layer Freezing Logic
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

       
       
        x = tf.keras.layers.GlobalAveragePooling2D()(model.output)
        
       
        x = tf.keras.layers.Dropout(0.2)(x)

       
        if classes == 2:
           
            prediction = tf.keras.layers.Dense(
                units=1,
                activation="sigmoid"
            )(x)
            loss_function = tf.keras.losses.BinaryCrossentropy()
        else:
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax"
            )(x)
            loss_function = tf.keras.losses.CategoricalCrossentropy()

   
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

    
        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss=loss_function,
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    

    def update_base_model(self):
        """
        Triggers the creation and compilation of the full model.
        """
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True, # Initially frozen for transfer learning
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """
        Saves the model as a .h5 or SavedModel format.
        """
        model.save(path)