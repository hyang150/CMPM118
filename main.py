## Importing Necessary Modules

import shutil  # to save it locally
import requests  # to get image from the web

# Global variables
Hair_id = int();
Nose_id = int();
body_id = int();
Bottom_id = int();
ear_id = int();

"""
Original Url:https://preview.bitmoji.com/avatar-builder-v3/preview/hair?scale=3
&gender=2
&style=5
&rotation=0
&body=7
&bottom=137
&brow=1574
&clothing_type=1
&ear=1430
&eye=1616
&eyelash=-1
&face_proportion=1
&footwear=0
&hair=1303
&is_tucked=0
&jaw=1407
&mouth=2340
&nose=1500
&pupil=2152
&top=54
"""
# Set up the image URL and filename
image_url_Ori = "https://preview.bitmoji.com/avatar-builder-v3/preview/hair?" \
            "scale=3" \
            "&gender=2" \
            "&style=5" \
            "&rotation=0" \
            "&body=7" \
            "&bottom=137" \
            "&brow=1574" \
            "&clothing_type=1" \
            "&ear=1430" \
            "&eye=1616" \
            "&eyelash=-1" \
            "&face_proportion=1" \
            "&footwear=0" \
            "&hair=1303" \
            "&is_tucked=0" \
            "&jaw=1407" \
            "&mouth=2340" \
            "&nose=1491" \
            "&pupil=2152" \
            "&top=54"


def hair_replace():
	for i in range(1300, 1400):
		str_hair_replace = str("hair=" + str(i))
	print(str_hair_replace)
	return str_hair_replace;


str_image_text_Dealed = image_url_Ori.replace("hair=1303", hair_replace());
print("str_image_text_Dealed",str_image_text_Dealed)
filename = image_url_Ori.split("/")[-1]

# do something for spilit the correct Part of the code.
print("filename",filename)

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(str_image_text_Dealed, stream=True)

if __name__ == "__main__":
	# Check if the image was retrieved successfully
	for i in range(1300, 1500):
		if r.status_code == 200:
			print("success at hair case" ,i)
			output_file_name = "default_face"+ filename + "hair" + i;
		# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
			r.raw.decode_content = True
		# Open a local file with wb ( write binary ) permission.
			with open(output_file_name, 'wb') as f:
				shutil.copyfileobj(r.raw, f)
				print('Image sucessfully Downloaded: ', filename)
		elif r.status_code == 400:
			print("bad request code" );
		else:
			print('Image Couldn\'t be retreived')
