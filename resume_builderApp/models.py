from django.db import models


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    

class Education(models.Model):
    DEGREE_CHOICES = (
        ('Phd', 'Phd'),
        ('Mtech/MA/MSc/MCom/MBA', 'Masters'),
        ('BE/Btech/BA/BSc/BCom', 'bachelors'),
        ('12th', 'High School')
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    stream = models.CharField(max_length=100)
    passing_year = models.DateField()
    result = models.CharField(max_length=5)


class ProjectOrJob(models.Model):
    WORK_CHOICES = (
        ('J', 'Job'),
        ('P', 'Project')

    )

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    work = models.CharField(max_length=1, choices=WORK_CHOICES)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    

class ProfessionalSkill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_detail = models.TextField()

    

class Academic(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    academic_detail = models.TextField()
    

class AreaOfInterest(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    area_of_interest_detail = models.TextField()
    
    