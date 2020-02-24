# 仮想環境 構築方法
- URL:https://kazuhira-r.hatenablog.com/entry/2019/01/09/231800
- URL:https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e
## 起動cmd
- `python3 -m venv {DirName}` 
- `source bin/activate` 
- /home/og/workspace-python/test-env 上記cmdを実行

## django 構築用
### 参考URL
- https://qiita.com/Saku731/items/ed64190a12a4498b9446
- https://qiita.com/gragragrao/items/373057783ba8856124f3
- https://qiita.com/gragragrao/items/9a85a372a9c3eec06243
### debug toolbar
- https://wonderwall.hatenablog.com/entry/2018/03/13/233000

## 構築時CMD履歴
```
# DjangoとDB接続用のlibをInstall
$ pip3 install -r requirements.txt

# appの全体設定に関連するファイルを格納
$ django-admin startprojcet app_config 

# app単体のフォルダを作成
$ cd app_config 
$ django-admin startapp app_folder
