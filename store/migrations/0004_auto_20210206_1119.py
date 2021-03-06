# Generated by Django 3.1.6 on 2021-02-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_date', models.IntegerField(max_length=20)),
                ('recycle_message', models.CharField(max_length=2000)),
                ('admin_message', models.CharField(max_length=2000)),
                ('sale_image', models.ImageField(upload_to='uploads/special/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
