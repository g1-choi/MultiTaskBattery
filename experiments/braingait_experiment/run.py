# Main Script for an example experiment
import sys

# sys.path.append('../../../MultiTaskBattery/')
sys.path.insert(0,
                '/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML/Projects/BrainGaitProject/MultiTaskBattery/')

import MultiTaskBattery.experiment_block as exp_block
import constants as const


def main(subj_id):
    """ Main experiment function.
    Ensure the constants.py file is updated before running the experiment
    (e.g., experiment name, eye tracker, screen settings, etc.).

    Args:
        subj_id (str): Subject ID
    """
    # sys.path.insert(0,
    # '/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML
    # /Projects/BrainGaitProject/MultiTaskBattery')
    my_Exp = exp_block.Experiment(const, subj_id=subj_id)
    #while True:
    my_Exp.confirm_run_info()#when run_info window is up, click cancel in
    # the dialog or press ESC will quit the program
    #have user enter this info only once, next one auto populate and jsut
    # continue, if in full screen mode, we won't have access to this run_info
    # popup once the main experiment window is shown
    my_Exp.init_run()
    my_Exp.run()
    return


if __name__ == "__main__":
    main('subject-00') #need to have this as a default value to get us
    # started, otherwise will error out
