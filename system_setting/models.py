from django.db import models

# Create your models here.
'''
[13] onad | 20200525 | Create Campus MVT with CRUD
'''


class Campus(models.Model):
    campus_code = models.CharField(
        max_length=64, unique=True, verbose_name="Campus Code"
    )
    campus_name = models.CharField(
        max_length=200, verbose_name="Campus Name"
    )
    campus_add = models.CharField(
        max_length=200, verbose_name="Campus Address"
    )
    registered_by = models.CharField(
        max_length=100,
        verbose_name="Registered By"
    )
    registered_date = models.DateField(auto_now_add=True)
    updated_by = models.CharField(
        max_length=100,
        verbose_name="Updated By"
    )
    updated_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.campus_code

    class Meta:
        db_table = "tbl_campus"
