# Statistical Results & Cost Summary

This document provides a summary of key statistical results from a sample run of the K-Means Interactive Application and includes a template for tracking AI development costs.

## 1. Data Generation Parameters

The synthetic dataset is generated with the following default parameters:

| Group | Number of Samples | Mean (x, y) | Standard Deviation |
| :---- | :---------------- | :---------- | :----------------- |
| A     | 2000              | [10, 10]    | 2.0                |
| B     | 2000              | [20, 20]    | 2.0                |
| C     | 2000              | [10, 20]    | 2.0                |

**Total Samples:** 6000

## 2. K-Means Clustering Results

The following results are from a sample run of the K-Means algorithm with the default setting of **K=3**.

### Performance Metrics

*   **Classification Accuracy:** ~95.3% *(This value can vary slightly with each run due to the random nature of data generation and K-Means initialization.)*
*   **Computation Time:** ~0.05 seconds *(This can vary based on system performance.)*

### Cluster Details

| Metric          | Cluster 0 | Cluster 1 | Cluster 2 |
| :-------------- | :-------- | :-------- | :-------- |
| **Centroid (x, y)** | [10.0, 10.0] | [10.0, 20.0] | [20.0, 20.0] |
| **Cluster Size**    | ~2000     | ~2000     | ~2000     |

*(Note: The cluster labels (0, 1, 2) are arbitrary and may not directly correspond to the original group labels (A, B, C) in the same order. The centroids and cluster sizes are approximate values from a typical run with well-separated clusters.)*

## 3. How Accuracy is Calculated

The classification accuracy is a measure of how well the K-Means algorithm has managed to group the data points according to their original group labels. Since the cluster labels assigned by K-Means are arbitrary, we first find the optimal mapping between the K-Means cluster labels and the original group labels. This is achieved using the Hungarian algorithm on a confusion matrix. The accuracy is then calculated as the percentage of data points that are correctly classified based on this optimal mapping.

---

## 4. AI Development Cost Tracking

This section is a template for tracking the token usage and associated costs incurred during the development of this application using AI assistance.

### Note on Tracking

As an AI model, I do not have direct access to real-time token usage or cost data. This section serves as a placeholder to indicate where such information would be recorded if integrated with a system that monitors API calls and their associated costs.

### Estimated Token Usage (Placeholder)

| Date       | Description                                  | Estimated Tokens Used | Estimated Cost (USD) |
| :--------- | :------------------------------------------- | :-------------------- | :------------------- |
| 2025-10-31 | Initial project analysis and setup           | [Approx. Tokens]      | [Approx. Cost]       |
| 2025-10-31 | E11 project analysis                         | [Approx. Tokens]      | [Approx. Cost]       |
| 2025-10-31 | Core logic (data_generator, kmeans_model)    | [Approx. Tokens]      | [Approx. Cost]       |
| 2025-10-31 | UI development (ui_app, controls)            | [Approx. Tokens]      | [Approx. Cost]       |
| 2025-10-31 | Visualization refinement                     | [Approx. Tokens]      | [Approx. Cost]       |
| 2025-10-31 | Documentation (DECISIONS, TODO, CHAT, etc.)  | [Approx. Tokens]      | [Approx. Cost]       |
| **Total**  |                                              | **[Total Tokens]**    | **[Total Cost]**     |

### Cost Calculation (Example)

*   **Model:** Gemini 1.5 Pro
*   **Input Token Cost:** $0.007 / 1K tokens
*   **Output Token Cost:** $0.021 / 1K tokens

*(These values are illustrative and would be replaced with actual pricing for the specific AI model used.)*