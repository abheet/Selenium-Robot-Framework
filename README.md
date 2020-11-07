# Home Assignment 
#Author: Abheet Singh Jamwal



Automation Scripts for Validating 
  Login Page
  SignUp Page
  ForgetPassword Page
  
  
  ****************Installation steps***********************
  
  Prerequisite:
  
  1) Python 2.x or 3.x
  2) Virtual Env
  
  *******Steps to set Up env*****
  1) Take Pull of repo 
  
  2) Go inside demp/SeleniumScript folder
  	i.e />cd demp/SeleniumScript
    
  3) Optional step can be skipped: If want to create own virtual env Install all required PIP packages
  	i.e 	:/>demp/SeleniumScript> pip install -r pip-requirement.txt (file available inside Current working dir)
    
  4 Activate  virtual env 
  	i.e :/> source demo_env/bin/activate <enter>
  
  5 Once (demo_env) is activated scripts are ready to run.
  
  ******* How to run scripts*************
  1)cd demp/SeleniumScript (i.e Current Working Directory)
  
  2) There are three test files under tests folder
  	if want to run all test suites
    CMD:> pytest <enter> This command detect all tests available in tests folder and execute all testcases at once
  
  if want to run only one test file
  CMD:> pytest -k <Test file name> <enter> (file name like test_forget_password, test_login or test signup...)
  
  if want to run any specific testcase within test file
    CMD:> pytest -k <Test file name>::<test Case method_name> <enter>  
  
  if want to run test case w.r.t maker like lowest,medium or highest tags    
  		CMD:>pytest -k <Test file name> -m lowest <enter>
  
  if want to get reports
  	CMD:> pytest -k <Test file name> --html report_name.html <enter>	
  
  if want to run test parallelly
  		CMD:> pytest -n 3 (3 is number of worker it can be any number)
  			
  
