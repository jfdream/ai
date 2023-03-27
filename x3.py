from moviepy.editor import *
import numpy as np

# 设置所有背景图片和 GIF 图片路径以及输出视频路径
backgrounds_path = ['/Users/yangyudong/Desktop/ai/1.png', 
'/Users/yangyudong/Desktop/ai/2.png', 
'/Users/yangyudong/Desktop/ai/3.png', 
'/Users/yangyudong/Desktop/ai/4.png']
gifs_path = ['/Users/yangyudong/Desktop/ai/x.gif', 
'/Users/yangyudong/Desktop/ai/x.gif', 
'/Users/yangyudong/Desktop/ai/x.gif', 
'/Users/yangyudong/Desktop/ai/x.gif']

video_name = '/Users/yangyudong/Desktop/ai/output_3.mp4'

frames = []

# 创建函数用于将 GIF 图片合成到背景图片上，并添加透明效果
def composite_with_alpha(background, gif, i):
    background_clip = ImageClip(background).set_duration(3)

    if i > 0:
        last_clip = frames[-1]
        last_clip = last_clip.set_end(last_clip.end - 1)
        last_clip = last_clip.fadeout(1)
        
        frames[-1] = last_clip
        # 将当前帧的淡入时间设置为1秒
        background_clip = background_clip.set_start(background_clip.start + 1)
        background_clip = background_clip.fadein(1)
    frames.append(background_clip)

    gif_clip = VideoFileClip(gif, has_mask=True).set_duration(3)
    def make_frame(t):
        gif_frame = gif_clip.get_frame(t)
        alpha = gif_clip.mask.get_frame(t)
        alpha = np.dstack((alpha, alpha, alpha))
        result = np.where(alpha == 0, background_clip.get_frame(t), gif_frame)
        return result.astype('uint8')
    return VideoClip(make_frame=make_frame, duration=3)

# 对每个背景图片和对应的 GIF 图片进行循环处理
videos = []
for i in range(len(backgrounds_path)):
    video = composite_with_alpha(backgrounds_path[i], gifs_path[i], i)
    videos.append(video)

# 将所有视频合并成一个大视频
final_video = concatenate_videoclips(videos)

# 输出视频
final_video.write_videofile(video_name, fps=24)
