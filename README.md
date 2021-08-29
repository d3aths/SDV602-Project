# SDV602-Project

## Documentation

### Issues and To-Do

The main window shows up when the program starts to run for some reason that I cant understand as yet, since I have set the code up for the main window to be inactive, and the first window that is read when the program runs is just supposed to be the window for login and register. I have played around with the `window.Hide()` method and inserted it at various points within the code, and the closest I can get is the window opening at first and then disappearing when something is clicked on the account window, which is not ideal.
  
\**UPDATE*\* all windows are now hidden and only come out when theyre needed properly now. aside from everything opening and disappearing in about 1 second at the very start of the app.

The buttons underneath the chart for interaction are still just a concept and I cannot work out how to implement something like that.

The main windows will navigate and draw up and be interactable properly, but when you reach the 3rd window and try to go back, window2 opens but will not take commands from there. I think this is to do with the event loop. You can see what I mean from the way I have it coded in a linear structure, each prev and next button on the window just follows along til the end, but at the end, it only opens the commands that the very end loop has. It doesnt actually jump back, to the section where window2 has its commands, or window1 has its commands either. I have no idea how you could get this to work properly without just writing a neverending loop of code at each point. So window1 would have to have the code for window2, window2 would have to have the code for both window1 and 3, and window3 would need window 2's. This seems very unnessecary conflation to me.
  
The output window was able to be written in and if you did that, it would interefere with the chat. I have made a workaround that makes the output box read only

### Storyboard

[Link here](https://github.com/d3aths/SDV602-Project/blob/master/Milestone-1/storyboard/Descriptions.md)
