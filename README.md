# Antagon 🎭
​世間に出す前に、あなたの論理にストレステストを。
​Antagon（アンタゴン）は、あなたの論文、論理、アイデアの脆弱性を徹底的に攻撃するために設計されたオープンソースのマルチエージェントAIツールです。
あなたの個人的な「悪魔の代弁者（Devil's Advocate）」として機能し、論理的誤謬を暴き、実証的な証拠を要求し、その前提を容赦なく問い詰めます。
# 🚀 なぜ Antagon なのか？
​何でも肯定し、親切に手伝ってくれる一般的なAIアシスタントとは異なり、Antagonは「あなたの最悪の批評家」になるように構築されています。
自分のアイデアをAIによる仮想の「レッドチーム攻撃（敵対的テスト）」にさらすことで、他人に見せる前に、自身の主張を強固に鍛え上げることができます。
# ​✨ コア機能
​マルチエージェントによる多角的な攻撃 (Red Teaming):
### ​🧐 細密家 (The Pedant): 
曖昧な定義や、ぼやけた専門用語の隙を突きます。
### ​🕵️ 懐疑主義者 (The Skeptic): 
論理の飛躍、誤った二項対立、相関関係と因果関係の混同を追及します。
### ​🔬 実証主義者 (The Empiricist): 
客観的なデータ、引用文献、反例を容赦無く要求します。
​プライバシー・ファースト & 運用コストゼロ (BYOK & Local LLM):
​Gemini API (BYOK): 自身のGoogle Gemini APIキーを入力する方式（Bring Your Own Key）により、超高速かつ無料枠の範囲内でクラウド推論を利用できます。
​Ollama サポート: Ollama経由でローカルモデル（llama3やgemma2など）を接続し、完全オフラインで実行可能です。あなたの未発表の論文データが外部のサーバーに送信されることは一切ありません。
​美しいCLIインターフェース: Rich ライブラリを活用した、没入感のあるリッチなターミナル体験を提供します。
# 🛠️ インストール方法
```bash
git clone https://github.com/yourusername/antagon.git
cd antagon
pip install -r Requirements
```

# 🎮 使い方
​AntagonのCLIを起動します：
```bash
python "Antagon Core CLI"
```
1. ​プラットフォームの選択: `gemini`、`ollama`、`openai`、`claude`、`copilot` から選択します。
2. ​テキストの入力: 攻撃対象となるあなたの主張、レポート、または論文のドラフトを貼り付けます。
3. 攻撃開始: 3つのAIエージェントが並列で文章を分析します。
4. 必要に応じて、分析結果をMarkdownファイルへ保存します。

### APIキーとプラットフォーム

APIキーは環境変数で設定できます。未設定の場合はCLIで非表示入力されます。

| プラットフォーム | 環境変数 | 既定モデル |
|---|---|---|
| Gemini | `GEMINI_API_KEY` | `gemini-1.5-flash` |
| OpenAI / ChatGPT | `OPENAI_API_KEY` | `gpt-4o-mini` |
| Claude | `ANTHROPIC_API_KEY` | `claude-3-5-sonnet-latest` |
| Copilot / GitHub Models | `GITHUB_TOKEN` | `openai/gpt-4o-mini` |

`copilot` はGitHub ModelsなどのOpenAI互換エンドポイントを利用します。実際に利用するエンドポイントとモデルは契約・アカウント設定に合わせて入力してください。OpenAI互換APIはベースURLを変更できるため、他の対応サービスも利用できます。

# 🧪 開発者向け
現在のテストは `unittest` で管理されています。リポジトリ直下で次を実行してください。
```bash
python -m unittest discover -s tests
```

# 🤝 コントリビュート
​Antagonは現在、CLI（コマンドライン）フェーズとして開発がスタートしたばかりです。
今後のロードマップとして、Next.js + React Flowを用いた「ノードベースのCanvas UI（Web版）」の構築を予定しています。アイデア、バグ報告、Pull Requestを大歓迎します！
