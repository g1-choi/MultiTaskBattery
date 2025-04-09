# Main Script for an example experiment
import sys

# sys.path.append('../../../MultiTaskBattery/')
sys.path.insert(0,
                '/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML/Projects/BrainGaitProject/MultiTaskBattery/')

import MultiTaskBattery.experiment_block as exp_block
import constants_rest as const #this will import first found on the search path,
# which i'm unsure which one will be imported, maybe it prioritize things in
# the same folder first?
from psychopy import event

def main(subj_id):
    """ Main experiment function to run a resting-state scan. The screen
    will display a white cross with black background, and wait for a space
    key press, when space is pressed. The system will quit.
    There is no data/participant response to record, so the run/subject info is
    technically not needed.

    Args:
        subj_id (str): Subject ID
    """
    # sys.path.insert(0,
    # '/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML
    # /Projects/BrainGaitProject/MultiTaskBattery')
    my_Exp = exp_block.Experiment(const, subj_id=subj_id)
    my_Exp.screen.fixation_cross()

    spacePressed = False
    while not spacePressed: #run at least once
        #show the cross untill space key is pressed
        while not spacePressed:
            keys = event.getKeys(['space'])  # look for space presses
            if 'space' in keys:
                spacePressed = True  # quit the while loop and quit experiment
    return

if __name__ == "__main__":
    main('subject-00') #need to have this as a default value to get us
    # started, otherwise will error out
    #a default ID is needed to start the Experiment object
