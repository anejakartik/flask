# Flask Upload App

As mentioned in mini task performs <b>JWT authentication</b> and allows user to <b>send images</b> through an api with throttle limit of <b>5 request per minute</b>.

This App is Hosted in AWS in case it needs testing just need an update to start instance so that testing commence

# Guide TO Execute The Application

  <h4>1) First, register user through this url.</h4>
        
    Here is the screenshot for registering users.
        
 ![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(6).png)
 
 
    In the above screenshot we can see on successfull registration user recieves an access code (authentication token) and 
    a refresh code (for use when authentication code expires).
    
    Note: Authentication Token generated expires within 5-15 minutes. 
    
  <h4>2) Secondly, user Login through this url.</h4> 
   
    In case a registered user come a login url is prepared. Here is the screenshot below:
![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(7).png)

    After Login user recieves fresh set of tokens.
   
  <h4>3) For checking users which are registered .</h4> 
  
    For checking all the Users registered in database we can use the following url, Here is the live working:
    
![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(8).png)    

    In the above screenshot we can clearly see the password being a protected information is store using a hash algorithm.
   
   <h4>4) Moving on how we are going to access the image upload API.</h4>
   
    Now, how are we going to access the file uploading api below is the screenshots for accessing the application:
    
      i) Adding authentication as header
![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(14).png) 

      ii) Next adding file you wish to send for upload. And the response returned for image sent successfully.
![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(9).png)        

    As throttle limit is 5 request per minute. If we exceed the limit it will display following error:
    
![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(10).png)


    Note: In case if authentication code expires it will show server error.
    
 <h4>5) For cases of expired authentication code, we can use the following url to get the fresh token.</h4>
 
    Note: For new refresh code we need refresh token earlier got during login or registration
    
![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(11).png)

 <h4>6) Finally Logout (Basically revoking access of the tokens)</h4>
 
     If we no longer need tokens so to perform logout operation.
      
      i) For revoking access to authentication token.

![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(12).png)

      ii) For revoking access to refresh token.
      
![image](https://github.com/anejakartik/flask/blob/master/screenshot/Screenshot%20(13).png)
 
 
# Conclusion:

  Hence the task is completed, looking for your reviews. Also available to give live demo for the application.
  
  In case you wish to run the code on your system, simply clone the code and install requirement.
  
  For Windows execution of Code commands:
  
  set FLASK_APP=run.py
 
  set FLASK_DEBUG=1
 
 flask run
  
  For Linux execution of Code:
  
  sudo Python3 run.py
  
  
  

  


