from django.db import models

from app.validatorsfile import uzbek_phone_validator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class WhyUs(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="media/")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'


class Services(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ServiceInfo(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    service_cat = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name


class Orders(BaseModel):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, validators=[uzbek_phone_validator])
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE)
    message = models.TextField()
    is_checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Tags(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Projects(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    link = models.URLField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title


class FaqType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    faq_type = models.ForeignKey(FaqType, on_delete=models.CASCADE)


class PriceList(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    limit_user = models.CharField(max_length=100)
    limit_date = models.CharField(max_length=100)


class Features(models.Model):
    title = models.CharField(max_length=100)
    is_checkout = models.BooleanField(default=False)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Partners(models.Model):
    image = models.ImageField(upload_to="media/")


class Workers(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    profession = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class FeadBack(BaseModel):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    description = models.TextField()
    profession = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    inform = models.TextField()
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.title
