import time

from .generics import GenericRetriesHandler


class RetryOnError(GenericRetriesHandler):
    retry_count = 5
    error_codes = []
    sleep = 1

    def is_eligible(self, response):
        if self.count < self.retry_count:
            if response.status_code in self.error_codes:
                time.sleep(self.sleep)
                return True

        return False
