from flask import Flask, request,jsonify
from utils.torch_utils import transform_image, get_prediction
app = Flask(__name__)
# now we define the allowed_file function

ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}
def allowed_file(filename):
    # xxx.png example of file name
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error':'no file was loaded'})
        #we also verify the supported file type as follow
        if not allowed_file(file.filename):
            return jsonify({'error':'format not supported'})
        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data ={'prediction':prediction.item(),'class_name':str(prediction.item())}
            return jsonify(data)
        except Exception as er:
            return jsonify({'error':er})
    else:
        return jsonify({'error':'only post method is accepted'})
        #return jsonify({'error':'eror during prediction'})
    # 1 load image
    # 2 image -->tensor
    # 3 prediction
    # 4 return json data
    #return jsonify({'result':1})
'''
if __name__=='__main__':
    app.run(debug=True)
'''