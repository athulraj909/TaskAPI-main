from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class tbl_personal(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='puser')
    Enquiry_no = models.IntegerField(blank=True,null=True)
    Enquiry_date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=200,blank=True,unique=True)
    Gender = models.CharField(max_length=50,blank=True)
    Qualification = models.CharField(max_length=100,blank=True)
    Address = models.CharField(max_length=200,blank=True)
    Contact_no = models.CharField(max_length=10,unique=True)
    WhatsApp_no = models.CharField(max_length=10,unique=True)
    DOB = models.DateField(blank=True)


    def save(self, *args, **kwargs):
        if not self.Enquiry_no:
            last_record = tbl_personal.objects.all().order_by('Enquiry_no').last()
            if last_record:
                self.Enquiry_no = last_record.Enquiry_no + 1
            else:
                self.Enquiry_no = 1
        super(tbl_personal, self).save(*args, **kwargs)


    def __str__(self):
        return self.Name


class tbl_college(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='coluser')
    College = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.College


class tbl_courses(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cuser')
    courses = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.courses

class tbl_work_experience(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='wuser')
    Experience = models.CharField(max_length=500,blank=True)


    def __str__(self):
        return self.Experience