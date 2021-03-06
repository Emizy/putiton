import hashlib
from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    Email = models.EmailField(null=True, blank=True, max_length=254)
    Phone = models.CharField(max_length=11, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    offer = models.TextField(blank=True, null=True)
    types = {
        ('Male', 'Male'),
        ('Female', 'Female'),
    }
    gender = models.CharField(choices=types, max_length=20, blank=True, null=True)
    r_types = {
        ('APPROVED', 'APPROVED'),
        ('UNAPPROVED', 'UNAPPROVED'),
        ('Nil', 'Nil'),
    }
    confirm = models.CharField(choices=r_types, max_length=20, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(blank=True, null=True, max_length=200)
    occupation = models.CharField(blank=True, null=True, max_length=200)
    location = models.CharField(blank=True, null=True, max_length=200)
    password = models.TextField(blank=True, null=True)
    con_password = models.TextField(blank=True, null=True)
    ch_types = {
        ('Free', 'Free'),
        ('NoSub', 'NoSub'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    }
    status = models.CharField(choices=ch_types, max_length=20, blank=True, null=True)
    image = models.FileField(null=True, blank=True)
    prices = models.CharField(max_length=11, blank=True, null=True)
    sub_date = models.DateField(max_length=30, blank=True, null=True)
    exp_date = models.DateField(max_length=30, blank=True, null=True)
    store_visit = models.PositiveSmallIntegerField(blank=True, null=True,default=0)

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.Email, self.status)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = createHash(self.password)
        super(Supplier, self).save(*args, **kwargs)


class Product(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField()
    product_name = models.CharField(max_length=300)
    types = {
        ('Bags', 'Bags'),
        ('Beads', 'Beads'),
        ('Clothing', 'Clothing'),
        ('Hairstylist', 'Hairstylist'),
        ('Jewelry', 'Jewelry'),
        ('MakeupArtist', 'MakeupArtist'),
        ('Shoes', 'Shoes'),
        ('Watches', 'Watches'),
        ('WeddingWears', 'WeddingWears'),
    }
    category = models.CharField(choices=types, max_length=20, blank=True, null=True)
    d_types = {
        ('Yes', 'Yes'),
        ('No', 'No'),
    }
    moderate = models.CharField(choices=d_types, max_length=20, blank=True, null=True)
    image1 = models.FileField(null=True, blank=True)
    image2 = models.FileField(null=True, blank=True)
    image3 = models.FileField(null=True, blank=True)
    color = models.CharField(max_length=200, blank=True)
    supp_user = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, blank=True, null=True)
    descrip = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    post_view = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return "%s - %s" % (self.category, self.product_name)


class reg(models.Model):
    Name = models.CharField(max_length=90, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True, max_length=254)
    Phone = models.CharField(max_length=11, blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s - %s" % (self.Name, self.Email)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = createHash(self.password)
        super(reg, self).save(*args, **kwargs)


def createHash(value):
    hash = hashlib.sha256()
    hash.update(str(value).encode(encoding='UTF-8'))
    return hash.hexdigest()


class Contact(models.Model):
    subject = models.CharField(max_length=40, null=True, blank=True, )
    Email = models.EmailField(null=True, blank=True, max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Supp_Ads(models.Model):
    supp_user = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, blank=True, null=True)
    price = models.IntegerField()
    product_name = models.CharField(max_length=300)
    types = {
        ('men', 'men'),
        ('women', 'women'),
        ('men_acc', 'men_acc'),
        ('beads', 'beads'),
        ('makeup', 'makeup'),
    }
    category = models.CharField(choices=types, max_length=20, blank=True, null=True)
    image1 = models.FileField(null=True, blank=True)
    image2 = models.FileField(null=True, blank=True)
    image3 = models.FileField(null=True, blank=True)
    color = models.CharField(max_length=200, blank=True)
    stats = models.CharField(max_length=200, blank=True)
    descrip = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name_plural = "Products"

    def __str__(self):
        return "%s - %s" % (self.supp_user.name, self.product_name)


class transaction(models.Model):
    supp_user = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, blank=True, null=True)
    bank = models.CharField(max_length=200, blank=True, null=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.supp_user.name, self.supp_user.Email)


class chat(models.Model):
    Email = models.EmailField(null=True, blank=True, max_length=254)
    descrip = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Email


class sup_complains(models.Model):
    sub_com = models.CharField(null=True, blank=True, max_length=254)
    full_com = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    supp_user = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return "%s - %s" % (self.supp_user.name, self.sub_com)


class XpresSoft(models.Model):
    name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.phone)


class message(models.Model):
    broadcast = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.broadcast, self.date)


class Users_Complains(models.Model):
    message = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.email)
