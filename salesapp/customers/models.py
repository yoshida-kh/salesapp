from django.db import models


class TimestampBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DetailBaseModel(models.Model):
    name = models.CharField(max_length=500, db_index=True)
    note = models.CharField(max_length=1000)

    class Meta:
        abstract = True


class Client(TimestampBaseModel, DetailBaseModel):
    address = models.CharField(max_length=1000)
    email = models.EmailField(max_length=250)
    tel = models.CharField(max_length=50)


class Person(TimestampBaseModel, DetailBaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    email = models.EmailField(max_length=250)
    tel = models.CharField(max_length=50)


class Status(TimestampBaseModel, DetailBaseModel):
    pass


class Sale(TimestampBaseModel, DetailBaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    amount = models.FloatField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
