# Generated by Django 4.0.6 on 2022-09-14 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=12, unique=True, verbose_name='사용자 아이디')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('type', models.CharField(choices=[('manager', '운영자'), ('general', '일반 사용자')], default='general', max_length=100, verbose_name='유저 유형')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
