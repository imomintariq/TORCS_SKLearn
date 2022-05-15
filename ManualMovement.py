import pygame
import pygame.freetype

import carState


class Keys:
    def __init__(self):
        """Stores the state of a keyboard"""
        self.up = False
        self.left = False
        self.down = False
        self.right = False
        self.shift_up = False
        self.shift_down = False
        self.space_bar = False


class Interface:
    def __init__(self):
        """Interface for cummunicating with keyboards and steering wheels"""
        pygame.init()
        WIDTH = 600
        HEIGHT = 480
        SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.pressed = Keys()

    def check_key(self, event_type, event_key):
        """Check a single key for a single event type"""
        for event in pygame.event.get():
            if event.type == event_type:
                if event.key == event_key:
                    return True
        return False

    def get_key_state(self):
        """Get states of all important keys"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pressed.up = True
                if event.key == pygame.K_DOWN:
                    self.pressed.down = True
                if event.key == pygame.K_LEFT:
                    self.pressed.left = True
                if event.key == pygame.K_RIGHT:
                    self.pressed.right = True
                if event.key == pygame.K_z:
                    self.pressed.shift_down = True
                if event.key == pygame.K_x:
                    self.pressed.shift_up = True
                if event.key == pygame.K_SPACE:
                    self.pressed.space_bar = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.pressed.up = False
                if event.key == pygame.K_DOWN:
                    self.pressed.down = False
                if event.key == pygame.K_LEFT:
                    self.pressed.left = False
                if event.key == pygame.K_RIGHT:
                    self.pressed.right = False
                if event.key == pygame.K_z:
                    self.pressed.shift_down = False
                if event.key == pygame.K_x:
                    self.pressed.shift_up = False
                if event.key == pygame.K_SPACE:
                    self.pressed.space_bar = False

        return self.pressed

    # def display_act(self, act):
    #     """Display the current action on the interface"""
    #     accel = "ACCEL: " + str(act.accel)
    #     brake = "BRAKE: " + str(act.brake)
    #     gear = "GEAR: " + str(act.gear)
    #     steer = "STEER: " + str(act.steer)
    #
    #     self.screen.fill((0, 0, 0))
    #
    #     accel, rect_accel = self.font.render(accel, (255, 255, 255))
    #     brake, rect_brake = self.font.render(brake, (255, 255, 255))
    #     gear, rect_gear = self.font.render(gear, (255, 255, 255))
    #     steer, rect_steer = self.font.render(steer, (255, 255, 255))
    #
    #     self.screen.blit(accel, (10, 10))
    #     self.screen.blit(brake, (10, rect_brake[1] + 20))
    #     self.screen.blit(gear, (10, 2 * rect_gear[1] + 30))
    #     self.screen.blit(steer, (10, 3 * rect_steer[1] + 40))


import numpy as np


class Action:
    def __init__(self):
        """An action is the instructions sent to the car"""
        self.accel = 0.2
        self.brake = 0
        self.gas = 0
        self.clutch = 0
        self.gear = 1
        self.steer = 0
        self.focus = [-90, -45, 0, 45, 90]
        self.meta = 0

    def get_act(self, accel=None, brake=None, gas=None, clutch=None, gear=None,
                steer=None, focus=None, meta=None):
        """Returns the specified values in a numpy array"""
        my_dict = {"accel":[], "brake":[], "gas":[], "clutch":[], "gear":[],
                "steer":[], "focus":[], "meta":[]}
        act = np.array([])
        if accel:
            act = np.append(act, self.accel)
            my_dict["accel"].append(self.accel)
        if brake:
            act = np.append(act, self.brake)
            my_dict["brake"].append(self.brake)
        if gas:
            act = np.append(act, self.gas)
            my_dict["gas"].append(self.gas)
        if clutch:
            act = np.append(act, self.clutch)
            my_dict["clutch"].append(self.clutch)
        if gear:
            act = np.append(act, self.gear)
            my_dict["gear"].append(self.gear)
        if steer:
            act = np.append(act, self.steer)
            my_dict["steer"].append(self.steer)
        if focus:
            act = np.append(act, self.focus)
            my_dict["focus"].append(self.focus)
        if meta:
            act = np.append(act, self.meta)
            my_dict["meta"].append(self.meta)
        return my_dict

    def set_act(self, act, accel=None, brake=None, gas=None, clutch=None,
                gear=None, steer=None, focus=None, meta=None):
        """Set the values specified with a numpy array"""
        i = 0
        if accel:
            self.accel = act[0][i]
            i += 1
        if brake:
            self.brake = act[0][i]
            i += 1
        if gas:
            self.gas = act[0][i]
            i += 1
        if clutch:
            self.clutch = act[0][i]
            i += 1
        if gear:
            self.gear = act[0][i]
            i += 1
        if steer:
            self.steer = act[0][i]
            i += 1
        if focus:
            self.focus = act[0][i]
            i += 1
        if meta:
            self.meta = act[0][i]
            i += 1

    def normalize_act(self):
        """Normalize action values to be between 0 and 1"""
        self.gas = (self.accel / 2) - (self.brake / 2) + 0.5
        self.gear = (self.gear + 1) / 7
        self.steer = (self.steer + 1) / 2

    def un_normalize_act(self):
        """Un-normalize action values to be betwen their original values"""
        if self.gas == 0.5:
            self.accel = 0
            self.accel = 0
        if self.gas > 0.5:
            self.accel = (self.gas - 0.5) * 2
            self.brake = 0
        elif self.gas < 0.5:
            self.brake = (0.5 - self.gas) * 2
            self.accel = 0
        self.gear = int(round((self.gear * 7) - 1))
        self.steer = (self.steer * 2) - 1

    def copy(self, act):
        """Copy an existing action to this"""
        self.accel = act.accel
        self.brake = act.brake
        self.gas = act.gas
        self.clutch = act.clutch
        self.gear = act.gear
        self.steer = act.steer
        self.focus = act.focus
        self.meta = act.meta

    def __clip(self, v, lo, hi):
        """Make sure the value v is between lo and hi"""
        if v > hi:
            return hi
        if v < lo:
            return lo
        return v


PI = 3.14159265359


class Expert:
    def __init__(self, interface, automatic=True):
        """Expert is the driver that the ANN is supposed to imitate"""
        self.prev_rpm = None
        self.prev_shift_up = False
        self.prev_shift_down = False
        self.act = Action()
        self.interface = interface
        self.automatic = automatic

    def __clip(self, v, lo, hi):
        """Makes sure that the value is between lo and hi"""
        if v < lo:
            return lo
        elif v > hi:
            return hi
        else:
            return v

    def get_expert_act(self, act, obs):
        """Get the action that the expert would preform"""

        new_act = Action()
        new_act.copy(act)

        key = self.interface.get_key_state()
        print(f"Key = {key.up}")

        if key.up:
            new_act.accel += .1
        else:
            new_act.accel -= .1

        if key.down:
            new_act.brake += .1
        else:
            new_act.brake -= .1

        if key.space_bar:
            new_act.brake += .1
        else:
            new_act.brake -= .1

        if key.left:
            new_act.steer += .02
        elif key.right:
            new_act.steer -= .02
        else:
            new_act.steer = 0

        # if self.automatic:
        #     rpm = obs.getRpm()
        #     gear = obs.getGear()
        #
        #     if self.prev_rpm is None:
        #         up = True
        #     else:
        #         if (self.prev_rpm - rpm) < 0:
        #             up = True
        #         else:
        #             up = False
        #
        #     if up and rpm > 7000:
        #         #self.prev_rpm = rpm
        #         new_act.gear += 1
        #
        #     if not up and rpm < 3000:
        #         #self.prev_rpm = rpm
        #         new_act.gear -= 1
        #
        # else:
        if key.shift_up and self.prev_shift_up is False:
            new_act.gear += 1
            self.prev_shift_up = True
        elif key.shift_up is False:
            self.prev_shift_up = False

        if key.shift_down and self.prev_shift_down is False:
            new_act.gear -= 1
            self.prev_shift_down = True
        elif key.shift_down is False:
            self.prev_shift_down = False

        # Make sure the values are valid
        new_act.accel = self.__clip(new_act.accel, 0, 1)
        new_act.brake = self.__clip(new_act.brake, 0, 1)
        new_act.gear = self.__clip(new_act.gear, -1, 7)
        new_act.steer = self.__clip(new_act.steer, -1, 1)
        new_act.gas = (new_act.accel / 2) - (new_act.brake / 2) + 0.5

        # Display the values on the interface
        # self.interface.display_act(new_act)

        # Update act
        self.act = new_act

        return self.act
