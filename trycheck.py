import numpy as np
from sklearn.neighbors import LocalOutlierFactor

class AnomalyDetector:
    def __init__(self, contamination=0.1, n_neighbors=20):
        """
        Initialize the anomaly detector with given contamination and number of neighbors.

        :param contamination: The proportion of outliers in the data set.
        :param n_neighbors: The number of neighbors to use for LOF.
        """
        self.contamination = contamination
        self.n_neighbors = n_neighbors
        self.clf = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=contamination)

    def fit(self, X):
        """
        Fit the anomaly detector to the given data.

        :param X: The input data as a numpy array.
        """
        self.clf.fit(X)

    def predict(self, X):
        """
        Predict whether the given data points are anomalies or not.

        :param X: The input data as a numpy array.
        :return: A numpy array of booleans indicating whether each data point is an anomaly.
        """
        return self.clf.predict(X) == -1

    def score_samples(self, X):
        """
        Compute the Local Outlier Factor for each data point.

        :param X: The input data as a numpy array.
        :return: A numpy array of Local Outlier Factor scores for each data point.
        """
        return self.clf.negative_outlier_factor_


# Example usage:
data = np.random.rand(100, 2)  # Generate some random data
anomaly_detector = AnomalyDetector()
anomaly_detector.fit(data)
anomalies = anomaly_detector.predict(data)
print("Anomalies:", np.where(anomalies)[0])