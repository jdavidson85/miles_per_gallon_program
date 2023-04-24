import tkinter


class MPG_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.gallons_label = tkinter.Label(self.gallons_frame,
                                           text=' Enter the number of gallons of gas the car holds: ')
        self.gallons_entry = tkinter.Entry(self.gallons_frame, width=10)
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        self.miles_label = tkinter.Label(self.miles_frame,
                                         text='Enter the number of miles it can be driven on a full tank: ')
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.result_label = tkinter.Label(self.mpg_frame,
                                          text='Number of miles that the car may be driven per gallon of gas : ')
        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mpg_frame, textvariable=self.mpg)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')

        self.calc_button = tkinter.Button(self.button_frame, text='Calculate MPG', command=self.calc_mpg)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.button_frame.pack()
        self.mpg_frame.pack()
        self.main_window.geometry("500x200")
        self.main_window.mainloop()

    def calc_mpg(self):
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())

        self.miles_per_gallon = self.miles / self.gallons
        self.mpg.set(str(round(self.miles_per_gallon, 2)))


carmpg = MPG_GUI()
