# --------------------------------------------------------------
#  customCornerPinIS.py
#  Version: 1.4.0
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
# ADD KNOBS TO GROUP NODE GUI
# --------------------------------------------------------------
# create cornerPin 'to' knobs
grp_to1 = nuke.XY_Knob('to1', 'to1')
grp_to2 = nuke.XY_Knob('to2', 'to2')
grp_to3 = nuke.XY_Knob('to3', 'to3')
grp_to4 = nuke.XY_Knob('to4', 'to4')

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

cornerPin_to_enable_knobs = []
cornerPin_to_enable_knobs.append(grp_to1_enable)
cornerPin_to_enable_knobs.append(grp_to2_enable)
cornerPin_to_enable_knobs.append(grp_to3_enable)
cornerPin_to_enable_knobs.append(grp_to4_enable)

# add 'to' and 'enable' knobs to group node GUI
for i in range(0,4):
	# add 'to' knobs to group GUI and set their values to the 'to' knob of the cornerPin node
	cornerPin2D_grp.addKnob(cornerPin_to_knobs[i])
	grp_cornerPin_knob_to = 'to' + str(i+1)
	cornerPin_to_knobs[i].setValue(cornerPin[grp_cornerPin_knob_to].getValue())

	# add the 'enabled' knobs to group GUI and set their values to enabled
	cornerPin2D_grp.addKnob(cornerPin_to_enable_knobs[i])
	grp_cornerPin_knob_enabled = 'enable' + str(i+1)
	cornerPin_to_enable_knobs[i].setValue(cornerPin[grp_cornerPin_knob_enabled].getValue())

	i += 1


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





# end the group
cornerPin2D_grp.end()



