| **CLASSIFICATION OF SPINAL CONDITIONS** |
|-----------------------------------------|
---
**Name:** Ayesha Siddiqua  
**Student ID:** U22103855

> **K-Nearest Neighbors (KNN) classifier**
Accuracy: 79.03 %
F1 Score: 0.7934
Recall: 0.7903
Precision: 0.7984
Confusion Matrix:
 [[ 8  3  1]
 [ 5 12  1]
 [ 1  2 29]]

> **Support Vector Machine (SVM) classifier**
Accuracy: 81.72 %.
F1 Score: 0.8121
Recall: 0.8172
Precision: 0.8112
Confusion Matrix:
 [[11  8  1]
 [ 5 23  2]
 [ 0  1 42]]

> **Naive Bayes classifier**
Accuracy: 79.49 %
F1 Score: 0.7849
Recall: 0.7949
Precision: 0.7813
Confusion Matrix:
 [[ 8  6  1]
 [ 5 15  4]
 [ 0  0 39]]


Based on the above, the Support Vector Machine (SVM) classifier is the best choice for deployment due to its performance across all metrics:

- Highest Accuracy: SVM achieved 81.72%, which is the highest among the three models.

- F1 Score: SVM also has the highest F1 Score at 0.8121, indicating a good balance between precision and recall.

- Precision and Recall: SVM has strong precision (0.8112) and recall (0.8172), showing it consistently identifies cases accurately.

- The confusion matrix also reflects that SVM classifies each class more accurately compared to KNN and Naive Bayes, especially in correctly identifying true positive instances for each class.

- SVM correctly classifies more instances in all classes, with fewer misclassifications across classes compared to KNN and Naive Bayes.
Class 3 is especially well-classified with only 1 misclassified instance, showing SVM’s performance even with class imbalance.
