"""
トップページに画像アップロードフォームが表示され、
アップロード後「判定」ボタンをクリックすると、
結果が表示されるような「predict」関数を作成
"""
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import classify_image
from PIL import Image
import numpy as np

def predict(request):
    #GET: データを取得（読み取り）するとき。ページの読み込みやフォームの初期表示。
    #主な用途: ページの表示や検索結果の取得
    if request.method == 'GET':
        form = ImageUploadForm()
        return render(request, 'home.html', {'form': form})
    #POST: データを送信（書き込み）するとき。フォームの送信や画像のアップロードなど。
    #サーバーにデータを送信するためのリクエスト
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
           #画像を取得して前処処理
            img_file = form.cleaned_data['image']
            image = Image.open(img_file).resize((224,224))
            image_array = np.array(image).reshape((1,224,224,3))

            #classify_image：画像判定をする関数
            results = classify_image(image_array)
            #予測結果を処理して適切な形式に変換
            predictions = process_results(results)  # ここでresultsを処理して`predictions`を得る
            img_data = request.POST.get('img_data')
            return render(request, 'home.html', {'form': form, 'predictions': predictions, 'img_data': img_data})
    else:
        form = ImageUploadForm()
        return render(request, 'home.html', {'form': form})
    
def process_results(results):    
# デコードされた結果の最初のリストを取得
    top_predictions = results[0]
    # 結果をフォーマットして人間が読める形式にする
    formatted_predictions = []
    for class_id, class_name, confidence in top_predictions:
        # 確率をパーセンテージに変換しフォーマット
        formatted_predictions.append((class_name, confidence * 100))
    # フォーマットされたリストを返す
    return formatted_predictions


