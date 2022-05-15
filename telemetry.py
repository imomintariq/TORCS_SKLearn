# -*- coding: utf-8 -*-
"""
Created on Sat May  7 00:20:01 2022

@author: Computer

"""
from itertools import count

from matplotlib.animation import FuncAnimation

import msgParser
import carState
import carControl
import matplotlib.pyplot as plt

x_axis = []
y_axis = []
index = count()
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])


def getTelemetry(state: carState.CarState):
    pass
    # print('track = ')
    # print(
    #     f"{state.track[0]}, {state.track[1]}, {state.track[2]}, {state.track[3]}, {state.track[4]}, {state.track[5]}, {state.track[6]}, {state.track[7]}, {state.track[8]}, {state.track[9]}, {state.track[10]}, {state.track[11]}, {state.track[12]}, {state.track[13]}, {state.track[14]}, {state.track[15]}, {state.track[16]}, {state.track[17]}, {state.track[18]}")
    # print(f"speed ={state.speedX}")
    # print(f"trackPosition = {state.trackPos}")
    # print(f"angle = {state.angle}")
    # print(f"current lap time = {state.curLapTime}")

