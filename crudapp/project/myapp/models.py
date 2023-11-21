from django.db import models

class Faculty(models.Model):
    faculty_number = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    academic_rank = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.faculty_number} - {self.first_name} {self.last_name}"
