import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits import mplot3d

if os.path.exists('Rect_Beam_list.csv'):
    df = pd.read_csv('Rect_Beam_list.csv')
    if len(df) >= 2:
        # ________________________________________________________________________________
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
        f_plot = np.hstack((f_plot, np.zeros(len(f_plot)).reshape(len(f_plot), 1)))
        f_plot = np.hstack((f_plot, np.zeros(len(f_plot)).reshape(len(f_plot), 1)))
        f_plot = np.hstack((f_plot, np.ones(len(f_plot)).reshape(len(f_plot), 1)))
        f_plot = np.hstack((f_plot, np.ones(len(f_plot)).reshape(len(f_plot), 1)))
        f_plot = pd.DataFrame(f_plot)
        f_plot.columns = ['x1', 'y1', 'x2', 'y2', 'z1', 'z2', 'z3', 'z4']

        print(f_plot)
        a_axis = plt.axes(projection="3d")
        x_p1 = f_plot.x1
        x_p2 = f_plot.x2
        y_p1 = f_plot.y1
        y_p2 = f_plot.y2
        z_p1 = f_plot.z1
        z_p2 = f_plot.z2
        z_p3 = f_plot.z3
        z_p4 = f_plot.z4

        # Plot the face of the structure
        for i in range(len(f_plot)):
            a_axis.plot((x_p1[i], x_p2[i]), (y_p1[i], y_p2[i]), (z_p1[i], z_p2[i]), c='blue')

        # Plot the back of the structure
        for i in range(len(f_plot)):
            a_axis.plot3D((x_p1[i], x_p2[i]), (y_p1[i], y_p2[i]), (z_p3[i], z_p4[i]), c='blue')

        x_max = np.max(x_p1)
        y_max = np.max(y_p1)
        x_m1 = np.min(x_p1)
        y_m1 = np.min(y_p1)

        # Plot the link of the structure
        for i in range(len(f_plot)):
            if x_p1[i] == x_p2[i] or y_p1[i] == y_p2[i]:
                a_axis.plot((x_m1, x_m1), (y_m1, y_m1), (0, 1), c='red')
                a_axis.plot((x_m1, x_m1), (y_max, y_max), (0, 1), c='red')
                a_axis.plot((x_max, x_max), (y_m1, y_m1), (0, 1), c='red')
                a_axis.plot((x_max, x_max), (y_max, y_max), (0, 1), c='red')

        a_axis.set_title("3D Structure representation")
        a_axis.set_xlabel("X axis")
        a_axis.set_ylabel("Y axis")
        a_axis.set_zlabel("Z axis")
        plt.show()

        # ________________________________________________________________________________
