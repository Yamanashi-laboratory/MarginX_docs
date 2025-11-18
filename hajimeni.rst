はじめに
========

***TEST 123***

本マニュアルの説明
---------------------

本マニュアルは超伝導回路のパラメータ最適化ツールである、**MarginX** の使い方を示す
ものである。本章でその概要、第２章で導入方法、第３章で入力ファイル、第４章で各メ
ニューの説明を行う。

本ツールの概要
----------------

MarginX はSFQ 回路にとどまらない、Josephson 接合(Josephson Junction: JJ) を含む超
伝導回路全般に用いることができるパラメータ最適化ツールである。このツールは2014
年に横浜国立大学の中石氏が作成したパラメータマージン抽出ツール[1] を改良して作成
された。MarginX における回路シミュレーションはJoSIM [2] を用いている。MarginX
はC++ で記述され、Linux 系のOS で使用することを前提として開発されているため、
Windows 環境下ではWSL、cygwin 等を用いないと使用できないことに注意していただ
きたい。MarginX に関する細かい説明は電子情報通信学会誌にて出版された論文[3] を確
認されたい。


参考文献
-------------

[1]Y. Yamanashi, S. Nakaishi, A. Sugiyama, N. Takeuchi, and N. Yoshikawa, ”Design
methodology of single-flux-quantum flip-flops composed of both 0- and π-shifted
Josephson junctions,” Supercond. Sci. Technol., vol. 31, no. 10, p. 105003, Oct. 2018.  


[2]J.A. Delport, K. Jackman, P.L. Roux, and C.J. Fourie, ”JoSIM - Superconductor SPICE
Simulator,” IEEE Trans. Appl. Supercond., vol. 29, no. 5, p. 1300905, Aug. 2019.  


[3]S. Matsuoka, N. Yoshikawa, and Y. Yamanashi,“MarginX: Simple and Fast Circuit
Parameter Optimization Tool for Superconductor Circuits,”IEICE Trans. Electron.,
vol. E108-C, no. 11, pp. 587-593, Nov. 2025.  