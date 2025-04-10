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
    totalRun = 2 #hard code this

    my_Exp.confirm_run_info()#when run_info window is up, click cancel in
    # the dialog or press ESC will quit the program
    #have user enter this info only once, next one auto populate and jsut
    # continue, if in full screen mode, we won't have access to this run_info
    # popup once the main experiment window is shown
    my_Exp.init_run()
    my_Exp.run()

    #if for some reason, the run didn't go as planned and we had to quit the
    # program halfway and you only want to do 1 more run isntead of 2 full
    # runs, change this number to 3, then call run.py again, this will avoid
    # going into the while loop again.
    nextRunNum = 2#if ran to this line, means run_info entered
    # successfully and ran through it once already

    while nextRunNum <= totalRun:
        #leave subj ID and wait for TTL unchanged, auto increment run
        # number and file name
        my_Exp.run_number = my_Exp.run_number +1      # auto increment by 1
        my_Exp.run_filename = f'run_{my_Exp.run_number:02d}.tsv'
        # assume file format is always run_xx.tsv
        my_Exp.init_run()
        my_Exp.run()
        nextRunNum  = nextRunNum + 1 #increment by 1, will run till
        # total run is complete
    return


if __name__ == "__main__":
    main('subject-00') #need to have this as a default value to get us
    # started, otherwise will error out
