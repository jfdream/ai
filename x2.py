from moviepy.editor import *
import numpy as np

# 设置背景图片和 GIF 图片路径以及输出视频路径

gif_path = '/Users/yangyudong/Desktop/ai/20230315-200621.gif'
background_path = '/Users/yangyudong/Desktop/Avatars_online/00001-491548963.png'
video_name = '/Users/yangyudong/Desktop/ai/output_2.mp4'

# 加载背景图片并设置其时长为 3 秒
background = ImageClip(background_path).set_duration(3)

# 加载 GIF 图片并设置其时长为 3 秒
gif = VideoFileClip(gif_path, has_mask=True).set_duration(3)

# 创建函数用于将 GIF 图片合成到背景图片上，并添加透明效果
def composite_with_alpha(t):
    gif_frame = gif.get_frame(t)
    alpha = gif.mask.get_frame(t)
    alpha = np.dstack((alpha, alpha, alpha))
    result = np.where(alpha == 0, background.get_frame(t), gif_frame)
    return result.astype('uint8')

# 创建一个 VideoClip 对象来包含合成后的视频
result = VideoClip(make_frame=composite_with_alpha, duration=3)

# 输出视频
result.write_videofile(video_name, fps=24)
