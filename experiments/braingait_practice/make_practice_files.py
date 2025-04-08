import sys
# sys.path.insert(0,'../../../MultiTaskBattery/') #didn't work
sys.path.insert(0,'/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML/Projects/BrainGaitProject/MultiTaskBattery/')
import MultiTaskBattery.task_file as tf
import MultiTaskBattery.utils as ut
import constants as const

#TODO: spatial navigation cannot be shorter than 30s, movie, StrangeStories, FrithHappe, Liking
# also can't be shorter then 30 since the trial_dur is 30 (1rep is min 30s)
# Movie, spatial navigation (imaging going through your room), probably
# doens't need to practice anyway?
tasks = ['movie','theory_of_mind','action_observation','finger_sequence',
         'visual_search','spatial_navigation','semantic_prediction',
         'verb_generation','n_back','contract_relax_glutes',
         'flexion_extension','auditory_narrative','sentence_reading','oddball']
#the task won't be generated the same order as the input order here and
# that's on purpose bc in task_file.make_run_file(), it shuffles the row,
# so that 2 runs are not in the same order either.
# #things that we would like to have but doesn't seem to be there: arithmatic,
# n_back_verbal

num_runs = 2  # Number of imaging runs, = 1, do only 1 practice, generate a
# few just to have extra options but in reality we won't use them

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
for r in range(5, 5+num_runs): #python is 0 indexing, range (a,b) = [a,b),
    # exclusive in 1 end. Start with 5 to have some gap and generate
    # different simulus than the the actual tasks (1,2)
    tfiles = [f'{task}_{r:02d}.tsv' for task in tasks]

    # Generate a target file for each run
    for task, tfile in zip(tasks, tfiles):
        if task == 'movie' or task == 'spatial_navigation':
            #these are minimum 30s long
            T = tf.make_run_file([task], tfile, instruction_dur=600,
                                 task_dur=30)
        else:
            T = tf.make_run_file([task], tfile, instruction_dur=600,
                                 task_dur=15)
        # set a very long time for instruction, 10mins, and wait for key press
        # instead. Task duration is half the usual length for practice, this arg
        # seems to only bed used to set up the run file start/end times,
        # the actula task duration is set in the args below (not automatically
        # propagated)
        T.to_csv(const.run_dir / f'practice_run_{r:02d}_{task}.tsv', sep='\t',
                 index=False)

        cl = tf.get_task_class(task)
        myTask = getattr(tf, cl)(const)

        # Add run number if necessary
        args = {}
        if myTask.name not in ut.tasks_without_run_number:
            args.update({'run_number': r})

        if myTask.name == 'movie' or myTask.name == 'spatial_navigation':
            args.update({'task_dur': 30}) #movie and spatial have to be 30s
        else:
            args.update({'task_dur': 15})  # for all practice tasks make it 15s long

        if myTask.name == 'movie': #specify a condition, do romance movie only
            args.update({'condition': 'romance'})
        # elif myTask.name == 'theory_of_mind': #specify a condition, do romance movie only
        #     args.update({'condition': 'practice'})

        # Make task file
        myTask.make_task_file(file_name=tfile, **args) #this meaks the task
        # file and save to task_files/taskfolder/task_runNum.tsv,
        # saves stimulus to display and for how long, using default
        # ocnfigurations (no parameter is passed, so will
        # use the default arg values in the corresponding task function in
        # task_file.py
        #for each task, there is trial_dur which is how long to display 1
        # story/image/audio, then task_dur = duration is the task block.
        # e.g., N-Back each image is shown for 2s (trial_dur = 2) and we keep
        # showing images for 30s (task_dur = 30)

#TODO: repeat the same task? --> make each their own run file, if need to
# repeat just rerun the same file again.
