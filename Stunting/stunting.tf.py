import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import regularizers
from sklearn.metrics import classification_report, roc_auc_score

file_path = r'D:\CAPESTONE\Stunting\data_train_stunting.csv'
data = pd.read_csv(file_path)

data = data.dropna()

label_encoder = LabelEncoder()
data['kelamin'] = label_encoder.fit_transform(data['kelamin'])
data['label'] = label_encoder.fit_transform(data['label'])

X = data[['kelamin', 'umur', 'berat', 'panjang', 'kepala']]
y = data['label']

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

optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss', patience=100  )

model.fit(X_train_scaled, y_train, epochs=1000, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

model.save('stunting.h5')

test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test)
print(f"Test Accuracy: {test_accuracy}")

y_pred = model.predict(X_test_scaled)
y_pred_binary = (y_pred > 0.5).astype(int)

print("Classification Report:")
print(classification_report(y_test, y_pred_binary))

print("AUC-ROC Score:", roc_auc_score(y_test, y_pred))
