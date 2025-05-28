from logfile import logclass

# Logs (Code on next slide)
class TestExample(logclass):
    def test_2ndtest(self):
        log = self.getthelogs()
        log.info("this is my first test case")
        log.info("test case is not starting")
        name = "vaibhav patil"
        if 'vaibhav' in name.lower():
            assert True
            log.info("test case pass")
        else:
            log.error("test case fail")
            assert False
