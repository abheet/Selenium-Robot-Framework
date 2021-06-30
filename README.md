#Page Object Model  implementation with Selenium-Python(pytest) Webpage automation
#Author: Abheet Singh Jamwal


Automation Scripts for Validating 
-Login Page
-SignUp Page
-ForgetPassword Page
  
  
#Installation steps
  
##Prerequistes
  
1) Python 2.x or 3.x
2) Virtual Env
  
Steps to set Up env
1) Take Pull of repo 

2) Go inside demp/SeleniumScript folder
	cmd: />cd demp/SeleniumScript

3) Optional step can be skipped: If want to create own virtual env Install all required PIP packages

	cmd:/>demp/SeleniumScript> pip install -r pip-requirement.txt (file available inside Current working dir)

4 Activate  virtual env 
	i.e :/> source demo_env/bin/activate 

5 Once (demo_env) is activated scripts are ready to run.
  
  
#How to run script:

  1)cd demp/SeleniumScript (i.e Current Working Directory)
  
  2) There are three test files under tests folder
  
  3)if want to run all test suites
  	CMD:> pytest  This command detect all tests available in tests folder and execute all testcases at once
  	
  4)if want to run only one test file
  	CMD:> pytest -k Test file name  (file name like test_forget_password, test_login or test signup...)
  	
  5)if want to run any specific testcase within test file
  	CMD:> pytest -k Test file name::test Case method_name
  	
  6)if want to run test case w.r.t maker like lowest,medium or highest tags
  	CMD:>pytest -k Test file name -m lowest 
  	
  7)if want to get reports
  	CMD:> pytest -k Test file name --html report_name.html 
  	
  8) if want to run test parallelly
  	CMD:> pytest -n 3 (3 is number of worker it can be any number)
  			
  
