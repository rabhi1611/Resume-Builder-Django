# Generated by Django 4.0.1 on 2022-05-24 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builderApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_of_interest_detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('Phd', 'Male'), ('Mtech/MA/MSc/MCom/MBA', 'Masters'), ('BE/Btech/BA/BSc/BCom', 'Masters'), ('12th', 'High School')], max_length=50)),
                ('stream', models.CharField(max_length=100)),
                ('passing_year', models.DateField()),
                ('result', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_detail', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_builderApp.person')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectOrJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(choices=[('J', 'Job'), ('P', 'Project')], max_length=1)),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_builderApp.person')),
            ],
        ),
        migrations.DeleteModel(
            name='resume',
        ),
        migrations.AddField(
            model_name='education',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_builderApp.person'),
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_builderApp.person'),
        ),
        migrations.AddField(
            model_name='academics',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_builderApp.person'),
        ),
    ]
