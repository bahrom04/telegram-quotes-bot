import os

def get_photo_list():
    file_path = os.path.join(os.getcwd(), 'whatIsLove')

    template_photo = os.path.join(file_path, 'template_photo')

    photo_list = os.listdir(template_photo)
    photo_lists = [x for x in photo_list if x.endswith('.png')]

    return template_photo + '/' + '1.png'


