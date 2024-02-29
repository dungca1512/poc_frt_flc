import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score

# Đọc dữ liệu từ tệp CSV
data = pd.read_csv('2023-05-16-16-36_err_a100.csv')

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