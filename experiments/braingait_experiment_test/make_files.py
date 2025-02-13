import sys
# sys.path.insert(0,'../../../MultiTaskBattery/') #didn't work
sys.path.insert(0,'/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML/Projects/BrainGaitProject/MultiTaskBattery/')
import MultiTaskBattery.task_file as tf
import MultiTaskBattery.utils as ut
import constants as const

tasks = ['n_back', 'action_observation','finger_sequence',
        'verb_generation', 'spatial_navigation','nonword_reading','demand_grid',
         'flexion_extension','visual_search','sentence_reading',
         'rest']
#things that we would like to have but doesn't seem to be there: arithmatic,
# n_back_verbal, n_back_pic (this might be the same as the currenet n_back?)

num_runs = 2  # Number of imaging runs

# Ensure task and run directories exist
ut.dircheck(const.run_dir)
for task in tasks:
    ut.dircheck(const.task_dir / task)

# run file is a tsv file containing: task_name: Name of the task - task_code:
# short name of the task - task_file: Name of the task file for this run -
# instruction_dur: Duration of the instruction screen before the task starts (in seconds)
# - start_time: Start time of the task (in seconds from the start of the run)
# - end_time: End time of the task (in seconds)

# Task Files Task files that specify the structure of the tasks within each
# run (e.g. the stimuli, the correct response, whether to display feedback,
# etc.).
#
# The task file can look very different, but typically  contains some of the
# following columns:
# trial_num: Trial number
# hand: Hand used for the task (left or right)
# trial_dur: Duration of the trial (in seconds)
# iti_dur: Inter-trial interval duration (in seconds)
# stim: Stimulus presented
# display_trial_feedback: Whether to display feedback after each trial
# start_time: Start time of the trial (in seconds)
# end_time: End time of the trial (in seconds)
# Key columns, for example in the case of four response keys (e.g. in the
# RMET task or Finger Sequence task): - key_one: Key for the first option -
# key_two: Key for the second option - key_three: Key for the third option -
# key_four: Key for the fourth option
# some of the tasks require run number because the stimuli depend on the run
# number (e.g., movie clips have a specific order for each run)

# Generate run and task files
for r in range(1, num_runs+1): #python is 0 indexing
    tfiles = [f'{task}_{r:02d}.tsv' for task in tasks]
    T = tf.make_run_file(tasks, tfiles, instruction_dur=15)
    T.to_csv(const.run_dir / f'run_{r:02d}.tsv', sep='\t', index=False)

    # Generate a target file for each run
    for task, tfile in zip(tasks, tfiles):
        cl = tf.get_task_class(task)
        myTask = getattr(tf, cl)(const)

        # Add run number if necessary
        args = {}
        if myTask.name not in ut.tasks_without_run_number:
            args.update({'run_number': r})

        # Make task file
        myTask.make_task_file(file_name=tfile, **args) #this meaks the task
        # file using default ocnfigurations (no parameter is passed, so will
        # use the default arg values in the corresponding task function in
        # task_file.py
