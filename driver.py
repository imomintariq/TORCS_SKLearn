from _csv import writer
from csv import DictWriter

import numpy as np
import pygame

import ManualMovement
import msgParser
import carState
import pickle
import carControl
import telemetry

# Number of sensors in observations
sensor_count = 29

# Number of availiable actions
action_count = 3

pickled_model = pickle.load(open('model3.pkl', 'rb'))
manual_keys = True


class Driver(object):
    '''
    A driver object for the SCRC
    '''

    def __init__(self, stage, interface, expert):
        '''Constructor'''
        self.observations_all = None
        self.obs = None
        self.act = ManualMovement.Action()
        self.WARM_UP = 0
        self.QUALIFYING = 1
        self.RACE = 2
        self.UNKNOWN = 3
        self.stage = stage
        self.interface = interface
        self.expert = expert
        self.action_list = []
        self.observation_list = []
        self.parser = msgParser.MsgParser()

        self.state = carState.CarState()

        self.control = carControl.CarControl()

        self.steer_lock = 0.785398
        self.max_speed = 100
        self.prev_rpm = None

    def init(self):
        '''Return init string with rangefinder angles'''

        self.angles = [0 for x in range(19)]

        for i in range(5):
            self.angles[i] = -90 + i * 15
            self.angles[18 - i] = 90 - i * 15

        for i in range(5, 9):
            self.angles[i] = -20 + (i - 5) * 5
            self.angles[18 - i] = 20 - (i - 5) * 5

        return self.parser.stringify({'init': self.angles})

    def drive(self, msg):

        # telemetry.getTelemetry(self.state)

        # self.interface.get_key_state()
        if manual_keys:
            self.act = self.expert.get_expert_act(self.act)
            self.step(self.act)

            # print(f"Expert Act = {self.act.accel}")

            # Normalizing
            # self.state.normalize_obs()
            self.state.setFromMsg(msg)

            obs_list = self.state.get_obs(angle=True, curLapTime=True, damage=True,
                                          distFromStart=True, distRaced=True, fuel=True,
                                          gear_1=True, lastLapTime=True, opponents=True, racePos=True,
                                          rpm=True, speedX=True, speedY=True, speedZ=True, track=True,
                                          trackPos=True, wheelSpinVel=True, z=True, focus_1=True, x=True,
                                          y=True, roll=True, pitch=True, yaw=True, speedGlobalX=True,
                                          speedGlobalY=True)

            self.observation_list.append(obs_list)

            # self.act.normalize_act()
            act_list = self.act.get_act(accel=True, brake=True, gas=True, clutch=True, gear_2=True,
                                        steer=True, focus_2=True, meta=True)

            self.action_list.append(act_list)
            # self.act.un_normalize_act()
            # self.gear()
            # self.step(self.act)

            return self.control.toMsg()
        else:
            # self.act = self.expert.get_expert_act(self.act)
            # self.step(self.act)

            # print(f"Expert Act = {self.act.accel}")

            # Normalizing
            # self.state.normalize_obs()
            self.state.setFromMsg(msg)

            obs_list = self.state.get_obs_for_prediction(angle=True, curLapTime=True, damage=True,
                                                         distFromStart=True, distRaced=True, fuel=True,
                                                         gear_1=True, lastLapTime=True, opponents=True, racePos=True,
                                                         rpm=True, speedX=True, speedY=True, speedZ=True, track=True,
                                                         trackPos=True, wheelSpinVel=True, z=True, focus_1=True, x=True,
                                                         y=True, roll=True, pitch=True, yaw=True, speedGlobalX=True,
                                                         speedGlobalY=True)
            print(obs_list)
            #obs_2d = [obs_list]
            act_list = pickled_model.predict(obs_list)
            print(act_list)
            self.act.set_act(act_list)
            self.step(self.act)
            return self.control.toMsg()

    def step(self, act):
        self.control.setAccel(act.accel)
        self.control.setBrake(act.brake)
        self.control.setClutch(act.clutch)
        self.control.setGear(act.gear)
        self.control.setSteer(act.steer)
        self.control.setMeta(act.meta)
        self.control.focus = act.focus

    def steer(self):
        angle = self.state.angle
        dist = self.state.trackPos

        # self.control.setSteer((angle - dist*0.5)/self.steer_lock)

    def gear(self):
        rpm = self.state.getRpm()
        gear = self.state.getGear()

        if self.prev_rpm == None:
            up = True
        else:
            if (self.prev_rpm - rpm) < 0:
                up = True
            else:
                up = False

        if up and rpm > 7000:
            gear += 1

        if not up and rpm < 3000:
            gear -= 1

        self.control.setGear(gear)

    def speed(self):
        speed = self.state.getSpeedX()
        accel = self.control.getAccel()

        if speed < self.max_speed:
            accel += 0.1
            if accel > 1:
                accel = 1.0
        else:
            accel -= 0.1
            if accel < 0:
                accel = 0.0

        self.control.setAccel(accel)

    def onShutDown(self):

        # print(self.observation_list)
        # print(self.action_list)
        field_names = ["angle", "curLapTime", "damage",
                       "distFromStart", "distRaced", "fuel",
                       "gear_1", "lastLapTime", "opponents", "racePos",
                       "rpm", "speedX", "speedY", "speedZ", "track",
                       "trackPos", "wheelSpinVel", "z", "focus_1", "x",
                       "y", "roll", "pitch", "yaw", "speedGlobalX",
                       "speedGlobalY", "accel", "brake", "gas", "clutch", "gear_2",
                       "steer", "focus_2", "meta"]
        with open('CSVFILE.csv', 'a') as f_object:
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)

            # Pass the dictionary as an argument to the Writerow()

            for observation, action_made in zip(self.observation_list, self.action_list):
                mydict = dict(observation.items())
                mydict.update(action_made.items())
                dictwriter_object.writerow(mydict)
                # print(mydict)

    def onRestart(self):
        pass
