import os
from moviepy.editor import VideoFileClip

def crop_and_split_video():
    input_path = input("Enter the path of the video: ")
    output_folder = "split_videos"

    os.makedirs(output_folder, exist_ok=True)
    crop_and_split_video(input_path, output_folder)
    print("Video cropping and splitting completed!")
    video_clip = VideoFileClip(input_path)
    max_duration = 30  # seconds

    num_clips = int(video_clip.duration / max_duration) + 1

    for i in range(num_clips):
        start_time = i * max_duration
        end_time = min((i + 1) * max_duration, video_clip.duration)
        clip = video_clip.subclip(start_time, end_time)
        
        # Crop the clip to YouTube Shorts resolution (1080x1920)
        width_to_crop = min(clip.w, clip.h * 1080 // 1920)
        height_to_crop = min(clip.h, clip.w * 1920 // 1080)
        x_center = clip.w // 2
        y_center = clip.h // 2
        x1 = x_center - width_to_crop // 2
        x2 = x_center + width_to_crop // 2
        y1 = y_center - height_to_crop // 2
        y2 = y_center + height_to_crop // 2
        clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
        
        # Resize the clip to YouTube Shorts resolution (1080x1920)
        clip = clip.resize(width=1080, height=1920)
        
        output_path = os.path.join(output_folder, f"clip_{i+1}.mp4")
        clip.write_videofile(output_path, codec='libx264', threads=4)

if __name__ == "__main__":
    pass
    
