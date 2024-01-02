# Transformers ライブラリの利用

HuggingFace の Transformers ライブラリを使う例です。

仮想環境を作成し、tensorflow と transformers ライブラリをインストールします。

```
$ source venv/bin/activate

(venv) $ pip install tensorflow
(venv) $ pip install transformers
```

`generateText.py` を実行します。

```
(venv) $ python generateText.py

```

`generateText.py` は以下の通りです。

```python
from transformers import pipeline, set_seed

generator = pipeline('text-generation', 
model='gpt2')

set_seed(42)

result = generator("New York is a city, ", max_length=30, num_return_sequences=5)

print(result)
```

以下のような出力を確認してください。

```
(venv) transformers-huggingface-demo % python generateText.py

[{'generated_text': 'New York is a city, \xa0there are many different ethnicities, \xa0there are differences from one ethnicity to another\xa0 and these differences'}, {'generated_text': "New York is a city, \xa0which as I write it is an entire nation as I don't believe to compare cities to countries, or even"}, {'generated_text': "New York is a city, ersatz. The people of NY have just arrived. But it's too crowded to get to us and it's"}, {'generated_text': 'New York is a city, \xa0to an extent, that resembles California or New Mexico, not because of any geography and social factors, but because'}, {'generated_text': 'New York is a city, \xa0that \xa0is no longer, the rest\xa0in a way: it has changed so radically in more ways'}]
```

## コードの解説

この Pythonコード は、Hugging Face の transformers ライブラリを使用して、GPT-2 モデルを活用したテキスト生成を行います。以下にコードの各部分について説明します。

1. インポート:

```python
from transformers import pipeline, set_seed
```

ここで、pipeline と set_seed を transformers ライブラリからインポートしています。pipeline は様々な自然言語処理タスクを簡単に実行できるようにするユーティリティで、set_seed は乱数生成のシードを設定するために使用されます。

2. テキスト生成パイプラインの作成:

```python
generator = pipeline('text-generation', model='gpt2')
```

ここで pipeline 関数を使ってテキスト生成（'text-generation'）タスクのためのパイプラインを作成しています。model='gpt2' パラメータにより、GPT-2 モデルがこのタスクのために使用されることを指定しています。

pipeline はまず、指定されたモデル（この場合はgpt2）がローカルにキャッシュされているかを確認します。キャッシュは通常、ユーザーのホームディレクトリ内の.cacheフォルダ（例えば、macOS や Linuxでは~/.cache/huggingface/transformers）にあります。モデルが見つかると、pipelineはそのモデルをロードして使用可能にします。

もしローカルにキャッシュされていない場合、pipeline は Hugging Face のモデルハブからモデルをダウンロードし、将来の使用のためにキャッシュに保存します。


3. 乱数生成のシード設定:

```python
set_seed(42)
```

乱数生成器のシード値を 42 に設定しています。これにより、結果の再現性が保たれます。つまり、同じシード値と入力を使用すると、同じ出力が生成されます。

4. テキスト生成の実行:

```python
result = generator("New York is a city, ", max_length=30, num_return_sequences=5)
```

生成パイプラインを使用してテキストを生成しています。ここでは、"New York is a city, " という初期テキストから始めて、最大30トークンの長さのテキストを 5 つ生成します。max_length は生成される各テキストの最大長を制御し、num_return_sequences は生成されるテキストの数を指定します。

5. 結果の出力:

```python
print(result)
```

生成されたテキストのリストを出力します。result は辞書のリストで、各辞書にはキー 'generated_text' が含まれ、その値として生成されたテキストが格納されています。

このコードは、GPT-2 を使用して、与えられた初期テキストから始まる複数の異なるテキストシーケンスを生成することで、テキスト生成の能力を示しています。


## ランセンス

MIT
