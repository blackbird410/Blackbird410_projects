import os.path

import numpy as np
import pandas as pd
from Truss_classes import *


def find_constraints():
    df = pd.read_csv("Node_list.csv")
    index = []
    l_cons = []
    l_n_cons = []
    j = 0
    for i in range(len(df)):
        if df["Reaction X"][i] or df["Reaction Y"][i]:
            if df["Reaction Y"][i]:
                l_cons.append(df["Node number"][i])
                l_cons.append(df["Node number"][i])
                index.append(j + 2)
                index.append(j + 1)
            else:
                l_cons.append(df["Node number"][i])
                l_cons.append(df["Node number"][i])
                index.append(j + 1)
                index.append(j + 2)
            j += 2
        else:
            l_n_cons.append(df["Node number"][i])
            l_n_cons.append(df["Node number"][i])
            j += 1
            index.append(j)
            j += 1
            index.append(j)

    l_displaced_node = l_n_cons + l_cons
    dct = {"D Index": index, "Displaced nodes": l_displaced_node}
    df = pd.DataFrame(dct)
    # print(str(df) + "\n___________**_____________")

    return df


def d_cosines():
    df_m = pd.read_csv("Rect_Beam_list.csv")
    df_n = pd.read_csv("Node_list.csv")

    lambda_x = []
    lambda_y = []
    index = []

    for i in range(len(df_m)):
        near_end = df_m["Starting node"][i]
        far_end = df_m["Ending node"][i]

        x_p_ne = df_n["Position X"][near_end - 1]
        y_p_ne = df_n["Position Y"][near_end - 1]
        x_p_fe = df_n["Position X"][far_end - 1]
        y_p_fe = df_n["Position Y"][far_end - 1]

        lambda_x.append((x_p_fe - x_p_ne) / df_m["Length"][i])
        lambda_y.append((y_p_fe - y_p_ne) / df_m["Length"][i])
        index.append(i + 1)

    dct = {"No member": index, "Lambda X": lambda_x, "Lambda Y": lambda_y}
    df = pd.DataFrame(dct)

    return df


def msm(l_x, l_y, lgt, a, e):
    assert -1 <= l_x <= 1, "Lambda X value is invalid."
    assert -1 <= l_y <= 1, "Lambda Y value is invalid."
    assert lgt > 0, "Length is invalid"

    m = np.array([l_x ** 2, l_x * l_y, -(l_x ** 2), -(l_x * l_y),
                  l_x * l_y, l_y ** 2, -(l_x * l_y), -(l_y ** 2),
                  -(l_x ** 2), -(l_x * l_y), l_x ** 2, l_x * l_y,
                  -(l_x * l_y), -(l_y ** 2), l_x * l_y, l_y ** 2]).reshape(4, 4)
    m = (a * e / (1000*lgt)) * m
    # This coefficient of 10e3 is added because the area and length are not in the same unit.

    return m


def ssm():
    l_lambda = d_cosines()
    df_m_data = pd.read_csv("Rect_Beam_list.csv")
    length = df_m_data["Length"]
    ym = df_m_data["Young modulus"]
    s_a = df_m_data["Area"]
    st_n = df_m_data["Starting node"]
    e_n = df_m_data["Ending node"]
    n_nodes = len(pd.read_csv("Node_list.csv"))
    const = find_constraints()
    msm_list = []
    ssm_list = []
    k_m = np.zeros((2 * n_nodes) ** 2).reshape(2 * n_nodes, 2 * n_nodes)
    n_m = len(l_lambda)

    open('Member_SM.txt', 'w')

    for count in range(n_m):
        m_stiff_mat = msm(l_lambda["Lambda X"][count], l_lambda["Lambda Y"][count],
                          length[count], s_a[count], ym[count])

        mat = np.round(m_stiff_mat, 3)

        txt = f"Member Stiffness Matrix {count + 1} :\n"

        with open('Member_SM.txt', 'a') as my_file:
            my_file.write(txt + str(mat) + "\n\n")

        msm_list.append(m_stiff_mat)

    for j in range(n_m):
        i = 0
        near_end_i = []
        far_end_i = []
        while i < len(const):
            if const["Displaced nodes"][i] == st_n[j]:
                near_end_i.append(const["D Index"][i])
                near_end_i.append(const["D Index"][i + 1])
                i += 2
            elif const["Displaced nodes"][i] == e_n[j]:
                far_end_i.append(const["D Index"][i])
                far_end_i.append(const["D Index"][i + 1])
                i += 2
            else:
                i += 1
        z_index = near_end_i + far_end_i

        m = np.round(msm_list[j], 3)
        # Vertical and horizontal stack of zeros rows
        for k in range(4, n_nodes * 2):
            z = np.zeros(k).reshape(1, k)
            m = np.vstack((m, z))
            z = np.zeros(k + 1).reshape(k + 1, 1)
            m = np.hstack((m, z))

        # _________________________________________________________________________
        for c in range(4):
            r = 3 - c
            if z_index[r] - 1 != r:
                # print(r, z_index[r])
                m[[r, z_index[r] - 1]] = m[[z_index[r] - 1, r]]
                m = m.T
                m[[r, z_index[r] - 1]] = m[[z_index[r] - 1, r]]
                m = m.T
            else:
                pass

        # _________________________________________________________________________

        ssm_list.append(m)

    for i in range(n_m):
        k_m += ssm_list[i]

    t = f"Structure Global Matrix :" \
        + "\n___________________________________________________________________________\n"

    if os.path.exists('Global_SM.txt'):
        os.remove('Global_SM.txt')
    with open('Global_SM.txt', 'w') as fle:
        with pd.option_context('display.max_colwidth', None,
                               'display.max_columns', None,
                               'display.max_rows', None):
            g_stiff = str(pd.DataFrame(np.round(k_m, 3)))
            fle.write(t + g_stiff + "\n\n")

    return np.round(k_m, 3)


def load_v():
    """This function put the applied loads in a vector of (1, n) where n is the dimension
    of the structure stiffness matrix. It returns an array for each applied load and the number
    of restraints in second position. So you need two variables to receive the results.

    Example:
        -----------
        list = []
        n_restraints = 0

        list, n_restraints = load_v()
        """

    df = find_constraints()
    n_l = len(df)
    restraints_count = 0
    list_l_v = []
    df_n = pd.read_csv("Node_list.csv")
    df_l = pd.read_csv("Load_list.csv").sort_values("Node applied")

    for i in range(int(n_l / 2)):
        if df_n["Reaction X"][i]:
            restraints_count += 1
        if df_n["Reaction Y"][i]:
            restraints_count += 1

    for j in range(len(df_l)):
        actual_load_no = df_l["Node applied"][j]
        k = 0
        l_v = []
        while k < len(df):
            if actual_load_no == df["Displaced nodes"][k]:
                l_v.append(df_l["Load on X"][j])
                l_v.append(df_l["Load on Y"][j])
                k += 2
            else:
                l_v.append(0)
                k += 1
        l_v = np.array(l_v).reshape(1, n_l).T
        list_l_v.append(l_v)

    s = np.array(np.zeros(n_l).reshape(n_l, 1))
    for i in range(len(list_l_v)):
        s += list_l_v[i]
    return s, restraints_count


def res_reactions():
    """This function determines the reactions of the structure and the displacements of each node.
    It returns an array of displacements (x and y) and an array of the reactions."""

    sum_load_vs, r_count = load_v()
    st_stiff_m = ssm()

    reduced_m_dim = len(sum_load_vs) - r_count
    reduced_m = st_stiff_m[0:reduced_m_dim, 0:reduced_m_dim]
    a = np.linalg.inv(reduced_m)
    b = sum_load_vs[0:reduced_m_dim]

    # Calculate the displacements by multiplying the inverse of the reduced SSM by the load vector.
    d = a.dot(b)
    d = np.vstack((d, np.zeros(r_count).reshape(r_count, 1)))
    # print("Displacements\n______________________\n" + str(d) + "\nReactions\n________________")

    reactions = np.round(st_stiff_m.dot(d), 3)

    nodes_pos = find_constraints()
    nodes_pos = nodes_pos[reduced_m_dim:len(nodes_pos)]

    r_nodes = list(nodes_pos["Displaced nodes"])
    r_values = list(reactions[reduced_m_dim - 1:reduced_m_dim - 1 + r_count])
    r_x = []
    r_y = []
    node = []

    for i in range(r_count):
        if not i % 2:
            r_x.append(str(r_values[i]).strip("[]"))
            if r_nodes[i] not in node:
                node.append(r_nodes[i])
        else:
            r_y.append(str(r_values[i]).strip("[]"))

    r_dct = {"Node": node, "Reaction X": r_x, "Reaction Y": r_y}

    df_r = pd.DataFrame(r_dct)
    r_txt = "Structure reactions\n_____________________________\n"
    if os.path.exists("Reactions.txt"):
        os.remove("Reactions.txt")
    with open("Reactions.txt", "w") as my_react:
        my_react.write(r_txt + str(df_r) + "\n\n")

    return d, reactions


def node_dsp():
    """This function returns a dataframe of the nodes displacements of the truss."""

    ind = find_constraints()
    displacements, react = res_reactions()
    displacements = displacements.reshape(len(ind))
    c1 = ind["D Index"]
    c2 = ind["Displaced nodes"]
    my_dct = {"D Index": c1, "Displaced nodes": c2, "Displacements": displacements}
    my_df = pd.DataFrame(my_dct)
    my_df = my_df.sort_values("Displaced nodes")

    node = []
    d_x = []
    d_y = []

    for cnt in range(len(my_df)):
        if ind["D Index"][cnt] % 2:
            node.append(my_df["Displaced nodes"][cnt])
            d_x.append(my_df["Displacements"][cnt])
        else:
            d_y.append(my_df["Displacements"][cnt])

    my_dct = {"Node": node, "Displacement on X": d_x, "Displacement on Y": d_y}
    data_f = pd.DataFrame(my_dct)
    data_f = data_f.sort_values("Node")

    data_f.to_csv('Node_dsp.csv')

    t = "Node displacements\n_________________________________________\n"

    if os.path.exists('Node_dsp.txt'):
        os.remove('Node_dsp.txt')
        open('Node_dsp.txt', 'w')
    with open('Node_dsp.txt', 'w') as my_f:
        my_f.write(t + str(data_f) + "\n\n")

    return data_f


def find_IE():
    theta = d_cosines()
    theta_x = theta['Lambda X']
    theta_y = theta['Lambda Y']

    n_dsp = node_dsp()
    m_data = pd.read_csv("Rect_Beam_list.csv")
    m_data_ym = np.array(m_data['Young modulus'])
    m_data_a = np.array(m_data['Area'])
    m_data_l = np.array(m_data['Length']) * 1000
    m_data_stn = np.array(m_data['Starting node'])
    m_data_en = np.array(m_data['Ending node'])
    m = len(m_data_ym)

    ie = []
    index = []

    for i in range(m):
        l_x = float(theta_x[i])
        l_y = float(theta_y[i])
        s = m_data_stn[i] - 1
        e = m_data_en[i] - 1
        d = [n_dsp['Displacement on X'][s], n_dsp['Displacement on Y'][s],
             n_dsp['Displacement on X'][e], n_dsp['Displacement on Y'][e]]
        d = np.array(d).T

        tampon = m_data_a[i] * m_data_ym[i] / m_data_l[i]
        tampon = tampon * np.array([-l_x, -l_y, l_x, l_y]).dot(d)

        ie.append(tampon)

        index.append(i+1)

    dct = {"Bar": index, "Internal force": ie}
    dct = pd.DataFrame(dct)

    t = "Internal forces\n_________________________________________\n"

    if os.path.exists("Internal_forces.txt"):
        os.remove("Internal_forces.txt")
        open('Internal_forces.txt', 'w')
    with open('Internal_forces.txt', 'w') as my_f:
        my_f.write(t + str(dct) + "\n\n")

    dct.to_csv('Internal_forces.csv')

    return dct


def results_text():
    node_dsp()
    find_IE()
    text1 = open("Member_SM.txt", "r")
    text2 = open("Global_SM.txt", "r")
    text3 = open('Node_dsp.txt', 'r')
    text4 = open("Reactions.txt", "r")
    text5 = open("Internal_forces.txt", "r")

    txt = "TRUSS ANALYSIS RESULTS\n_____________________________________________\n"

    if os.path.exists('Results.txt'):
        os.remove('Results.txt')
    with open('Results.txt', 'w') as my_f:
        my_f.write(txt + str(text1.read()) + "\n\n")
        my_f.write(str(text2.read()) + "\n\n")
        my_f.write(str(text3.read()) + "\n\n")
        my_f.write(str(text4.read()) + "\n\n")
        my_f.write(str(text5.read()) + "\n\n")
