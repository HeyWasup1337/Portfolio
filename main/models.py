from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Изображение")
    link = models.URLField(blank=True, verbose_name="Ссылка на проект")
    github_link = models.URLField(blank=True, verbose_name="Ссылка на GitHub")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['-created_at']


class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name="Навык")
    icon = models.CharField(max_length=50, blank=True, help_text="Например: emoji или CSS-класс иконки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"