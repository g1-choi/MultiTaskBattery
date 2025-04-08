from psychopy import event,core

from psychopy import core, event

class TTLClockTest:

    def __init__(self):
        """
        TTLClock class is used for counting the number of TTL pulses and the time of the last TTL pulse
        """
        self.clock      = core.Clock() #
        self.ttl_count      = 0    # the number of ttl pulses
        self.ttl_time       = 0    # time stamp of the last incoming ttl pulse
        self.ttl_button = 'b'  # the button used for simulating a ttl pulse,
        # in MRRC, pressing the ttl_pulse button is equivalent to typing =

    def wait_for_first_ttl(self, wait=True):
            """ This function waits for the first TTL and then resets the
            clock appropriately
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

    def update(self):
        """ updates the ttl count and time of the last ttl pulse
        """
        # get all the ttl pulses in the buffer
        # keys = event.getKeys([self.ttl_button], timeStamped=self.clock)
        keys = event.getKeys()

        # checks if the pressed key is the key used as the ttl pulse
        for k in keys:
            self.ttl_count += 1 # each time a ttl button is pressed, ttl count increases
            self.ttl_time = k[1] # the time when the ttl button has been pressed
            print(f"TR count: {self.ttl_count} -    TR time: {self.ttl_time}", end = "\r")

def main():
    ttl = TTLClockTest()
    ttl.wait_for_first_ttl(True)
    print('Wait over, key press detected.')

if __name__ == "__main__":
    main() #need to have this as a default value to get us
    # started, otherwise will error out