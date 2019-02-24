### load/save files, file dialogs and all that
import numpy as np
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

def add_filters(dialog):
    filter_npz = Gtk.FileFilter()
    filter_npz.set_name("compressed numpy file .npz")
    filter_npz.add_pattern("*.npz")
    dialog.add_filter(filter_npz)
    ##
    filter_any = Gtk.FileFilter()
    filter_any.set_name("all files")
    filter_any.add_pattern("*")
    dialog.add_filter(filter_any)

def onTimeout():
    Gtk.main_quit()
    return False
    
def fileChooser(save):
    ## response variables here
    response = None
    fName = None
    ##
    if save:
        dialog = Gtk.FileChooserDialog("File to save the current world:", gtkRootWin,
                                       Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        dialog.set_do_overwrite_confirmation(True)
        dialog.set_current_name("crazy-world.npz")
    else:
        dialog = Gtk.FileChooserDialog("World to load:", gtkRootWin,
                                       Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
    add_filters(dialog)
    dialog.connect("destroy", Gtk.main_quit)
    ##
    response = dialog.run()
    fName = dialog.get_filename()
    dialog.destroy()
    ##
    GLib.timeout_add(100, onTimeout)
    Gtk.main()
    return response, fName

def loadWorld():
    response, fName = fileChooser(False)
    if response == Gtk.ResponseType.OK:
        s = np.load(fName)
        return s
    else:
        # cancel pressed
        return None
        
def saveWorld(world, home, stuff):
    response, fName = fileChooser(True)
    if response == Gtk.ResponseType.OK:
        np.savez_compressed(fName,
                            world=world,
                            home = np.array(home),
                            stuff = np.array([x for x in stuff.items()]))

## Global window
gtkRootWin = Gtk.Window(title="File chooser GTK parent")
gtkRootWin.connect("destroy", Gtk.main_quit)
gtkRootWin.hide()
