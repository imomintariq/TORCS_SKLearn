import msgParser
import numpy as np


class CarState(object):
    '''
    Class that hold all the car state variables
    '''

    def __init__(self):
        '''Constructor'''
        self.parser = msgParser.MsgParser()
        self.sensors = None
        self.angle = None
        self.curLapTime = None
        self.damage = None
        self.distFromStart = None
        self.distRaced = None
        self.focus = None
        self.fuel = None
        self.gear = None
        self.lastLapTime = None
        self.opponents = None
        self.racePos = None
        self.rpm = None
        self.speedX = None
        self.speedY = None
        self.speedZ = None
        self.track = None
        self.trackPos = None
        self.wheelSpinVel = None
        self.z = None

    def setFromMsg(self, str_sensors):
        self.sensors = self.parser.parse(str_sensors)

        self.setAngleD()
        self.setCurLapTimeD()
        self.setDamageD()
        self.setDistFromStartD()
        self.setDistRacedD()
        self.setFocusD()
        self.setFuelD()
        self.setGearD()
        self.setLastLapTimeD()
        self.setOpponentsD()
        self.setRacePosD()
        self.setRpmD()
        self.setSpeedXD()
        self.setSpeedYD()
        self.setSpeedZD()
        self.setTrackD()
        self.setTrackPosD()
        self.setWheelSpinVelD()
        self.setZD()

    def toMsg(self):
        self.sensors = {}

        self.sensors['angle'] = [self.angle]
        self.sensors['curLapTime'] = [self.curLapTime]
        self.sensors['damage'] = [self.damage]
        self.sensors['distFromStart'] = [self.distFromStart]
        self.sensors['distRaced'] = [self.distRaced]
        self.sensors['focus'] = self.focus
        self.sensors['fuel'] = [self.fuel]
        self.sensors['gear'] = [self.gear]
        self.sensors['lastLapTime'] = [self.lastLapTime]
        self.sensors['opponents'] = self.opponents
        self.sensors['racePos'] = [self.racePos]
        self.sensors['rpm'] = [self.rpm]
        self.sensors['speedX'] = [self.speedX]
        self.sensors['speedY'] = [self.speedY]
        self.sensors['speedZ'] = [self.speedZ]
        self.sensors['track'] = self.track
        self.sensors['trackPos'] = [self.trackPos]
        self.sensors['wheelSpinVel'] = self.wheelSpinVel
        self.sensors['z'] = [self.z]

        return self.parser.stringify(self.sensors)

    def getFloatD(self, name):
        try:
            val = self.sensors[name]
        except KeyError:
            val = None

        if val != None:
            val = float(val[0])

        return val

    def getFloatListD(self, name):
        try:
            val = self.sensors[name]
        except KeyError:
            val = None

        if val != None:
            l = []
            for v in val:
                l.append(float(v))
            val = l

        return val

    def getIntD(self, name):
        try:
            val = self.sensors[name]
        except KeyError:
            val = None

        if val != None:
            val = int(val[0])

        return val

    def setAngle(self, angle):
        self.angle = angle

    def setAngleD(self):
        self.angle = self.getFloatD('angle')

    def getAngle(self):
        return self.angle

    def setCurLapTime(self, curLapTime):
        self.curLapTime = curLapTime

    def setCurLapTimeD(self):
        self.curLapTime = self.getFloatD('curLapTime')

    def getCurLapTime(self):
        return self.curLapTime

    def setDamage(self, damage):
        self.damage = damage

    def setDamageD(self):
        self.damage = self.getFloatD('damage')

    def getDamage(self):
        return self.damage

    def setDistFromStart(self, distFromStart):
        self.distFromStart = distFromStart

    def setDistFromStartD(self):
        self.distFromStart = self.getFloatD('distFromStart')

    def getDistFromStart(self):
        return self.distFromStart

    def setDistRaced(self, distRaced):
        self.distRaced = distRaced

    def setDistRacedD(self):
        self.distRaced = self.getFloatD('distRaced')

    def getDistRaced(self):
        return self.distRaced

    def setFocus(self, focus):
        self.focus = focus

    def setFocusD(self):
        self.focus = self.getFloatListD('focus')

    def setFuel(self, fuel):
        self.fuel = fuel

    def setFuelD(self):
        self.fuel = self.getFloatD('fuel')

    def getFuel(self):
        return self.fuel

    def setGear(self, gear):
        self.gear = gear

    def setGearD(self):
        self.gear = self.getIntD('gear')

    def getGear(self):
        return self.gear

    def setLastLapTime(self, lastLapTime):
        self.lastLapTime = lastLapTime

    def setLastLapTimeD(self):
        self.lastLapTime = self.getFloatD('lastLapTime')

    def setOpponents(self, opponents):
        self.opponents = opponents

    def setOpponentsD(self):
        self.opponents = self.getFloatListD('opponents')

    def getOpponents(self):
        return self.opponents

    def setRacePos(self, racePos):
        self.racePos = racePos

    def setRacePosD(self):
        self.racePos = self.getIntD('racePos')

    def getRacePos(self):
        return self.racePos

    def setRpm(self, rpm):
        self.rpm = rpm

    def setRpmD(self):
        self.rpm = self.getFloatD('rpm')

    def getRpm(self):
        return self.rpm

    def setSpeedX(self, speedX):
        self.speedX = speedX

    def setSpeedXD(self):
        self.speedX = self.getFloatD('speedX')

    def getSpeedX(self):
        return self.speedX

    def setSpeedY(self, speedY):
        self.speedY = speedY

    def setSpeedYD(self):
        self.speedY = self.getFloatD('speedY')

    def getSpeedY(self):
        return self.speedY

    def setSpeedZ(self, speedZ):
        self.speedZ = speedZ

    def setSpeedZD(self):
        self.speedZ = self.getFloatD('speedZ')

    def getSpeedZ(self):
        return self.speedZ

    def setTrack(self, track):
        self.track = track

    def setTrackD(self):
        self.track = self.getFloatListD('track')

    def getTrack(self):
        return self.track

    def setTrackPos(self, trackPos):
        self.trackPos = trackPos

    def setTrackPosD(self):
        self.trackPos = self.getFloatD('trackPos')

    def getTrackPos(self):
        return self.trackPos

    def setWheelSpinVel(self, wheelSpinVel):
        self.wheelSpinVel = wheelSpinVel

    def setWheelSpinVelD(self):
        self.wheelSpinVel = self.getFloatListD('wheelSpinVel')

    def getWheelSpinVel(self):
        return self.wheelSpinVel

    def setZ(self, z):
        self.z = z

    def setZD(self):
        self.z = self.getFloatD('z')

    def getZ(self):
        return self.z

    def normalize_obs(self):
        """Normalizes the values of the observation to between 0 and 1"""
        PI = 3.14159265359
        self.angle = (self.angle + PI) / (2 * PI)
        self.damage = self.damage / 10000
        self.focus = [sensor / 200 for sensor in self.focus]
        self.fuel = self.fuel / 100
        self.gear = (self.gear + 1) / 7
        self.opponents = [opponent / 200 for opponent in self.opponents]
        self.rpm = self.rpm / 10000
        self.speedX = (self.speedX + 300) / 600
        self.speedY = (self.speedX + 300) / 600
        self.speedZ = (self.speedZ + 300) / 600
        self.track = [(sensor / 200) + 0.005 for sensor in self.track]
        self.trackPos = (self.trackPos + 10) / 20
        self.wheelSpinVel = [(spin + 300) / 600 for spin in self.wheelSpinVel]

    def get_obs(self, angle=None, curLapTime=None, damage=None,
                distFromStart=None, distRaced=None, fuel=None,
                gear=None, lastLapTime=None, opponents=None, racePos=None,
                rpm=None, speedX=None, speedY=None, speedZ=None, track=None,
                trackPos=None, wheelSpinVel=None, z=None, focus=None, x=None,
                y=None, roll=None, pitch=None, yaw=None, speedGlobalX=None,
                speedGlobalY=None):
        my_dict = {"angle": [], "curLapTime": [], "damage": [],
                   "distFromStart": [], "distRaced": [], "fuel": [],
                   "gear": [], "lastLapTime": [], "opponents": [], "racePos": [],
                   "rpm": [], "speedX": [], "speedY": [], "speedZ": [], "track": [],
                   "trackPos": [], "wheelSpinVel": [], "z": [], "focus": [], "x": [],
                   "y": [], "roll": [], "pitch": [], "yaw": [], "speedGlobalX": [],
                   "speedGlobalY": []};
        """Return the specified values in a numpy array"""
        obs = np.array([])
        if angle:
            obs = np.append(obs, self.angle)
            my_dict["angle"].append(self.angle)
        if curLapTime:
            obs = np.append(obs, self.curLapTime)
            my_dict["curLapTime"].append(self.curLapTime)
        if damage:
            obs = np.append(obs, self.damage)
            my_dict["damage"].append(self.damage)
        if distFromStart:
            obs = np.append(obs, self.distFromStart)
            my_dict["distFromStart"].append(self.distFromStart)
        if distRaced:
            obs = np.append(obs, self.distRaced)
            my_dict["distRaced"].append(self.distRaced)
        if fuel:
            obs = np.append(obs, self.fuel)
            my_dict["fuel"].append(self.fuel)
        if gear:
            obs = np.append(obs, self.gear)
            my_dict["gear"].append(self.gear)
        if lastLapTime:
            obs = np.append(obs, self.lastLapTime)
            my_dict["lastLapTime"].append(self.lastLapTime)
        if opponents:
            obs = np.append(obs, self.opponents)
            my_dict["opponents"].append(self.opponents)
        if racePos:
            obs = np.append(obs, self.racePos)
            my_dict["racePos"].append(self.racePos)
        if rpm:
            obs = np.append(obs, self.rpm)
            my_dict["rpm"].append(self.rpm)
        if speedX:
            obs = np.append(obs, self.speedX)
            my_dict["speedX"].append(self.speedX)
        if speedY:
            obs = np.append(obs, self.speedY)
            my_dict["speedY"].append(self.speedY)
        if speedZ:
            obs = np.append(obs, self.speedZ)
            my_dict["speedZ"].append(self.speedZ)
        if track:
            obs = np.append(obs, self.track)
            my_dict["track"].append(self.track)
        if trackPos:
            obs = np.append(obs, self.trackPos)
            my_dict["trackPos"].append(self.trackPos)
        if wheelSpinVel:
            obs = np.append(obs, self.wheelSpinVel)
            my_dict["wheelSpinVel"].append(self.wheelSpinVel)
        if z:
            obs = np.append(obs, self.z)
            my_dict["z"].append(self.z)
        if focus:
            obs = np.append(obs, self.focus)
            my_dict["focus"].append(self.focus)
        if x:
            obs = np.append(obs, self.x)
            my_dict["x"].append(self.x)
        if y:
            obs = np.append(obs, self.y)
            my_dict["y"].append(self.y)
        if roll:
            obs = np.append(obs, self.roll)
            my_dict["roll"].append(self.roll)
        if pitch:
            obs = np.append(obs, self.pitch)
            my_dict["pitch"].append(self.pitch)
        if yaw:
            obs = np.append(obs, self.yaw)
            my_dict["yaw"].append(self.yaw)
        if speedGlobalX:
            obs = np.append(obs, self.speedGlobalX)
            my_dict["speedGlobalX"].append(self.speedGlobalX)
        if speedGlobalY:
            obs = np.append(obs, self.speedGlobalY)
            my_dict["speedGlobalY"].append(self.speedGlobalY)
        return my_dict
