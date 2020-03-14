# --------------------------------------------------------------
#  setProjectSettings.py
#  Version: 0.3.0
#  Last Updated: March 14th 2020
#  Tested on Windows Nuke 11.2v4
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
        # -----------------------------------------------------------------------------------------------------------------------------------------
        # GATHER INFORMATION ABOUT THE USER SELECTED NODE
        # -----------------------------------------------------------------------------------------------------------------------------------------
        # check if the selected node is a read
        if n[0].Class() == 'Read':
            read = n[0]

            # get the frame range
            fr_first = str(int(read['first'].getValue()))
            fr_last = str(int(read['last'].getValue()))

            # get the resolution 
            res_width = read.width()
            res_height = read.height()

            # get pixel aspect ratio
            pixel_aspect = read.pixelAspect()

            # get current format string
            current_proj_format = nuke.knob('root.format')

            # create format string
            new_proj_format = '%s %s 0 0 %s %s %s' % (res_width, res_height, res_width, res_height, pixel_aspect)
        # -----------------------------------------------------------------------------------------------------------------------------------------


        # -----------------------------------------------------------------------------------------------------------------------------------------
        # CREATE A LIST OF ALL CURRENTLY LOADED ROOT FORMATS
        # -----------------------------------------------------------------------------------------------------------------------------------------
            # get a list of all currently loaded formats
            # one list has all information except for the name, the other has all information including the name of the format
            nameless_format_list = []
            named_format_list = []

            # get a list of all the loaded nuke formats
            scriptFormats = nuke.formats()

            # loop for all formats to add entries to the lists containing resolution, asepct ratio, and name (for the named list only)
            for f in scriptFormats:
                new_nameless = '%s %s 0 0 %s %s %s' % (f.width(), f.height(), f.width(), f.height(), f.pixelAspect())
                new_named = '%s %s 0 0 %s %s %s %s' % (f.width(), f.height(), f.width(), f.height(), f.pixelAspect(), f.name())
                nameless_format_list.append(new_nameless)
                named_format_list.append(new_named)
        # -----------------------------------------------------------------------------------------------------------------------------------------


        # -----------------------------------------------------------------------------------------------------------------------------------------
        # CHECK IF THE INCOMING FORMAT IS ALREADY IN THE LOADED LIST OF FORMATS
        # -----------------------------------------------------------------------------------------------------------------------------------------
            # loop through each entry inthe nameless list
            for i in range(len(nameless_format_list)):

                # if an entry in the nameless list matches the project format from the selected read node
                # and if that entry does not contain the text 'None' at the end
                if nameless_format_list[i] == new_proj_format and re.search('None$', named_format_list[i]) == None:
                    #print '\nnew_proj_format: %s\nnamless0%s: %s\nnamed0%s: %s\nregex: %s' % (new_proj_format, i, nameless_format_list[i], i, named_format_list[i], re.search('None$', named_format_list[i]))

                    # confirm with the user that all the settings are correct
                    askMessage = 'frame range: <b>%s-%s</b>\n\nfull size format: <b>%sx%s %s</b>\n\nConfirm?' % (fr_first, fr_last, res_width, res_height, pixel_aspect)
                    if nuke.ask(askMessage):

                        # set the project format to the new project format
                        nuke.knob('root.format', new_proj_format)

                        # set the frist/last frame
                        nuke.knob('root.first_frame', fr_first)
                        nuke.knob('root.last_frame', fr_last)
                        return
                    else:
                        return
        # -----------------------------------------------------------------------------------------------------------------------------------------


        # -----------------------------------------------------------------------------------------------------------------------------------------
        # PROMT THE USER TO CREATE A NEW ROOT FORMAT
        # -----------------------------------------------------------------------------------------------------------------------------------------
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
                askMessage = 'frame range: <b>%s-%s</b>\n\nfull size format: <b>%sx%s %s</b>\n\nConfirm?' % (fr_first, fr_last, res_width, res_height, pixel_aspect)
                if nuke.ask(askMessage):
                    # set the project format to the new project format
                    nuke.knob('root.format', new_proj_format)

                    # set the frist/last frame
                    nuke.knob('root.first_frame', fr_first)
                    nuke.knob('root.last_frame', fr_last)

                    return
                # if the user cancels, exit the script
                else:
                    return
        # -----------------------------------------------------------------------------------------------------------------------------------------


        # -----------------------------------------------------------------------------------------------------------------------------------------
        # CATCH THE USER SELECTING THE WRONG INPUTS
        # -----------------------------------------------------------------------------------------------------------------------------------------
        # wrong node class selected
        else: 
            nuke.message('You must select a read node')
    else: 
        # too many nodes selected 
        nuke.message('Select only one Read node')
        # -----------------------------------------------------------------------------------------------------------------------------------------

projectSettings()
