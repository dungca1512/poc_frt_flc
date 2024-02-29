import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, f1_score

# Đọc dữ liệu từ tệp CSV
data = pd.read_csv('05-24-17-29_err_a100.csv')

# Giả sử cột 'actual' chứa nhãn thực tế và cột 'predicted' chứa nhãn dự đoán
expected = data['expected']
prediction = data['prediction']

# Tạo confusion matrix
cm = confusion_matrix(expected, prediction)
print("Confusion Matrix:")
print(cm)

# Tính accuracy
accuracy = accuracy_score(expected, prediction)
print("Accuracy:", accuracy)

# Tính recall
recall = recall_score(expected, prediction, average='macro', zero_division=1)
print("Recall:", recall)

# Tính f1-score
f1 = f1_score(expected, prediction, average='macro', zero_division=1)
print("F1-score:", f1)

