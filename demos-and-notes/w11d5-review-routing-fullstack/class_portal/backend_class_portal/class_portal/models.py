from tkinter import CASCADE
from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rubric = models.TextField()
    course = models.IntegerField()

    def __str__(self):
        return f"title: {self.title}, description: {self.description}, rubric: {self.rubric}"

class Grade(models.Model):
    # mocking foreign key for student field with an integer
    student = models.IntegerField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"student: {self.student}, assignment: {self.assignment}, grade: {self.grade}"


