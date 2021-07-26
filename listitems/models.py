from django.db import models
import datetime

from django.db.models.deletion import PROTECT

class Owner(models.Model):
    
    # 各フィールドの定義
    name = models.CharField('持ち主名', max_length=100)
    number = models.CharField('学籍番号', max_length=100)
    comment = models.CharField('コメント', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    CHOICES = (
        (1, '忘れ物'),
        (2, '放置物品'),
    )
    # STATUS = (
    #     (1, '未申請'),
    #     (2, '持ち主'),
    #     (3, '廃棄')
    # )
    # 期日の設定
    due_date = datetime.date.today() + datetime.timedelta(weeks=2)
    
    # 各フィールドの定義
    name = models.CharField('物品名', max_length=100)
    founder = models.CharField('発見者名', max_length=100)
    left_or_unknown = models.IntegerField(choices=CHOICES, default=1, null=True)
    photo = models.ImageField('写真', upload_to='images/')
    date = models.DateField('発見日', default=datetime.date.today)
    deadline = models.DateField('期日', default=due_date, max_length=100)
    comment = models.CharField('コメント', max_length=100, blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, verbose_name='持ち主', null=True, blank=True)
    # status = models.IntegerField(choices=STATUS, default=1, null=True)

    def __str__(self):
        return self.name