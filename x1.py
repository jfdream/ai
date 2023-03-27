from moviepy.editor import *
import os

image_folder = '/Users/yangyudong/Desktop/Avatars_online'
video_name = '/Users/yangyudong/Desktop/ai/output_1.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
images.sort()

# frames = []
# for image in images:
#     clip = ImageClip(os.path.join(image_folder, image)).set_duration(1)
#     # clip = clip.fadein(0.5).fadeout(0.5)    
#     frames.append(clip)

frames = []
for i, image in enumerate(images):
    clip = ImageClip(os.path.join(image_folder, image)).set_duration(3)
    if i > 0:
        # 将上一帧的淡出时间设置为1秒
        last_clip = frames[-1]
        last_clip = last_clip.set_end(last_clip.end - 1)
        last_clip = last_clip.fadeout(1)
        
        frames[-1] = last_clip
        # 将当前帧的淡入时间设置为1秒
        clip = clip.set_start(clip.start + 1)
        clip = clip.fadein(1)
    frames.append(clip)

video = concatenate_videoclips(frames, method='compose')
video.write_videofile(video_name, fps=24)