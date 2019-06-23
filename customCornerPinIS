# --------------------------------------------------------------
#  customCornerPinIS.py
#  Version: 1.0.0
#  Last Updated: June 23th, 2019
# --------------------------------------------------------------

'''
MENU.PY ADDITIONS
from customCornerPinIS import *
nuke.addOnUserCreate(createCheckBox, nodeClass='CornerPin2D')
nuke.addKnobChanged(customCornerPin, createCheckBox, nodeClass='CornerPin2D')
'''
import nuke
import nukescripts






def myFunction():
	count = 0
	while checkBox.getValue() == 1:
		nuke.createNode('Blur')
		print 'box is checked'
		if count == 3:
			break
		count += 1

	val = 0
	while checkBox.getValue() == 0:
		nuke.createNode('Grade')
		print 'box is not checked'
		if val == 3:
			break
		val += 1


def customCornerPin(boolBox):
	cornerPin = nuke.thisNode()
	cornerPin_to1 = cornerPin['to1']
	cornerPin_to2 = cornerPin['to2']
	cornerPin_to3 = cornerPin['to3']
	cornerPin_to4 = cornerPin['to4']

	if boolBox == True:
		if cornerPin_to1.isAnimated() or cornerPin_to2.isAnimated() or cornerPin_to3.isAnimated() or cornerPin_to4.isAnimated():
			# check to see if a new keyframe is created, and if so, key the other 3 knobs
			if cornerPin_to1.isKey():
				cornerPin_to2.setValue(cornerPin_to2.getValue())
				cornerPin_to3.setValue(cornerPin_to3.getValue())
				cornerPin_to4.setValue(cornerPin_to4.getValue())
			if cornerPin_to2.isKey():
				cornerPin_to1.setValue(cornerPin_to1.getValue())
				cornerPin_to3.setValue(cornerPin_to3.getValue())
				cornerPin_to4.setValue(cornerPin_to4.getValue())
			if cornerPin_to3.isKey():
				cornerPin_to1.setValue(cornerPin_to1.getValue())
				cornerPin_to2.setValue(cornerPin_to2.getValue())
				cornerPin_to4.setValue(cornerPin_to4.getValue())
			if cornerPin_to4.isKey():
				cornerPin_to1.setValue(cornerPin_to1.getValue())
				cornerPin_to2.setValue(cornerPin_to2.getValue())
				cornerPin_to3.setValue(cornerPin_to3.getValue())

			else: 
				print 'no key was created'

def createCheckBox():
	cornerPin = nuke.thisNode()
	checkBox = nuke.Boolean_Knob('auto_keyframing', 'auto keyframing')
	if cornerPin.knob('checkBox'):
		return
	else:
		cornerPin.addKnob(checkBox)

	return checkBox
