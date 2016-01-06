# PySideでJanomeを使ってみた

## Janome
@moco_betaさんがMecabを簡単に使えるよなツールを作られたということで試してみました.

>辞書内包／Pure Python実装の形態素解析器 Janome を公開しました
>一応の基本機能がととのったので、できたてほやほやではありますが、Python製の形態素解析器 Janome を公開しました。
>http://mocobeta-backup.tumblr.com/post/115843098157/pure-python-janome

## Janomeの使い方
[Janome v0.2 documentation](http://mocobeta.github.io/janome/ "Janome v0.2 documentation")

```python
    (venv) $ pip install janome
    (venv) $ python
    >>> from janome.tokenizer import Tokenizer
    >>> t = Tokenizer()
    >>> for token in t.tokenize('すもももももももものうち'):
    ...     print(token)
    ...
    すもも 名詞,一般,*,*,*,*,すもも,スモモ,スモモ
    も    助詞,係助詞,*,*,*,*,も,モ,モ
    もも  名詞,一般,*,*,*,*,もも,モモ,モモ
    も    助詞,係助詞,*,*,*,*,も,モ,モ
    もも  名詞,一般,*,*,*,*,もも,モモ,モモ
    の    助詞,連体化,*,*,*,*,の,ノ,ノ
    うち  名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ
```

## Janomeを使ってみるツール
文章を入力するとJanomeを使って形態素解析を行い結果を表示するだけのアプリです
![app_ver1.0]
[app_ver1.0]: ./image/janome-app_ver1.0.jpg



※ 作成者moco_betaさんに感謝いたします
