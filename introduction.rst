********
導入方法
********


ダウンロード及びコンパイル
------------------------

MarginX のソースはGitHub(https://github.com/Yamanashi-laboratory/MarginX)で公開されている。
以下、MarginX の導入方法について説明する。
以下のコマンドで、カレントディレクトリにMarginX をダウンロードする。

.. code-block:: bash
   
   git clone https://github.com/Yamanashi-laboratory/MarginX

次に、ダウンロードしたフォルダに移動し、以下の手順でbuild フォルダを作成してそこ
に移動する。

.. code-block:: bash

   cd MarginX
   mkdir build
   cd build

その後、以下の手順でコンパイルを行う。

.. code-block:: bash

   cmake ..
   cmake --build .

コンパイルが完了されると、MarginX/build 下に実行ファイル”MarginX”が生成される。
パスを通したりシンボリックリンクを作成するなどしてこの実行ファイルを用意に実行できるように
しておくとよい。

