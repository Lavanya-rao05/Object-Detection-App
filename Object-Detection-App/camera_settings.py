import os
import cv2

attrib_list = {
    'exposure': cv2.CAP_PROP_EXPOSURE,
    'contrast': cv2.CAP_PROP_CONTRAST
}

def check_settings():
    VIDEO_CHECK = cv2.VideoCapture(0)

    if not os.path.exists('camera_settings.log'):
        with open('camera_settings.log', 'w') as f:
            for attrib, index in attrib_list.items():
                f.write(f'{attrib} = {VIDEO_CHECK.get(index)}\n')
    else:
        with open('camera_settings.log', 'r') as f:
            lines = f.read().split('\n')
            for line in lines:
                if line.strip():  # Skip empty lines
                    attrib, value = line.split(' = ')
                    if attrib in attrib_list:
                        try:
                            VIDEO_CHECK.set(attrib_list[attrib], float(value))
                        except ValueError:
                            print(f"Error setting {attrib} with value {value}")

    print('*'*28)
    print('* Checking camera settings *')
    print('*'*28)
    for attrib, index in attrib_list.items():
        print(f'{attrib} = {VIDEO_CHECK.get(index)}')

    VIDEO_CHECK.release()

def reset_settings():
    if not os.path.exists('camera_settings.log'):
        print('"camera_settings.log" does not exist!')
        print('Verify your camera settings!')
        return False

    VIDEO_CHECK = cv2.VideoCapture(0)
    with open('camera_settings.log', 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            if line.strip():  # Skip empty lines
                attrib, value = line.split(' = ')
                if attrib in attrib_list:
                    try:
                        VIDEO_CHECK.set(attrib_list[attrib], float(value))
                    except ValueError:
                        print(f"Error resetting {attrib} with value {value}")

    VIDEO_CHECK.release()
    return True
# import os
# import cv2

# attrib_list = {
#     'exposure': cv2.CAP_PROP_EXPOSURE,
#     'contrast': cv2.CAP_PROP_CONTRAST
# }

# def check_settings():
#     VIDEO_CHECK = cv2.VideoCapture(0)

#     if not os.path.exists('camera_settings.log'):
#         f = open('camera_settings.log', 'w')
#         for attrib, index in attrib_list.items():
#             f.writelines(f'{attrib} = {VIDEO_CHECK.get(index)}\n')
#         f.close()

#     else:
#         f = open('camera_settings.log', 'r')
#         lines = f.read().split('\n')
#         for line in lines:
#             attrib = line.split(' = ')
#             if attrib[0] in attrib_list.keys():
#                 VIDEO_CHECK.set(attrib_list[attrib[0]], eval(attrib[1]))
#         f.close()
    
#     print('*'*28)
#     print('* Checking camera settings *')
#     print('*'*28)
#     for attrib, index in attrib_list.items():
#         print(f'{attrib} = {VIDEO_CHECK.get(index)}')

#     VIDEO_CHECK.release()

# def reset_settings():
#     if not os.path.exists('camera_settings.log'):
#         print('"camera_settings.log" does not exist!')
#         print('Verify your camera settings!')
#         return False
#     else:
#         VIDEO_CHECK = cv2.VideoCapture(0)
#         f = open('camera_settings.log', 'r')
#         lines = f.read().split('\n')
#         for line in lines:
#             attrib = line.split(' = ')
#             if attrib[0] in attrib_list.keys():
#                 VIDEO_CHECK.set(attrib_list[attrib[0]], eval(attrib[1]))
#         f.close()
#         VIDEO_CHECK.release()
#     return True


