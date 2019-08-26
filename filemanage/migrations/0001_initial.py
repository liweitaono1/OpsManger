# Generated by Django 2.1.4 on 2019-08-03 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDownload_Audit_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_content', models.TextField(verbose_name='工单申请内容')),
                ('dest_server', models.TextField(verbose_name='目标服务器')),
                ('dest_path', models.CharField(max_length=200, verbose_name='文件路径')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.Order_System')),
            ],
            options={
                'verbose_name': '工单管理',
                'verbose_name_plural': '文件下载审核工单表',
                'db_table': 'opsmanage_filedownload_audit_order',
                'permissions': (('filemanage_read_filedownload_audit_order', '读取文件下载审核工单权限'), ('filemanage_change_filedownload_audit_order', '更改文件下载审核工单权限'), ('filemanage_add_filedownload_audit_order', '添加文件下载审核工单权限'), ('filemanage_delete_filedownload_audit_order', '删除文件下载审核工单权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='FileUpload_Audit_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_path', models.CharField(max_length=200, verbose_name='目标服务器文件路径')),
                ('order_content', models.TextField(verbose_name='工单申请内容')),
                ('dest_server', models.TextField(verbose_name='目标服务器')),
                ('chown_user', models.CharField(max_length=100, verbose_name='文件宿主')),
                ('chown_rwx', models.CharField(max_length=100, verbose_name='文件权限')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.Order_System')),
            ],
            options={
                'verbose_name': '工单管理',
                'verbose_name_plural': '文件上传审核工单表',
                'db_table': 'opsmanage_fileupload_audit_order',
                'permissions': (('filemanage_read_fileupload_audit_order', '读取文件上传审核工单权限'), ('filemanage_change_fileupload_audit_order', '更改文件上传审核工单权限'), ('filemanage_add_fileupload_audit_order', '添加文件上传审核工单权限'), ('filemanage_delete_fileupload_audit_order', '删除文件上传审核工单权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(max_length=500, upload_to='./file/upload/%Y%m%d%H%M%S/', verbose_name='文件上传路径')),
                ('file_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='文件类型')),
                ('file_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploadfiles', to='filemanage.FileUpload_Audit_Order')),
            ],
            options={
                'db_table': 'opsmanage_uploadfiles',
                'default_permissions': (),
            },
        ),
    ]
