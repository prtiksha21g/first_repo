from django.db import models

class student(models.Model):
    username = models.CharField(max_length=100,blank=False,null=False)
    password=models.TextField(blank=False,null=False)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    emailid=models.EmailField(default=False,null=False)
    # class Meta:
    #     db_table='student1'
        #__tablename__='student'
# Create your models here.
    def __str__(self):
        return self.ename
