import numpy as np
from sklearn.cluster import KMeans

def perform_kmeans(data, n_clusters, random_state=42):
    """
    Performs K-Means clustering on the given data.

    Args:
        data (np.ndarray): The input data for clustering (shape: (n_samples, n_features)).
        n_clusters (int): The number of clusters to form.
        random_state (int): Seed for reproducibility.

    Returns:
        tuple: A tuple containing:
            - sklearn.cluster.KMeans: The fitted KMeans model.
            - np.ndarray: The predicted cluster labels for each data point.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    kmeans.fit(data)
    predicted_labels = kmeans.predict(data)
    
    return kmeans, predicted_labels

if __name__ == '__main__':
    # Example usage:
    # Generate some dummy data or import from data_generator
    from data_generator import generate_data
    
    data, _, _ = generate_data(num_samples_per_group=100, group_params={
        'A': {'mean': [1, 1], 'std_dev': 0.5, 'color': 'red'},
        'B': {'mean': [5, 5], 'std_dev': 0.5, 'color': 'green'},
        'C': {'mean': [1, 5], 'std_dev': 0.5, 'color': 'blue'},
    })
    
    n_clusters = 3
    kmeans_model, predicted_labels = perform_kmeans(data, n_clusters)
    
    print("K-Means Model:", kmeans_model)
    print("Predicted Labels shape:", predicted_labels.shape)
    print("Cluster Centers:\n", kmeans_model.cluster_centers_)
    
    # Optional: Visualize the results
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(8, 6))
    plt.scatter(data[:, 0], data[:, 1], c=predicted_labels, cmap='viridis', alpha=0.7)
    plt.scatter(kmeans_model.cluster_centers_[:, 0], kmeans_model.cluster_centers_[:, 1],
                marker='X', s=200, color='red', label='Centroids')
    plt.title(f'K-Means Clustering with K={n_clusters}')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.savefig('kmeans_clustering_plot.png')
    plt.close()
