# --------------------------------------------------------------
#  customCornerPinIS.py
#  Version: 1.0.1
#  Last Updated: June 24th, 2019
# --------------------------------------------------------------

'''
MENU.PY ADDITIONS
from customCornerPinIS import *
nuke.addOnUserCreate(createCheckBox, nodeClass='CornerPin2D')
'''
import nuke
import nukescripts



def customCornerPin():
	cornerPin = nuke.thisNode()
	cornerPin_to1 = cornerPin['to1']
	cornerPin_to2 = cornerPin['to2']
	cornerPin_to3 = cornerPin['to3']
	cornerPin_to4 = cornerPin['to4']

	print cornerPin['auto_keyframing'].getValue()

	if cornerPin['auto_keyframing']:
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
	
	nuke.addKnobChanged(customCornerPin, nodeClass='CornerPin2D')
