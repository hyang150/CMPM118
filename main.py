## Importing necessary Modules
import json
import multiprocessing
import os  # use OS lib to create
import shutil  # to save it locally
import requests  # to get image from the web

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

"""
Global variables
"""

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
ear_dictionary = {"ear": []}
eyes_dictionary = {"eyes": []}
hair_dictionary = {"hair": []}
mouth_dictionary = {"mouth": []}
nose_dictionary = {"nose": []}
pupil_dictionary = {"pupil": []}
Output_dictionary = {"Output": []}


def ear_download():
    """
    This is the ear replace funtion
    it will replace all the ear on the default faces from orginal link
    :return: it does not return anything, but it will generate the files
    """
    try:
        os.mkdir('result')
    except FileExistsError:
        print("folder already exists");

    try:
        os.mkdir("result/ear_result");
    except FileExistsError:
        print("folder already exists");

    for i in range(1422, 1490):  # The range here could be changed to check every number.
        str_ear_replace = str("ear=" + str(i));  # replace the string in the url
        print(str_ear_replace);
        str_image_text_Dealed = image_url_Ori.replace("ear=1430", str_ear_replace)
        r = requests.get(str_image_text_Dealed, stream=True);
        if r.status_code == 200:
            print("success get ear case", i);
            ear_dictionary["ear"].append(i);  # update the list
            output_file_name = "result/ear_result/" + "default_face" + "ear_" + str(i) + ".png";
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True;
            # Open a local file with wb ( write binary ) permission.
            with open(output_file_name, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ', output_file_name);
        elif r.status_code == 400:
            print("bad request code for ear ", i);
            # time.sleep(random.random())# no ddos!
        else:
            print('Image Couldn\'t be retreived');
    ear_json_data = json.dumps(ear_dictionary)
    Json_file = "result/ear_result/ear.json"
    with open(Json_file, "w") as f:
        f.write(ear_json_data);
        print("succssful create the Json of ear")


def eye_download():
    """
    This is the eye replace funtion
    it will replace all the eye on the default faces from orginal link
    :return: it does not return anything, but it will generate the files
    """
    try:
        os.mkdir('result');
    except FileExistsError:
        print("folder already exists");

    try:
        os.mkdir("result/eyes_result");
    except FileExistsError:
        print("folder already exists");

    for i in range(0, 3000):  # The range here could be changed to check every number.
        str_eyes_replace = str("eyes=" + str(i));  # replace the string in the url
        print(str_eyes_replace);
        str_image_text_Dealed = image_url_Ori.replace("eyes=1616", str_eyes_replace);
        r = requests.get(str_image_text_Dealed, stream=True);
        if r.status_code == 200:
            print("success get eyes case", i);
            eyes_dictionary["eyes"].append(i);  # update the list
            output_file_name = "result/eyes_result/" + "default_face" + "eyes_" + str(i) + ".png";
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True;
            # Open a local file with wb ( write binary ) permission.
            with open(output_file_name, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ', output_file_name);
        elif r.status_code == 400:
            print("bad request code for eyes ", i);
        else:
            print('Image Couldn\'t be retreived');
    eyes_json_data = json.dumps(eyes_dictionary)
    Json_file = "result/eyes_result/eyes.json"
    with open(Json_file, "w") as f:
        f.write(eyes_json_data);
        print("succssful create the Json of eyes")


def hair_download():
    """
    This is the hair replace funtion
    it will replace all the hair on the default faces from orginal link
    :return: it does not return anything, but it will generate the files
    """
    try:
        os.mkdir('result');
    except FileExistsError:
        print("folder already exists");

    try:
        os.mkdir("result/hair_result");
    except FileExistsError:
        print("folder already exists");

    for i in range(1300, 5000):  # The range here could be changed to check every number.
        str_hair_replace = str("hair=" + str(i));  # replace the string in the url
        print(str_hair_replace);
        str_image_text_Dealed = image_url_Ori.replace("hair=1303", str_hair_replace);
        r = requests.get(str_image_text_Dealed, stream=True);
        if r.status_code == 200:
            print("success get hair case", i);
            hair_dictionary["hair"].append(i);  # update the list
            output_file_name = "result/hair_result/" + "default_face" + "_hair_" + str(i) + ".png";
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True;
            # Open a local file with wb ( write binary ) permission.
            with open(output_file_name, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ', output_file_name);
        elif r.status_code == 400:
            print("bad request code for hair ", i);
        else:
            print('Image Couldn\'t be retreived');
    hair_json_data = json.dumps(hair_dictionary)
    Json_file = "result/hair_result/hair.json"
    with open(Json_file, "w") as f:
        f.write(hair_json_data);
        print("succssful create the Json of hair")


def mouth_download():
    """
    This is the mouth replace funtion
    it will replace all the mouth on the default faces from orginal link
    :return: it does not return anything, but it will generate the files
    """
    try:
        os.mkdir('result');
    except FileExistsError:
        print("folder already exists");

    try:
        os.mkdir("result/mouth_result");
    except FileExistsError:
        print("folder already exists");

    for i in range(2127, 5000):  # The range here could be changed to check every number.
        str_mouth_replace = str("mouth=" + str(i));  # replace the string in the url
        print(str_mouth_replace);
        str_image_text_Dealed = image_url_Ori.replace("mouth=2340", str_mouth_replace);
        r = requests.get(str_image_text_Dealed, stream=True);
        if r.status_code == 200:
            print("success get mouth case", i);
            mouth_dictionary["mouth"].append(i);  # update the list
            output_file_name = "result/mouth_result/" + "default_face" + "_mouth_" + str(i) + ".png";
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True;
            # Open a local file with wb ( write binary ) permission.
            with open(output_file_name, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ', output_file_name);
        elif r.status_code == 400:
            print("bad request code for mouth ", i);
        else:
            print('Image Couldn\'t be retreived');
    mouth_json_data = json.dumps(mouth_dictionary)
    Json_file = "result/mouth_result/mouth.json"
    with open(Json_file, "w") as f:
        f.write(mouth_json_data);
        print("succssful create the Json of mouth")


def nose_download():
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

    for i in range(0, 6000):  # The range here could be changed to check every number.
        str_nose_replace = str("nose=" + str(i));  # replace the string in the url
        print(str_nose_replace);
        str_image_text_Dealed = image_url_Ori.replace("nose=1491", str_nose_replace);
        r = requests.get(str_image_text_Dealed, stream=True);
        if r.status_code == 200:
            print("success get nose case", i);
            nose_dictionary["nose"].append(i);  # update the list
            output_file_name = "result/nose_result/" + "default_face" + "_nose_" + str(i) + ".png";
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
    nose_json_data = json.dumps(nose_dictionary)
    Json_file = "result/nose_result/nose.json"
    with open(Json_file, "w") as f:
        f.write(nose_json_data);
        print("succssful create the Json of nose")


def pupil_download():
    """
    This is the pupil replace funtion
    it will replace all the pupil on the default faces from orginal link
    :return: it does not return anything, but it will generate the files
    """
    try:
        os.mkdir('result');
    except FileExistsError:
        print("folder already exists");

    try:
        os.mkdir("result/pupil_result");
    except FileExistsError:
        print("folder already exists");

    for i in range(0, 3000):  # The range here could be changed to check every number.
        str_pupil_replace = str("pupil=" + str(i));  # replace the string in the url
        print(str_pupil_replace);
        str_image_text_Dealed = image_url_Ori.replace("pupil=2152", str_pupil_replace);
        r = requests.get(str_image_text_Dealed, stream=True);
        if r.status_code == 200:
            print("success get pupil case", i);
            pupil_dictionary["pupil"].append(i);  # update the list
            output_file_name = "result/pupil_result/" + "default_face" + "_pupil_" + str(i) + ".png";
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True;
            # Open a local file with wb ( write binary ) permission.
            with open(output_file_name, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ', output_file_name);
        elif r.status_code == 400:
            print("bad request code for pupil ", i);
        else:
            print('Image Couldn\'t be retreived');
    pupil_json_data = json.dumps(pupil_dictionary)
    Json_file = "result/pupil_result/pupil.json"
    with open(Json_file, "w") as f:
        f.write(pupil_json_data);
        print("succssful create the Json of pupil")


def total_download():
    """
        This is the total replacement function.
	    it will replace all the face part on the default faces from orginal link
	    Ho
	    :return: it does not return anything, but it will generate the files
	"""

    try:
        os.mkdir('result');
    except FileExistsError:
        print("folder already exists");

    word_list_total = word_list;

    for j in range(1, len(word_list_total)):
        # from 1 because scale do not need change
        face_part = word_list[j];
        word_need_replace = word_range_list[j]

        dir_text = "result/" + face_part;

        try:
            os.mkdir(dir_text);
        except FileExistsError:
            print("folder already exists");
        Output_dictionary.update({face_part: []});

        print("Output_dictionary", Output_dictionary)
        print("start to work with", dir_text);
        ##################################################################

        ##ilterate the whole range of the code.
        for i in range(0, 30000):  # The range here could be changed to check every number.

            str_replace = str("&" + face_part + "=" + str(i));  # replace the string in the url
            print("str_replace", str_replace);

            str_image_text_Dealed = image_url_Ori.replace(word_need_replace, str_replace);
            print("str_image_text_Dealed", str_image_text_Dealed)
            r = requests.get(str_image_text_Dealed, stream=True);

            if r.status_code == 200:
                print("success get nose case", i);
                output_file_name = "result/" + face_part + "/default_face" + str(i) + ".png";

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
        json_file_data = json.dumps(Output_dictionary)
        json_file_name = "nose.json"
        with open(json_file_name, "w") as f:
            f.write(json_file_data);
            print("succssful create the Json of nose")


if __name__ == "__main__":
    # if len(word_range_list) == len(word_list):
    #   total_download();
    #p1 = multiprocessing.Process(target=ear_download());
    #p2 = multiprocessing.Process(target=eye_download());
    #p3 = multiprocessing.Process(target=hair_download());
    p4 = multiprocessing.Process(target=mouth_download());
    p5 = multiprocessing.Process(target=nose_download());
    p6 = multiprocessing.Process(target=pupil_download());
    #p1.start();
    #p2.start();
    #p3.start();
    p4.start();
    p5.start();
    p6.start();
