from moviepy.editor import *
from moviepy.video.fx.all import crop

import pandas as pd




    # Load the video file
clip = VideoFileClip("G:\Python\pythonRepo\Python\gita.mp4")

# Read the Excel file
df = pd.read_excel('G:\Python\pythonRepo\Python\gita.xlsx')

# Loop through the rows of the Excel file and print the values
for index, row in df.iterrows():
    #print(row['Topics'], row['Definition'])
    words = row['Definition'].split()
    # Get the total number of words in the paragraph
    num_words = len(words)
    # Calculate the index of the middle word
    mid_index = num_words // 2

    # Join the first half of the words into a string
    first_half = ' '.join(words[:mid_index])

    # Join the second half of the words into a string
    second_half = ' '.join(words[mid_index:])

    # Print the two equal paragraphs
    print("1--------------",first_half,"...")
    print("2-------------",second_half)

    # Add the first text clip
    #row['Topics']
    title1 = TextClip(row['Topics'], 
                      fontsize=50, font='Lane', 
                      color='black',
                    align='center')
                    #.margin(6)

    title1 = title1.set_position(("center", "center"), relative=True).set_duration(clip.duration)

    tc_width, tc_height = title1.size
    color_clip = ColorClip(size=(tc_width+100, tc_height+50),color=(255,255,255))
    color_clip = color_clip.set_opacity(.8)
    # color_clip.save_frame("./images/colorClip.png") 
    # title1.save_frame("./images/title1.png") 
    final_clip = CompositeVideoClip([color_clip,title1]).set_duration(clip.duration)
    final_clip = final_clip.set_position(("center",0))
    # final_clip.save_frame("./images/final_clip.png") 

    print("---------------num_words-----------------------",len(row['Definition']))

    # Add the second text clip
    if(len(row['Definition']) > 250):
        size = (480,640)
    else:
        size = (480,480)


    print("--------------------------------------",size)



    first_half = first_half+"..."
    title2 = TextClip(first_half, 
                    fontsize=50,
                      color='black',
                        font='Aparajita',
                     method='caption',
                      align='center', interline=5, size=size)
    title2 = title2.set_position(("center", 2)).set_duration(8)

    tc2_width, tc2_height = title2.size
    color_clip2 = ColorClip(size=(tc2_width+100, tc2_height+50),color=(255,255,255))
    color_clip2 = color_clip2.set_opacity(.8)
    # color_clip2.save_frame("./images/colorClip2.png") 
    # title2.save_frame("./images/title2.png") 
    final_clip2 = CompositeVideoClip([color_clip2,title2]).set_duration(8)
    final_clip2 = final_clip2.set_position(("center"))
    # final_clip2.save_frame("./images/final_clip2.png") 


    # Add the third text clip
    
    title3 = TextClip(second_half,
                    fontsize=50,
                    color='black',
                    font='Aparajita',
                    method='caption', align='center', interline=5, size=size)
    title3 = title3.set_position(("center",2))

    tc3_width, tc3_height = title3.size
    color_clip3 = ColorClip(size=(tc3_width+20, tc3_height+10),color=(255,255,255))
    color_clip3 = color_clip3.set_opacity(.8)
    # color_clip3.save_frame("./images/colorClip3.png") 
    title3.save_frame("../Files/images/title3.png") 
    final_clip3 = CompositeVideoClip([color_clip3,title3])
    final_clip3 = final_clip3.set_position(("center")).set_duration(7).set_start(8)
    # final_clip3.save_frame("./images/final_clip3.png")
    # Combine the video clip with the two text clips


    video_with_text = CompositeVideoClip([clip, final_clip, final_clip2, final_clip3])

    # Define the target height and width
    target_height = 1920
    target_width = 1080

        # Define the desired resolution
    new_size = (1920, 1080)  # or any other resolution you want
    fps = 30
    # Resize the clip to the new resolution
    #resized_clip = video_with_text.resize(new_size)
    resized_clip = video_with_text.resize(height=target_height)

    video_fps = resized_clip.set_fps(fps)

    # Crop the video to the desired aspect ratio
   # cropped_clip = crop(resized_clip, width=target_width, height=int(target_width * 16 / 9), x_center=target_height/2, y_center=target_width/2)

    print("../videos/"+row['Topics']+".mp4")

    # Save the modified video file
    video_fps.write_videofile("../videos/"+row['Topics']+".mp4")


