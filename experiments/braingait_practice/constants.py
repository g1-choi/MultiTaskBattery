# constants.py defines parameters and settings for an experiment
# it is passed to the Experiment class on initialization
from pathlib import Path
import os
import MultiTaskBattery as mtb

#Necessary definitions for the experiment:
exp_name = 'braingait_practice' # name of the experiment

#UNCOMMENT THIS FOR SCANNING
response_keys    = ['1', '2', '3', '4'] # scanner keys for right hand

#COMMENT THIS FOR SCANNING
#response_keys    = ['a', 's', 'd', 'f']

#not used
response_fingers = ['Pinky', 'Ring','Middle', 'Index']

# Directory definitions for experiment
exp_dir = Path(os.path.dirname(os.path.realpath(__file__)))   # where the
# experiment code is stored, 1 directory above this file
task_dir = exp_dir / "practice_task_files"  # contains target files for the task
run_dir    = exp_dir / "practice_run_files"     # contains run files for each
# session
data_dir   = exp_dir / "practice_data"          # This is where the result files
# are
# being saved

# do run_file_name as a formated string, start with run 05 bc the randomized
# tasks are randomized run 5 and 6 (the stimulus sometimes are generated
# based on run-number, this avoids using same stimulus as the actual scanner
# task)
default_run_filename = 'practice_run_05.tsv'

# This is were the stimuli for the different task are stored, 2 directories
# above this files
package_dir = Path(os.path.dirname(os.path.dirname(os.path.realpath(mtb.__file__))))
stim_dir   = package_dir / "stimuli"

# Is the Eye tracker being used?
eye_tracker = False                                     # do you want to do  eyetracking?

# Running in debug mode?
debug = False                                           # set to True for
# debugging, set to true won't show the dialog for you to enter subject info

# Screen settings for subject display
screen = {}
screen['size'] = [1024, 768]        # screen resolution
screen['fullscr'] = False           # full screen, if false it's in a separate
# window
screen['number'] = 1                # 0 = main display, 1 = secondary display
