import random
import urllib.request
import urllib.error
import json
import config

user_agent = "Pandora-bot 1.0.0"

def gen_url(tags):
    tags = tags.replace(" ","+")
    url = config.base_donmai_url + "/posts/random.json?tags=" + tags
    return url

def get_json(url):
    header={"User-agent": user_agent}
    req = urllib.request.Request(url=url, headers=header)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        return None
    except urllib.error.URLError as e:
        return None
    else:
        data = json.loads(response.read().decode("utf-8"))
        return data

def get_image_url(json_file):
    if "success" not in json_file:
        if "file_url" in json_file:
            if "large_file_url" in json_file and ".zip" in json_file["file_url"] and ".zip" not in json_file["large_file_url"]:
                url = "Id:" + str(json_file["id"]) + "\n" + config.base_donmai_url + json_file["large_file_url"]
                return url
            elif ".zip" not in json_file["file_url"]:
                url = "Id:" + str(json_file["id"]) + "\n" + config.base_donmai_url + json_file["file_url"]
                return url
            else:
                return None
        else:
            return None
    else:
        return None

async def get_random_img(tags):
    json = get_json(gen_url(tags))
    if json is None:
        return "Sorry master... I could not find the image"
    url = get_image_url(json)
    if url is None:
        return "Sorry master... I could not load the image"
    return url
