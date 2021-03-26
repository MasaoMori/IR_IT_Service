# growi

[growi](https://github.com/weseek/growi)をdockerでホストするための設定です.起動するためには以下の設定が必要です.

### 設定

- サーバーがプロキシを使用している場合
`docker-compose.yml`の`ESJAVAOTPS`にプロキシの設定を追加する.
- `.env`ファイルを作成して, `HACKMD_URI`と`GROWI_URI`を定義する.

設定例

```ex
HACKMD_URI=http://url
GROWI_URI=http://url
```

### 起動方法

```bash
docker-compose up -d
```
