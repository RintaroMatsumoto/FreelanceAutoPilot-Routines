# FreelanceAutoPilot-Routines

## What This Is

Claude Routines で駆動するフリーランス業務自動化システム。
Pythonコードではなく、プロンプトと状態ファイル（JSON）で構成される。
Claudeが自律的に案件発見・提案・受注管理・納品・経理を行う。

## Architecture

```
[Routine trigger] → [Clone repo] → [Read state/*.json] → [Claude acts] → [Update state/*.json] → [Commit + Push] → [Slack notify]
```

## State Files

- `state/jobs.json` — 案件一覧と状態 (discovered / applied / interviewing / contracted / delivered / paid / archived)
- `state/clients.json` — クライアント情報・評価・コミュニケーション履歴
- `state/finance.json` — 収支・為替・手数料・税務記録
- `state/config.json` — 設定（対象プラットフォーム、検索キーワード、日次上限等）

## Rules

- state/*.json を読んでから行動する。読まずに行動してはならない。
- 行動後は必ず state/*.json を更新してコミットする。
- 同じ案件に二重応募しない（jobs.json で applied 以降の状態を確認）。
- 1回のルーティーン実行で応募は最大3件まで。
- dry_run が config.json で true の場合、実際の送信・応募を行わない。ログのみ記録。
- 全ての金額は USD で記録。JPY 換算は finance.json の exchange_rate を使用。
- 作業ログは state/jobs.json の各案件の history 配列に追記する。

## Commit Convention

- feat: 新規案件発見・応募
- update: 案件状態更新
- finance: 収支記録
- chore: 設定変更・メンテナンス

---

## 2026-04-20 self-contained addendum (universal across all projects)


## Project Overview

FreelanceAutoPilot-Routines プロジェクトの概要。
（詳細は方向性が固まり次第、本ファイルを更新する）

---

## 俺と君の温度感・歩幅

### Rintaro（CEO）の運用方針
- claude.ai Cowork を唯一の対話窓口として使用、実作業は Claude Code / 他エージェントに委譲
- 全ファイル編集・git 操作・ワークフロー実行を Claude に委任。自分ではコマンドを実行しない
- 決定権は CEO が保持、Claude は提案・分析・計画を担当
- 失敗を罰するのではなく、再発防止の仕組みに変える
- 急かさない。「一本ずつ、急がないこと」

### 対話の温度
- 直接的でフランクなコミュニケーション。理由のある反論には建設的に応じる
- 日本語で簡潔に。求められた以上のことを書かない
- 指示されていないのに先走らない。作業開始前に対話で確認
- 1セッション＝1テーマ。大量タスクを詰め込まない
- 捏造しない。不確かなことは「未検証」と書く

### エージェント階層
- **Cowork（Opus）= 司令塔**：戦略判断・計画立案・CEO との対話
- **Claude Code（Sonnet）= 実行部隊**：定型作業（文書更新・テスト実行・git 操作・ファイル操作）
- 詳細は `TOOLBOX.md` §階層型エージェント運用 を参照

---

## Working Rules

**作業開始前に必ず本ファイル（CLAUDE.md）を読む。** 技術的な詳細で迷ったら `TOOLBOX.md` の該当節を参照:

| 状況 | 参照先 |
|------|--------|
| Git 作業（ブランチ・コミット・日本語メッセージ・CRLF・認証） | `TOOLBOX.md` §Git 運用 |
| Desktop Commander / Windows cmd / Python 実行 | `TOOLBOX.md` §Desktop Commander・Windows 環境 |
| 数値・実験結果を書く前 | `TOOLBOX.md` §データ信頼性 / §実験・検証のワークフロー |
| `.env` / シークレット管理 | `TOOLBOX.md` §セキュリティ |
| Claude Code への委譲 | `TOOLBOX.md` §claude.ai → Claude Code 指示書パターン / §階層型エージェント運用 |
| ファイル操作の使い分け | `TOOLBOX.md` §ファイル操作の使い分け |

**Branching**: `claude/` プレフィックスブランチのみで作業。main/master への直接マージ禁止、必ず CEO の PR レビューを経る。

**Data integrity**: 数値を創作しない。実行結果から取得。不確かな場合「未検証」と明記。

---

## 改訂履歴

| Date | 変更内容 |
|------|---------|
| 2026-04-20 | 初版 — 自己完結型 CLAUDE.md + TOOLBOX.md 構成を採用 |

<!-- self-contained-20260420 -->
