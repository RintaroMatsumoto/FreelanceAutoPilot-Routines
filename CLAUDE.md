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
