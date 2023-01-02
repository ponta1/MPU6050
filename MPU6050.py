import serial
import sys
from direct.showbase.ShowBase import ShowBase

COM_PORT = "COM5"
COM_SPEED = 115200

serial_rcv = ""     # シリアルで受信したデータ

class Gyro3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.cube = self.loader.loadModel("models/misc/rgbCube")
        self.cube.reparentTo(self.render)
        self.cube.setScale(1, 1, 1)
        self.cube.setPos(0, 10, 0)
        self.cube.setHpr(45, 0, 45) # yaw, pitch. roll
        self.taskMgr.add(self.cubeMotionTask, "CubeMotionTask")

        try:
            self.ser = serial.Serial(COM_PORT, COM_SPEED)
        except IOError:
            print("COMポートが開けません:" + COM_PORT)
            sys.exit()

    def cubeMotionTask(self, task):
        global serial_rcv
        #self.cube.setHpr(45, 0, task.time * 10) # yaw, pitch. roll

        # シリアルの受信
        while self.ser.in_waiting > 0:
            rcv = self.ser.read(1)
            if rcv != b'\r' and rcv != b'\n':
                serial_rcv = serial_rcv + rcv.decode('utf-8')
            if rcv == b'\n':
                #print("RECV:" + serial_rcv)
                rpy = serial_rcv.split(',')
                if len(rpy) == 3:
                    roll = float(rpy[0])
                    pitch = float(rpy[1])
                    yaw = float(rpy[2])
                    #print(str(roll) + " " + str(pitch) + " " + str(yaw))
                    self.cube.setHpr(yaw, pitch, roll) # yaw, pitch. roll
                serial_rcv = ""
                break

        return task.cont

gyro3d = Gyro3D()
gyro3d.run()
