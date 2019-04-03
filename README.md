# Django+element ui的博客程序
python3
Django 1.11
Sqlite3
Element ui

## 3/28新增Docker一键部署
<pre>
chmod 777 start.sh
./start.sh
</pre>


## 运行截图
![](https://i.imgur.com/omVoltq.png)



![](https://i.imgur.com/TLWnmvS.png)


## 运行方式
<pre>
mkdir na
cd na
git clone https://github.com/ngauerh/Naga.git
vitualenv env
source env/bin/activate
pip install -r requirements.txt
</pre>

启动程序后去程序后台修改网站信息，自我简介和推广素材


# 搜索功能
使用 Whoosh 作为搜索引擎，但在 django haystack 中为 Whoosh 指定的分词器是英文分词器，可能会使得搜索结果不理想，我们把这个分词器替换成 jieba 中文分词器。这里需要在项目环境下的Lib\site-packages\haystack\backends的目录中新建一个文件 ChineseAnalyzer.py，其中代码如下：

<pre>

import jieba

from whoosh.analysis import RegexAnalyzer
from whoosh.analysis import Tokenizer, Token


class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        t = Token(positions, chars, removestops=removestops, mode=mode,
                  **kwargs)
        seglist = jieba.cut(value, cut_all=True)
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
                t.endchar = start_char + value.find(w) + len(w)
            yield t


def ChineseAnalyzer():
    return ChineseTokenizer()

</pre>

再把 haystack/backends/whoosh_backends.py 文件复制一份到当前目录下，重命名为 whoosh_cn_backends.py（之前我们在 settings.py 中 的 HAYSTACK_CONNECTIONS 指定的就是这个文件），然后修改whoosh_cn_backends.py中的代码：

<pre>
# 顶部引入刚才添加的中文分词
from .ChineseAnalyzer import ChineseAnalyzer
</pre>

找到如下一行代码:

<pre>
schema_fields[field_class.index_fieldname] = TEXT(stored=True, analyzer=StemmingAnalyzer(), field_boost=field_class.boost, sortable=True)
</pre>

修改为:

<pre>
schema_fields[field_class.index_fieldname] = TEXT(stored=True, analyzer=ChineseAnalyzer(), field_boost=field_class.boost, sortable=True)
</pre>

建立索引文件
运行命令 python manage.py rebuild_index