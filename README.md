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

## サービス再起動
スクリプト内のこちらで再起動させているのでnginx以外を再起動させる場合は書き換えてください。
```
os.system("systemctl reload nginx")
```

## 動作確認
Ubuntu 22.04、Certbot 1.21.0、Nginx 1.18.0で動作確認をしています。