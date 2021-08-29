
import tkinter.font as font
import RabinKarp as rk
import tkinter as tk
from PIL import Image, ImageTk

pri_clr = 'white'
scnd_clr = 'light blue'
myrk = rk.RabinKarp()


def search_func():

    myrk.ifempty(txt_pat.get("1.0", "end"),
                 txt_para.get("1.0", "end"))
    if (myrk.prompt):
        myrk.check(txt_pat.get("1.0", "end").lower(),
                   txt_para.get("1.0", "end").lower())
        if (myrk.prompt2):
            myrk.search(txt_pat.get("1.0", "end").lower(),
                        txt_para.get("1.0", "end").lower(), 100007, txt_indexes, lbl_times)
            myrk.highlight_pattern(
                txt_para, txt_pat.get("1.0", "end").strip().lower())
            myrk.comma_remover(txt_indexes)


root = tk.Tk()
root.title('Rabin-Karp')
w = 700
h = 600
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(background=pri_clr)

myFont_btn = font.Font(family='Helvetica', size="10", weight="bold")
myFont_lbl = font.Font(family='Helvetica', size="40", weight="bold")


lbl_search = tk.Label(root, text='Search A Word', font=myFont_lbl,
                      background=pri_clr, pady='10')
lbl_search.pack()

canvas_1 = tk.Canvas(root, height='500', width='700',
                     bg=pri_clr, highlightthickness='0')
canvas_1.pack()

img_1 = ImageTk.PhotoImage(Image.open(
    "search.png").resize((40, 40), Image.ANTIALIAS))
panel_1 = tk.Label(canvas_1, image=img_1)
panel_1.grid(row='2', column='1', pady='15', padx='5')

txt_pat = tk.Text(canvas_1, height=3, width=40, bg=scnd_clr, highlightthickness=1,
                  highlightcolor="blue", highlightbackground="red")
txt_pat.grid(row='2', column='2', pady='15', padx='5')

img_2 = ImageTk.PhotoImage(Image.open(
    "location.png").resize((40, 40), Image.ANTIALIAS))
panel_2 = tk.Label(canvas_1, image=img_2)
panel_2.grid(row='1', column='1', pady='15', padx='5')

txt_indexes = tk.Text(canvas_1, height=3, width=40,
                      bg=scnd_clr, state='disabled')
txt_indexes.grid(row='1', column='2', pady='15', padx='5')

lbl_times = tk.Label(canvas_1, text='  ', font=myFont_btn,
                     background=pri_clr, )
lbl_times.grid(row='2', column='3', pady='15', padx='5')

canvas_2 = tk.Canvas(root, height='500', width='700',
                     bg=pri_clr, highlightthickness='0')
canvas_2.pack(expand=True)

img_3 = ImageTk.PhotoImage(Image.open(
    "write (2).png").resize((40, 40), Image.ANTIALIAS))
panel_3 = tk.Label(canvas_2, image=img_3)
panel_3.grid(row='1', column='1', pady='15', padx='5')


txt_para = tk.Text(canvas_2, height=15, width=60, bg=scnd_clr, highlightthickness=1,
                   highlightcolor="blue", highlightbackground="red")
txt_para.grid(row='1', column='2', pady='15', padx='5')

lbl_none = tk.Label(canvas_2, text='   ', background=pri_clr,)
lbl_none.grid(row='1', column='3', pady='15', padx='5')

canvas_3 = tk.Canvas(root, height='200', width='500',
                   bg=pri_clr, highlightthickness='0')
canvas_3.pack()

btn_Search = tk.Button(canvas_3, text='Search', font=myFont_btn,
                       width='10', height='2', bg=scnd_clr, command=search_func)
btn_Search.grid(row='1', column='1', pady='10', padx='50')

btn_Clear = tk.Button(canvas_3, text='Clear', font=myFont_btn,
                      width='10', height='2', bg=scnd_clr,
                      command=lambda: myrk.clear(txt_pat, txt_indexes, txt_para, lbl_times))
btn_Clear.grid(row='1', column='2', pady='10', padx='50')

root.mainloop()
