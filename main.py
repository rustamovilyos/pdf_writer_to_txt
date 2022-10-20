from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from pathlib import Path
from PyPDF2 import PdfReader

window = Tk()
window.title("Добро пожаловать в приложение")
window.geometry('850x550')
tab_control = ttk.Notebook(window)

fileLoad = ttk.Frame(tab_control)
tab_control.add(fileLoad, text='Загрузить файл')
tab_control.pack(fill='both')

scan_dir = ttk.Frame(tab_control)
tab_control.add(scan_dir, text='Сканер папку')
tab_control.pack(fill='both')


def scan_files():
    file_path = Path.cwd()
    pdf_files = list(file_path.glob('**/*.pdf'))
    listBOX = Listbox(scan_dir, width=100, height=40)
    listBOX.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    for i in pdf_files:
        result_search = f'pdf file in this path: {i}'
        listBOX.insert(END, result_search)
        print(result_search)


scan_dir.rowconfigure(0, minsize=800, weight=1)
scan_dir.columnconfigure(1, minsize=800, weight=1)
s_button = ttk.Frame(scan_dir)
btn_scan = ttk.Button(s_button, text="Сканировать", command=scan_files)

btn_scan.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

s_button.grid(row=0, column=0, sticky="ns")

# def addingToTxt():
#     reader = PdfReader('testPdfText.pdf')
#     text = ''
#     li = []
#     listbox_adding = Listbox(scan_dir, width=100, height=40)
#     listbox_adding.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#     for a in reader.pages:
#         text += a.extract_text() + '\n'
#
#     li.append(text)
#     listbox_adding.insert(END, li)


fileLoad.rowconfigure(0, minsize=800, weight=1)
fileLoad.columnconfigure(1, minsize=800, weight=1)


def open_file():
    """Открывает файл для редактирования"""
    listbox_adding = Listbox(fileLoad, width=100, height=40)
    listbox_adding.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    pdf_files = askopenfilenames(
        filetypes=[("Text Files", "*.pdf"), ("All Files", "*.*")]
    )

    for filepath in pdf_files:
        reader = PdfReader(filepath)
        # list_t = text.split('\n')

        with open('text.txt', 'a') as f:
            text = ''
            for a in reader.pages:
                text += a.extract_text() + '\n'

            f.write('\n'.join(text.split('\n')))

        listbox_adding.insert(END, text.split('\n'))


fr_buttons = ttk.Frame(fileLoad)
btn_open = ttk.Button(fr_buttons, text="Загрузить файл", command=open_file)

btn_open.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

window.mainloop()
