import tkinter as tk
from tkinter import filedialog
from src.strabismus.kernel import kernel

class StrabismusApp:
    def __init__(self):
        self.filename = ''

    def use_last_callback(self):
        with open('.aeisconfig', 'r') as aeisconfig:
            self.filename = aeisconfig.read().strip('\n')
            kernel.analyze_direction(self.filename)

    def open_new_file_callback(self):
        self.filename = filedialog.askopenfilename()
        kernel.analyze_direction(self.filename)

    def run(self):
        root = tk.Tk()
        root.lift()
        root.attributes('-topmost', True)
        root.after_idle(root.attributes, '-topmost', False)

        frame = tk.Frame(root)
        frame.pack()

        use_last_button = tk.Button(frame,
                                    text='Use last',
                                    command=self.use_last_callback)
        use_last_button.pack(side=tk.LEFT)

        open_new_file_button = tk.Button(frame,
                                         text='Open new file',
                                         command=self.open_new_file_callback)
        open_new_file_button.pack(side=tk.LEFT)

        root.mainloop()

        if self.filename:
            with open('.aeisconfig', 'w') as aeisconfig:
                aeisconfig.write(self.filename)


if __name__ == '__main__':
    app = StrabismusApp()
    app.run()

