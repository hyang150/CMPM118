## Importing Necessary Modules
import shutil  # to save it locally
import requests  # to get image from the web
import os #use OS lib to create
import json

#Global variables
Nose_Dictionary = {"Nose" : []}
Ear_Dictionary = {"Ear":[]}
Eye_Dictionary = {"Eye":[]}
"""
Original Url:
https://preview.bitmoji.com/avatar-builder-v3/preview/hair?
scale=3
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

def nose_replace():
	"""
	This is the nose replace funtion
	it will replace all the nose on the default faces from orginal link

	:return: it does not return anything, but it will generate the files
	"""
	try:
		os.mkdir('result');
	except FileExistsError:
		print("folder already exists");
	
	try:
		os.mkdir("result/nose_result");
	except FileExistsError:
		print("folder already exists");
	
	for i in range(1434, 2000):# The range here could be changed to check every number.
		str_nose_replace = str("nose=" + str(i)); #replace the string in the url
		print(str_nose_replace);
		str_image_text_Dealed = image_url_Ori.replace("nose=1491", str_nose_replace);
		r = requests.get(str_image_text_Dealed, stream=True);
		if r.status_code == 200:
			print("success get nose case", i);
			Nose_Dictionary["Nose"].append(i); #update the list
			output_file_name = "result/nose_result/"+"default_face" + "_nose_" + str(i) + ".png";
			# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
			r.raw.decode_content = True;
			# Open a local file with wb ( write binary ) permission.
			with open(output_file_name, 'wb') as f:
				shutil.copyfileobj(r.raw, f)
				print('Image sucessfully Downloaded: ', output_file_name);
		elif r.status_code == 400:
			print("bad request code for nose ", i);
		else:
			print('Image Couldn\'t be retreived');
	Nose_json_data = json.dumps(Nose_Dictionary)
	Json_file = "Nose.json"
	with open(Json_file,"wb") as f:
		f.write(Nose_json_data);
		print("succssful create the Json of Nose")
			

if __name__ == "__main__":
	# Check if the image was retrieved successfully
	nose_replace();
