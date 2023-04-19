from moviepy.editor import *

# Load the video file
clip = VideoFileClip("G:\Python\pythonRepo\Python\sample.mp4")


# Add the first text clip
title1 = TextClip("Quantum Entanglement", fontsize=50, font='Montserrat-SemiBold', color='black',
                   bg_color='white', stroke_color='black', stroke_width=2, 
                   align='center').margin(6)

title1 = title1.set_position(('center', 0.05), relative=True).set_duration(clip.duration)

# Add border radius to the text clip
# title1 = title1.fx(vfx.mirror_x) \
#            .with_mask(vfx.mask_color(title1, [0, 0, 0])) \
#            .fx(vfx.mirror_x) \
#            .fx(vfx.make_border, width=5, color=(255,255,255)) \
#            .with_position(('center', 5), relative=True)

# Add the second text clip
size = (640, 480)
title2 = TextClip("A  way that", 
                  fontsize=70, color='white', bg_color='black', font='Anton',
                  method='caption', align='center', interline=5, size=size)
title2 = title2.set_position(("center", "center")).set_duration(6)

# Add the third text clip
sizen = (480, 840)
title3 = TextClip("  large distances.",
                  fontsize=70, color='white', bg_color='black', font='Anton',
                  method='caption', align='center', interline=5, size=sizen)
title3 = title3.set_position(("center", "center")).set_duration(5).set_start(6)


# Combine the video clip with the two text clips
video_with_text = CompositeVideoClip([clip, title1, title2, title3])

# Save the modified video file
video_with_text.write_videofile("output_video.mp4")


