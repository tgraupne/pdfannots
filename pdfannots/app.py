import os
import tkinter
from tkinter import Tk, Scrollbar, Text, RIGHT, Button, filedialog, messagebox, END, Frame, Label
from tkinter.ttk import Style


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("PDF Notes Exporter")
        self.style = Style(self.root)
        self.style.theme_use('aqua')

        self.main_frame = Frame(self.root)
        self.main_frame.grid(row=0, column=0)

        # Init Button Frame
        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid(row=0, column=0, rowspan=1, columnspan=3)

        self.open_file_button = Button(self.button_frame, text='Open PDF File', command=self.event_open_file)
        self.open_file_button.grid(row=0, column=0, rowspan=1, columnspan=1)

        self.open_preview_button = Button(self.button_frame, text='Open Preview', command=self.event_open_preview)
        self.open_preview_button.grid(row=0, column=1, rowspan=1, columnspan=1)

        self.export_annotations_button = Button(self.button_frame, text='Export', command=self.event_export)
        self.export_annotations_button.grid(row=0, column=2, rowspan=1, columnspan=1)

        # Init Frame for PDF File Name
        self.file_name_frame = Frame(self.main_frame)
        self.file_name_frame.grid(row=1, column=0, rowspan=1, columnspan=3)

        self.file_name_label = Label(self.file_name_frame, text='...', borderwidth=1, relief="ridge")

        # Init Frame for Annotation Preview
        self.annotation_preview_frame = Frame(self.main_frame)
        self.annotation_preview_frame.grid(row=3, column=0)
        self.annotation_preview_scrollbar = Scrollbar(self.annotation_preview_frame, orient='vertical')
        self.annotation_preview = Text(self.annotation_preview_frame, yscrollcommand=self.annotation_preview_scrollbar.set)


    def event_open_file(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("PDF files",
                                                          "*.pdf"),
                                                         ("all files",
                                                          "*.*")))

        # Change label contents
        self.file_name_label.configure(text=filename)
        self.file_name_label.pack()

    def event_open_preview(self):
        annotations = self.get_annotations()



    def show_annotation_preview_frame(self):
        # self.annotation_preview_frame.pack()
        # self.annotation_preview_scrollbar.config(command=self.annotation_preview.yview)
        self.annotation_preview_scrollbar.pack()
        self.annotation_preview.pack()

    def show(self):
        self.root.mainloop()

    def event_export(self):
        folder_selected = filedialog.askdirectory()
        if len(folder_selected) > 0:
            output_file = folder_selected + '/export.md'
            if len(self.textArea.get("1.0", "end-1c")) > 0:
                with open(output_file, 'w') as f:
                    f.write(self.textArea.get("1.0", "end-1c"))
                messagebox.showinfo("pdfannots", "Sucess")
            else:
                messagebox.showwarning("pdfannots", "Without Output. Please, upload a pdf file")
        # else:
        #     messagebox.showwarning("pdfannots", "Choose a folder")


if __name__ == '__main__':
    app = App()
    app.show()
