# 講習会までの準備

自分のラップトップパソコン(ノートパソコン)を用意する(Windows / Mac) 可。

## LaTeXの環境構築
### Windowsユーザー向け
https://www.tug.org/texlive/acquire-netinstall.html から install-tl-windows.exe をダウンロードし、**インストールを完了させる**。
インストールに約1時間かかるので、インストールで分からないことがあれば、講習会の前日までに質問すること。

LaTeXファイルを編集するため、https://code.visualstudio.com/ から Download for Windowsで、 VSCode***.exeをダウンロードし、インストールを完了させる。
インストール中に出てくる「追加タスク」の項目は、すべてチェックを入れておくと良いだろう。

### Macユーザー向け
全体で5時間以上かかる。xcodeを持っていれば2時間ぐらい。
開発環境等を全く持っていない人はまずterminalを開き以下のコマンドを入力。
```
xcode-select --install
```
インストールをクリックし、xcodeとcommandline toolを手に入れる(とても時間がかかる)と、開発用の様々なコマンドが使えるようになる。

Homebrewをインストール
```
>/usr/bin/ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)
```

LaTeX環境のためにghostscriptとMacTeXをinstall&更新
```
brew install ghostscript
brew cask install mactex
sudo tlmgr update --self --all  #とても時間がかかる
```

PATHの設定
terminalのshellの設定ファイル(bashなら.bash_profile, zshなら.zshrc)に以下の記述を追加
```
export PATH=/usr/local/texlive/2018/bin/x86_64-darwin:$PATH
```

VSCodeのインストール
```
brew cask install visual-studio-code
```

# 講習会の内容

以下の内容を予定している。

* latexの環境が正しくインストールされていることを確認する
* VSCodeをインストールする
* VSCodeの拡張機能をインストールし、設定する
* sample.tex を自分でコンパイルしPDFファイルができることを確認する
* テキスト内容を一通り解説する
* サンプルの内容を書き換えてPDFファイルができることを確認する

# 講習会の日程
* 2018年度 11月7日(水) 13:00~14:00 部屋未定
* 2019年度 11月11日(月) 13:30~14:30 部屋未定