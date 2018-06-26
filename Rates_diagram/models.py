from django.db import models


# Create your models here.
class Rates_all(models.Model):
    symbol = models.CharField(max_length=24)
    bid = models.SmallIntegerField(default=0)
    ask = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s %s %s" % (self.symbol, self.bid, self.created)

    class Meta:
        verbose_name = 'Котирровки'
        verbose_name_plural = 'Котирровки'





