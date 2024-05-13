


def about():
 print('''Bottom video is placed in the collage video folder and top memes and video clips are posted in the image video folder''')


from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
import os

video_folder = 'collagevideo'
imagevideo_folder = 'imagevideo'
output_folder = 'results/collage_results'

def vdeoproc():
    bottom_file = r'C:\Users\gokul\OneDrive\Desktop\MEME-CREATOR-V1\collagevideo\meme1.mp4'  # Specify the bottom video filename

    # Load the bottom video from the "video" folder
    bottom_path = os.path.join(video_folder, bottom_file)
    bottom_clip = VideoFileClip(bottom_path)
    bottom_clip = bottom_clip.resize(height=960)

    # Iterate through the top images/videos in the "imagevideo" folder
    top_files = sorted([f for f in os.listdir(imagevideo_folder) if f.endswith('.mp4') or f.endswith('.jpg') or f.endswith('.png')or f.endswith('.jpeg')])

    for index, top_file in enumerate(top_files):
        top_path = os.path.join(imagevideo_folder, top_file)
        try:
            create_collage(bottom_clip, top_path, index)
        except Exception as e:
            print(f"Error processing {top_path}: {e}")
            continue

def create_collage(bottom_clip, top_path, index):
    output_path = os.path.join(output_folder, f'collage_{index}.mp4')

    top_clip = VideoFileClip(top_path) if top_path.endswith('.mp4') else ImageClip(top_path, duration=bottom_clip.duration)
    top_clip = top_clip.resize(height=1000)

    # Resize and crop the top clip to fit without black edges
    top_clip = top_clip.resize((1080, 990)).crop(x1=0, y1=0, x2=1080, y2=990)

    final_clip = CompositeVideoClip([top_clip.set_position(("center", 25)),  # Adjust the y value here
                                     bottom_clip.set_position(("center", 1000))], 
                                    size=(1080, 1910))

    final_clip.write_videofile(output_path, codec='libx264')
    print(f"Collage {index} creation successful.")

if __name__ == "__main__":
    pass
