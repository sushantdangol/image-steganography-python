from PIL import Image
import numpy as np

# Split the text into characters and store them in a list
def split(text):
    return [char for char in text]

#convert the characters into their respective ASCII Value
def str_to_asc(text):
    list = []

    for asc in text:
        list.append(ord(asc))

    return list

#convert ascii to string
def asc_to_str(text):
    list = []

    for st in text:
        list.append(chr(st))

    return list

#Convert the ASCII Values into binary
def asc_to_bin(asc):
    list = []

    for bin in asc:
        list.append("{0:08b}".format(bin))

    return list

def img_to_rgb(img):
    return np.array( img)

#Store the ASCII/String and its respective binary number in pairs
def asc_bin():
    # dict_a = {}
    list_a = []

    for bin_code, y in zip([char for char in bin_list], split_text):
        list_a.append( (y, [char for char in bin_code]) )
        # dict_a.update( {y: [char for char in bin_code]} )

    return list_a
    # return dict_a

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
    return np.array(list_def, dtype=np.uint8).reshape(img_rgb.shape) #add dtype to convert fron int32 to uint8


'''
Intit Code
'''

#Enter the text to be inserted.
text_message = input('Enter the text:')

#import image
new_img = Image.open('D:\original.jpeg')

'''Assigning variable to the converted lists'''
split_text = split(text_message) #variable to store the characters that were splitted
asc_list = str_to_asc(split_text) #variable to store ascii converted values
bin_list = asc_to_bin(asc_list) #variable to store binary converted values

img_rgb = img_to_rgb(new_img) #variable to store the list on rgb values from the image
img_bin = rgb_to_bin(img_rgb) #variable to store the list of binary value from rgb
rgb_bin = bin_to_rgb(img_bin) #varialble to store the list of rgb values from binary


# print(asc_bin())
# print(asc_to_bin(asc_list))s


'''Check if the original values and converted values match or not'''
# print(img_bin)
# print(rgb_bin)
# print('----------------------------------------------------------------')
# print(img_rgb)

'''To find the data type of the arrays'''
# print(rgb_bin.dtype)#data type of converted array
# print('----------------------------------------------------------------')
# print(img_rgb.dtype)#data type of original array
#############################################################


'''Save the encrypted Image'''
# modi_img = Image.fromarray(rgb_bin)
# modi_img.save('D:\modified222.jpeg')
# print('Image has been Encrypted')
