# Storyboards for Milestone 1

## Contents
- [Main Page](#main-page)  
- [Chat](#chat)  
- [Login](#login-page)  

## Main Page
![main window](https://raw.githubusercontent.com/d3aths/SDV602-Project/master/Milestone-1/storyboard/main%20window%20v3.png?token=AD26CGCOK64SHGCV52V6TOLBFRAUI)

In theory these buttons would interact with the graph, with the user being able to zoom in on points, refresh the graph back to its original view, scroll along the axes, and save a picture of where they move to. These controls come built in with matplotlib.  
Other than that, this is a basic generated matplot graph and interface that i have customised slightly for the needs. The buttons prev and next will change screens to the previous or next uploaded data, along with its summary and possibly chat box.

<h2 align="right">
  
[⬆](#contents)

---

## Chat
![chat](https://raw.githubusercontent.com/d3aths/SDV602-Project/master/Milestone-1/storyboard/project%20chat.gif?token=AD26CGBHZGNS5EZBZGHYXC3BFRBWK)

The user inputs the text they want to send and then either presses enter or clicks the send button. this gets sent to the chat. Curerntly it is cheesing it and i manually assigned my name to the messages by hardcoding.

<h2 align="right">
  
[⬆](#contents)

---
  
## Login Page
![loginreg](https://raw.githubusercontent.com/d3aths/SDV602-Project/master/Milestone-1/storyboard/loginreg.png?token=AD26CGB2UIAYRYHEZB72UATBGFW2Y)
  
This is a modal window that pops up when you run the program. So you cannot interact with the main window until you login or register. Upon clicking either button, a new modal window appears. All these windows are currently coded and working in the program, aside from the error windows which were made in an editing program. The only thing that is not done is any kind of storage for the user/pass and validation to check correct logins. So the screens are just placeholders without function right now.

### Login
![login](https://raw.githubusercontent.com/d3aths/SDV602-Project/master/Milestone-1/storyboard/login.png?token=AD26CGDJNRA3JTWQ5LLFR33BGFW2M)

The login window. It remains unstyled for now
  
![loginerror](https://raw.githubusercontent.com/d3aths/SDV602-Project/master/Milestone-1/storyboard/loginfailed.png?token=AD26CGANOMRBUNHOPGCFH73BGFXH6)
 
Concept of an error message that would appear if the user does not input a valid username or password
  
### Register
![reg](https://raw.githubusercontent.com/d3aths/SDV602-Project/master/Milestone-1/storyboard/reg.png?token=AD26CGEHIB7NG37XXCNLNQ3BGFXKY)
  
Register window which appears as a modal when you click the register button
  
![regerror](https://raw.githubusercontent.com/d3aths/SDV602-Project/master/Milestone-1/storyboard/regfailed.png?token=AD26CGGRF4B2IFT7CBMSZGTBGFXNE)
  
Concept of error that might appear while registering, if a user tries to input a taken name
  
<h2 align="right">
  
[⬆](#contents)
  
## Notes, Errors, Etc
The main window shows up when the program starts to run for some reason that I cant understand as yet, since I have set the code up for the main window to be inactive, and the first window that is read when the program runs is just supposed to be the window for login and register. I have played around with the `window.Hide()` method and inserted it at various points within the code, and the closest I can get is the window opening at first and then disappearing when something is clicked on the account window, which is not ideal.

The buttons underneath the chart for interaction are still just a concept and I cannot work out how to implement something like that.
The prev and next buttons are not currently coded to switch windows within the saame main window.
I'm not sure what to do for a 3rd screen without just saying "oh i'll have 3 different charts and each window they appear on can be classified as my 3 screens.
