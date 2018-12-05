#!/usr/bin/env python2

import logging
import time

class Event(object):
    def __init__(self, message="", log_level=logging.INFO):
        self.message = message
        self.log_level = log_level


def scrub_log(log_msg):
    scrubbed_msg = str(log_msg)
    # Assume there is code here to modify scrubbed_msg and remove PII.
    return scrubbed_msg


def should_log(log_msg, logger, log_level, log_time=time.time()):
    scrub_log(log_msg)
    log_msg = u"%s :: %s >> %s" % log_time, log_level, log_msg
    should_log = (logging.getLogger().getEffectiveLevel() >= logging.WARN)
    return (should_log, log_msg)


def main():
    #
    # Assume there is some code here, and we eventually get to this point,
    # where we need to log the custom log object `event`. This object has
    # the attributes `message` and `log_level`.
    #
    # ...
    event = Event(message="passé", log_level=logging.ERROR)
    logger = logging.getLogger(__name__)
    if should_log(event.message, logger, event.log_level)[0]:
        logger.log(event.log_level,
                   should_log(event.message, logger, event.log_level)[1])


if __name__ == "__main__":
    main()  # Example snippet showing how to use this functionality.
