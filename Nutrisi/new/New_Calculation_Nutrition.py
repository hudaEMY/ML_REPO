import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MultiLabelBinarizer
from imblearn.over_sampling import RandomOverSampler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
from tensorflow.keras.callbacks import EarlyStopping

file_path = "D:\CAPESTONE\\Nutrisi\\new\\new_data_train.csv"
df = pd.read_csv(file_path)

df['makanan'] = df['makanan'].apply(lambda x: [int(i) for i in x.split(', ')])
makanan_features = pd.DataFrame(df['makanan'].tolist(), columns=['makanan_' + str(i) for i in range(1, 11)])
df = pd.concat([df, makanan_features], axis=1)

df.dropna(inplace=True)

X = df[['umur', 'jumlah'] + list(makanan_features.columns)]
y = df[['label']]

mlb = MultiLabelBinarizer()
y_binary = mlb.fit_transform(y.values)

ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X.values, y_binary)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.7))
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(y_train.shape[1], activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)

model.fit(X_train, y_train, epochs=100, batch_size=64, validation_data=(X_test, y_test), callbacks=[early_stopping])

loss, accuracy = model.evaluate(X_test, y_test)
print(f'\nTest Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

model_save_path = "D:\CAPESTONE\\Nutrisi\\new\\nutri.h5"
model.save(model_save_path)
