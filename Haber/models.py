from django.db import models

class New(models.Model):

    name = models.TextField(verbose_name='Haberin Adı')
    content = models.TextField(verbose_name='Haberin İçeriği')
    date = models.DateTimeField(max_length=50,verbose_name='Tarih')
    editor = models.CharField(max_length=50,verbose_name='Haberi Yayınlayan')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haber'

class Work(models.Model):

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name='Kullanıcı')
    Work = models.TextField(verbose_name="İş Tagleri")

    

    class Meta:
        verbose_name = 'Kullanıcı İş Tagleri'
        verbose_name_plural = 'Kullanıcı İş Tagleri'

class Life(models.Model):

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name='Kullanıcı')
    Life = models.TextField(verbose_name="Günlük Hayat Tagleri")


    class Meta:
        verbose_name = 'Kullanıcı Günlük Hayat Seçimleri'
        verbose_name_plural = 'Kullanıcı Günlük Hayat Seçimleri'

class News(models.Model):

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name='Kullanıcı')
    News = models.TextField(verbose_name="Haber Tagleri")

    

    class Meta:
        verbose_name = 'Kullanıcı Haber Seçimleri'
        verbose_name_plural = 'Kullanıcı Haber Seçimleri'

class Event(models.Model):

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name='Kullanıcı')
    Event = models.TextField(verbose_name="Haber Tagleri")

 
    class Meta:
        verbose_name = 'Kullanıcı Etkinlik Seçimleri'
        verbose_name_plural = 'Kullanıcı Etkinlik Seçimleri'




