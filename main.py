from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    """ホームページを表示"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>川上家のサーバーページ</title>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%);
                color: #ffffff;
                min-height: 100vh;
                overflow-x: hidden;
            }}
            
            .stars {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 1;
            }}
            
            .star {{
                position: absolute;
                background: white;
                border-radius: 50%;
                animation: twinkle 3s infinite;
            }}
            
            @keyframes twinkle {{
                0%, 100% {{ opacity: 0.3; }}
                50% {{ opacity: 1; }}
            }}
            
            .container {{
                position: relative;
                z-index: 2;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            .header {{
                text-align: center;
                margin-bottom: 50px;
                padding: 40px 0;
            }}
            
            .title {{
                font-family: 'Orbitron', monospace;
                font-size: 3.5em;
                font-weight: 900;
                background: linear-gradient(45deg, #00d4ff, #ff6b6b, #4ecdc4, #45b7d1);
                background-size: 400% 400%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: gradientShift 4s ease-in-out infinite;
                text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
                margin-bottom: 20px;
            }}
            
            @keyframes gradientShift {{
                0%, 100% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
            }}
            
            .subtitle {{
                font-size: 1.3em;
                color: #b8c5d6;
                margin-bottom: 30px;
                font-weight: 300;
            }}
            
            .status-indicator {{
                display: inline-block;
                padding: 8px 20px;
                background: rgba(76, 175, 80, 0.2);
                border: 2px solid #4caf50;
                border-radius: 25px;
                color: #4caf50;
                font-weight: 600;
                animation: pulse 2s infinite;
            }}
            
            @keyframes pulse {{
                0% {{ box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.7); }}
                70% {{ box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }}
                100% {{ box-shadow: 0 0 0 0 rgba(76, 175, 80, 0); }}
            }}
            
            .nav {{
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-bottom: 50px;
                flex-wrap: wrap;
            }}
            
            .nav a {{
                color: white;
                text-decoration: none;
                padding: 15px 30px;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 30px;
                transition: all 0.3s ease;
                backdrop-filter: blur(10px);
                font-weight: 500;
                position: relative;
                overflow: hidden;
            }}
            
            .nav a::before {{
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
                transition: left 0.5s;
            }}
            
            .nav a:hover::before {{
                left: 100%;
            }}
            
            .nav a:hover {{
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }}
            
            .content-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 30px;
                margin-bottom: 50px;
            }}
            
            .card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 30px;
                backdrop-filter: blur(15px);
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }}
            
            .card::before {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #00d4ff, #ff6b6b, #4ecdc4);
                transform: scaleX(0);
                transition: transform 0.3s ease;
            }}
            
            .card:hover::before {{
                transform: scaleX(1);
            }}
            
            .card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
                background: rgba(255, 255, 255, 0.08);
            }}
            
            .card h3 {{
                font-family: 'Orbitron', monospace;
                font-size: 1.5em;
                margin-bottom: 15px;
                color: #00d4ff;
            }}
            
            .card p {{
                color: #b8c5d6;
                line-height: 1.6;
                margin-bottom: 15px;
            }}
            
            .feature-list {{
                list-style: none;
            }}
            
            .feature-list li {{
                padding: 8px 0;
                color: #b8c5d6;
                position: relative;
                padding-left: 25px;
            }}
            
            .feature-list li::before {{
                content: '🚀';
                position: absolute;
                left: 0;
                top: 8px;
            }}
            
            .footer {{
                text-align: center;
                padding: 40px 0;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                color: #b8c5d6;
            }}
            
            .server-time {{
                font-family: 'Orbitron', monospace;
                font-size: 1.1em;
                color: #4ecdc4;
                margin-top: 20px;
            }}
            
            .tech-stack {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 15px;
            }}
            
            .tech-tag {{
                background: rgba(0, 212, 255, 0.2);
                color: #00d4ff;
                padding: 5px 12px;
                border-radius: 15px;
                font-size: 0.9em;
                border: 1px solid rgba(0, 212, 255, 0.3);
            }}
            
            @media (max-width: 768px) {{
                .title {{
                    font-size: 2.5em;
                }}
                
                .nav {{
                    flex-direction: column;
                    align-items: center;
                }}
                
                .content-grid {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="stars" id="stars"></div>
        
        <div class="container">
            <div class="header">
                <h1 class="title">川上家のサーバーページ</h1>
                <p class="subtitle">次世代のWebサーバー技術で構築された、未来への扉</p>
                <div class="status-indicator">🟢 システム稼働中</div>
            </div>
            
            <div class="nav">
                <a href="/">🏠 ホーム</a>
                <a href="/about">📋 システム概要</a>
                <a href="/api/status">🔧 API</a>
                <a href="/contact">📧 お問い合わせ</a>
            </div>
            
            <div class="content-grid">
                <div class="card">
                    <h3>🚀 高性能サーバー</h3>
                    <p>Google Cloud Platformの最新技術を活用した、高速で安定したWebサーバーです。</p>
                    <ul class="feature-list">
                        <li>99.9%の稼働率保証</li>
                        <li>自動スケーリング対応</li>
                        <li>グローバルCDN配信</li>
                        <li>リアルタイム監視</li>
                    </ul>
                </div>
                
                <div class="card">
                    <h3>🎨 モダンデザイン</h3>
                    <p>最新のWebデザイントレンドを取り入れた、美しく使いやすいインターフェース。</p>
                    <ul class="feature-list">
                        <li>レスポンシブデザイン</li>
                        <li>ダークモード対応</li>
                        <li>アニメーション効果</li>
                        <li>アクセシビリティ配慮</li>
                    </ul>
                </div>
                
                <div class="card">
                    <h3>🔧 技術スタック</h3>
                    <p>最先端の技術を組み合わせて構築された、堅牢なシステム基盤。</p>
                    <div class="tech-stack">
                        <span class="tech-tag">Python 3.12</span>
                        <span class="tech-tag">Flask</span>
                        <span class="tech-tag">Google Cloud</span>
                        <span class="tech-tag">Docker</span>
                        <span class="tech-tag">Gunicorn</span>
                    </div>
                </div>
                
                <div class="card">
                    <h3>📊 リアルタイム統計</h3>
                    <p>サーバーの稼働状況とパフォーマンスをリアルタイムで監視・表示。</p>
                    <ul class="feature-list">
                        <li>CPU使用率監視</li>
                        <li>メモリ使用量追跡</li>
                        <li>レスポンス時間測定</li>
                        <li>エラー率監視</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer">
                <p>© 2024 川上家のサーバーページ - 未来を創造する技術</p>
                <div class="server-time">サーバー時刻: {current_time}</div>
            </div>
        </div>
        
        <script>
            // 星空エフェクト
            function createStars() {{
                const starsContainer = document.getElementById('stars');
                const starCount = 200;
                
                for (let i = 0; i < starCount; i++) {{
                    const star = document.createElement('div');
                    star.className = 'star';
                    star.style.left = Math.random() * 100 + '%';
                    star.style.top = Math.random() * 100 + '%';
                    star.style.width = Math.random() * 3 + 'px';
                    star.style.height = star.style.width;
                    star.style.animationDelay = Math.random() * 3 + 's';
                    starsContainer.appendChild(star);
                }}
            }}
            
            // ページ読み込み時に星空を作成
            window.addEventListener('load', createStars);
            
            // リアルタイム時刻更新
            function updateTime() {{
                const now = new Date();
                const timeString = now.toLocaleString('ja-JP');
                const timeElement = document.querySelector('.server-time');
                if (timeElement) {{
                    timeElement.textContent = 'サーバー時刻: ' + timeString;
                }}
            }}
            
            setInterval(updateTime, 1000);
        </script>
    </body>
    </html>
    """

@app.route("/about")
def about():
    """概要ページを表示"""
    return """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>システム概要 - 川上家のサーバーページ</title>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%);
                color: #ffffff;
                min-height: 100vh;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            
            .header {
                text-align: center;
                margin-bottom: 50px;
                padding: 40px 0;
            }
            
            .title {
                font-family: 'Orbitron', monospace;
                font-size: 3em;
                font-weight: 900;
                background: linear-gradient(45deg, #00d4ff, #ff6b6b, #4ecdc4);
                background-size: 400% 400%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: gradientShift 4s ease-in-out infinite;
                margin-bottom: 20px;
            }
            
            @keyframes gradientShift {
                0%, 100% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
            }
            
            .nav {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-bottom: 50px;
                flex-wrap: wrap;
            }
            
            .nav a {
                color: white;
                text-decoration: none;
                padding: 15px 30px;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 30px;
                transition: all 0.3s ease;
                backdrop-filter: blur(10px);
                font-weight: 500;
            }
            
            .nav a:hover {
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
            
            .content {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 40px;
                backdrop-filter: blur(15px);
                margin-bottom: 30px;
            }
            
            .section {
                margin-bottom: 40px;
            }
            
            .section h2 {
                font-family: 'Orbitron', monospace;
                font-size: 2em;
                color: #00d4ff;
                margin-bottom: 20px;
                border-bottom: 2px solid rgba(0, 212, 255, 0.3);
                padding-bottom: 10px;
            }
            
            .tech-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            
            .tech-item {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                transition: all 0.3s ease;
            }
            
            .tech-item:hover {
                transform: translateY(-5px);
                background: rgba(255, 255, 255, 0.08);
            }
            
            .tech-item h3 {
                color: #4ecdc4;
                margin-bottom: 10px;
            }
            
            .tech-item p {
                color: #b8c5d6;
                font-size: 0.9em;
            }
            
            .feature-list {
                list-style: none;
                margin-top: 15px;
            }
            
            .feature-list li {
                padding: 10px 0;
                color: #b8c5d6;
                position: relative;
                padding-left: 30px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            .feature-list li::before {
                content: '⚡';
                position: absolute;
                left: 0;
                top: 10px;
                color: #ff6b6b;
            }
            
            .footer {
                text-align: center;
                padding: 40px 0;
                color: #b8c5d6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1 class="title">📋 システム概要</h1>
            </div>
            
            <div class="nav">
                <a href="/">🏠 ホーム</a>
                <a href="/about">📋 システム概要</a>
                <a href="/api/status">🔧 API</a>
                <a href="/contact">📧 お問い合わせ</a>
            </div>
            
            <div class="content">
                <div class="section">
                    <h2>🛠️ 技術スタック</h2>
                    <div class="tech-grid">
                        <div class="tech-item">
                            <h3>Python 3.12</h3>
                            <p>最新のPythonランタイムで高速処理を実現</p>
                        </div>
                        <div class="tech-item">
                            <h3>Flask Framework</h3>
                            <p>軽量で柔軟なWebフレームワーク</p>
                        </div>
                        <div class="tech-item">
                            <h3>Google Cloud Platform</h3>
                            <p>世界最高水準のクラウドインフラ</p>
                        </div>
                        <div class="tech-item">
                            <h3>Docker</h3>
                            <p>コンテナ化による高効率デプロイ</p>
                        </div>
                        <div class="tech-item">
                            <h3>Gunicorn</h3>
                            <p>本番環境対応のWSGIサーバー</p>
                        </div>
                        <div class="tech-item">
                            <h3>HTML5/CSS3</h3>
                            <p>モダンなフロントエンド技術</p>
                        </div>
                    </div>
                </div>
                
                <div class="section">
                    <h2>🚀 システム機能</h2>
                    <ul class="feature-list">
                        <li><strong>レスポンシブWebデザイン</strong> - すべてのデバイスで最適な表示</li>
                        <li><strong>RESTful API</strong> - 標準的なAPI設計による高互換性</li>
                        <li><strong>リアルタイム監視</strong> - システム稼働状況の即座把握</li>
                        <li><strong>自動スケーリング</strong> - 負荷に応じた自動リソース調整</li>
                        <li><strong>セキュリティ強化</strong> - 最新のセキュリティ対策実装</li>
                        <li><strong>高速CDN配信</strong> - グローバルな高速アクセス</li>
                    </ul>
                </div>
                
                <div class="section">
                    <h2>📊 パフォーマンス指標</h2>
                    <ul class="feature-list">
                        <li><strong>応答時間</strong> - 平均50ms以下</li>
                        <li><strong>稼働率</strong> - 99.9%以上</li>
                        <li><strong>同時接続数</strong> - 10,000接続対応</li>
                        <li><strong>データ転送</strong> - 無制限</li>
                        <li><strong>バックアップ</strong> - 自動日次バックアップ</li>
                        <li><strong>障害復旧</strong> - RTO 15分以内</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer">
                <p>© 2024 川上家のサーバーページ - 次世代技術の実現</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/contact")
def contact():
    """お問い合わせページを表示"""
    return """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>お問い合わせ - 川上家のサーバーページ</title>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%);
                color: #ffffff;
                min-height: 100vh;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            
            .header {
                text-align: center;
                margin-bottom: 50px;
                padding: 40px 0;
            }
            
            .title {
                font-family: 'Orbitron', monospace;
                font-size: 3em;
                font-weight: 900;
                background: linear-gradient(45deg, #00d4ff, #ff6b6b, #4ecdc4);
                background-size: 400% 400%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: gradientShift 4s ease-in-out infinite;
                margin-bottom: 20px;
            }
            
            @keyframes gradientShift {
                0%, 100% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
            }
            
            .nav {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-bottom: 50px;
                flex-wrap: wrap;
            }
            
            .nav a {
                color: white;
                text-decoration: none;
                padding: 15px 30px;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 30px;
                transition: all 0.3s ease;
                backdrop-filter: blur(10px);
                font-weight: 500;
            }
            
            .nav a:hover {
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
            
            .content {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 40px;
                backdrop-filter: blur(15px);
                margin-bottom: 30px;
            }
            
            .form-group {
                margin-bottom: 25px;
            }
            
            .form-group label {
                display: block;
                margin-bottom: 8px;
                color: #00d4ff;
                font-weight: 600;
            }
            
            .form-group input,
            .form-group textarea {
                width: 100%;
                padding: 15px;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                color: white;
                font-size: 16px;
                transition: all 0.3s ease;
            }
            
            .form-group input:focus,
            .form-group textarea:focus {
                outline: none;
                border-color: #00d4ff;
                box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
            }
            
            .form-group input::placeholder,
            .form-group textarea::placeholder {
                color: rgba(255, 255, 255, 0.5);
            }
            
            .submit-btn {
                background: linear-gradient(45deg, #00d4ff, #4ecdc4);
                color: white;
                padding: 15px 40px;
                border: none;
                border-radius: 30px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            .submit-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(0, 212, 255, 0.4);
            }
            
            .contact-info {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 30px;
                backdrop-filter: blur(15px);
            }
            
            .contact-info h3 {
                color: #4ecdc4;
                margin-bottom: 20px;
                font-family: 'Orbitron', monospace;
            }
            
            .contact-item {
                display: flex;
                align-items: center;
                margin-bottom: 15px;
                padding: 10px 0;
            }
            
            .contact-item .icon {
                font-size: 1.5em;
                margin-right: 15px;
                color: #ff6b6b;
            }
            
            .contact-item .text {
                color: #b8c5d6;
            }
            
            .footer {
                text-align: center;
                padding: 40px 0;
                color: #b8c5d6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1 class="title">📧 お問い合わせ</h1>
            </div>
            
            <div class="nav">
                <a href="/">🏠 ホーム</a>
                <a href="/about">📋 システム概要</a>
                <a href="/api/status">🔧 API</a>
                <a href="/contact">📧 お問い合わせ</a>
            </div>
            
            <div class="content">
                <h2 style="color: #00d4ff; margin-bottom: 30px; font-family: 'Orbitron', monospace;">お問い合わせフォーム</h2>
                <p style="color: #b8c5d6; margin-bottom: 30px;">川上家のサーバーページについてご質問やご意見がございましたら、お気軽にお問い合わせください。</p>
                
                <form action="/api/contact" method="POST">
                    <div class="form-group">
                        <label for="name">お名前</label>
                        <input type="text" id="name" name="name" required placeholder="山田太郎">
                    </div>
                    
                    <div class="form-group">
                        <label for="email">メールアドレス</label>
                        <input type="email" id="email" name="email" required placeholder="example@email.com">
                    </div>
                    
                    <div class="form-group">
                        <label for="message">メッセージ</label>
                        <textarea id="message" name="message" rows="6" required placeholder="お問い合わせ内容をご記入ください..."></textarea>
                    </div>
                    
                    <button type="submit" class="submit-btn">送信する</button>
                </form>
            </div>
            
            <div class="contact-info">
                <h3>その他の連絡方法</h3>
                <div class="contact-item">
                    <div class="icon">📧</div>
                    <div class="text">Email: info@kawakami-server.com</div>
                </div>
                <div class="contact-item">
                    <div class="icon">📱</div>
                    <div class="text">Phone: +81-3-1234-5678</div>
                </div>
                <div class="contact-item">
                    <div class="icon">🏢</div>
                    <div class="text">Address: 東京都渋谷区川上ビル</div>
                </div>
                <div class="contact-item">
                    <div class="icon">⏰</div>
                    <div class="text">営業時間: 24時間365日対応</div>
                </div>
            </div>
            
            <div class="footer">
                <p>© 2024 川上家のサーバーページ - いつでもお気軽にご連絡ください</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/api/status")
def api_status():
    """APIステータスエンドポイント"""
    return jsonify({
        "status": "success",
        "message": "川上家のサーバーは正常に動作しています",
        "timestamp": datetime.now().isoformat(),
        "version": "2.0.0",
        "framework": "Flask",
        "python_version": "3.12",
        "server_name": "川上家のサーバーページ",
        "uptime": "99.9%",
        "response_time": "50ms"
    })

@app.route("/api/contact", methods=["POST"])
def api_contact():
    """お問い合わせAPIエンドポイント"""
    data = request.form
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')
    
    # 実際のアプリケーションでは、ここでメール送信やデータベース保存を行います
    return jsonify({
        "status": "success",
        "message": "お問い合わせを受け付けました。川上家のサーバーチームより早急にご連絡いたします。",
        "data": {
            "name": name,
            "email": email,
            "message": message[:100] + "..." if len(message) > 100 else message
        },
        "timestamp": datetime.now().isoformat()
    })

@app.route("/api/users")
def api_users():
    """ユーザー一覧APIエンドポイント（サンプル）"""
    users = [
        {"id": 1, "name": "川上太郎", "email": "taro@kawakami.com", "role": "システム管理者"},
        {"id": 2, "name": "川上花子", "email": "hanako@kawakami.com", "role": "開発者"},
        {"id": 3, "name": "川上一郎", "email": "ichiro@kawakami.com", "role": "オペレーター"}
    ]
    return jsonify({
        "status": "success",
        "users": users,
        "count": len(users),
        "server": "川上家のサーバーページ"
    })

if __name__ == "__main__":
    # ローカル開発用の設定
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
