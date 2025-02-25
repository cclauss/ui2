""" A module that builds on Pythonista's `ui` module """

# Dump ui into namespace so that `import ui2` can be used interchangably with
# `import ui`
from ui import *

# Load subpackages
from ui2.shapes import *
from ui2.ui_io import *
import ui2.path_helpers as pathutil

# Load replacements for ui functions
from ui2.animate import *
from ui2.transition import *
from ui2.delay import *

# Load view classes
from ui2.view_classes.PathView import PathView
from ui2.view_classes.ProgressPathView import ProgressPathView
from ui2.view_classes.BlurView import BlurView
