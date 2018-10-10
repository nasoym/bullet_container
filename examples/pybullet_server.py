import pybullet
import pybullet_data

from influxdb import InfluxDBClient

pybullet.connect(pybullet.DIRECT)
pybullet.resetSimulation()
pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
plane = pybullet.loadURDF("plane.urdf")
sphere = pybullet.loadURDF("sphere2.urdf", basePosition=[0,0,10])
pybullet.setGravity(0,0,-9.8)

influxclient = InfluxDBClient('influxdb', 8086)
influxclient.create_database('points')

while True:
	pybullet.stepSimulation()
	point=pybullet.getBasePositionAndOrientation(sphere)
	influxclient.write_points([{"measurement":"points","tags":{"id":sphere},"fields":{"x":point[0][0],"y":point[0][1],"z":point[0][2]}}],database="points")

#pybullet.disconnect()
#influxclient.close()

