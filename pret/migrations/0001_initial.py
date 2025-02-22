# Generated by Django 5.0.8 on 2024-08-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=20)),
                ('montant_du_pret', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duree_de_remboursement', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
