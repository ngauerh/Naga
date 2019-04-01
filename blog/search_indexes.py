from haystack import indexes
# 修改此处，为你自己的model
from .models import Blog


# 类名为模型类的名称+Index
class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 修改此处，为你自己的model
        return Blog

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

