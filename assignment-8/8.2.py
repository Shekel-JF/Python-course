import PyPDF2  # pip install PyPDF2
import tkinter as tk
from tkinter import filedialog

okno = tk.Tk()
okno.title("My PDF text extractor")
okno.geometry("800x600")

# dodać widget Text i umieściś z jakimś marginesem
text = tk.Text(okno, bg='white', fg='black', font=('Times New Roman', 12), wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

def clear_text():
   text.delete(1.0, tk.END)

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
   okno.destroy

# utworzyć widget Menu i jego strukturę jak na rysunku
mbar = tk.Menu(okno)
mfile = tk.Menu(mbar, tearoff=0)
# Open powinno wołać open_pdf
mfile.add_command(label="Open", command=open_pdf)
# Clear powinno wołać clear_text
mfile.add_command(label="Clear", command=clear_text)
# Quit powinno wołać quit_app
mfile.add_command(label="Quit", command=quit_app)

mbar.add_cascade(label="File", menu=mfile)
okno.config(menu=mbar)
okno.mainloop()