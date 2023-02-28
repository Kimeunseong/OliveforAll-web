import io
import os
from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from bson.binary import Binary
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# app = Flask(__name__, template_folder='./templates/html/', static_folder='./static/', static_url_path='/static/')
app = Flask(__name__)


# MongoDB 연결
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@3.36.96.232', 27017) # AWS 서버 연결
db = client.dballstar

# 업로드된 이미지 파일을 저장할 경로
app.config['UPLOAD_PATH'] = 'uploads'

# 허용할 이미지 파일 확장자 목록
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'jpeg', 'png', 'JPEG', 'JPG', "PNG"])

# 업로드된 이미지 파일의 최대 크기 (5MB)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


def allowed_file(filename):
    """
    허용된 파일인지 검사하는 함수
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def predict_model(model, imgName):
    """
    모델 로드하는 함수
    """
    img_path = 'uploads/' + imgName
    # UserImage = load_img(img_path, target_size=(200, 150))
    UserImage = load_img(img_path, target_size=(100, 75))

    UserImage = img_to_array(UserImage)
    UserImage = UserImage.reshape(-1, 100, 75, 3)
    # UserImage = UserImage.reshape(-1, 200, 150, 3)
    UserImage = UserImage / 255.0
    prediction = model.predict(UserImage)
    classNumber = str(np.argmax(prediction))
    return classNumber

def delete_image(imgName):
    """
    predict하고 나서 필요없는 이미지를 삭제하는 함수
    """
    if os.path.isfile('uploads/' + imgName):
        os.remove('uploads/' + imgName)
    return 'okay'

@app.route('/')
def index():
    """
    인덱스 페이지
    """
    # return render_template('index2.html')
    return render_template('./html/MainPage.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    파일 업로드 페이지
    """
    if request.method == 'POST':
        # 파일이 업로드되었는지 확인
        if 'photo' not in request.files:
            return redirect(request.url)
        photo = request.files['photo']
        # 파일이 비어있는지 확인
        if photo.filename == '':
            return redirect(request.url)
        # 허용된 파일인지 확인
        if not allowed_file(photo.filename):
            error = 'Only JPG, JPEG, PNG, and GIF files are allowed.'
            # return render_template('upload2.html', error=error)
            return render_template('./html/ImageUpload.html', error=error)
        
        # 메모리에 파일 저장
        os.makedirs(app.config['UPLOAD_PATH'], exist_ok=True)  # 경로 생성
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        # 파일 데이터를 바이너리 형식으로 변환
        file_data = Binary(photo.read())
        # MongoDB에 파일 데이터 저장
        db.photos.insert_one({'filename':filename, 'data': file_data})

        # 모델에 이미지 넣고 predict
        print(predict_model(model, filename))
        prodNumber = predict_model(model, filename)
        result = db.prodInfo_review.find_one({'num':int(prodNumber)}, {'_id':False})
        # 예측 확인 후 메모리 속 이미지는 삭제하기
        delete_image(filename)
        
        # return render_template('prod_info3.html', result=result)
        return render_template('./html/ProductInfoPage.html', result=result)
    return render_template('./html/ImageUpload.html')


@app.route('/photo/<photo_id>')
def show_image(photo_id):
    """
    MongoDB에서 이미지 데이터를 불러와서 웹 페이지에 표시하는 함수
    """
    # MongoDB에서 파일 데이터 불러오기
    photo = db.photos.find_one({'_id': ObjectId(photo_id)})
    # 바이너리 데이터 디코딩
    file_data = photo['data'].decode()
    # 이미지 데이터를 웹 페이지에 전송
    return send_file(io.BytesIO(file_data), mimetype='image/jpeg')

@app.route('/photo/<photo_id>')
def view_photo(photo_id):
    photo = db.photos.find_one({'_id': ObjectId(photo_id)})
    return render_template('./html/ProductInfoPage.html', photo=photo)

@app.route('/prodinfo')
def view_prodInfo():
    """
    제품 상세 페이지
    """
    return render_template('./html/ProductInfoPage.html')

if __name__ == '__main__':
    model = load_model('static/assets/model/final_model.h5')
    # model = load_model('static/assets/model/xception_best_model.h5')
    app.run('0.0.0.0', port=5000, debug=True)