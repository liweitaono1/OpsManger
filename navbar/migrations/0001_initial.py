# Generated by Django 2.1.4 on 2019-08-03 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nav_Third',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, unique=True)),
                ('icon', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '站内导航管理',
                'verbose_name_plural': '第三方站点分类表',
                'db_table': 'opsmanage_nav_third',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Nav_Third_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav_name', models.CharField(max_length=100)),
                ('width', models.CharField(max_length=50, verbose_name='宽度')),
                ('height', models.CharField(max_length=50, verbose_name='高度')),
                ('url', models.TextField()),
                ('nav_third', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nav_third_number', to='navbar.Nav_Third')),
            ],
            options={
                'verbose_name': '站内导航管理',
                'verbose_name_plural': '第三方站点详情表',
                'db_table': 'opsmanage_nav_third_number',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Nav_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '站内导航管理',
                'verbose_name_plural': '站内导航分类表',
                'db_table': 'opsmanage_nav_type',
                'permissions': (('nav_read_nav_type', '读取站内导航权限'), ('nav_change_nav_type', '更改站内导航权限'), ('nav_add_nav_type', '添加站内导航权限'), ('nav_delete_nav_type', '删除站内导航权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Nav_Type_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav_name', models.CharField(max_length=100)),
                ('nav_desc', models.CharField(max_length=200)),
                ('nav_url', models.TextField()),
                ('nav_img', models.FileField(blank=True, null=True, upload_to='./avatar/', verbose_name='图片路径')),
                ('nav_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nav_type_number', to='navbar.Nav_Type')),
            ],
            options={
                'verbose_name': '站内导航管理',
                'verbose_name_plural': '站内导航详情表',
                'db_table': 'opsmanage_nav_number',
                'permissions': (('nav_read_nav_number', '读取站内导航详情权限'), ('nav_change_nav_number', '更改站内导航详情权限'), ('nav_add_nav_number', '添加站内导航详情权限'), ('nav_delete_nav_number', '删除站内导航详情权限')),
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='nav_type_number',
            unique_together={('nav_type', 'nav_name')},
        ),
        migrations.AlterUniqueTogether(
            name='nav_third_number',
            unique_together={('nav_third', 'nav_name')},
        ),
    ]
