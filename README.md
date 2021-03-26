# IRのための業務システム・メタ情報管理ツール

## はじめに

このシステム設定ドキュメントは、IRを進めるために必要な業務システムのデータを効率的に収集し、DWを円滑に構築することを目的とした文書です。


# ir-meta

## 始め方

このリポジトリは, docker, docker-compose を使って nginx, growi, redmine, jupyterhub を構築するための設定例です.

## 事前準備

### docker, docker-compose のインストール

公式のガイドラインに従ってください.

[docker](https://docs.docker.com/get-docker/)
[docker-compose](https://docs.docker.com/compose/install/)
[proxy](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy)

docker を sudo つけずに実行できるようにする場合の[参照](https://docs.docker.com/engine/install/linux-postinstall/)

### firewall の設定

サイトを公開するためのポート開放には`ufw`を使います. (20番を有効にせずセッションを切ると ssh接続ができなくなるので注意が必要です)

```bash
ufw allow 20
ufw allow 80
ufw allow 465
ufw allow 8080
```

変更した後は

```bash
ufw reload
```

`Status: inactive` と出る場合はまず以下を実行してください.

```bash
ufw enable
```

### 起動方法

`proxy`が全てのアプリケーションに依存しているので一番最後に起動する必要があります.
起動方法は以下です. それぞれの`README.md`も参照してください.

起動 (`docker-compose.yml`の変更を反映させる)

```bash
docker-compose up -d
```

停止

```bash
docker-compose stop
```

再起動

```bash
docker-compose restart
```

環境をリセットする (コンテナ・ネットワーク・ボリューム・イメージを削除する)

```bash
docker-compose down
```

`tmux`がサーバーで使える場合に2回目の起動からは`tmux`のセッションに入った後

```bash
./start
```

で全てを起動することができます.
