import pytest
@pytest.mark.usefixtures("setup")
class Test_login:
    # @pytest.mark.skip  # skip function
   def test_2sttest(self):
       print('this is my 1st test')
   # @pytest.mark.xfail # xfail function
   def test_3sttest(self):
       print('this is my 2st test')
   # assert 2==3 ,"else part this is function fail"


# Logs examples

