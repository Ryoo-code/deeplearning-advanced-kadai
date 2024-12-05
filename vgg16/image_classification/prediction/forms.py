#画像をアップロードする為のファイル
#formsモジュールをインポートする事でユーザーからの
#データ入力を管理できる便利なクラスなどが使用可能
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()