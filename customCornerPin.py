# --------------------------------------------------------------
#  customCornerPinIS.py
#  Version: 1.4.1
#  Last Updated: July 5th, 2019
# --------------------------------------------------------------
# --------------------------------------------------------------
#  USAGE
#
#  Adds a checkbox which allows nuke to automatically set 
#  keyframes on corner pin points when the user creates a new
#  keyframe on any corner point
# --------------------------------------------------------------
# --------------------------------------------------------------
#  MENU.PY ADDITIONS
#  myGizmosMenu.addCommand('customCornerPin', 'nuke.createNode(\"customCornerPin\")', shortcutContext=2)
# --------------------------------------------------------------


# --------------------------------------------------------------
# GLOBAL IMPORTS
# --------------------------------------------------------------
import nuke
import nukescripts


# --------------------------------------------------------------
# CREATE GROUP NODE 
# --------------------------------------------------------------
cornerPin2D_grp = nuke.nodes.Group()
cornerPin2D_grp.setName('CornerPin2D')
cornerPin2D_grp.begin()

# create the input, output, and cornerPin nodes for the group
grp_input = nuke.createNode('Input')
cornerPin = nuke.createNode('CornerPin2D')
grp_output = nuke.createNode('Output')


# --------------------------------------------------------------
# GLOBAL VARIABLES
# --------------------------------------------------------------
# create cornerPin 'to' knobs
grp_to1 = nuke.XY_Knob('to1', 'to1')
grp_to2 = nuke.XY_Knob('to2', 'to2')
grp_to3 = nuke.XY_Knob('to3', 'to3')
grp_to4 = nuke.XY_Knob('to4', 'to4')

# add the knobs to a list
cornerPin_to_knobs = []
cornerPin_to_knobs.append(grp_to1)
cornerPin_to_knobs.append(grp_to2)
cornerPin_to_knobs.append(grp_to3)
cornerPin_to_knobs.append(grp_to4)

# create cornerPin 'to enable' knobs
grp_to1_enable = nuke.Boolean_Knob('grp_enable1', 'enable1')
grp_to2_enable = nuke.Boolean_Knob('grp_enable2', 'enable2')
grp_to3_enable = nuke.Boolean_Knob('grp_enable3', 'enable3')
grp_to4_enable = nuke.Boolean_Knob('grp_enable4', 'enable4')

# add the knobs to a list
cornerPin_to_enable_knobs = []
cornerPin_to_enable_knobs.append(grp_to1_enable)
cornerPin_to_enable_knobs.append(grp_to2_enable)
cornerPin_to_enable_knobs.append(grp_to3_enable)
cornerPin_to_enable_knobs.append(grp_to4_enable)



# --------------------------------------------------------------
# UPDATE GROUP GUI
# --------------------------------------------------------------
def update_group_gui():
	# return the current group context
	group_cornerPin = nuke.thisGroup()

	# add knobs from cornerPin_to_enable_knobs and cornerPin_to_knobs to the group GUI
	for i in range(0,4):
		# check to see if any of the 'toX' knobs exist, if not, add them to the GUI
		if not group_cornerPin.knob('to1') or not group_cornerPin.knob('to2') or not group_cornerPin.knob('to3') or not group_cornerPin.knob('to4'):
			# add 'to' knobs to the group GUI
			# this adds all the knobs to the group but returns a 'Runtimeerror: must specify a knob' error 
			group_cornerPin.addKnob(cornerPin_to_knobs[i])

		# check to see if the enable knobs exist, if not, add them to the GUI
		if not group_cornerPin.knob('enable1') or not group_cornerPin.knob('enable2') or not group_cornerPin.knob('enable3') or not group_cornerPin.knob('enable4'):
			# add 'enabled' knobs to group GUI
			# this adds all the checkboxes to the group but returns a 'Runtimeerror: must specify a knob' error 
			group_cornerPin.addKnob(cornerPin_to_enable_knobs[i])

		# set the values of the enabled checkboxes to the grouped cornerPin values
		grp_cornerPin_knob_enabled = 'enable' + str(i+1)
		cornerPin_to_enable_knobs[i].setValue(cornerPin[grp_cornerPin_knob_enabled].getValue())

		# set the values of the group knobs to the grouped cornerPin node values
		grp_cornerPin_knob_to = 'to' + str(i+1)
		cornerPin_to_knobs[i].setValue(cornerPin[grp_cornerPin_knob_to].getValue())


# --------------------------------------------------------------
# SET KNOB VALUES
# --------------------------------------------------------------
def set_knob_values():
	# find the cornerPin node within the group
	node_cornerPin = nuke.thisNode()
	# assign cornerPin 'to' fields to a variable
	cornerPin_to1 = node_cornerPin['to1']
	cornerPin_to2 = node_cornerPin['to2']
	cornerPin_to3 = node_cornerPin['to3']
	cornerPin_to4 = node_cornerPin['to4']

	# assign cornerPin 'from' fields to a variable
	cornerPin_from1 = node_cornerPin['from1']
	cornerPin_from2 = node_cornerPin['from2']
	cornerPin_from3 = node_cornerPin['from3']
	cornerPin_from4 = node_cornerPin['from4']

	# return the current group context
	group_cornerPin = nuke.thisGroup()

	# check to see if the auto_keyframing box is checked
	if group_cornerPin.knob('auto_keyframing') == True:
		# check to see if there is a keyframe of any of the 'to' knobs
		if cornerPin_to1.isKey() or cornerPin_to2.isKey() or cornerPin_to3.isKey() or cornerPin_to4.isKey():
			# save the current value of each to knob
			val_to1 = cornerPin_to1.getValue()
			val_to2 = cornerPin_to2.getValue()
			val_to3 = cornerPin_to3.getValue()
			val_to4 = cornerPin_to4.getValue()

			# check to see if there is no animation on any of the to knobs
			if not cornerPin_to1.isAnimated() or not cornerPin_to2.isAnimated() or not cornerPin_to3.isAnimated() or not cornerPin_to4.isAnimated():
				# add animation to the to knobs
				cornerPin_to1.setAnimated()
				cornerPin_to2.setAnimated()
				cornerPin_to3.setAnimated()
				cornerPin_to4.setAnimated()

			# set the value of the to knobs to the saved value
			cornerPin_to1.setValue(val_to1)
			cornerPin_to2.setValue(val_to2)
			cornerPin_to3.setValue(val_to3)
			cornerPin_to4.setValue(val_to4)

	update_group_gui()




# --------------------------------------------------------------
# ADD KNOBS TO GROUP NODE GUI
# --------------------------------------------------------------

update_group_gui()

# add copy from, remove key to, and auto keyframing knobs
grp_copy_from = nuke.PyScript_Knob('grp_copy_from', "Copy 'from'")
grp_copy_from.setFlag(nuke.STARTLINE)
# ADD BUTTON FUNCTIONALITY AND LOGIC HERE
cornerPin2D_grp.addKnob(grp_copy_from)

remove_key_to = nuke.PyScript_Knob('remove_key_to', "Remove key 'to'")
cornerPin2D_grp.addKnob(remove_key_to)

autokeyframing = nuke.Boolean_Knob('auto_keyframing', 'auto keyframing')
autokeyframing.setFlag(nuke.STARTLINE)
cornerPin2D_grp.addKnob(autokeyframing)




nuke.addKnobChanged(set_knob_values, nodeClass='CornerPin2D')
# end the group
cornerPin2D_grp.end()



