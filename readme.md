# Github CI-CD Python Flask Example

### About GitHub CI-CD
GitHub Actions now makes it easier to automate how you build, test, and deploy your projects on any platform, including Linux, macOS, and Windows. Run your workflows in a container or in a virtual machine. Actions also supports more languages and frameworks than ever, including Node.js, Python, Java, PHP, Ruby, C/C++, .NET, Android, and iOS. Testing multi-container apps? You can now test your web service and its database together by simply adding some docker-compose to your workflow file.


### Project Description
In this project I created a simple flask application and in this repository I also added some github actions. 
1) <b>Python Application Action </b>- Runs python application in a ubuntu environment by installing all dependencies from pythonapp.yml file. If everything runs  successfully it shows grren tick.
2) <b>Deployment to Heroku </b>- Whenever I push something or change something in my repository then github actions automatically works and deploy my code to heroku app.

### Python VirtualEnvironment Command

1) Install virtualenv using
	> pip install virtualenv 

2) Now in which ever directory you are, this line below will create a virtualenv there
	> virtualenv myenv
  And here also you can name it anything.

3) Now if you are same directory then type,
	> myenv\Scripts\activate

4) For Deactivating 
	>deactivate

### Project Snaps
![alt text](https://github.com/wolfblunt/Github-CI-CD-Example/blob/master/Images/Action.png)

![alt text](https://github.com/wolfblunt/Github-CI-CD-Example/blob/master/Images/GreenTick.png)


### Heroku App Path

* To Visit our application follow the link below. 
https://github-ci-cd-flaskapp.herokuapp.com/


## Code credit

Code credits for this code go to [Aman Khandelwal](https://github.com/wolfblunt)





