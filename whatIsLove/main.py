'''
What is love?
'''

from moviepy.editor import VideoFileClip,TextClip,CompositeVideoClip
import os
import textwrap


# text = '''Agar siz baxtli hayot kechirishni istasangiz, uni odamlarga yoki narsalarga emas, balki maqsadga bog'lang. - Albert Eynshteyn'''

def make_video(user_id, text, template_number):


    # Path to the video
    file_path = os.path.join(os.getcwd(), 'whatIsLove')
    video_path = os.path.join(file_path, 'uploads')
    created_video_path = os.path.join(file_path, 'created')
    video_path_file = os.path.join(video_path, f'{template_number}.mp4')

    # cheking path if it is aviable
    

    # Wrap the text every 20 or 27 characters
    wrapped_text = textwrap.fill(text, 35)  # Adjust the line length as needed

    video = VideoFileClip(video_path_file)
    vid_duration = video.duration

    # it returns (width, height) on the list
    vid_size = video.size

    # gets proper font size like in this example: 720/20=36px or 300/20=15px
    font_size = vid_size[0] / 18

    txt_clip = (TextClip(wrapped_text, stroke_width=1.5, bg_color='black', font="Tahoma", fontsize=font_size, color='white', kerning=2)
                    .set_position('center')
                    .set_duration(vid_duration))

    result = CompositeVideoClip([video, txt_clip])
    result.write_videofile(os.path.join(created_video_path, f'{user_id}.mp4'), fps=30)

