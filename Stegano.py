from PIL import Image
import numpy as np

def split(text):
    #Split the text into characters and store them in a list
    return [char for char in text]

def str_to_asc(text):
    #convert the characters into their respective ASCII Value
    list = []

    for asc in text:
        list.append(ord(asc))

    return list

def asc_to_bin(asc):
    #Convert the ASCII Values into binary
    list = []

    for bin in asc:
        list.append("{0:08b}".format(bin))

    return list

def img_to_rgb(img):
    return np.array( img)

'''
Intit Code
'''

#Enter the text to be inserted.
text_message = input('Enter the text:')

split_text = split(text_message)
asc_list = str_to_asc(split_text)
bin_list = asc_to_bin(asc_list)

new_img = Image.open('D:\original.jpeg')
img_rgb = img_to_rgb(new_img)

#Store the ASCII/String and its respective binary number in pairs
def asc_bin():
    # dict_a = {}
    list_a = []

    for bin_code, y in zip([char for char in bin_list], split_text):
        list_a.append( (y, [char for char in bin_code]) )
        # dict_a.update( {y: [char for char in bin_code]} )

    return list_a
    # return dict_a

# print(asc_bin())
# print(asc_to_bin(asc_list))

#convert rgb values into binary
def rgb_to_bin(img):

    list_def = []

    for x in np.nditer(img):
        list_def.append("{0:08b}".format(x))

    return np.array(list_def).reshape(img_rgb.shape)

#convert binary into rgb values
def bin_to_rgb(img):
    list_def = []

    for x in np.nditer(img):
        list_def.append(int(str(x), 2))

    # new_array = np.array(list_def).astype(int).reshape(img_rgb.shape)
    # return new_array
    return np.array(list_def).reshape(img_rgb.shape)

img_bin = rgb_to_bin(img_rgb)
rgb_bin = bin_to_rgb(img_bin)

# print(img_bin)
print(rgb_bin)

# modi_img = Image.fromarray(img_rgb)
# modi_img.save('D:\modified.jpeg')
# print(img_rgb.shape)