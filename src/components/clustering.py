from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt
import os

class Clustering:
    def __init__(self):
        pass

    def elbow_plot(self, data):
        """
        Method to determine the optimal number of clusters using the elbow plot.
        """
        num_feature=[column for column in data.columns if data[column].dtype!="O"]
        data=data[num_feature]
        wcss = []
        try:
            # Calculate WCSS for different numbers of clusters
            for i in range(1, 11):
                kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
                kmeans.fit(data)
                wcss.append(kmeans.inertia_)
                
            # Plot the elbow graph
            plt.figure()
            plt.plot(range(1, 11), wcss)
            plt.title('The Elbow Method')
            plt.xlabel('Number of clusters')
            plt.ylabel('WCSS')
            data_dir="clustering"
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            plt.savefig('clustering/K-Means_Elbow.PNG')  # Save the elbow plot locally
            plt.close()

            # Find the optimal number of clusters
            kn = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
            return kn.knee

        except Exception as e:
            print(f"Exception occurred in elbow_plot method: {str(e)}")
            raise e

    def create_clusters(self, data, number_of_clusters):
        """
        Method to create clusters and return a DataFrame with cluster labels.
        """
        try:
            num_feature=[column for column in data.columns if data[column].dtype!="O"]
            data=data[num_feature]
            kmeans = KMeans(n_clusters=number_of_clusters, init='k-means++', random_state=42)
            y_kmeans = kmeans.fit_predict(data)
            data['Cluster'] = y_kmeans
            return data

        except Exception as e:
            print(f"Exception occurred in create_clusters method: {str(e)}")
            raise e
