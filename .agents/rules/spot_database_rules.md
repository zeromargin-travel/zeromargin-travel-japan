# 📘 Spot Database Architecture & Complete Quality Control Rulebook
**Document Version**: `v5.0.0` (Complete Fundamental Architecture & Disambiguation Edition - 2026-08-15)  
**File Location**: `docs/SPOT_DATABASE_RULES.md`  
**Automated Rule Location**: `.agents/rules/spot_database_rules.md`

---

## 📜 16大厳格品質管理チェックリスト（The 16 Master Principles）

1. **全6言語ハイブリッド名称 (`name_ja`, `name_en`, `name_es`, `name_zh`, `name_fr`, `name_de`)**:
   - フォーマット: `現地名（日本語翻訳名）`, `現地名 (English Name)`

2. **Wikipedia自動画像取得 & 都市名曖昧さ回避**:
   - `Sachsenhausen`, `Notre-Dame` 等の同名地名は `"{title} ({cityName})"` で検索。
   - 不適切キーワード（`konzentrationslager`, `cemetery` 等）は自動拒否。
   - `onerror="display='none'"` 永久禁止。`AITravelEngine.handleImageError()` 適用。

3. **0% Overlap Rule**: `desc`（基本説明）と `tip`（現地裏技）のテキスト重複禁止。

4. **IDキー結びつけ限定原則**: 配列インデックス代入禁止。必ず `spot['id']` で代入。

5. **文脈混入自動検知**: スポット間での他スポット名誤混入を自動検知・警告。

6. **英語漏れゼロ原則**: 非英語フィールドへの英語原文残存を禁止。

7. **Kids & Family分離**: 酒場・追悼施設・墓地は `kids: false`。

8. **統合ビルド**: データ変更後は必ず `python3 scripts/rebuild_js_database.py` を実行。
