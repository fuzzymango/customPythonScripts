# --------------------------------------------------------------
#  setProjectSettings.py
#  Version: 0.1.0
#  Last Updated: March 2nd 2020
#  Tested on Nuke 11
# --------------------------------------------------------------
import nuke 
import nukescripts


'''
TO DO
- [x] lock frame range
- *DONE* ID non-square pixel aspect ratios and set project accordingly
- allow user to specify if they want to set frame range or resolution 
- new format resolution detected! Enter new format name: 
	- dialogue box when a new format is detected
'''

def projectSettings():
	# get selected node(s)
	try:
		n = nuke.selectedNodes()
	except:
		nuke.message('You must select a node')

	# see if there is only 1 node selected 
	if len(n) is 1: 
		# check if the selected node is a read
		if n[0].Class() == 'Read':
			read = n[0]

			# get the frame range
			fr_first = int(read['first'].getValue())
			fr_last = int(read['last'].getValue())

			# get the resolution 
			res_width = read.width()
			res_height = read.height()

			# get pixel aspect ratio
			pixel_aspect = read.pixelAspect()


			# set project framerange to read range
			nuke.knob('root.first_frame', str(fr_first))
			nuke.knob('root.last_frame', str(fr_last))

			# set project resoultion to read resolution
			proj_format = str(res_width) + ' ' + str(res_height) + ' ' + str(pixel_aspect)
			nuke.knob('root.format', proj_format)

			nuke.message('frame range: ' + str(fr_first) + '-' + str(fr_last) + '\nFull size format: ' + proj_format)
		else: 
			# wrong node class selected
			nuke.message('Wrong node class selected')
	else: 
		# too many nodes selected 
		nuke.message('Select only one node of class Read')

projectSettings()
