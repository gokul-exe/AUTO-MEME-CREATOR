import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, AudioFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

audiopath = "audio_files"
single_image_background_folder = 'background/double image background'
meme_folder = 'memes'
output_folder = 'results/double_image_results'  # Change the output folder path

def doubleimg(image_filenames, index):
    audio_path = os.path.join(audiopath, "music1.mp3")
    video_path = os.path.join(single_image_background_folder, "background.mp4")
    image_path1 = os.path.join(meme_folder, image_filenames[0])
    image_path2 = os.path.join(meme_folder, image_filenames[1])
    output_path = os.path.join(output_folder, f"{index}.mp4")  # Output video path

    target_duration = 30  # seconds

    video_duration = VideoFileClip(video_path).duration

    # Check if the video duration is greater than the target duration
    if video_duration > target_duration:
        video_clip = VideoFileClip(video_path).subclip(0, target_duration)
    else:
        # Concatenate the video clips to loop it
        loop_factor = int(target_duration / video_duration) + 1
        video_clips = [VideoFileClip(video_path) for _ in range(loop_factor)]
        video_clip = concatenate_videoclips(video_clips)
        video_clip = video_clip.subclip(0, target_duration)

    image_clip1 = ImageClip(image_path1)
    image_clip2 = ImageClip(image_path2)

    # Resize the video clip to 1080x1080
    video_clip = video_clip.resize(height=1080, width=1080)

    # Resize and position the image clips on top
    meme_width = 500 # Adjust width as needed
    meme_height = 500  # Adjust height as needed
    image_clip1 = image_clip1.resize(width=meme_width, height=meme_height)
    image_clip1 = image_clip1.set_position(("center", 20))

    image_clip2 = image_clip2.resize(width=meme_width, height=meme_height)
    image_clip2 = image_clip2.set_position(("center", video_clip.h - meme_height - 20))

    # Create a composite clip with both video and image
    composite_clip = CompositeVideoClip([video_clip, image_clip1.set_duration(target_duration)])
    composite_clip = CompositeVideoClip([composite_clip, image_clip2.set_duration(target_duration)])

    # Load the audio clip
    audio_clip = AudioFileClip(audio_path)

    # Set audio for the composite clip
    final_clip = composite_clip.set_audio(audio_clip)

    final_clip.write_videofile(output_path, codec='libx264')
    print(f"VIDEO CREATION SUCCESSFUL: {output_path}")
def doublproc():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    meme_images = os.listdir(meme_folder)
    total_images = len(meme_images)
    
    for index in range(0, total_images, 2):
        if index + 1 < total_images:
            image_filenames = [meme_images[index], meme_images[index + 1]]
            doubleimg(image_filenames, index // 2 + 1)

if __name__ == "__main__":
    pass
    
