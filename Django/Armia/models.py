# models.py

from django.db import models

class WeaponModel(models.Model):
    name = models.CharField(max_length=99, blank=False, verbose_name="Название модели")

    def __str__(self):
        return self.name

class EnginiryType(models.Model):
    name = models.CharField(max_length=98, blank=False, verbose_name="Тип инженерии")

    def __str__(self):
        return self.name

class MilitaryBase(models.Model):
    id = models.CharField(max_length=100, primary_key=True, verbose_name="Локация")
    base_type = models.CharField(max_length=30, verbose_name="Тип базы")

    def __str__(self):
        return f"Тип: {self.base_type}, местоположение: {self.id}"

class Weapon(models.Model):
    type = models.CharField(max_length=50, null=False, verbose_name="Тип оружия")
    model = models.ForeignKey('WeaponModel', on_delete=models.CASCADE, null=True, verbose_name="Модель оружия")
    ammo_amount = models.IntegerField(null=False, verbose_name="Количество боезапаса")
    military_base = models.ForeignKey('MilitaryBase', on_delete=models.CASCADE, verbose_name="Военная база")

    def __str__(self):
        return f"Тип: {self.type}, Количество боезапаса: {self.ammo_amount}"

class Enginiry(models.Model):
    function = models.CharField(max_length=200, null=False, verbose_name="Функция")
    military_base = models.ForeignKey(MilitaryBase, on_delete=models.CASCADE, verbose_name="Военная база")
    enginiry_type = models.ForeignKey(EnginiryType, on_delete=models.CASCADE, verbose_name="Тип инженерии")
    id = models.AutoField(primary_key=True, verbose_name="Идентификатор")

    def __str__(self):
        return f"Функция: {self.function}"

class BaseCodes(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Идентификатор")
    military_base = models.ForeignKey(MilitaryBase, on_delete=models.CASCADE, verbose_name="Военная база")

    def __str__(self):
        return f"Шифр: {self.id}, Военная база: {self.military_base}"
class Army(models.Model):
    type = models.CharField(max_length=40, verbose_name="Тип армии")
    country = models.CharField(max_length=40, verbose_name="Страна")
    base_cipher = models.ForeignKey(BaseCodes, on_delete=models.CASCADE, verbose_name="Код базы")

    def __str__(self):
        return f"Тип: {self.type}, Страна: {self.country}"

class Soldier(models.Model):
    full_name = models.CharField(max_length=99, null=False, verbose_name="Полное имя")
    rank = models.CharField(max_length=40, verbose_name="Звание")
    job = models.CharField(max_length=200, verbose_name="Должность")
    enginiry = models.ForeignKey(Enginiry, on_delete=models.CASCADE, null=True, verbose_name="Техника")
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, verbose_name="Оружие")
    military_base = models.ForeignKey(MilitaryBase, on_delete=models.CASCADE, null=True, verbose_name="Военная база")
    id = models.AutoField(primary_key=True, verbose_name="Идентификатор")

    def __str__(self):
        return f"Имя: {self.full_name}, Ранг: {self.rank}, Должность: {self.job}"
