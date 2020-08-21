# MovieSmasher
This program is specificly made for Wyze V2 videos. The V2 creates small 1 min. videos, this program is intended to take these small video's and make one larger video

This program is mostly untested and provided as is for the Wyze community. This program requires that you download ffmpeg and place ffmpeg.exe in the same location as this script (or compiled exe), a link to there page can be found below.

https://ffmpeg.org/download.html


In order to use, press the "Open" button, then select all movie clips you want to merge into one. MovieSmasher will sort them alphabeticly, and combine them in that order. For this reason its best to not change the name of the files provided by the V2.

after selecting video's "File selected = True" indicates you are ready to press the "Merge" button and concatinate the selected video's.

Once the "Merge" button has been pressed, you will see the console window display the output provided by ffmpeg. Its normal for MovieSmasher to appear to be frozed during this time. When the process is finished "Merge Complete" will be displayed and in the same folder as MovieSmasher will be an .mp4 file with the name provided (or output.mp4) that is the combined video clips.
