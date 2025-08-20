# 私のWebサーバー

Google Cloud Platformのサンプルコードを基に作成された、モダンなWebサーバーです。

## 🚀 機能

- **レスポンシブデザイン**: モバイル、タブレット、デスクトップに対応
- **RESTful API**: JSON形式のAPIエンドポイント
- **モダンなUI**: グラデーションとガラスモーフィズムを使用した美しいデザイン
- **Google Cloud対応**: App Engineに簡単にデプロイ可能

## 🛠️ 技術スタック

- **バックエンド**: Flask (Python 3.12)
- **フロントエンド**: HTML5, CSS3, JavaScript
- **デプロイ**: Google Cloud App Engine
- **WSGIサーバー**: Gunicorn

## 📁 プロジェクト構造

```
home-server/
├── main.py              # メインアプリケーションファイル
├── requirements.txt     # Python依存関係
├── app.yaml            # Google Cloud App Engine設定
├── Dockerfile          # Docker設定
└── README.md           # このファイル
```

## 🏃‍♂️ ローカル実行

### 前提条件

- Python 3.12以上
- pip（Pythonパッケージマネージャー）

### セットアップ

1. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

2. アプリケーションを実行:
```bash
python main.py
```

3. ブラウザでアクセス:
```
http://localhost:8080
```

## 🌐 利用可能なエンドポイント

### Webページ
- `/` - ホームページ
- `/about` - 概要ページ
- `/contact` - お問い合わせページ

### APIエンドポイント
- `GET /api/status` - サーバーステータス
- `POST /api/contact` - お問い合わせ送信
- `GET /api/users` - ユーザー一覧（サンプル）

## ☁️ Google Cloud App Engineへのデプロイ

### 前提条件

- Google Cloud SDKがインストールされている
- Google Cloudプロジェクトが作成されている
- App Engine APIが有効になっている

### デプロイ手順

1. Google Cloud SDKでログイン:
```bash
gcloud auth login
```

2. プロジェクトを設定:
```bash
gcloud config set project YOUR_PROJECT_ID
```

3. アプリケーションをデプロイ:
```bash
gcloud app deploy
```

4. ブラウザでアクセス:
```bash
gcloud app browse
```

## 🐳 Docker実行

### Dockerイメージのビルド
```bash
docker build -t my-web-server .
```

### Dockerコンテナの実行
```bash
docker run -p 8080:8080 my-web-server
```

## 🎨 デザイン特徴

- **グラデーション背景**: 美しい紫から青へのグラデーション
- **ガラスモーフィズム**: 半透明のガラス効果
- **レスポンシブナビゲーション**: すべてのデバイスに対応
- **ホバーエフェクト**: インタラクティブな要素

## 📝 ライセンス

このプロジェクトはApache License 2.0の下で公開されています。

## 🤝 貢献

プルリクエストやイシューの報告を歓迎します！

## 📞 サポート

ご質問やご意見がございましたら、お気軽にお問い合わせください。
