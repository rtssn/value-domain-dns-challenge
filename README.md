# value-domain-dns-challenge

CertbotでのDNSチャレンジをバリュードメインAPIを利用して行うPythonスクリプトです。

## API KEYについて
API KEYはスクリプトと同じディレクトリにapikey.txtというファイルを作成してそこに記述してください。

## certbotの設定ファイル例

```
manual_auth_hook = /opt/value-domain-hook.py
manual_cleanup_hook = /opt/value-domain-hook DELETE
```

## 引数について
DELETEを追加することでCertbotで追加したレコードを削除します。(Certbotが設定した環境変数に依存しています。)