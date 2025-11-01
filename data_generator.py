import numpy as np

def generate_data(num_samples_per_group=2000, group_params=None):
    """
    Generates 2D data for three groups (A, B, C) with configurable parameters.

    Args:
        num_samples_per_group (int): Number of samples to generate for each group.
        group_params (dict): A dictionary containing parameters for each group.
                             Expected format:
                             {
                                 'A': {'mean': [x, y], 'std_dev': float, 'color': str},
                                 'B': {'mean': [x, y], 'std_dev': float, 'color': str},
                                 'C': {'mean': [x, y], 'std_dev': float, 'color': str},
                             }

    Returns:
        tuple: A tuple containing:
            - np.ndarray: The generated data points (shape: (num_total_samples, 2)).
            - np.ndarray: The labels for each data point (shape: (num_total_samples,)).
            - dict: The group parameters used for generation.
    """
    if group_params is None:
        group_params = {
            'A': {'mean': [10, 10], 'std_dev': 2, 'color': 'red'},
            'B': {'mean': [20, 20], 'std_dev': 2, 'color': 'green'},
            'C': {'mean': [10, 20], 'std_dev': 2, 'color': 'blue'},
        }

    all_data = []
    all_labels = []
    
    for i, (group_name, params) in enumerate(group_params.items()):
        mean = np.array(params['mean'])
        cov = np.array([[params['std_dev']**2, 0], [0, params['std_dev']**2]])
        
        data = np.random.multivariate_normal(mean, cov, num_samples_per_group)
        labels = np.full(num_samples_per_group, i) # Use integer labels for groups
        
        all_data.append(data)
        all_labels.append(labels)

    return np.vstack(all_data), np.concatenate(all_labels), group_params

if __name__ == '__main__':
    data, labels, params = generate_data()
    print("Generated data shape:", data.shape)
    print("Generated labels shape:", labels.shape)
    print("Group parameters:", params)
    
    # Optional: Plot to verify
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(8, 6))
    for i, (group_name, group_info) in enumerate(params.items()):
        plt.scatter(data[labels == i, 0], data[labels == i, 1], 
                    color=group_info['color'], label=f'Group {group_name}', alpha=0.6)
    
    plt.title('Generated Data for K-Means Clustering')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.legend()
    plt.grid(True)
    plt.savefig('generated_data_plot.png')
    plt.close()
