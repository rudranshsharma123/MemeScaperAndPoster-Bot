from instabot import Bot
import PIL
import PIL.Image 
import shutil
import os
# shutil.rmtree("C:/Users/gaura/Desktop/config")
userName = 'your username'
passWord = 'your passwords'

class instagramBot():
    def __init__(self, bot):
        self.bot = bot
    
    def correct_ratio(self, photo):
        '''
        Uuse this function to get the correct aspect ration and the image size needed for the instabot lib to post on InstaGram. 
        '''
        
        from instabot.api.api_photo import compatible_aspect_ratio, get_image_size

        return compatible_aspect_ratio(get_image_size(photo))
    
#     def prepare_and_fix_photo(self, photo):
#         with open(photo, "rb") as f:
#             img = PIL.Image.open(f)
#             img = strip_exif(img)
#             if not correct_ratio(photo):
#                 img = crop_maximize_entropy(img)
#             photo = os.path.join(tempfile.gettempdir(), "instacron.jpg")
#             img.save(photo)
#         return photo

#     def strip_exif(self, img):
#         """Strip EXIF data from the photo to avoid a 500 error."""
#         data = list(img.getdata())
#         image_without_exif = PIL.Image.new(img.mode, img.size)
#         image_without_exif.putdata(data)
#         return image_without_exif

#     def crop_maximize_entropy(self, img, min_ratio=4 / 5, max_ratio=90 / 47):
#         from scipy.optimize import minimize_scalar

#         w, h = img.size
#         data = np.array(img)
#         ratio = w / h
#         if ratio > max_ratio:  # Too wide
#             w_max = int(max_ratio * h)

#             def _crop(x):
#                 return crop(x, y=0, data=data, w=w_max, h=h)

#             xy_max = w - w_max
#         else:  # Too narrow
#             h_max = int(w / min_ratio)

#             def _crop(y):
#                 return crop(x=0, y=y, data=data, w=w, h=h_max)

#             xy_max = h - h_max

#         to_minimize = lambda xy: -_entropy(_crop(xy))  # noqa: E731
#         x = minimize_scalar(to_minimize, bounds=(0, xy_max), method="bounded").x
#         return PIL.Image.fromarray(_crop(x))
    
    def post_on_page(self, images:list):
        '''
        Use this funciton to log into Instagram and post the content you want to.
        '''
        
        self.bot.login(username=userName, password=passWord)
        for i in images:
            # shutil.rmtree("C:/Users/gaura/Desktop/Reddit Proj/config")
            allowed_image_extensions = ['.jpg', '.jpeg', '.png']
            allowed_gif_extensions = ['.gif']
            path = i
            _, ext = os.path.splitext(i)
            # print(ext in allowed_gif_extensions, ext in allowed_image_extensions)
            if ext in allowed_gif_extensions or ext in allowed_image_extensions:
                
                im=PIL.Image.open(path)
                im=im.resize((598,598))
                im.save(path)
                self.bot.upload_photo(path, caption="I am bot")



# path = "https://i.redd.it/zb2iebry8wx61.png"
# im=PIL.Image.open(path)
# im=im.resize((598,598))
# im.save(path)

# myBot = Bot()
# # myBot.login(ask_for_code=True)
# myBot.login(username=userName, password=passWord)

# myBot.upload_photo(path, caption="I am Bot")
