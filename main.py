## Importing Necessary Modules
import json
import os  # use OS lib to create
import shutil  # to save it locally
import requests  # to get image from the web

# Global variables
Output_Dictionary = {}

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

word_range_list = ["scale=3",
                   "&gender=2",
                   "&style=5",
                   "&rotation=0",
                   "&body=7",
                   "&bottom=137",
                   "&brow=1574",
                   "&clothing_type=1",
                   "&ear=1430",
                   "&eye=1616",
                   "&eyelash=-1",
                   "&face_proportion=1",
                   "&hair=1303",
                   "&is_tucked=0",
                   "&jaw=1407",
                   "&mouth=2340",
                   "&nose=1491",
                   "&pupil=2152",
                   "&top=54"]

word_list = ['scale', 'gender', 'style', 'rotation', 'body',
             'bottom', 'brow', 'clothing_type', 'ear', 'eye',
             'eyelash', 'face_proportion', 'hair',
             'is_tucked', 'jaw', 'mouth', 'nose', 'pupil', 'top']


def replacement():
    """This is the nose replace funtion.
	it will replace all the nose on the default faces from orginal link
	:return: it does not return anything, but it will generate the files
	"""

    try:
        os.mkdir('result');
    except FileExistsError:
        print("folder already exists");

    word_list_total = word_list;

    for j in range(1,len(word_list_total)):
        #from 1 becasue scale do not need change
        face_part = word_list[j];
        word_need_replace = word_range_list[j]

        dir_text = "result/" + face_part;

        try:
            os.mkdir(dir_text);
        except FileExistsError:
            print("folder already exists");
        Output_Dictionary.update({face_part: []});

        print("Output_Dictionary",Output_Dictionary)
        print("start to work with", dir_text);
        ##################################################################

        ##ilterate the whole range of the code.
        for i in range(1999, 2000):  # The range here could be changed to check every number.

            str_replace = str("&" + face_part + "=" + str(i));  # replace the string in the url
            print("str_replace",str_replace);

            str_image_text_Dealed = image_url_Ori.replace(word_need_replace, str_replace);
            print("str_image_text_Dealed",str_image_text_Dealed)
            r = requests.get(str_image_text_Dealed, stream=True);

            if r.status_code == 200:
                print("success get nose case", i);
                output_file_name = "result/"+ face_part + "/default_face" + str(i) + ".png";

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
        json_file_data = json.dumps(Output_Dictionary)
        json_file_name = "Nose.json"
        with open(json_file_name, "w") as f:
            f.write(json_file_data);
            print("succssful create the Json of Nose")


if __name__ == "__main__":
    # Check if the image was retrieved successfully
    print("the length of word range list is", len(word_range_list))
    print("the length of replace word", len(word_list))
    replacement()
