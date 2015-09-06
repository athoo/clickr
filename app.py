from flask import Flask, make_response
import os
import json
from functools import wraps

def allow_cross_domain(fun):
	@wraps(fun)
	def wrapper_fun(*args, **kwargs):
		rst = make_response(fun(*args, **kwargs))
		rst.headers['Access-Control-Allow-Origin'] = '*'
		rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
		allow_headers = "Referer,Accept,Origin,User-Agent"
		rst.headers['Access-Control-Allow-Headers'] = allow_headers
		return rst
	return wrapper_fun


app = Flask(__name__)

@app.route("/")
@allow_cross_domain
def hello():
    return "Hello World!"

@app.route("/api/v1/data/<data_name>")
@allow_cross_domain
def host_data(data_name):
    path_to_data = "data/" + data_name + ".json"
    with open(path_to_data) as f:
        data = json.load(f)
        print data
    json_data = json.dumps(data)
    return str(json_data)

# @app.route('/task_name/<task_name>')
# @allow_cross_domain
# def query_task(task_name):
#     ongoing_imgs=[]
#     task_photos = flickr.photos.search(text=task_name)
#     for item in task_photos['photos']['photo'][:]:
#         farm_id = item['farm']
#         server_id = item['server']
#         pic_id = item['id']
#         secret = item['secret']
#         url = "https://farm{}.staticflickr.com/{}/{}_{}.jpg".format(farm_id,server_id,pic_id,secret)
#         ongoing_imgs.append(url)
#     json_imgs = json.dumps(ongoing_imgs)
#     return str(json_imgs)
#
# @app.route('/img_id/<img_id>')
# @allow_cross_domain
# def get_tags(img_id):
# #     return "hello%s"%img_id
#     tags_cloud=[]
#     tags = flickr.tags.getListPhoto(photo_id=img_id)
#     for tag in tags['photo']["tags"]["tag"]:
#         tags_cloud.append(tag['_content'])
# #     json_tags = json.dumps(tags_cloud)
# #     return json_tags
#     json_tags = json.dumps(tags_cloud)
#     return json_tags


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
