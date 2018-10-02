import pybullet
pybullet.connect(pybullet.DIRECT)
pybullet.resetSimulation()
import pybullet_data
pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
plane = pybullet.loadURDF("plane.urdf")
sphere = pybullet.loadURDF("sphere2.urdf", basePosition=[0,0,10])
pybullet.setGravity(0,0,-9.8)

pybullet.stepSimulation()
print(pybullet.getBasePositionAndOrientation(sphere))
pybullet.stepSimulation()
print(pybullet.getBasePositionAndOrientation(sphere))
pybullet.stepSimulation()
print(pybullet.getBasePositionAndOrientation(sphere))

pybullet.disconnect()

