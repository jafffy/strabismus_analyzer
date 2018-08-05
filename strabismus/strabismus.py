import tkinter as tk
from tkinter import filedialog
from strabismus.kernel import kernel
import os


class StrabismusApp:
    def __init__(self):
        self.data_repo_path = ''

        self.root = tk.Tk()
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)

        frame = tk.Frame(self.root)
        frame.pack()

        self.data_repo_entry = tk.Entry(frame)
        self.data_repo_entry.pack(side=tk.LEFT)

        tk.Button(frame,
                  text='Use last',
                  command=self.use_last_callback)\
            .pack(side=tk.LEFT)

        tk.Button(frame,
                  text='Open new data repos',
                  command=self.open_new_data_repo_callback)\
            .pack(side=tk.LEFT)

        self.pid_entry = tk.Entry(frame)
        self.pid_entry.pack(side=tk.LEFT)

        tk.Button(frame,
                  text='Find PID',
                  command=self.find_pid) \
            .pack(side=tk.LEFT)

    def use_last_callback(self):
        with open('.aeis_config', 'r') as aeis_config:
            self.data_repo_path = aeis_config.read().strip('\n')
            self.data_repo_entry.insert(0, self.data_repo_path)

    def open_new_data_repo_callback(self):
        self.data_repo_path = filedialog.askdirectory()
        self.data_repo_entry.insert(0, self.data_repo_path)

    def find_pid(self):
        ans = os.path.join(self.data_repo_path, self.pid_entry.get())
        kernel.analyze_direction(os.path.join(ans, '간헐적외사시_left.csv'))
        kernel.analyze_direction(os.path.join(ans, '간헐적외사시_right.csv'))

    def run(self):
        self.root.mainloop()

        if self.data_repo_path:
            with open('.aeis_config', 'w') as aeis_config:
                aeis_config.write(self.data_repo_path)


if __name__ == '__main__':
    app = StrabismusApp()
    app.run()

