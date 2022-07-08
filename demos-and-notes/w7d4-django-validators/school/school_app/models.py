from django.db import models
from django.core.validators import RegexValidator
from .validators import is_locker_digit_valid

# Create your models here.

class Professor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Locker(models.Model):
    locker_number = models.IntegerField(unique=True, validators=[is_locker_digit_valid])
    # TODO: Add combination validator
    combination = models.CharField(max_length=10)

    def __str__(self):
        return f"LOCKER: {self.locker_number}"

class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    # null=True means that we are able to create a student who does not yet have a locker.
    locker = models.OneToOneField(Locker, null=True,  blank=True, on_delete=models.SET_NULL, related_name="student")

    # Get all enrollments for self
    # Sum up grades & average to get GPA
    def get_gpa(self):
        num_enrollments = 0
        grade_sum = 0
        for enrollment in self.enrollments.all():
            num_enrollments += 1
            grade = enrollment.grade
            if(grade == 'A'):
                grad = .9
            # Fill in the rest ...
            grade_sum += grade 
        
        return grade_sum / num_enrollments


class Course(models.Model):
    name = models.CharField(max_length=255)
    # many to one relationship, done in SQL with a foreign key
    # One professor can teach multiple courses,
    # Each course only has one professor
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="courses")
    
    # Uses our Enrollment join table to form a many-to-many relationship between students & courses, i.e. 
    # it means one student can be in many courses and one course can have many students.
    students = models.ManyToManyField(Student, through="Enrollment")

# Our join table for the many-to-many relationship
# between students and courses
class Enrollment(models.Model):
    # on_delete=models.CASCADE means If the student is deleted, their enrollments are also deleted
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")

    # on_delete=models.PROTECT means A course CANNOT be deleted if students are enrolled
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="enrollments")

    grade = models.CharField(max_length=2, validators=([RegexValidator(regex=r"[ABCDF][+-]?")]))

    class Meta:
        # TODO: Use UniqueConstraint with constraints option instead
        # See: https://docs.djangoproject.com/en/4.0/ref/models/options/#unique-together
        unique_together = (("student", "course"))
