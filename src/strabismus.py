import tkinter as tk
from tkinter import filedialog
import numpy as np
from numpy import genfromtxt
import math


class StrabismusApp:
    def __init__(self):
        self.filename = ''

    def analyze_direction(self, log_location):
        DIRECTION = [1, 2, 3]
        DIRECTION_WITH_TIME = [0, 4, 5, 6]

        direction_logs = genfromtxt(log_location, delimiter=',')
        directions_with_time = direction_logs[:, DIRECTION_WITH_TIME]

        mean_direction = np.mean(directions_with_time[:, DIRECTION], axis=0)

        mean_angle = 0
        std_angle = 0

        for (time, x, y, z) in directions_with_time:
            direction = np.array([x, y, z])
            print(time, direction)

            angle = math.atan2(
                np.linalg.norm(np.cross(direction, mean_direction)),
                np.dot(direction, mean_direction))

            mean_angle += angle
            std_angle += angle ** 2

        mean_angle /= len(directions_with_time)
        std_angle = (std_angle / len(directions_with_time) - mean_angle ** 2) ** 0.5

        print(mean_angle, std_angle)

    def use_last(self):
        with open('.aeisconfig', 'r') as aeisconfig:
            self.filename = aeisconfig.read().strip('\n')
            self.analyze_direction(self.filename)

    def open_new_file(self):
        self.filename = filedialog.askopenfilename()
        self.analyze_direction(self.filename)

    def run(self):
        root = tk.Tk()
        root.lift()
        root.attributes('-topmost', True)
        root.after_idle(root.attributes, '-topmost', False)

        frame = tk.Frame(root)
        frame.pack()

        use_last_button = tk.Button(frame,
                                    text='Use last',
                                    command=self.use_last)
        use_last_button.pack(side=tk.LEFT)

        open_new_file_button = tk.Button(frame,
                                         text='Open new file',
                                         command=self.open_new_file)
        open_new_file_button.pack(side=tk.LEFT)

        root.mainloop()

        if self.filename:
            with open('.aeisconfig', 'w') as aeisconfig:
                aeisconfig.write(self.filename)


if __name__ == '__main__':
    app = StrabismusApp()
    app.run()

