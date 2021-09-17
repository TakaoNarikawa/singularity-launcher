# Singularity Launcher

## 何のためのモノ？

Singularity 環境に入る際、環境ファイルへのパスを毎回入力するのが面倒であったので
少しでも楽になればと思い作成しました

![](https://github.com/TakaoNarikawa/singularity-launcher/blob/main/screenshots/sing-launch.gif?raw=true)

## 使い方

クローンします

```
$ git clone https://github.com/TakaoNarikawa/singularity-launcher.git
$ cd singularity-launcher
```

モジュールを使用するため `venv` で環境を作ります

```
$ python3 -m venv ~/envs/cli
$ ~/envs/cli/bin/pip3 install -r requirements.txt
```

`.bashrc` 等にエイリアスを作成します

```
$ vim ~/.bashrc
```

```sh
alias sing-launch='${venv環境パス}/bin/python3 ${cli.py へのパス} --envdir ${Singularity env ディレクトリ}'
```

自分の場合は次のようになりました

```sh
alias sing-launch='~/envs/cli/bin/python3 ~/Code/Others/singularity-launcher/cli.py --envdir ~/Code/Singularity/envs'
```

`.bashrc` を読み込み直すのを忘れないでください

```
$ source ~/.bashrc
```

これでコマンドが使えます

```sh
$ sing-launch 
[?] Select Singlarity Environment File: /home0/narikawat/Code/Singularity/envs/pytorch.sif
   /home0/narikawat/Code/Singularity/envs/tf2.sif
 > /home0/narikawat/Code/Singularity/envs/pytorch.sif

Singularity(pytorch.sif) $
```
