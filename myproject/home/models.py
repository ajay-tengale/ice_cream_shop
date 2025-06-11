from django.db import models

#makemigration-create changes and store in a file
#migrate-apply the pending changes created by makemigrations
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    flavor = models.CharField(max_length=15)  # if you're now storing it as a numeric ID
    quantity = models.IntegerField()  # ✅ Add this field
    address = models.TextField()
   
    date=models.DateField()




    def __str__(self):        #for this show the name insted of conact be regestered
        return self.name




