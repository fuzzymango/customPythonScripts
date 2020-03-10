# --------------------------------------------------------------
#  setProjectSettings.py
#  Version: 0.1.1
#  Last Updated: March 10th 2020
#  Tested on Nuke 11
# --------------------------------------------------------------
import nuke 
import nukescripts


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

			# get current format string
			current_proj_format = nuke.knob('root.format')

			# create format string
			#new_proj_format = str(res_width) + ' ' + str(res_height) + ' 0 0 ' + str(res_width) + ' ' + str(res_height) + str(pixel_aspect)
			new_proj_format = '%s %s 0 0 %s %s %s' % (res_width, res_height, res_width, res_height, pixel_aspect)

			# get a list of all currently loaded formats
			format_list = []
			scriptFormats = nuke.formats()
			for f in scriptFormats:
			    new = '%s %s 0 0 %s %s %s' % (f.width(), f.height(), f.width(), f.height(), f.pixelAspect())
			    format_list.append(new)


			# check to see if the new project format matches a current project format
			for i in format_list:
				print '\n%s \n%s\n' % (i, new_proj_format)
				# if there's a match, set the project format and display the completion message
				if i == new_proj_format:
					# set the project format to i
					nuke.knob('root.format', i)

					# set the frist/last frame
					nuke.knob('root.first_frame', str(fr_first))
					nuke.knob('root.last_frame', str(fr_last))

					# set pixel aspect


					# display to the user how the format will be set
					nuke.message('frame range: ' + str(fr_first) + '-' + str(fr_last) + '\nFull size format: ' + new_proj_format)
					break

			# if there is not a match, request the user to enter a name for the new format
				else: 
					# prompt user to enter name of new format and save that as a string called txt
					messageText = 'New format detected! Enter a name for the new format'
					txt = nuke.getInput(messageText, 'new_format')

					# check to see if the user left the field blank
					if txt is '':
						nuke.message('give your format a name')
						break
					else: 
						# append the name of the new project format 
						new_proj_format = new_proj_format + ' ' + txt

						# confirm with the user that all the settings are correct
						askMessage = 'frame range: %s - %s\nFull size format: %s\nConfirm?' % (fr_first, fr_last, new_proj_format)
						if nuke.ask(askMessage):
							# set the project format to the new project format
							nuke.knob('root.format', new_proj_format)

							# set the frist/last frame
							nuke.knob('root.first_frame', str(fr_first))
							nuke.knob('root.last_frame', str(fr_last))

							break
						# if the user cancels, exit the script
						else:
							break

			# wrong node class selected
			nuke.message('Wrong node class selected')
	else: 
		# too many nodes selected 
		nuke.message('Select only one Read node')

projectSettings()
