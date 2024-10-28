import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button


class InteractiveGraph:
    def __init__(self, on_point_added_event):
        self.x_min, self.x_max = 0.0, 10.0
        self.y_min, self.y_max = 0.0, 10.0
        self.points = np.empty((0, 2), dtype=float)
        self.plot_objects = []
        self.centroid_plot_objects = []
        self.fig, self.ax = plt.subplots()
        self.setup_plot()
        self.init_button()
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.point_added_event = on_point_added_event
        plt.show()

    def setup_plot(self) -> None:
        """Initializes the plot with specified x and y limits."""
        self.ax.set_xlim(self.x_min, self.x_max)
        self.ax.set_ylim(self.y_min, self.y_max)
        self.ax.set_title("Click to add points")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")

    def init_button(self) -> None:
        """Initializes the clear points button."""
        ax_button = plt.axes([0.8, 0.05, 0.1, 0.075])  # Position of the button
        button = Button(ax_button, 'Clear Points')
        button.on_clicked(self.clear_points)

    def point_added(self, x: float, y: float) -> None:
        """Callback function when a new point is added."""
        print(f"Point added at ({x}, {y})")
        print(self.points[0])
        print(self.points[0][0])
        print(self.points.shape)
        self.point_added_event(self, self.points, 10, self.ax, self.change_color)

    def on_click(self, event) -> None:
        """Event handler for mouse clicks to add points to the plot."""
        if event.inaxes != self.ax:
            return
        x, y = event.xdata, event.ydata
        self.points = np.append(self.points, [[x, y]], axis=0)
        plot_object = self.ax.plot(x, y, 'ko')
        self.plot_objects.append(plot_object[0])
        self.point_added(x, y)
        plt.draw()

    def clear_points(self, event) -> None:
        """Event handler to clear all points from the plot."""
        self.points = np.empty((0, 2), dtype=float)  # Reset points array
        self.plot_objects.clear()  # Clear all plot objects
        self.ax.cla()  # Clear the axis
        self.setup_plot()  # Re-setup the plot with the initial settings
        plt.draw()

    def change_color(self, color_list):
        for i in range(len(color_list)):
            self.plot_objects[i].set_color(color_list[i])
        plt.draw()

    def show_centroid(self, centroid1, centroid2):
        plot_obj1 = self.ax.plot(centroid1[0], centroid1[1], 'r+')
        plot_obj2 = self.ax.plot(centroid2[0], centroid2[1], 'b +')

        # remove the previous plot objects if they exist
        if self.centroid_plot_objects:
            for i in range(len(self.centroid_plot_objects)):
                self.centroid_plot_objects[i][0].remove()
        self.centroid_plot_objects.clear()
        self.centroid_plot_objects.append(plot_obj1)
        self.centroid_plot_objects.append(plot_obj2)
