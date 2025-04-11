# Main Script for an example experiment
import sys

# sys.path.append('../../../MultiTaskBattery/')
sys.path.insert(0,
                '/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML/Projects/BrainGaitProject/MultiTaskBattery/')

import MultiTaskBattery.experiment_block as exp_block
import constants_practice as const
from psychopy import visual,event,gui
import string

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

    #practice them in order
    tasks = ['movie', 'action_observation','auditory_narrative', 'verb_generation', 'spatial_navigation',
             'flexion_extension','contract_relax_glutes','finger_sequence',
             'sentence_reading', 'visual_search', 'semantic_prediction',
             'n_back','oddball','theory_of_mind']

    my_Exp = exp_block.Experiment(const, subj_id=subj_id)
    # #give a GUI to ask if want to do 1 task at a time or do a full run through?
    # # a dialog box pops up so you can enter info
    # # Set up input box
    # #TODO: this is not enough, bc it will display trial feedback at the end of
    # # each one, we want it to move on. So easiest to just do an actual run
    # inputDlg = gui.Dlg(title=f"{my_Exp.exp_name}")
    # inputDlg.addField('Run 1 task at a time?',
    #                   initial=True)  # a checkbox for ttl pulse (set it true for scanning)
    # inputDlg.show()
    #
    # if inputDlg.OK:
    #     practice1AtATime = bool(inputDlg.data[0])
    # else:
    #     sys.exit()

    my_Exp.confirm_run_info()#when run_info window is up, click cancel in
    # the dialog or press ESC will quit the program

    # find out which task we are starting from, using the file name, remove
    # starting tag, ending digits and tsv, then check index within the tasks
    # list.
    rmvDigits = str.maketrans('', '', string.digits)
    curTaskName = my_Exp.run_filename  # in format
    # practice_run_##_oddball.tsv
    curTaskName = curTaskName.translate(rmvDigits)  # now will be practice_run__oddball.tsv
    curTaskName = curTaskName.replace("practice_run__","")  # now will be oddball.tsv
    curTaskName = curTaskName.replace(".tsv", "")  # now will be oddball
    nextTaskIdx = tasks.index(curTaskName)

    while nextTaskIdx < len(tasks):
        my_Exp.init_run()
        my_Exp.run(isPractice=True)

        # if practice1AtATime:
        # now give a screen to ask if want to repeat or continue?
        instr_visual = visual.TextStim(my_Exp.screen.window,
                                       text=f"Continue to next task: \npress "
                                            f"-> (right arrow key)\nRepeat "
                                            f"this task "
                                            f"again:\n"
                                            f"press <- (left arrow key)",
                                       color=[-1, -1, -1])
        # instr.size = 0.8
        instr_visual.draw()
        my_Exp.screen.window.flip()
        # then set up the run info accordingly, always increment run-number
        # for repeat of the same task, or keep run# to 1 for first try of a
        # new task.
        keyPressed = False
        while not keyPressed:
            keys = event.getKeys(['left', 'right'])  # look for space presses
            if keys:  # if not empty, something is pressed
                keyPressed = True

        if 'right' in keys:
            # set up run info for next task
            nextTaskIdx += 1  # increment to laod next task now
            my_Exp.run_number = 1  # reset to 1
            # restart at run05 randomization order for the next task.
            my_Exp.run_filename = f'practice_run_05' \
                                  f'_{tasks[nextTaskIdx]}.tsv'
        elif 'left' in keys:
            # Otherwise stay at the same task and increment run number
            my_Exp.run_number = my_Exp.run_number + 1
            # make the file and run-number independent, always loop
            # through file 5-9 for each repeat regardless of the current
            # run number, and restart from 5 again if more repeats are
            # needed.
            curFileDigits = [c for c in my_Exp.run_filename if c.isdigit()]
            curFileDigits = int("".join(curFileDigits))
            curFileDigits = (curFileDigits+1) % 5 + 5 #bound it to
            # between[5,9] and start from 6 (1st repeat will be run_06)
            my_Exp.run_filename = f'practice_run_{curFileDigits:02d}' \
                                  f'_{tasks[nextTaskIdx]}.tsv'
            #do the same task but go to next digits

        # else: #full run thorugh, always auto increment to next one
        #     nextTaskIdx += 1
        #     # my_Exp.run_number = 5 #run number 5 will use stimulus 9 #keep
        #     # using the same run number
        #     my_Exp.run_filename = f'practice_run_09' \
        #                       f'_{tasks[nextTaskIdx]}.tsv'
        #     #for run through always use order 09

    return


if __name__ == "__main__":
    main('subject-00') #need to have this as a default value to get us
    # started, otherwise will error out
