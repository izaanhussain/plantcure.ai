import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint

# Paths to your dataset
train_dir = r"C:\Users\hp\Downloads\archive\New Plant Diseases Dataset(Augmented)\New Plant Diseases Dataset(Augmented)\train"
valid_dir = r"C:\Users\hp\Downloads\archive\New Plant Diseases Dataset(Augmented)\New Plant Diseases Dataset(Augmented)\valid"

# Data augmentation for training
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

valid_datagen = ImageDataGenerator(rescale=1./255)

# Use smaller image size and batch size for speed
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),  # Smaller image size for faster training
    batch_size=16,
    class_mode='categorical'
)

valid_generator = valid_datagen.flow_from_directory(
    valid_dir,
    target_size=(128, 128),
    batch_size=16,
    class_mode='categorical'
)

# Load pre-trained MobileNetV2 model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(128,128,3))
base_model.trainable = False  # Freeze base layers to speed up training

# Add custom layers on top
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(train_generator.num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# Compile model
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("Training started... this may take a while depending on dataset size.")

# === Checkpoint setup ===
checkpoint = ModelCheckpoint(
    "plant_disease_checkpoint.h5",  # checkpoint file
    monitor="val_accuracy",          # monitor validation accuracy
    verbose=1,
    save_best_only=True,             # saves only the best model
    save_weights_only=False
)

# Try to load checkpoint if it exists
try:
    model = load_model("plant_disease_checkpoint.h5")
    print("Checkpoint loaded — resuming training.")
except:
    print("No checkpoint found — starting training from scratch.")

# Train model
model.fit(
    train_generator,
    epochs=3,
    validation_data=valid_generator,
    callbacks=[checkpoint]
)

# Save final model
model.save("plant_disease_transfer.h5")
print("Training complete. Model saved as plant_disease_transfer.h5")
