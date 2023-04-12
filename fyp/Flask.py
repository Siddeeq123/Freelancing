
import flask,jsonify
import werkzeug
import time
import os
import  demo
from test_gradel
app = flask.Flask(__name__)

@app.route('/upload', methods=['POST'])
def handle_request():
    #result=predictOutput("D:/comsats project/AI part/fyp/2.JPG")
    print("here1")
    files_ids = flask.request.files.getlist("file")
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d")

        path = "testinmges/"+timestr

        isFile = os.path.exists(path)
        print(isFile)
        if isFile==False:
            os.mkdir("testinmges/"+timestr)
        timestr2 = time.strftime("%Y%m%d-%H%M%S")
        imagefile.save("testinmges/"+timestr+"/"+timestr2+'_'+filename)
        image_num = image_num + 1
        print("aaaaaaaaaaaaaa")
    # result=predictOutput("testinmges/"+timestr+"/"+timestr2+'_'+filename)
    result = demo.predictOutputs("testinmges/"+timestr+"/"+timestr2+'_'+filename)
    return result
@app.route('/demo', methods=['POST','GET'])
def fun():
    result="demo.predictOutputs(img)"
    return result


@app.route('/',methods=['POST'])
def index():
    return  "hellow"
   # # if request.method == "POST":
   #  imagefile=request.files['image']
   #  filename =werkzeug.utils.secure_filename(imagefile.filename)
   #  imagefile.save("./fyp/"+filename)
   #  return  jsonify({
   #      "message":"image uploaded "
   #  })



    # print("asdfd")
    # files_ids = flask.request.files.getlist("file")
    # return filename

