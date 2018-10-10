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

pybullet.stepSimulation()
print(pybullet.getBasePositionAndOrientation(sphere))
influxclient.write_points([{"measurement":"foo","tags":{"id":"123"},"fields":{"x":4,"y":5}}],database="points")

