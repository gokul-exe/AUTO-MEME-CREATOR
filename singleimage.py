import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, AudioFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.audio.fx.all import audio_loop

audiopath = "audio_files"
single_image_background_folder = 'background/single image background'
meme_folder = 'memes'
output_folder = 'results/single_memes_output'  # Change the output folder path

def singleimg(image_filename, index):
    audio_path = os.path.join(audiopath, "music1.mp3")
    video_path = os.path.join(single_image_background_folder, "background.mp4")
    image_path = os.path.join(meme_folder, image_filename)
    output_path = os.path.join(output_folder, f"{index}.mp4")  # Output video path

    target_duration = 10# seconds

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

    image_clip = ImageClip(image_path)

    # Resize the video clip to 1080x1080
    video_clip = video_clip.resize(height=1080, width=1080)

    # Resize and position the image clip on top
    meme_width = 540  # Adjust width as needed
    meme_height = 540  # Adjust height as needed
    image_clip = image_clip.resize(width=meme_width, height=meme_height)
    image_clip = image_clip.set_position(("center", 20))

    # Create a composite clip with both video and image
    composite_clip = CompositeVideoClip([video_clip, image_clip.set_duration(target_duration)])

    

    # Trim or loop the audio to match the target duration
    audio_clip = AudioFileClip(audio_path)
    if audio_clip.duration > target_duration:
        audio_clip = audio_clip.subclip(0, target_duration)
    else:
        audio_clip = audio_loop(audio_clip, duration=target_duration)

    # Set audio for the composite clip
    final_clip = composite_clip.set_audio(audio_clip)

    # Set audio for the composite clip
    final_clip = composite_clip.set_audio(audio_clip)

    final_clip.write_videofile(output_path, codec='libx264')
    print(f"VIDEO CREATION SUCCESSFUL: {output_path}")
def singleproc():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)    
    meme_images = os.listdir(meme_folder)
    for index, image_filename in enumerate(meme_images, start=1):
        if image_filename.lower().endswith('.jpg') or image_filename.lower().endswith('.png') or image_filename.lower().endswith('.jpeg'):
            singleimg(image_filename, index)



if __name__ == "__main__":
    pass