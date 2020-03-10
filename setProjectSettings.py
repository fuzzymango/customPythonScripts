# --------------------------------------------------------------
#  setProjectSettings.py
#  Version: 0.2.2
#  Last Updated: March 10th 2020
#  Tested on Nuke 11
# --------------------------------------------------------------
import nuke 
import nukescripts
import re

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
			new_proj_format = '%s %s 0 0 %s %s %s' % (res_width, res_height, res_width, res_height, pixel_aspect)

			# get a list of all currently loaded formats
			nameless_format_list = []
			named_format_list = []
			scriptFormats = nuke.formats()
			for f in scriptFormats:
			    new_nameless = '%s %s 0 0 %s %s %s' % (f.width(), f.height(), f.width(), f.height(), f.pixelAspect())
			    new_named = '%s %s 0 0 %s %s %s %s' % (f.width(), f.height(), f.width(), f.height(), f.pixelAspect(), f.name())
			    nameless_format_list.append(new_nameless)
			    named_format_list.append(new_named)


			# check to see if the new project format matches a current project format
			for i in nameless_format_list:
				print '\ni: %s \nnew format: %s\n' % (i, new_proj_format)
				# if there's a match, set the project format and display the completion message
				# if i = new project format and i does not contain any letters
				print 'regex: %s\ni: %s' % (re.search('[a-zA-Z]', i), i)
				if i == new_proj_format and re.search('[a-zA-Z]', named_format_list[named_format_list.index(i)]):
						# confirm with the user that all the settings are correct
						askMessage = 'frame range: %s - %s\nFull size format: %s\nConfirm?' % (fr_first, fr_last, new_proj_format)
						if nuke.ask(askMessage):
							# set the project format to the new project format
							nuke.knob('root.format', new_proj_format)

							# set the frist/last frame
							nuke.knob('root.first_frame', str(fr_first))
							nuke.knob('root.last_frame', str(fr_last))
							
							return
						else:
							return


			# if there is not a match, request the user to enter a name for the new format
			# prompt user to enter name of new format and save that as a string called txt
			messageText = 'New format detected! Enter a name for the new format'
			txt = nuke.getInput(messageText, 'new_format')

			# check to see if the user left the field blank
			if txt is '':
				message = nuke.message('give your format a name')

				return
			else: 
				# append the name of the new project format
				try:
					new_proj_format = new_proj_format + ' ' + txt
				# catch a type error that throws when the user cancels the format name box
				except TypeError as e:
					return

				# confirm with the user that all the settings are correct
				askMessage = 'frame range: %s - %s\nFull size format: %s\nConfirm?' % (fr_first, fr_last, new_proj_format)
				if nuke.ask(askMessage):
					# set the project format to the new project format
					nuke.knob('root.format', new_proj_format)

					# set the frist/last frame
					nuke.knob('root.first_frame', str(fr_first))
					nuke.knob('root.last_frame', str(fr_last))

					return
				# if the user cancels, exit the script
				else:
					return

			# wrong node class selected
			nuke.message('Wrong node class selected')
	else: 
		# too many nodes selected 
		nuke.message('Select only one Read node')

projectSettings()
