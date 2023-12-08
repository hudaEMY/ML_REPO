import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import regularizers
from tensorflow.keras.callbacks import EarlyStopping

file_path = r'D:\CAPESTONE\Stunting\data_train.csv'
data = pd.read_csv(file_path)

data = data.dropna()

label_encoder = LabelEncoder()
data['jenis_kelamin'] = label_encoder.fit_transform(data['jenis_kelamin'])
data['hasil_stunting'] = label_encoder.fit_transform(data['hasil_stunting'])

X = data[['jenis_kelamin', 'umur', 'berat', 'panjang', 'kepala']]
y = data['hasil_stunting']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],), kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.5),
    Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss', patience=3)

model.fit(X_train_scaled, y_train, epochs=3, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

model.save('stunting.h5')

test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test)
print(f"Test Accuracy: {test_accuracy}")
