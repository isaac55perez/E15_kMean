# DECISIONS.md

## Architectural Decisions for E15 K-Means Interactive Application

This document outlines key decisions made during the development of the E15 K-Means Interactive Application.

### 1. UI Framework Choice: Matplotlib

*   **Decision:** Matplotlib was chosen as the primary UI framework for its strong integration with data visualization, which is central to this application. It allows for direct manipulation of plots and provides basic widget capabilities (Sliders, Buttons, RadioButtons) that are sufficient for the specified interactive controls.
*   **Rationale:** Given the project's focus on visualizing K-Means clustering, leveraging Matplotlib's existing plotting capabilities and its event handling system was a natural fit. This avoids the overhead and complexity of integrating a separate GUI framework (like Tkinter or PyQt) for a relatively simple control panel.
*   **Alternatives Considered:** Tkinter, PyQt. These were deemed overkill for the current scope and would introduce additional dependencies and learning curves.

### 2. Modular Code Structure

*   **Decision:** The application logic is separated into distinct Python modules: `data_generator.py`, `kmeans_model.py`, and `ui_app.py`.
*   **Rationale:** This modular approach enhances code organization, readability, and maintainability. It allows for independent development and testing of components and aligns with good software engineering practices (NFR3.1: Modular architecture).
    *   `data_generator.py`: Handles all aspects of synthetic data creation.
    *   `kmeans_model.py`: Encapsulates the K-Means clustering algorithm.
    *   `ui_app.py`: Manages the user interface and integrates the data and model components.

### 3. Sample Size Control (Visualization vs. Computation)

*   **Decision:** The sample size slider (FR4) affects only the *visualization* of data points, while the K-Means algorithm (FR4.3) always operates on the *full dataset* (6000 points).
*   **Rationale:** This design choice addresses the performance requirement (NFR1.3: Support up to 6000 points without lag) by allowing users to view a smaller, more manageable subset of points without compromising the accuracy or consistency of the K-Means computation. It also ensures that the K-Means results are always based on the complete data, providing a stable basis for analysis.

### 4. Voronoi-style Region Coloring

*   **Decision:** The K-Means visualization (FR7.1) uses Voronoi-style region coloring to represent cluster assignments.
*   **Rationale:** This method provides a clear and intuitive visual representation of the decision boundaries created by the K-Means algorithm. By coloring the background based on which cluster centroid is closest, it effectively illustrates the partitioning of the feature space.

### 5. Data Point Coloring

*   **Decision:** Data points are colored according to their *original group labels* (A, B, C) rather than their predicted K-Means cluster assignments.
*   **Rationale:** This allows for a direct visual comparison between the ground truth (original groups) and the K-Means clustering results (represented by the Voronoi regions). It helps in assessing the accuracy and effectiveness of the clustering algorithm, especially in identifying how well K-Means separates the predefined groups.
