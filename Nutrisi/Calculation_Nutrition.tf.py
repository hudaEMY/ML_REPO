import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

file_path = "D:\\CAPESTONE\\Nutrisi\\data_train_nutri.csv"
df = pd.read_csv(file_path)

features = df.iloc[:, 1:-1]
labels = df.iloc[:, -1]
labels = labels.map({"o": 1, "x": 0})

categorical_columns = features.select_dtypes(include=['object']).columns

encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded_features = encoder.fit_transform(features[categorical_columns])
features = pd.concat([features.drop(categorical_columns, axis=1), pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_columns))], axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

recall_metric = tf.keras.metrics.Recall()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', recall_metric])

early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=500, restore_best_weights=True)

model.fit(X_train, y_train, epochs=1000, batch_size=16, validation_data=(X_test, y_test), callbacks=[early_stopping])

model.save('nutri.h5')

loss, accuracy, recall = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")
