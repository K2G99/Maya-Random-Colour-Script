import random
import maya.cmds as cmds

selected_light = cmds.ls( selection=True)
my_light = selected_light[0]

colorR = random.random()
colorG = random.random()
colorB = random.random()
    
cmds.setAttr(f"{my_light}.color" , colorR , colorG , colorB, type = "double3")
