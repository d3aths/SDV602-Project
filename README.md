# SDV602-Project

## Documentation

### Issues and To-Do

The main window shows up when the program starts to run for some reason that I cant understand as yet, since I have set the code up for the main window to be inactive, and the first window that is read when the program runs is just supposed to be the window for login and register. I have played around with the `window.Hide()` method and inserted it at various points within the code, and the closest I can get is the window opening at first and then disappearing when something is clicked on the account window, which is not ideal.
  
\**UPDATE*\* all windows are now hidden and only come out when theyre needed properly now. aside from everything opening and disappearing in about 1 second at the very start of the app.

The buttons underneath the chart for interaction are still just a concept and I cannot work out how to implement something like that.

The main windows will navigate and draw up and be interactable properly, but when you reach the 3rd window and try to go back, window2 opens but will not take commands from there. I think this is to do with the event loop. You can see what I mean from the way I have it coded in a linear structure, each prev and next button on the window just follows along til the end, but at the end, it only opens the commands that the very end loop has. It doesnt actually jump back, to the section where window2 has its commands, or window1 has its commands either. I have no idea how you could get this to work properly without just writing a neverending loop of code at each point. So window1 would have to have the code for window2, window2 would have to have the code for both window1 and 3, and window3 would need window 2's. This seems very unnessecary conflation to me. So as of now the requirements are still satisfied for this milestone as all the windows appear and are working, you just can't navigate 100%. I thought a way to fix this would be put `window.read()` on the switching buttons but that didnt work. Idk how to give back command properly to the screens.
  
The output window was able to be written in and if you did that, it would interefere with the chat. I have made a workaround that makes the output box read only

The chat on all windows was outputting to window3, no matter if you were currently on window1 or window2. I spent a lot of time trying to figure out what was happening with this, I thought it may have been the keys assigned to the multilines and outputs at first so experimented with isolating that and changing them around. Nothing worked. I looked up the problem and attributed it to pysimplegui. Since the last output box was on window3 and python reads in a linear way, everything was just going to that output element. I fixed this by changing all the outputs to a multiline element and using [this solution](https://github.com/PySimpleGUI/PySimpleGUI/issues/2674) from pysimple's github that had the same problem as I did. Now it it working as expected, and it is still read-only.

### Storyboard

[Link here](https://github.com/d3aths/SDV602-Project/blob/master/Milestone-1/storyboard/Descriptions.md)
