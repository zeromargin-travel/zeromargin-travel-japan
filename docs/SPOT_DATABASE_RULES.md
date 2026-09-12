# 📘 Spot Database Architecture & Complete Quality Control Rulebook
**Document Version**: `v5.0.0` (Complete Fundamental Architecture & Disambiguation Edition - 2026-08-15)  
**File Location**: `docs/SPOT_DATABASE_RULES.md`  
**Automated Rule Location**: `.agents/rules/spot_database_rules.md`

---

## 🎯 目的（Purpose）
今後、何千・何万件と新しい都市や観光スポットがアプリに追加されても、データの品質劣化、英語漏れ、翻訳表示のアンバランス、同名地名による画像誤割り当て、データズレ（スワップ）、画像未反映・枠消滅、UIレイアウト要素の破綻が**二度と発生しないよう、すべてのデータベース構築・自動検証・画像パイプライン項目を完備したマスタールールブック**です。

---

## 📜 16大厳格品質管理チェックリスト（The 16 Master Principles）

### 1. 🌐 全6言語対応「現地語＋翻訳名」ハイブリッド名称基準（Universal Hybrid Name Standard）
旅行者が現地で「Google Maps」「Uber」「標識」「紙の地図」で場所を照合できるよう、全6言語（日・英・西・中・仏・独）において**現地オリジナル名**と**各言語の翻訳名**をセットで保持します。

- **JSONデータ構造基準 (`data/cities/*.json`)**:
  - `name_ja`: `現地名（日本語名称）`
  - `name_en`: `現地名 (English Name)`
  - `name_es`: `現地名 (Nombre en español)`
  - `name_zh`: `現地名 (中文名称)`
  - `name_fr`: `現地名 (Nom en français)`
  - `name_de`: `現地名 (Deutscher Name)`

---

### 2. 📸 Wikipedia自動画像取得・都市名曖昧さ回避 & センシティブ判定（Universal Wikipedia Photo & Safety Rules）
- **都市名による曖昧さ回避（City-Qualified Disambiguation）**:
  - `Sachsenhausen`, `Notre-Dame`, `St. Peter` 等の同名地名・汎称名詞の画像取得時、Wikipedia APIへは必ず都市名を付与した `"{title} ({cityName})"` または `"{title}, {cityName}"` で優先検索します。
- **センシティブ・不適切キーワードのブラックリスト判定**:
  - カテゴリーが「追悼施設・墓地」以外であるにもかかわらず、取得結果のURL・タイトル・概要に `konzentrationslager`, `concentration_camp`, `cemetery` 等のキーワードが含まれる場合は**自動で即座に拒否**します。
- **UI破壊的エラーハンドラの絶対禁止**:
  - `onerror="this.parentElement.style.display='none'"` 等の親要素を非表示にしてヘッダー枠を削除するコードを**永久に禁止**します。
  - 画像読み込みエラー発生時は、即座に「グラデーション付きカテゴリーヘッダーカード」（カテゴリーアイコン・ジャンル名・評価★）へ自動換装する `AITravelEngine.handleImageError()` を適用します。

---

### 3. 🚫 概要欄（desc）とワンポイント解説（tip）の重複完全排除（0% Overlap Rule）
- **概要欄（`desc`）**: どのような場所か、歴史的・建築的価値（基本情報1〜2文）。
- **ワンポイント解説（`tip`）**: **概要欄の内容・名称・基本説明を1文字も重複・再掲しない！** 現地での「具体的で実践的な裏技・コツ」のみ。

---

### 4. 🔑 IDキー結びつけ限定原則（ID-Only Keyed Data Binding Principle）
- スポットデータの補正・翻訳・プロパティ追加を行う際、配列インデックス（`spots[i]`）による一括代入を**完全に禁止**します。
- 必ず `spot['id']`（例: `f_19`, `m_5`, `p_2`）を唯一のキーとしてプロパティを結びつけ、スポットの追加・削除・並べ替えがあってもデータの連鎖的スワップ（ズレ）が発生しない構造を保証します。

---

### 5. 🛡️ スポット間文脈混入自動検知（Cross-Contamination Context Leak Guard）
- ビルドパイプライン（`rebuild_js_database.py`）実行時、Aスポットの文章内に同一都市のBスポットの固有名詞が不自然に混入していないかを全自動スキャンします。
- 混入を検知した場合はビルド警告を出力し、データの安全性を検証します。

---

### 6. 🇩🇪 ドイツ語・フランス語・スペイン語・中国語・日本語フィールドの英語漏れ完全ゼロ原則
- `desc_de`, `desc_fr`, `desc_es`, `desc_zh`, `desc_ja` の非英語フィールドに、英語の原文（`"World-class gallery..."`, `"located in..."` 等）を残存させることを禁止します。

---

### 7. 👶 「Kids & Family」タグ判定の厳格分離規則（Strict Kids Tag Auditing）
- ナイトライフ、酒場、追悼施設、墓地、風俗街等は `kids: false` を強制。

---

### 8. ☔ 雨天タグ（rain）の論理的整合性ルール
- 「Museum & Gallery」「Shopping」は `rain: true`。
- 「Scenery & Walk」は `rain: false`。

---

### 9. 🚀 統合ビルド＆3層コンプライアンス検証コマンド
データベースの更新時は必ず `python3 scripts/rebuild_js_database.py` を実行し、`🛡️ 3-Layer Compliance Guard PASSED` を確認します。
