# Generated by Django 2.1.4 on 2019-08-03 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_High_Risk_SQL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sql', models.CharField(max_length=200, unique=True, verbose_name='SQL内容')),
            ],
            options={
                'verbose_name': '数据库管理',
                'verbose_name_plural': '自定义高危SQL表',
                'db_table': 'opsmanage_custom_high_risk_sql',
                'permissions': (('database_read_custom_high_risk_sql', '读取高危SQL表权限'), ('database_change_custom_high_risk_sql', '更改高危SQL表权限'), ('database_add_custom_high_risk_sql', '添加高危SQL表权限'), ('database_delete_custom_high_risk_sql', '删除高危SQL表权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Database_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db', models.SmallIntegerField(verbose_name='db_id')),
                ('group', models.SmallIntegerField(verbose_name='用户id')),
            ],
            options={
                'verbose_name': '数据库管理',
                'verbose_name_plural': '用户组数据库分配表',
                'db_table': 'opsmanage_database_group',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='DataBase_Server_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_env', models.CharField(choices=[('alpha', '开发环境'), ('beta', '测试环境'), ('ga', '生产环境')], default=None, max_length=10, verbose_name='环境类型')),
                ('db_type', models.CharField(blank=True, max_length=10, null=True, verbose_name='数据库类型')),
                ('db_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='数据库名')),
                ('db_mode', models.SmallIntegerField(choices=[(1, '单例'), (2, '主从'), (3, 'pxc'), (4, 'Tidb'), (5, 'Bhproxy'), (6, 'ProxySQL')], default=1, verbose_name='架构类型')),
                ('db_user', models.CharField(blank=True, max_length=100, null=True, verbose_name='用户')),
                ('db_passwd', models.CharField(blank=True, max_length=100, null=True, verbose_name='密码')),
                ('db_port', models.IntegerField(verbose_name='端口')),
                ('db_mark', models.CharField(blank=True, max_length=100, null=True, verbose_name='标识')),
                ('db_rw', models.CharField(blank=True, choices=[('read', '只读'), ('r/w', '读写'), ('write', '可写')], max_length=20, null=True, verbose_name='读写类型')),
                ('db_assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='database_total', to='asset.Assets', verbose_name='assets_id')),
            ],
            options={
                'verbose_name': '数据库管理',
                'verbose_name_plural': '数据库信息表',
                'db_table': 'opsmanage_database_server_config',
                'permissions': (('database_read_database_server_config', '读取数据库信息表权限'), ('database_change_database_server_config', '更改数据库信息表权限'), ('database_add_database_server_config', '添加数据库信息表权限'), ('database_delete_database_server_config', '删除数据库信息表权限'), ('database_query_database_server_config', '数据库查询查询权限'), ('databases_dml_database_server_config', '数据库执行DML语句权限'), ('database_binlog_database_server_config', '数据库Binglog解析权限'), ('database_schema_database_server_config', '数据库表结构查询权限'), ('database_optimize_database_server_config', '数据库SQL优化建议权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Database_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db', models.SmallIntegerField(verbose_name='db_id')),
                ('user', models.SmallIntegerField(verbose_name='用户id')),
                ('tables', models.TextField(blank=True, null=True, verbose_name='可以操作的表')),
                ('privs', models.CharField(blank=True, max_length=250, null=True, verbose_name='SQL类型')),
            ],
            options={
                'verbose_name': '数据库管理',
                'verbose_name_plural': '用户数据库分配表',
                'db_table': 'opsmanage_database_user',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SQL_Execute_Histroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exe_user', models.CharField(max_length=100, verbose_name='执行人')),
                ('exe_sql', models.TextField(verbose_name='执行的SQL内容')),
                ('exec_status', models.SmallIntegerField(blank=True, null=True, verbose_name='执行状态')),
                ('exe_result', models.TextField(blank=True, null=True, verbose_name='执行结果')),
                ('exe_time', models.IntegerField(default=0, verbose_name='执行时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='执行时间')),
                ('exe_db', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.DataBase_Server_Config', verbose_name='数据库id')),
            ],
            options={
                'verbose_name': '数据库管理',
                'verbose_name_plural': 'SQL执行历史记录表',
                'db_table': 'opsmanage_sql_execute_histroy',
                'permissions': (('database_read_sql_execute_histroy', '读取SQL执行历史表权限'), ('database_change_sql_execute_histroy', '更改SQL执行历史表权限'), ('database_add_sql_execute_histroy', '添加SQL执行历史表权限'), ('database_delete_sql_execute_histroy', '删除SQL执行历史表权限')),
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='database_user',
            unique_together={('db', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='database_group',
            unique_together={('db', 'group')},
        ),
        migrations.AlterUniqueTogether(
            name='database_server_config',
            unique_together={('db_port', 'db_assets', 'db_env', 'db_name')},
        ),
    ]