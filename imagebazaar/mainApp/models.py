from django.db import models

#Create Category model
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title

#Create Image model
class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    added_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title +" "+str(self.added_date)
