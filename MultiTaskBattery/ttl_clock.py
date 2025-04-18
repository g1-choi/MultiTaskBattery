# Created 2023: Bassel Arafat, Jorn Diedrichsen, Ince Husain
from psychopy import core, event

class TTLClock:

    def __init__(self):
        """
        TTLClock class is used for counting the number of TTL pulses and the time of the last TTL pulse
        """
        self.clock      = core.Clock() #
        self.ttl_count      = 0    # the number of ttl pulses
        self.ttl_time       = 0    # time stamp of the last incoming ttl pulse
        self.ttl_button = 'equal'  # the button used for simulating a ttl
        # pulse,in MRRC, pressing the ttl_pulse button is equivalent to typing =
        # the key name returned from getKeys for = is 'equal' instead of '='

    def reset(self, start_time=0):
        """ resets the clock and ttl-counter
        Args:
            start_time (float):
                the time in seconds to start the clock from
        """
        self.clock.reset(start_time)
        self.ttl_count = 0
        self.ttl_time = 0

    def wait_for_first_ttl(self, wait = True):
        """ This function waits for the first TTL and then resets the clock appropriately
        Args:
            wait (bool):
                if True, the function will wait for the first TTL
        """
        if wait:
            print('Waiting for first TTL...')
            while self.ttl_count == 0:
                self.update()
        self.clock.reset()
        self.ttl_time = 0

    def wait_until(self,time):
        """waits until the given time since the beginning of the run
        Args:
            time (float):
                time in seconds
        Returns:
            real_time (float):
                time that the real start occurs
            start_ttl (int):
                Number of TRs recorded since the beginning of the run
            start_ttl_time (float):
                Time since the last TR  """
        while self.clock.getTime() < time:
            self.update()
        return self.clock.getTime(), self.ttl_count, self.clock.getTime()-self.ttl_time

    def get_time(self):
        """returns the current time of the clock
        Returns:
            time (float):
                the current time of the clock
        """
        return self.clock.getTime()

    def update(self):
        """ updates the ttl count and time of the last ttl pulse
        """
        # get all the ttl pulses in the buffer
        keys = event.getKeys([self.ttl_button], timeStamped=self.clock)
        # SL: the first arg should be a list of keys to check for, if it's None
        # will check for everything, note that if i change self.ttl_button to
        # a list it won't work bc here it wraps that attribute into a list
        # again so the key to check will be [[key]] which likely is not legit
        # argument style and might cause return to be empty
        # To see what key was pressed and their key names. Can run in console
        # event.getKeys(), this wlll print out all the recent key presses
        # that were detected since the last call of event.GetKeys() but this
        # seems to work only if we have a UI open and key press happens when
        # focusing on the UI window

        # checks if the pressed key is the key used as the ttl pulse
        for k in keys:
            self.ttl_count += 1 # each time a ttl button is pressed, ttl count increases
            self.ttl_time = k[1] # the time when the ttl button has been pressed
            print(f"TR count: {self.ttl_count} -    TR time: {self.ttl_time}", end = "\r")