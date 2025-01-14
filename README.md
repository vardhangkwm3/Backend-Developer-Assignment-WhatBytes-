This is the assignment project "ProAuthenticator".
  -- To run this project one have to install all the dependencies in the requirements.txt
  -- using command "pip install -r requirements.txt"

To activate the virtual enviroment the command is :-
  -- Here i used "virtualenv" as this is the name of the virtual enviroment.
  -- "./virtualenv/Scripts/activate"

After activating the virtual enviroment:-
  -- run the command "python manage.py runserver".

If it shows Unapplied Migrations Issue:-
  -- use the command "python manage.py migrate" to resolve these issues.

When Server is Live:-
  -- You will be seeing a "login" form also having link to the "signup" page then go to the signup page to create a new user.
  -- after successfully creating a user you will be redirected to the "login" page and here you can login in the device using the email or username you defined at the time of "signup", 
     you can try to login from both.
  -- After successfully login the user will be redirected to the home page, which is greeting the user as "Welcome 'Your username'", and is consisting of two functionalities "Profile" and "Change Password".
  -- when click on profile it will redirect to "profile" page showing the details of loged in user like "username", "email", "joined_date", "Last_Active".
  -- On clicking "Change Password" we are redirected to "Change Password" page here user have to provide "old password" to change "new password" after clicking on
     submit the message is shown in the form of breadcrumb that "Password Changed Successfully".

When User is Not Authenticated:-
  -- The "forgot password" functionality is there(if in any case user forgot password).
