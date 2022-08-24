import random as rd

import numpy as np

gen = 5000
group_num = 20
agent_num = 26
# fraction of fighters who die if a war occur
cap_delta_f = 0.14
# fraction of civils who die if the group loses
cap_delta_c = 2.5


class Agent():

    def __init__(self, P_or_T, A_or_N):
        self.P_or_T = P_or_T
        self.A_or_N = A_or_N
        self.allele = [ P_or_T, A_or_N ]


class Group():
    def __init__(self, agent_list):
        agent_P_or_T_list = [ agent.P_or_T for agent in agent_list ]
        agent_A_or_N_list = [ agent.A_or_N for agent in agent_list ]

        self.agents = agent_list
        self.size = len(agent_list)
        self.P_freq = agent_P_or_T_list.count('P') / self.size
        self.T_freq = agent_P_or_T_list.count('T') / self.size
        self.A_freq = agent_A_or_N_list.count('A') / self.size
        self.N_freq = agent_A_or_N_list.count('N') / self.size
        self.PA_freq = self.A_freq * self.P_freq
        self.P_num = agent_P_or_T_list.count('P')
        self.T_num = agent_P_or_T_list.count('T')
        self.A_num = agent_A_or_N_list.count('A')
        self.N_num = agent_A_or_N_list.count('N')
        self.PA_num = self.A_freq * self.P_freq * self.size


def group_interaction(group_i, group_j):
    f_i_T = group_i.T_freq
    f_j_T = group_j.T_freq

    # hostile probability
    h_ij = 1 - f_i_T * f_j_T
    f_i_PA = group_i.PA_freq
    f_j_PA = group_j.PA_freq

    delta_ij = f_i_PA - f_j_PA
    abs_delta_ij = abs(delta_ij)
    lambda_i = 0.5 + 0.5 * delta_ij

    if rd.random() < delta_ij:
        # i stronger
        if delta_ij>0:
            if rd.random() < lambda_i:
                # i wins
                # civils die
                group_j.size -= (group_j.size - group_j.PA_num) * cap_delta_c * abs_delta_ij
                group_i.size -= group_i.PA_num * cap_delta_f
                group_j.size -= group_i.PA_num * cap_delta_f




            else:
                pass
            # draw
            # civils die

        # i weaker
        else:
            if rd.random() < lambda_i:
                # i loses
                # civils die
                group_i.size -= (group_i.size - group_i.PA_num) * cap_delta_c * abs_delta_ij
                group_i.size -= group_i.PA_num * cap_delta_f
                group_j.size -= group_i.PA_num * cap_delta_f

                # repopulation of loser

            else:
            # draw
            # civils die





        # it is a draw
        # fighters die




    else:

    return 0


# for i in range(gen):
#
#     if group_interaction == 'hosile':

group_1 = Group([ Agent('T', 'N') for i in range(agent_num) ])

print(group_1.size)
print(group_1.P_freq)
print(group_1.T_freq)
print(group_1.A_freq)
print(group_1.N_freq)
print(group_1.PA_freq)
