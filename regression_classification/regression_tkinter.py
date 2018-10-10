from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from regression_classification import regression_CART


def re_draw(tols, toln):
    re_draw.f.clf() # clear figure
    re_draw.a = re_draw.f.add_subplot(111)
    if chk_btn_var.get():
        if toln < 2 :
            toln = 2
        my_tree = regression_CART.create_tree(re_draw.raw_dat, regression_CART.model_leaf, regression_CART.model_err, (tols, toln))
        y_hat = regression_CART.creat_fore_cast(my_tree, re_draw.test_dat, regression_CART.model_tree_eval)
    else:
        my_tree = regression_CART.create_tree(re_draw.raw_dat, ops=(tols, toln))
        y_hat = regression_CART.creat_fore_cast(my_tree, re_draw.test_dat)
    re_draw.a.scatter(re_draw.raw_dat[:, 0].tolist(), re_draw.raw_dat[:, 1].tolist(), s=5)
    re_draw.a.plot(re_draw.test_dat, y_hat, linewidth=2.0)
    re_draw.canvas.show()


def get_inputs():
    try:
        toln = int(toln_entry.get())
    except:
        toln = 10
        print('enter integer for toln')
        toln_entry.delete(0, END)
        toln_entry.insert(0, '10')
    try:
        tols = float(tols_entry.get())
    except:
        tols = 1.0
        print('enter float for tols')
        tols_entry.delete(0, END)
        tols_entry.insert(0, '1.0')

    return toln, tols


def draw_new_tree():
    toln, tols = get_inputs()
    re_draw(tols, toln)

root = Tk()
re_draw.f = Figure(figsize=(5, 4), dpi=100)
re_draw.canvas = FigureCanvasTkAgg(re_draw.f, master=root)
re_draw.canvas.show()
re_draw.canvas.get_tk_widget().grid(row=0, columnspan=3)

Label(root, text='toln').grid(row=1, column=0)
# widget input
toln_entry = Entry(root)
toln_entry.grid(row=1, column=1)
toln_entry.insert(0, '10')

Label(root, text='tols').grid(row=2, column=0)
tols_entry = Entry(root)
tols_entry.grid(row=2, column=1)
tols_entry.insert(0, '1.0')

# widget button
Button(root, text='ReDraw', command=draw_new_tree).grid(row=1, column=2, rowspan=3)

# widget checkbutton
chk_btn_var = IntVar()
chk_btn = Checkbutton(root, text='Model tree', variable=chk_btn_var)
chk_btn.grid(row=3, column=0, columnspan=2)

re_draw.raw_dat = np.matrix(regression_CART.load_data('sine.txt'))
re_draw.test_dat = np.arange(min(re_draw.raw_dat[:, 0]), max(re_draw.raw_dat[:, 0]), 0.01)
re_draw(1.0, 10)

root.mainloop()

