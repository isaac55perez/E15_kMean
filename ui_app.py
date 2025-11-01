import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np

from data_generator import generate_data
from kmeans_model import perform_kmeans, calculate_accuracy

class KMeansApp:
    def __init__(self):
        self.num_samples_per_group = 2000
        self.group_params = {
            'A': {'mean': [10, 10], 'std_dev': 2, 'color': 'red'},
            'B': {'mean': [20, 20], 'std_dev': 2, 'color': 'green'},
            'C': {'mean': [10, 20], 'std_dev': 2, 'color': 'blue'},
        }
        self.n_clusters = 3
        self.accuracy = 0.0

        self.fig, (self.ax_plot, self.ax_controls) = plt.subplots(1, 2, figsize=(15, 7), gridspec_kw={'width_ratios': [3, 1]})
        self.ax_plot.set_title("K-Means Visualization")
        self.ax_controls.set_title("Controls")
        self.ax_controls.set_facecolor('lightgray')
        self.ax_controls.set_xticks([])
        self.ax_controls.set_yticks([])

        self.data, self.labels, _ = generate_data(self.num_samples_per_group, self.group_params)
        self.kmeans_model, self.predicted_labels = perform_kmeans(self.data, self.n_clusters)

        # Data for plotting (can be a subset)
        self.display_data = self.data
        self.display_predicted_labels = self.predicted_labels
        self.display_labels = self.labels

        self.setup_controls()
        self.update_plot()
        self.compute_kmeans(None) # Calculate and display initial accuracy

    def setup_controls(self):
        # Sample Size Slider
        control_panel_bbox = self.ax_controls.get_position()
        ax_sample_size_pos = [
            control_panel_bbox.x0 + 0.02,  # x-start, slightly in from left of control panel
            control_panel_bbox.y1 - 0.1,  # y-start, near top of control panel
            control_panel_bbox.width - 0.04, # width, slightly less than control panel width
            0.03 # height
        ]
        ax_sample_size = self.fig.add_axes(ax_sample_size_pos)
        self.sample_size_slider = Slider(
            ax=ax_sample_size,
            label='Sample Size (%)',
            valmin=1,
            valmax=100,
            valinit=100,
            valstep=1,
            valfmt='%0.0f%%',
        )
        self.sample_size_slider.on_changed(self.update_sample_size)

        # Group Selector Radio Buttons
        ax_group_selector = self.fig.add_axes([control_panel_bbox.x0 + 0.02, control_panel_bbox.y1 - 0.25, control_panel_bbox.width - 0.04, 0.1])
        self.group_radio_buttons = RadioButtons(ax_group_selector, ('A', 'B', 'C'))
        self.group_radio_buttons.on_clicked(self.select_group)
        self.selected_group = 'A' # Default selected group

        # Regenerate Data Button
        ax_regenerate_button = self.fig.add_axes([control_panel_bbox.x0 + 0.02, control_panel_bbox.y1 - 0.35, control_panel_bbox.width - 0.04, 0.05])
        self.regenerate_button = Button(ax_regenerate_button, 'Regenerate Data')
        self.regenerate_button.on_clicked(self.regenerate_data)

        # Mean Adjustment Buttons
        mean_button_width = (control_panel_bbox.width - 0.04) / 3
        mean_button_height = 0.05
        mean_y_start = control_panel_bbox.y1 - 0.45

        ax_mean_up = self.fig.add_axes([control_panel_bbox.x0 + 0.02 + mean_button_width, mean_y_start + mean_button_height, mean_button_width, mean_button_height])
        self.mean_up_button = Button(ax_mean_up, '↑')
        self.mean_up_button.on_clicked(lambda event: self.adjust_mean(1, 'y'))

        ax_mean_down = self.fig.add_axes([control_panel_bbox.x0 + 0.02 + mean_button_width, mean_y_start - mean_button_height, mean_button_width, mean_button_height])
        self.mean_down_button = Button(ax_mean_down, '↓')
        self.mean_down_button.on_clicked(lambda event: self.adjust_mean(-1, 'y'))

        ax_mean_left = self.fig.add_axes([control_panel_bbox.x0 + 0.02, mean_y_start, mean_button_width, mean_button_height])
        self.mean_left_button = Button(ax_mean_left, '←')
        self.mean_left_button.on_clicked(lambda event: self.adjust_mean(-1, 'x'))

        ax_mean_right = self.fig.add_axes([control_panel_bbox.x0 + 0.02 + 2 * mean_button_width, mean_y_start, mean_button_width, mean_button_height])
        self.mean_right_button = Button(ax_mean_right, '→')
        self.mean_right_button.on_clicked(lambda event: self.adjust_mean(1, 'x'))

        # Standard Deviation Slider
        ax_std_dev = self.fig.add_axes([control_panel_bbox.x0 + 0.02, control_panel_bbox.y1 - 0.55, control_panel_bbox.width - 0.04, 0.03])
        self.std_dev_slider = Slider(
            ax=ax_std_dev,
            label='Std Dev',
            valmin=1,
            valmax=10,
            valinit=self.group_params[self.selected_group]['std_dev'],
            valstep=0.5,
            valfmt='%0.1f',
        )
        self.std_dev_slider.on_changed(self.update_std_dev)

        # K-Means K Value Slider
        ax_k_slider = self.fig.add_axes([control_panel_bbox.x0 + 0.02, control_panel_bbox.y1 - 0.65, control_panel_bbox.width - 0.04, 0.03])
        self.k_slider = Slider(
            ax=ax_k_slider,
            label='K Value',
            valmin=2,
            valmax=5,
            valinit=self.n_clusters,
            valstep=1,
            valfmt='%0.0f',
        )
        self.k_slider.on_changed(self.update_k_value)

        # Compute K-Means Button
        ax_compute_kmeans_button = self.fig.add_axes([control_panel_bbox.x0 + 0.02, control_panel_bbox.y1 - 0.75, control_panel_bbox.width - 0.04, 0.05])
        self.compute_kmeans_button = Button(ax_compute_kmeans_button, 'Compute K-Means')
        self.compute_kmeans_button.on_clicked(self.compute_kmeans)

        # Accuracy Display
        self.accuracy_text = self.fig.text(control_panel_bbox.x0 + 0.02, control_panel_bbox.y1 - 0.85, "")

    def update_k_value(self, val):
        self.n_clusters = int(val)

    def compute_kmeans(self, event):
        import time
        start_time = time.time()
        self.kmeans_model, self.predicted_labels = perform_kmeans(self.data, self.n_clusters)
        self.accuracy = calculate_accuracy(self.labels, self.predicted_labels)
        end_time = time.time()
        print(f"K-Means computation time: {end_time - start_time:.4f} seconds")
        self.accuracy_text.set_text(f"Success Rate: {self.accuracy:.2f}%")
        self.update_sample_size(self.sample_size_slider.val) # Update plot with current sample size


    def adjust_mean(self, change, axis):
        idx = 0 if axis == 'x' else 1
        self.group_params[self.selected_group]['mean'][idx] += change
        self.regenerate_data(None) # Pass None as event, as it's not from a button click

    def update_std_dev(self, val):
        self.group_params[self.selected_group]['std_dev'] = val
        self.regenerate_data(None) # Pass None as event


    def select_group(self, label):
        self.selected_group = label
        print(f"Selected group: {self.selected_group}") # For debugging

    def regenerate_data(self, event):
        self.data, self.labels, _ = generate_data(self.num_samples_per_group, self.group_params)
        self.kmeans_model, self.predicted_labels = perform_kmeans(self.data, self.n_clusters)
        self.update_sample_size(self.sample_size_slider.val) # Update plot with current sample size


    def update_sample_size(self, val):
        percentage = val / 100.0
        num_display_samples = int(self.data.shape[0] * percentage)

        # Ensure consistent random sampling for reproducibility
        np.random.seed(42) # Use a fixed seed for consistent sampling
        indices = np.random.choice(self.data.shape[0], num_display_samples, replace=False)
        
        self.display_data = self.data[indices]
        self.display_predicted_labels = self.predicted_labels[indices]
        self.display_labels = self.labels[indices]
        self.update_plot()

    def update_plot(self):
        self.ax_plot.clear()

        # Get plot limits
        x_min, x_max = self.data[:, 0].min() - 1, self.data[:, 0].max() + 1
        y_min, y_max = self.data[:, 1].min() - 1, self.data[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                             np.arange(y_min, y_max, 0.1))

        # Predict cluster for each point in the meshgrid
        Z = self.kmeans_model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        # Plot Voronoi regions with pastel colors
        self.ax_plot.contourf(xx, yy, Z, cmap='Pastel1', alpha=0.6)

        # Define colormap based on original group colors
        unique_labels = np.unique(self.labels)
        colors = [self.group_params[list(self.group_params.keys())[i % len(self.group_params)]]['color'] for i in unique_labels]
        cmap = plt.cm.colors.ListedColormap(colors)

        # Plot data points with original group colors
        scatter = self.ax_plot.scatter(self.display_data[:, 0], self.display_data[:, 1],
                                     c=self.display_labels,
                                     cmap=cmap, alpha=0.7, s=30, edgecolors='k')

        # Plot cluster centers
        self.ax_plot.scatter(self.kmeans_model.cluster_centers_[:, 0], self.kmeans_model.cluster_centers_[:, 1],
                             marker='X', s=200, color='red', label='Centroids')

        self.ax_plot.set_title("K-Means Visualization")
        self.ax_plot.set_xlabel("Feature 1")
        self.ax_plot.set_ylabel("Feature 2")
        self.ax_plot.legend()
        self.fig.canvas.draw_idle()

    def run(self):
        plt.show()

if __name__ == '__main__':
    app = KMeansApp()
    app.run()
