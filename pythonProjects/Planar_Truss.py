import os

import numpy as np
import pandas as pd

from Truss_classes import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from calc_functions import *


def Truss_2D():
    root = Tk()
    root.title('Planar Truss analysis by Neil T. Rigaud')
    root.geometry('960x520')
    root['bg'] = '#fb0'
    root.resizable(False, False)
    try:
        root.iconbitmap("Valknut.ico")
    except:
        pass

    fig = plt.Figure(figsize=(6, 5), dpi=100)
    ax = fig.add_subplot(111)
    chart_type = FigureCanvasTkAgg(fig, root)
    chart_type.get_tk_widget().grid(row=1, column=1, rowspan=6)
    fig.patch.set_facecolor('gray')
    ax.set_title('2D Truss representation', c='blue')

    def open_n_data():
        if os.path.exists('Node_list.csv'):
            pass
        else:
            n_d = pd.DataFrame([], columns=['Node number', 'Position X', 'Position Y', 'Reaction X', 'Reaction Y'])
            n_d.to_csv('Node_list.csv')
            del n_d

        n_data = Toplevel()
        n_data.title('Node entry')
        n_data.geometry('480x520')
        n_data['bg'] = '#fb0'
        try:
            n_data.iconbitmap("Valknut.ico")
        except:
            pass
        n_data.resizable(False, False)

        l_data = pd.read_csv('Node_list.csv')

        l_node_num = list(l_data['Node number'])
        l_x_pos = list(l_data['Position X'])
        l_y_pos = list(l_data['Position Y'])
        l_x_reaction = list(l_data['Reaction X'])
        l_y_reaction = list(l_data['Reaction Y'])

        def btn_cancel():
            e_1.delete(0, END)
            e_2.delete(0, END)
            e_3.delete(0, END)
            c_1.deselect()
            c_2.deselect()

        def button_save_node():
            node = TrussNode(int(e_1.get()), float(e_2.get()), float(e_3.get()), bool(v_1.get()), bool(v_2.get()))

            l_node_num.append(node.node_num)
            l_x_pos.append(node.x_pos)
            l_y_pos.append(node.y_pos)
            l_x_reaction.append(node.x_reaction)
            l_y_reaction.append(node.y_reaction)

            e_1.delete(0, END)
            e_2.delete(0, END)
            e_3.delete(0, END)
            c_1.deselect()
            c_2.deselect()

            node_dict = {'Node number': l_node_num, 'Position X': l_x_pos, 'Position Y': l_y_pos,
                         'Reaction X': l_x_reaction, 'Reaction Y': l_y_reaction}
            b_df = pd.DataFrame(node_dict).sort_values(['Node number'])
            os.remove('Node_list.csv')
            b_df.to_csv('Node_list.csv')

            update_n_list()
            n_data.destroy()
            open_n_data()

        frame_1 = LabelFrame(n_data, text='Data entry', padx=15, pady=20, font=("Helvetica", 10), bg='#fb0')
        frame_2 = LabelFrame(n_data, text='Database', padx=15, pady=20, font=("Helvetica", 10), bg='#fb0')

        # Database view definition
        # ________________________________________________________________
        def update_n_list():
            node_data = pd.read_csv('Node_list.csv')

            n_n = list(node_data['Node number'])
            x_pos = list(node_data['Position X'])
            y_pos = list(node_data['Position Y'])
            x_reaction = list(node_data['Reaction X'])
            y_reaction = list(node_data['Reaction Y'])

            my_tree = ttk.Treeview(frame_2, show='headings', height=10)

            my_tree['columns'] = ('Node number', 'Position X', 'Position Y', 'Reaction X', 'Reaction Y')

            my_tree.column("Node number", anchor=W, width=60)
            my_tree.column("Position X", anchor=W, width=80)
            my_tree.column("Position Y", anchor=W, width=80)
            my_tree.column("Reaction X", anchor=W, width=80)
            my_tree.column("Reaction Y", anchor=W, width=80)

            my_tree.heading("Node number", text='Node #', anchor=W)
            my_tree.heading('Position X', text='Position X (m)', anchor=W)
            my_tree.heading('Position Y', text='Position Y (m)', anchor=W)
            my_tree.heading('Reaction X', text='Reaction X', anchor=W)
            my_tree.heading('Reaction Y', text='Reaction Y', anchor=W)

            for i in range(len(n_n)):
                my_tree.insert(parent="",
                               index='end',
                               iid=str(i),
                               text=str(i),
                               values=(n_n[i], x_pos[i], y_pos[i], x_reaction[i], y_reaction[i]))

            my_tree.pack(padx=5)

        # ________________________________________________________________
        # End of Database definition
        update_n_list()

        label_1 = Label(frame_1, text='Node number :', font=("Helvetica", 10), bg='#fb0')
        label_2 = Label(frame_1, text='Position X :', font=("Helvetica", 10), bg='#fb0')
        label_3 = Label(frame_1, text='Position Y :', font=("Helvetica", 10), bg='#fb0')

        e_1 = Entry(frame_1, width=25, borderwidth=5, bg='light blue')
        e_2 = Entry(frame_1, width=25, borderwidth=5, bg='light blue')
        e_3 = Entry(frame_1, width=25, borderwidth=5, bg='light blue')

        v_1 = IntVar()
        v_2 = IntVar()

        c_1 = Checkbutton(frame_1, text='Reaction on the X axis', font=("Helvetica", 10), bg='#fb0', variable=v_1)
        c_2 = Checkbutton(frame_1, text='Reaction on the Y axis', font=("Helvetica", 10), bg='#fb0', variable=v_2)

        button_save = Button(frame_1, text='Submit', padx=10, pady=10, bg='green', fg='white',
                             font=("Helvetica", 10), command=button_save_node)
        button_cancel = Button(frame_1, text='Clear entry', padx=10, pady=10, bg='light yellow',
                               font=("Helvetica", 10), command=btn_cancel)
        button_delete = Button(frame_1, text='Delete', padx=10, pady=10, bg='red', fg='white',
                               font=("Helvetica", 10), command=btn_cancel)

        frame_1.grid(row=0, column=0, padx=10, ipadx=10)
        frame_2.grid(row=1, column=0, padx=10, ipadx=10)

        label_1.grid(row=1, column=0)
        label_2.grid(row=2, column=0)
        label_3.grid(row=3, column=0)

        e_1.grid(row=1, column=1, columnspan=2)
        e_2.grid(row=2, column=1, columnspan=2)
        e_3.grid(row=3, column=1, columnspan=2)

        c_1.grid(row=4, column=0, columnspan=2)
        c_2.grid(row=4, column=2)

        button_save.grid(row=5, column=0, ipadx=10)
        button_cancel.grid(row=5, column=1, ipadx=10)
        button_delete.grid(row=5, column=2, ipadx=15)

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

    def open_m_data():
        # Verify the existence of an un-empty list node
        if os.path.exists('Node_list.csv'):
            df = pd.read_csv('Node_list.csv')
            if len(df) > 2:
                if os.path.exists('Rect_Beam_list.csv'):
                    pass
                else:
                    b_d = pd.DataFrame([], columns=['Material', 'Young modulus', 'Base', 'Height', 'Starting node',
                                                    'Ending node', 'Length', 'Area', 'Inertia'])
                    b_d.to_csv('Rect_Beam_list.csv')
                    del b_d

                m_data = Toplevel()
                m_data.title('Member data entry')
                m_data.geometry("670x600")
                m_data['bg'] = '#fb0'
                try:
                    m_data.iconbitmap("Valknut.ico")
                except:
                    pass
                m_data.resizable(False, False)

                l_data = pd.read_csv('Rect_Beam_list.csv')

                l_material = list(l_data['Material'])
                l_young_mod = list(l_data['Young modulus'])
                l_length = list(l_data['Length'])
                l_base = list(l_data['Base'])
                l_height = list(l_data['Height'])
                l_st_node = list(l_data['Starting node'])
                l_end_node = list(l_data['Ending node'])
                l_area = list(l_data['Area'])
                l_inertia = list(l_data['Inertia'])

                def btn_cancel():
                    e_1.delete(0, END)
                    e_2.delete(0, END)
                    e_3.delete(0, END)
                    e_4.delete(0, END)
                    e_5.delete(0, END)
                    e_6.delete(0, END)

                def button_save_member():
                    beam = RectBeam(e_1.get(), float(e_2.get()), float(e_3.get()), float(e_4.get()),
                                    int(e_5.get()), int(e_6.get()))

                    l_material.append(beam.material)
                    l_young_mod.append(beam.young_modulus)
                    l_length.append(beam.calc_length())
                    l_base.append(beam.base)
                    l_height.append(beam.height)
                    l_st_node.append(beam.st_node)
                    l_end_node.append(beam.end_node)
                    l_area.append(beam.calc_area())
                    l_inertia.append(beam.calc_inertia())

                    e_1.delete(0, END)
                    e_2.delete(0, END)
                    e_3.delete(0, END)
                    e_4.delete(0, END)
                    e_5.delete(0, END)
                    e_6.delete(0, END)

                    beam_dict = {'Material': l_material, 'Young modulus': l_young_mod, 'Base': l_base,
                                 'Height': l_height,
                                 'Starting node': l_st_node, 'Ending node': l_end_node, 'Length': l_length,
                                 'Area': l_area, 'Inertia': l_inertia}

                    b_df = pd.DataFrame(beam_dict)
                    os.remove('Rect_Beam_list.csv')
                    b_df.to_csv('Rect_Beam_list.csv')

                    update_m_list()
                    m_data.destroy()
                    show_truss()
                    open_m_data()

                frame_1 = LabelFrame(m_data, text='Data entry', padx=15, pady=20, bg='#fb0')
                frame_2 = LabelFrame(m_data, text='Database', padx=10, pady=20, bg='#fb0')

                # Database view definition
                # _____________________________________________________________________________________________________
                def update_m_list():
                    beam_data = pd.read_csv('Rect_Beam_list.csv')

                    m = list(beam_data['Material'])
                    ym = list(beam_data['Young modulus'])
                    b = list(beam_data['Base'])
                    h = list(beam_data['Height'])
                    st_n = list(beam_data['Starting node'])
                    end_n = list(beam_data['Ending node'])
                    l_l = list(beam_data['Length'])
                    ar = list(beam_data['Area'])
                    inert = list(beam_data['Inertia'])

                    my_tree = ttk.Treeview(frame_2, show='headings', height=10)

                    my_tree['columns'] = ('No bar', 'Material', 'Young modulus', 'Base', 'Height', 'Starting node',
                                          'Ending node', 'Length', 'Area', 'Inertia')

                    my_tree.column("No bar", anchor=W, width=50)
                    my_tree.column("Material", anchor=W, width=60)
                    my_tree.column("Young modulus", anchor=W, width=75)
                    my_tree.column("Base", anchor=W, width=60)
                    my_tree.column("Height", anchor=W, width=65)
                    my_tree.column("Starting node", anchor=W, width=60)
                    my_tree.column("Ending node", anchor=W, width=65)
                    my_tree.column("Length", anchor=W, width=70)
                    my_tree.column("Area", anchor=W, width=60)
                    my_tree.column("Inertia", anchor=W, width=60)

                    my_tree.heading("No bar", text='No bar', anchor=W)
                    my_tree.heading('Material', text='Material', anchor=W)
                    my_tree.heading('Young modulus', text='Y. mod (MPa)', anchor=W)
                    my_tree.heading('Base', text='Base(mm)', anchor=W)
                    my_tree.heading('Height', text='Height(mm)', anchor=W)
                    my_tree.heading('Starting node', text='St. node', anchor=W)
                    my_tree.heading('Ending node', text='End. node', anchor=W)
                    my_tree.heading('Length', text='Length(m)', anchor=W)
                    my_tree.heading('Area', text='Area', anchor=W)
                    my_tree.heading('Inertia', text='Inertia', anchor=W)

                    for i in range(len(l_l)):
                        my_tree.insert(parent="",
                                       index='end',
                                       iid=str(i),
                                       text=str(i),
                                       values=(i + 1, m[i], ym[i], b[i], h[i], st_n[i], end_n[i], l_l[i], ar[i], inert[i]))

                    my_tree.pack(padx=5)

                # _____________________________________________________________________________________________________
                # End of database definition

                update_m_list()

                label_1 = Label(frame_1, text='Material:', bg='#fb0', font=('Cambria math bold', 12))
                label_2 = Label(frame_1, text='Young modulus (MPa) :', bg='#fb0', font=('Cambria math bold', 12))
                label_3 = Label(frame_1, text='Base (mm) :', bg='#fb0', font=('Cambria math bold', 12))
                label_4 = Label(frame_1, text='Height (mm) :', bg='#fb0', font=('Cambria math bold', 12))
                label_5 = Label(frame_1, text='Starting node:', bg='#fb0', font=('Cambria math bold', 12))
                label_6 = Label(frame_1, text='Ending node :', bg='#fb0', font=('Cambria math bold', 12))

                e_1 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
                e_2 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
                e_3 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
                e_4 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
                e_5 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')
                e_6 = Entry(frame_1, width=50, borderwidth=5, bg='light blue')

                button_save = Button(frame_1, text='SUBMIT', padx=25, pady=10, bg='green', fg='white',
                                     font=('Cambria math bold', 12), command=button_save_member)
                button_cancel = Button(frame_1, text='CLEAR INPUT', padx=5, pady=10, bg='red', fg='white',
                                       font=('Cambria math bold', 12), command=btn_cancel)

                frame_1.grid(row=0, column=0, padx=10)
                frame_2.grid(row=1, column=0, padx=5)

                label_1.grid(row=1, column=0)
                label_2.grid(row=2, column=0)
                label_3.grid(row=3, column=0)
                label_4.grid(row=4, column=0)
                label_5.grid(row=5, column=0)
                label_6.grid(row=6, column=0)

                e_1.grid(row=1, column=1)
                e_2.grid(row=2, column=1)
                e_3.grid(row=3, column=1)
                e_4.grid(row=4, column=1)
                e_5.grid(row=5, column=1)
                e_6.grid(row=6, column=1)

                button_save.grid(row=9, column=0)
                button_cancel.grid(row=9, column=1)
            else:
                messagebox.showwarning("ERROR", "You need to first enter at least 3 valid nodes.")
                open_n_data()
        else:
            messagebox.showwarning("ERROR", "You need to first enter at least 3 valid nodes.")
            open_n_data()

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

    def open_l_data():
        # Verify the existence of an un-empty list of members
        if os.path.exists('Rect_Beam_list.csv'):
            df = pd.read_csv('Rect_Beam_list.csv')
            if len(df) >= 2:
                if os.path.exists('Load_list.csv'):
                    pass
                else:
                    l_d = pd.DataFrame([], columns=['Node applied', 'Load on X', 'Load on Y'])
                    l_d.to_csv('Load_list.csv')
                    del l_d

                load_data = Toplevel()
                load_data.title('Load entry')
                load_data.geometry("460x525")
                load_data['bg'] = "#fb0"

                try:
                    load_data.iconbitmap("Valknut.ico")
                except:
                    pass
                
                l_data = pd.read_csv('Load_list.csv')

                l_node_app = list(l_data['Node applied'])
                l_x_load = list(l_data['Load on X'])
                l_y_load = list(l_data['Load on Y'])

                def btn_cancel():
                    e_1.delete(0, END)
                    e_2.delete(0, END)
                    e_3.delete(0, END)

                def button_save_load():
                    load = TrussLoad(int(e_1.get()), float(e_2.get()), float(e_3.get()))

                    l_node_app.append(load.node_app)
                    l_x_load.append(load.x_load)
                    l_y_load.append(load.y_load)

                    e_1.delete(0, END)
                    e_2.delete(0, END)
                    e_3.delete(0, END)

                    load_dict = {'Node applied': l_node_app, 'Load on X': l_x_load, 'Load on Y': l_y_load}
                    b_df = pd.DataFrame(load_dict)
                    os.remove('Load_list.csv')
                    b_df.to_csv('Load_list.csv')
                    update_l_list()
                    load_data.destroy()
                    open_l_data()

                frame_1 = LabelFrame(load_data, text='Data entry', padx=10, pady=20, bg='#fb0')
                frame_2 = LabelFrame(load_data, text='Database', padx=10, pady=20, bg='#fb0')

                # Database view definition
                # ________________________________________________________________
                def update_l_list():
                    load_database = pd.read_csv('Load_list.csv')

                    node_app = list(load_database['Node applied'])
                    x_load = list(load_database['Load on X'])
                    y_load = list(load_database['Load on Y'])

                    my_tree = ttk.Treeview(frame_2, show='headings', height=10)

                    my_tree['columns'] = ('Load number', 'Node applied', 'Load on X', 'Load on Y')

                    my_tree.column("Load number", anchor=W, width=60)
                    my_tree.column("Node applied", anchor=W, width=120)
                    my_tree.column("Load on X", anchor=W, width=110)
                    my_tree.column("Load on Y", anchor=W, width=110)

                    my_tree.heading("Load number", text='Load #', anchor=W)
                    my_tree.heading('Node applied', text='Applied node', anchor=W)
                    my_tree.heading('Load on X', text='Load on X', anchor=W)
                    my_tree.heading('Load on Y', text='Load on Y', anchor=W)

                    for i in range(len(node_app)):
                        my_tree.insert(parent="",
                                       index='end',
                                       iid=str(i),
                                       text=str(i),
                                       values=(i + 1, node_app[i], x_load[i], y_load[i]))

                    my_tree.pack(padx=5)

                # ________________________________________________________________
                # End of Database definition

                update_l_list()

                label_1 = Label(frame_1, text='Node applied:', bg='#fb0')
                label_2 = Label(frame_1, text='Load on X axis (kip):', bg='#fb0')
                label_3 = Label(frame_1, text='Load on Y axis (kip):', bg='#fb0')

                e_1 = Entry(frame_1, width=30, borderwidth=5, bg='light blue')
                e_2 = Entry(frame_1, width=30, borderwidth=5, bg='light blue')
                e_3 = Entry(frame_1, width=30, borderwidth=5, bg='light blue')

                button_save = Button(frame_1, text='Submit data', padx=10, pady=10, bg='green',
                                     command=button_save_load)
                button_cancel = Button(frame_1, text='Cancel', padx=10, pady=10, bg='red', command=btn_cancel)

                frame_1.grid(row=0, column=0, padx=10, ipadx=5)
                frame_2.grid(row=1, column=0, padx=10, ipadx=5)

                label_1.grid(row=1, column=0)
                label_2.grid(row=2, column=0)
                label_3.grid(row=3, column=0)

                e_1.grid(row=1, column=1)
                e_2.grid(row=2, column=1)
                e_3.grid(row=3, column=1)

                button_save.grid(row=4, column=0, columnspan=2, ipadx=70)
                button_cancel.grid(row=5, column=0, columnspan=2, ipadx=83)

            else:
                messagebox.showwarning("WARNING", "You need to enter at least 2 valid members.")
                open_m_data()
        else:
            messagebox.showwarning("WARNING", "You need to enter at least 2 valid members.")
            open_m_data()

    def reset_database():
        response = messagebox.askyesnocancel('WARNING', 'Do you want to reset the database ?')
        if response:
            if os.path.exists('Rect_Beam_list.csv'):
                os.remove('Rect_Beam_list.csv')
            if os.path.exists('Node_list.csv'):
                os.remove('Node_list.csv')
            if os.path.exists('Load_list.csv'):
                os.remove('Load_list.csv')
            plt.clf()
        else:
            pass

    def show_truss():
        # Verify the existence of an un-empty list of members
        if os.path.exists('Rect_Beam_list.csv'):
            df = pd.read_csv('Rect_Beam_list.csv')
            if len(df) >= 2:
                nodes = pd.read_csv('Node_list.csv')
                nodes_xp = list(nodes['Position X'])
                nodes_yp = list(nodes['Position Y'])
                members = pd.read_csv('Rect_Beam_list.csv')
                m_stn = list(members['Starting node'])
                m_en = list(members['Ending node'])
                x1 = []
                x2 = []
                y1 = []
                y2 = []
                for i in range(len(members)):
                    s = m_stn[i]
                    e = m_en[i]

                    x1.append(nodes_xp[s - 1])
                    x2.append(nodes_xp[e - 1])
                    y1.append(nodes_yp[s - 1])
                    y2.append(nodes_yp[e - 1])

                f_plot = pd.DataFrame([x1, y1, x2, y2])
                f_plot = f_plot.T
                f_plot.columns = ['x1', 'y1', 'x2', 'y2']

                figure = plt.Figure(figsize=(6, 5), dpi=100)
                a = figure.add_subplot(111)
                chart_t = FigureCanvasTkAgg(figure, root)
                chart_t.get_tk_widget().grid(row=1, column=1, rowspan=6)
                a.plot((f_plot.x1, f_plot.x2), (f_plot.y1, f_plot.y2), c='blue')
                figure.patch.set_facecolor('gray')
                a.set_title('2D Truss representation', c='blue')
            else:
                messagebox.showwarning("WARNING", "You need to enter at least 2 valid members.")
                open_m_data()
        else:
            messagebox.showwarning("WARNING", "You need to enter at least 2 valid members.")
            open_m_data()

    def show_truss_ie():
        # Verify the existence of an un-empty list of members
        if os.path.exists('Internal_forces.csv'):
            forces = pd.read_csv('Internal_forces.csv')
            forces = forces['Internal force']

            if os.path.exists('Rect_Beam_list.csv'):
                df = pd.read_csv('Rect_Beam_list.csv')
                n_m = len(df)
                if n_m >= 2:
                    nodes = pd.read_csv('Node_list.csv')
                    nodes_xp = list(nodes['Position X'])
                    nodes_yp = list(nodes['Position Y'])
                    members = pd.read_csv('Rect_Beam_list.csv')
                    m_stn = list(members['Starting node'])
                    m_en = list(members['Ending node'])
                    x1 = []
                    x2 = []
                    y1 = []
                    y2 = []
                    for i in range(n_m):
                        s = m_stn[i]
                        e = m_en[i]

                        x1.append(nodes_xp[s - 1])
                        x2.append(nodes_xp[e - 1])
                        y1.append(nodes_yp[s - 1])
                        y2.append(nodes_yp[e - 1])

                    f_plot = pd.DataFrame([x1, y1, x2, y2])
                    f_plot = f_plot.T
                    f_plot.columns = ['x1', 'y1', 'x2', 'y2']

                    figure = plt.Figure(figsize=(6, 5), dpi=100)
                    a = figure.add_subplot(111)
                    chart_t = FigureCanvasTkAgg(figure, root)
                    chart_t.get_tk_widget().grid(row=1, column=1, rowspan=6)

                    colors = []
                    for i in range(n_m):
                        if forces[i] > 0:
                            a.plot((f_plot.x1[i], f_plot.x2[i]), (f_plot.y1[i], f_plot.y2[i]), c='green')
                            colors.append('green')
                        elif forces[i] < 0:
                            a.plot((f_plot.x1[i], f_plot.x2[i]), (f_plot.y1[i], f_plot.y2[i]), c='red')
                            colors.append('red')
                        else:
                            a.plot((f_plot.x1[i], f_plot.x2[i]), (f_plot.y1[i], f_plot.y2[i]), c='black')
                            colors.append('black')

                    figure.patch.set_facecolor('gray')
                    a.set_title('2D Truss representation', c='blue')
                else:
                    messagebox.showwarning("WARNING", "You need to enter at least 2 valid members.")
                    open_m_data()
            else:
                messagebox.showwarning("WARNING", "You need to enter at least 2 valid members.")
                open_m_data()

        else:
            messagebox.showwarning("WARNING", "Please calculate the truss first.")

    def show_truss_deform():
        # Verify the existence of an un-empty list of members
        if os.path.exists('Rect_Beam_list.csv'):
            df = pd.read_csv('Rect_Beam_list.csv')
            if len(df) >= 2:
                nodes = pd.read_csv('Node_list.csv')
                dsp = pd.read_csv('Node_dsp.csv')
                d_x = np.array(dsp['Displacement on X'])
                d_y = np.array(dsp['Displacement on Y'])
                nodes_xp = np.array(nodes['Position X']) + d_x
                nodes_yp = np.array(nodes['Position Y']) + d_y
                members = pd.read_csv('Rect_Beam_list.csv')
                m_stn = list(members['Starting node'])
                m_en = list(members['Ending node'])
                x1 = []
                x2 = []
                y1 = []
                y2 = []
                for i in range(len(members)):
                    s = m_stn[i]
                    e = m_en[i]

                    x1.append(nodes_xp[s - 1])
                    x2.append(nodes_xp[e - 1])
                    y1.append(nodes_yp[s - 1])
                    y2.append(nodes_yp[e - 1])

                f_plot = pd.DataFrame([x1, y1, x2, y2])
                f_plot = f_plot.T
                f_plot.columns = ['x1', 'y1', 'x2', 'y2']

                figure = plt.Figure(figsize=(6, 5), dpi=100)
                a = figure.add_subplot(111)
                chart_t = FigureCanvasTkAgg(figure, root)
                chart_t.get_tk_widget().grid(row=1, column=1, rowspan=6)
                a.plot((f_plot.x1, f_plot.x2), (f_plot.y1, f_plot.y2), c='red')
                figure.patch.set_facecolor('gray')
                a.set_title('2D Truss representation', c='blue')
            else:
                messagebox.showwarning("WARNING", "You need to enter at least 2 valid members.")
                open_m_data()
        else:
            messagebox.showwarning("WARNING", "You need to enter at least 2 valid members.")
            open_m_data()

    def show_results():
        res = Tk()
        res.title('RESULT OF ANALYSIS')
        res.geometry("750x520")
        res['bg']='#fb0'
        res.resizable(False, False)
        try:
            res.iconbitmap("Valknut.ico")
        except:
            pass

        def op_reactions():
            if not t.compare("end-1c", "==", "1.0"):
                t.delete('1.0', END)
            if os.path.exists('Reactions.txt'):
                file = open('Reactions.txt').read()
                t.insert(1.0, file)
            else:
                messagebox.showwarning("WARNING", "Please make sure you have entered a correct structure "
                                                  "and respected the process!")

        def op_IE():
            if not t.compare("end-1c", "==", "1.0"):
                t.delete('1.0', END)
            if os.path.exists('Internal_forces.txt'):
                file = open('Internal_forces.txt').read()
                t.insert(1.0, file)
            else:
                messagebox.showwarning("WARNING", "Please make sure you have entered a correct structure "
                                                  "and respected the process!")

        def op_ND():
            if not t.compare("end-1c", "==", "1.0"):
                t.delete('1.0', END)
            if os.path.exists('Node_dsp.txt'):
                # os.startfile('Node_dsp.txt')
                file = open('Node_dsp.txt').read()
                t.insert(1.0, file)
            else:
                messagebox.showwarning("WARNING", "Please make sure you have entered a correct structure "
                                                  "and respected the process!")

        def op_MSM():
            if not t.compare("end-1c", "==", "1.0"):
                t.delete('1.0', END)
            if os.path.exists('Member_SM.txt'):
                file = open('Member_SM.txt').read()
                t.insert(1.0, file)
            else:
                messagebox.showwarning("WARNING", "Please make sure you have entered a correct structure "
                                                  "and respected the process!")

        def op_SSM():
            if not t.compare("end-1c", "==", "1.0"):
                t.delete('1.0', END)
            if os.path.exists('Global_SM.txt'):
                file = open('Global_SM.txt').read()
                t.insert(1.0, file)
            else:
                messagebox.showwarning("WARNING", "Please make sure you have entered a correct structure "
                                                  "and respected the process!")

        lab_1 = Label(res, text='PLEASE CHOOSE THE TYPE OF RESULT : ', font=("Helvetica", 15, 'bold'), bg='#fb0')

        t = Text(res, padx=5)

        but_1 = Button(res, text='REACTIONS', padx=2, pady=20, bg='light green', command=op_reactions)
        but_2 = Button(res, text='INTERNAL FORCES', padx=2, pady=20, bg='light green', command=op_IE)
        but_3 = Button(res, text='NODES DISPLACEMENTS', padx=2, pady=20, bg='light green', command=op_ND)
        but_4 = Button(res, text='Member Stiffness Matrices', padx=2, pady=20, bg='light green', command=op_MSM)
        but_5 = Button(res, text='Global Stiffness Matrices', padx=2, pady=20, bg='light green', command=op_SSM)

        lab_1.grid(column=0, row=0, columnspan=5)

        but_1.grid(column=0, row=1)
        but_2.grid(column=1, row=1)
        but_3.grid(column=2, row=1)
        but_4.grid(column=3, row=1)
        but_5.grid(column=4, row=1)

        t.grid(column=0, row=2, columnspan=5, padx=10)

        res.mainloop()

    def calc():
        if os.path.exists("Load_list.csv"):
            df = pd.read_csv("Load_list.csv")
            if len(df) == 0:
                messagebox.showwarning("WARNING", "The structure is unloaded. Please add loads first.")
                open_l_data()
            else:
                # Calculations
                # _________________________________________________________________________________________
                results_text()
                show_results()
        else:
            messagebox.showwarning("WARNING", "The structure is unloaded. Please add loads first.")
            open_l_data()

        pass

    def unavailable():
        messagebox.showinfo('Info', 'Sorry, this feature is not available yet.')

    def util():
        messagebox.showinfo('Info', 'Hello ! Welcome to my truss analysis program.\n'
                                    'This program was designed using the python language and multiple libraries as :\n'
                                    '- Tkinter\n- Pandas\n- Matplotlib\n- Os (Operating system)\n\n'
                                    'Steps for good use of this program:\n'
                                    '1) Enter the truss data in the same order as the buttons are displayed.\n'
                                    '2) Use the show button for the representation.\n'
                                    '3) Calculate and verify the results.\n'
                                    '4) Then you can see the deformed shape and internals efforts diagram.\n'
                                    '5) Finally you can reset the database for new analysis.\n\n'
                                    'Enjoy :) !!!')

    def exit_TA():
        root.destroy()

    if os.path.exists('Rect_Beam_list.csv'):
        df = pd.read_csv('Rect_Beam_list.csv')
        if len(df) >= 2:
            show_truss()
        else:
            pass
    else:
        pass

    b_1 = Button(root, text='NODE DATA', padx=28, pady=20, bg='light blue', command=open_n_data)
    b_2 = Button(root, text='MEMBER DATA', padx=20, pady=20, bg='light blue', command=open_m_data)
    b_3 = Button(root, text='LOAD DATA', padx=29, pady=20, bg='light blue', command=open_l_data)
    b_4 = Button(root, text='SHOW TRUSS', padx=26, pady=20, bg='light blue', command=show_truss)
    b_5 = Button(root, text='CALCULATE', padx=29, pady=20, bg='light blue', command=calc)
    b_6 = Button(root, text='RESULTS', padx=38, pady=20, bg='light blue', command=show_results)
    b_7 = Button(root, text='INTERNAL FORCES DIAG.', padx=10, pady=20, bg='light blue', command=show_truss_ie)
    b_8 = Button(root, text='DEFORMED SHAPE', padx=26, pady=20, bg='light blue', command=show_truss_deform)
    b_9 = Button(root, text='HELP', padx=63, pady=20, bg='purple', fg='white', command=util)
    b_10 = Button(root, text='EXIT', padx=65, pady=20, bg='red', fg='white', command=exit_TA)
    b_11 = Button(root, text='RESET DATA', padx=45, pady=20, bg='red', fg='white', command=reset_database)

    b_1.grid(row=1, column=0)
    b_2.grid(row=2, column=0)
    b_3.grid(row=3, column=0)
    b_4.grid(row=4, column=0)
    b_5.grid(row=5, column=0)
    b_6.grid(row=6, column=0)

    b_7.grid(row=1, column=3)
    b_8.grid(row=2, column=3)
    b_9.grid(row=3, column=3)
    b_10.grid(row=4, column=3)
    b_11.grid(row=5, column=3)

    root.mainloop()

