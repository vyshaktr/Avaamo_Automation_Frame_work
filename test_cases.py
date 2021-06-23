import time

from PageObjects.Google_Form import google_form
from PageObjects.Menuoptions import Menu_options
from Testdata.Datafile import Testdata

import pytest

# @pytest.mark.usefixtures("setup")
from PageObjects.landingPage import landing
from PageObjects.signin import signin
from utilities.Actionclass import Actions
from utilities.BaseClass import Baseclass


class TestCases(Baseclass):
    @pytest.mark.smoke
    # Test case to validate Landing page (Test case ID : 1 )
    # Authored by vyshak on 23/06/2021
    def test_welcomescreen(self):
        log=self.getLogger()
        log.info("Step 1 :Launching Avammo website")
        land=landing(self.driver)
        #self.wait(self,"//*[contains(@class,'avm-welcome')]")
        time.sleep(2)
        log.info("Step 2 :Verification of  Welcome message")
        assert "Hello and welcome to IRA agent" == land.Welcome().text
        log.info("Step 3 :Click on Welcome message")
        land.Welcome().click()
        self.waitfor(3)

        if(land.botstart().is_displayed()):
            log.info("Step 4 :Verification of Agentname")
            assert "IRA iffco tokio" == land.Agentname().text
            log.info("Agent name is present as expected")
        else:
            assert  True== False
        log.info("Step 5 :Verification of Get started button")

        if land.Get_started().is_displayed():
            land.Get_started().click()
        else:
            assert  True== False
        log.info("Step 6 :Moving inside the bot")
        self.swtich_frame("avaamoIframe")
        self.waitfor(2)
        if not land.TextArea().is_displayed():
            land.DownwardIcon().click()
        else:
            log.info("Text area already exists")
        log.info("Step 7 :Sending input")
        land.TextArea().send_keys(Testdata.User_input1)
        land.Sendbtn().click()
        self.waitfor(3)
        log.info("Step 8 : Verifying agent Reply")
        Agentreply=land.Agentreply().text
        log.info("Agent Reply is : "+Agentreply +"")


    @pytest.mark.smoke
    # Test case to validate Invalid sign in  (Test case ID : 2 )
    # Authored by vyshak on 23/06/2021
    def test_Menu_options(self):
        log = self.getLogger()
        log.info("Step 1 :Launching Avammo website")
        land = landing(self.driver)
        Menu=Menu_options(self.driver)
        # self.wait(self,"//*[contains(@class,'avm-welcome')]")
        time.sleep(2)
        log.info("Step 2 :Verification of  Welcome message")
        assert "Hello and welcome to IRA agent" == land.Welcome().text
        log.info("Step 3 :Click on Welcome message")
        land.Welcome().click()
        self.waitfor(3)

        if (land.botstart().is_displayed()):
            log.info("Step 4 :Verification of Agentname")
            assert "IRA iffco tokio" == land.Agentname().text
            log.info("Agent name is present as expected")
        else:
            assert True == False
        log.info("Step 5 :Verification of Get started button")

        if land.Get_started().is_displayed():
            land.Get_started().click()
        else:
            assert True == False
        log.info("Step 6 :Moving inside the bot")
        self.swtich_frame("avaamoIframe")
        self.waitfor(2)
        if not land.TextArea().is_displayed():
            log.info("Step 7 :Clicking on start over button")
            Menu.Startover().click()
        else:
            land.DownwardIcon().click()
            Menu.Startover().click()
        self.waitfor(2)
        log.info("Step 8 :Clicking on Download Motor Policy")
        Menu.Downloadpolicy().click()
        self.waitfor(2)
        Menu.Downloadbtn().click()
        self.windowhandles(1)
        log.info("Step 9 :Verifying downloaded link")
        log.info(self.driver.title)
        self.driver.close()
        self.windowhandles(0)




    @pytest.mark.smoke
    # Test case to validate wrong password (Test case ID : 4 )
    # Authored by vyshak on 23/06/2021
    def test_Form_submit(self):
        Gform=google_form(self.driver)
        log = self.getLogger()
        log.info("Step 1 :Launching Avammo website")
        land = landing(self.driver)
        # self.wait(self,"//*[contains(@class,'avm-welcome')]")
        time.sleep(2)
        log.info("Step 2 :Verification of  Welcome message")
        assert "Hello and welcome to IRA agent" == land.Welcome().text
        log.info("Step 3 :Click on Welcome message")
        land.Welcome().click()
        self.waitfor(3)

        if (land.botstart().is_displayed()):
            log.info("Step 4 :Verification of Agentname")
            assert "IRA iffco tokio" == land.Agentname().text
            log.info("Agent name is present as expected")
        else:
            assert True == False
        log.info("Step 5 :Verification of Get started button")

        if land.Get_started().is_displayed():
            land.Get_started().click()
        else:
            assert True == False
        log.info("Step 6 :Moving inside the bot")
        self.swtich_frame("avaamoIframe")
        self.waitfor(2)
        if not land.TextArea().is_displayed():
            land.DownwardIcon().click()
        else:
            log.info("Text area already exists")
        log.info("Step 7 :Sending "+Testdata.User_input2+" as input")
        land.TextArea().send_keys(Testdata.User_input2)
        land.Sendbtn().click()
        self.waitfor(3)
        log.info("Step 8 :Checking for form")
        if Gform.Form().is_displayed():
            log.info("Form is present")
        else:
            log.info("Form is not present Failed")
            assert True== False
        log.info("Step 9 : Filling the data inside the form")
        log.info("Entering Full name")
        Gform.Fullname().send_keys(Testdata.Full_name)
        log.info("Entering Address")
        Gform.Address().send_keys(Testdata.Address)
        log.info("Radio button selection")
        Gform.radiobtn().click()
        Gform.Dropdown().click()
        self.waitfor(1)
        Gform.option1().click()
        log.info("Star Rating")
        Gform.starrate().click()
        self.waitfor(1)
        Gform.submitbuton().click()
        self.waitfor(1)
        log.info("Step  10: Verifying success message")
        assert "Submitted successfully1"==Gform.Successmsg().text

    @pytest.mark.smoke
    # Test case to validate wrong password (Test case ID : 3 )
    # Authored by vyshak on 23/06/2021
    def test_Google_call(self):
        Gform = google_form(self.driver)
        log = self.getLogger()
        log.info("Step 1 :Launching Avammo website")
        land = landing(self.driver)
        # self.wait(self,"//*[contains(@class,'avm-welcome')]")
        time.sleep(2)
        log.info("Step 2 :Verification of  Welcome message")
        assert "Hello and welcome to IRA agent" == land.Welcome().text
        log.info("Step 3 :Click on Welcome message")
        land.Welcome().click()
        self.waitfor(3)

        if (land.botstart().is_displayed()):
            log.info("Step 4 :Verification of Agentname")
            assert "IRA iffco tokio" == land.Agentname().text
            log.info("Agent name is present as expected")
        else:
            assert True == False
        log.info("Step 5 :Verification of Get started button")

        if land.Get_started().is_displayed():
            land.Get_started().click()
        else:
            assert True == False
        log.info("Step 6 :Moving inside the bot")
        self.swtich_frame("avaamoIframe")
        self.waitfor(2)
        if not land.TextArea().is_displayed():
            land.DownwardIcon().click()
        else:
            log.info("Text area already exists")
        log.info("Step 7 :Sending " + Testdata.User_input3 + " as input")
        land.TextArea().send_keys(Testdata.User_input3)
        land.Sendbtn().click()
        self.waitfor(3)
        log.info("Verify Google and call options tab presence")
        if Gform.Google_callbox().is_displayed():
            log.info("Step 8 :Verify Google and call options  present")
        else:
            log.info("Step 8 : Google and call options not present")
            assert True == False
        log.info("Step 9 : Clicking on google link")
        Gform.Googlelink().click()
        self.waitfor(2)
        if Gform.Googletitle().is_displayed():
            log.info(" Google link has been opened")
        else:
            log.info("Failed to open google link")
            assert True == False
        log.info(" Closing google link")
        Gform.Googlelink_close().click()
        log.info("Step 10 : Clicking on call link")
        Gform.Calllink().click()
        self.waitfor(2)
        self.windowhandles(1)
        #log.info("Step 11 :Verifying Call link")
        #log.info(self.driver.title)
        self.driver.close()
        self.windowhandles(0)

    @pytest.mark.smoke
    # Test case to validate few objectives  (Test case ID : 3 )
    # Authored by vyshak on 23/06/2021
    def test_objectives(self):
        log = self.getLogger()
        log.info("Step 1 :Launching Avammo website")
        land = landing(self.driver)
        Menu = Menu_options(self.driver)
        # self.wait(self,"//*[contains(@class,'avm-welcome')]")
        time.sleep(2)
        log.info("Step 2 :Verification of  Welcome message")
        assert "Hello and welcome to IRA agent" == land.Welcome().text
        log.info("Step 3 :Click on Welcome message")
        land.Welcome().click()
        self.waitfor(3)

        if (land.botstart().is_displayed()):
            log.info("Step 4 :Verification of Agentname")
            assert "IRA iffco tokio" == land.Agentname().text
            log.info("Agent name is present as expected")
        else:
            assert True == False
        log.info("Step 5 :Verification of Get started button")

        if land.Get_started().is_displayed():
            land.Get_started().click()
        else:
            assert True == False
        log.info("Step 6 :Moving inside the bot")
        self.swtich_frame("avaamoIframe")
        self.waitfor(2)
        if not land.TextArea().is_displayed():
            log.info("Step 7 :Clicking on start over button")
            Menu.Startover().click()
        else:
            land.DownwardIcon().click()
            Menu.Startover().click()
        self.waitfor(2)
        log.info("Step 8 :Clicking on Renew Motor Policy")
        Menu.Renewpolicylink().click()
        self.waitfor(4)
        log.info("Step 9 : Verify agent respone")
        log.info(land.Agentresponse().text)
        log.info("Sending " + Testdata.Invalid_Policynumber + " as input")
        land.TextArea().send_keys(Testdata.Invalid_Policynumber)
        land.Sendbtn().click()
        self.waitfor(3)
        if (land.Agentresponse_invalid_policy())=="No Node found for this node id 32":
            log.info("Invalid Policy Entered")
        else:
            log.info("Entering valid policy")
        log.info("Sending " + Testdata.Valid_Policynumber + " as input")
        land.TextArea().send_keys(Testdata.Valid_Policynumber)
        land.Sendbtn().click()
        self.waitfor(3)
        assert "Can you help me with your vehicle registration number?" == land.Agentresponse_valid_policy().text
        log.info("Step 10 :Enter valid Registration number")
        land.TextArea().send_keys(Testdata.Valid_Registration_number)
        land.Sendbtn().click()
        self.waitfor(2)
        log.info("Step 11 :Enter valid phone number")
        land.TextArea().send_keys(Testdata.Valid_phonenumber)
        land.Sendbtn().click()
        self.waitfor(2)
        log.info("Step 11 :Enter valid Email")
        land.TextArea().send_keys(Testdata.Valid_Email)
        land.Sendbtn().click()
        self.waitfor(3)
        assert "Is the above information correct?"== land.Agentresponseinfo().text
        log.info("Step 12 :Clicking yes button")
        land.YesButton().click()
        self.waitfor(3)
        assert "Your policy will be renewed..Have a great day" == land.AgentFinal().text
















