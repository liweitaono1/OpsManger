# Generated by Django 2.1.4 on 2019-08-03 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assets_type', models.CharField(choices=[('server', '服务器'), ('vmser', '虚拟机'), ('switch', '交换机'), ('route', '路由器'), ('printer', '打印机'), ('scanner', '扫描仪'), ('firewall', '防火墙'), ('storage', '存储设备'), ('wifi', '无线设备')], default='server', max_length=100, verbose_name='资产类型')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='资产编号')),
                ('sn', models.CharField(blank=True, max_length=100, null=True, verbose_name='设备序列号')),
                ('buy_time', models.DateField(blank=True, null=True, verbose_name='购买时间')),
                ('expire_date', models.DateField(blank=True, null=True, verbose_name='过保修期')),
                ('buy_user', models.SmallIntegerField(blank=True, null=True, verbose_name='购买人')),
                ('management_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True, verbose_name='制造商')),
                ('provider', models.CharField(blank=True, max_length=100, null=True, verbose_name='供货商')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='资产型号')),
                ('status', models.SmallIntegerField(blank=True, null=True, verbose_name='状态')),
                ('put_zone', models.SmallIntegerField(blank=True, null=True, verbose_name='放置区域')),
                ('group', models.SmallIntegerField(blank=True, null=True, verbose_name='使用组')),
                ('business', models.SmallIntegerField(blank=True, null=True, verbose_name='业务类型')),
                ('project', models.SmallIntegerField(blank=True, null=True, verbose_name='项目类型')),
                ('host_vars', models.TextField(blank=True, null=True, verbose_name='ansible主机变量')),
                ('mark', models.TextField(blank=True, null=True, verbose_name='资产标示')),
                ('cabinet', models.SmallIntegerField(blank=True, null=True, verbose_name='机柜位置')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '总资产表',
                'db_table': 'opsmanage_assets',
                'permissions': (('assets_read_assets', '读取资产权限'), ('assets_change_assets', '更改资产权限'), ('assets_add_assets', '添加资产权限'), ('assets_delete_assets', '删除资产权限'), ('assets_dumps_assets', '导出资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Cabinet_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinet_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='机柜名称')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '机柜资产表',
                'db_table': 'opsmanage_cabinet_assets',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Disk_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_volume', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘容量')),
                ('device_status', models.SmallIntegerField(blank=True, null=True, verbose_name='硬盘状态')),
                ('device_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘型号')),
                ('device_brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘生产商')),
                ('device_serial', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘序列号')),
                ('device_slot', models.SmallIntegerField(blank=True, null=True, verbose_name='硬盘插槽')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Assets')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '磁盘资产表',
                'db_table': 'opsmanage_disk_assets',
                'permissions': (('assets_read_disk', '读取磁盘资产权限'), ('assets_change_disk', '更改磁盘资产权限'), ('assets_add_disk', '添加磁盘资产权限'), ('assets_delete_disk', '删除磁盘资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Line_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '出口线路资产表',
                'db_table': 'opsmanage_line_assets',
                'permissions': (('assets_read_line', '读取出口线路资产权限'), ('assets_change_line', '更改出口线路资产权限'), ('assets_add_line', '添加出口线路资产权限'), ('assets_delete_line', '删除出口线路资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Log_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assets_id', models.IntegerField(blank=True, default=None, null=True, verbose_name='资产类型id')),
                ('assets_user', models.CharField(default=None, max_length=50, verbose_name='操作用户')),
                ('assets_content', models.CharField(default=None, max_length=100, verbose_name='名称')),
                ('assets_type', models.CharField(default=None, max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='执行时间')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '项目配置操作记录表',
                'db_table': 'opsmanage_log_assets',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Network_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandwidth', models.CharField(blank=True, max_length=100, null=True, verbose_name='背板带宽')),
                ('ip', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='管理ip')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('passwd', models.CharField(blank=True, max_length=100, null=True)),
                ('sudo_passwd', models.CharField(blank=True, max_length=100, null=True)),
                ('port', models.DecimalField(decimal_places=0, default=22, max_digits=6)),
                ('port_number', models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')),
                ('firmware', models.CharField(blank=True, max_length=100, null=True, verbose_name='固件版本')),
                ('cpu', models.CharField(blank=True, max_length=100, null=True, verbose_name='cpu型号')),
                ('stone', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存大小')),
                ('configure_detail', models.TextField(blank=True, max_length=100, null=True, verbose_name='配置说明')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Assets')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '网络资产表',
                'db_table': 'opsmanage_network_assets',
                'permissions': (('assets_read_network', '读取网络资产权限'), ('assets_change_network', '更改网络资产权限'), ('assets_add_network', '添加网络资产权限'), ('assets_delete_network', '删除网络资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='NetworkCard_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(blank=True, max_length=20, null=True)),
                ('macaddress', models.CharField(blank=True, max_length=64, null=True, verbose_name='MAC')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('module', models.CharField(blank=True, max_length=50, null=True)),
                ('mtu', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.SmallIntegerField(blank=True, null=True, verbose_name='是否在线')),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Assets')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '服务器网卡资产表',
                'db_table': 'opsmanage_networkcard_assets',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Project_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('project_owner', models.SmallIntegerField(blank=True, null=True, verbose_name='项目负责人')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '项目资产表',
                'db_table': 'opsmanage_project_assets',
                'permissions': (('assets_read_project', '读取产品线权限'), ('assets_change_project', '更改产品线权限'), ('assets_add_project', '添加产品线权限'), ('assets_delete_project', '删除产品线权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Raid_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raid_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': 'Raid资产表',
                'db_table': 'opsmanage_raid_assets',
                'permissions': (('assets_read_raid', '读取Raid资产权限'), ('assets_change_raid', '更改Raid资产权限'), ('assets_add_raid', '添加Raid资产权限'), ('assets_delete_raid', '删除Raid资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Ram_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存型号')),
                ('device_volume', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存容量')),
                ('device_brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存生产商')),
                ('device_slot', models.SmallIntegerField(blank=True, null=True, verbose_name='内存插槽')),
                ('device_status', models.SmallIntegerField(blank=True, null=True, verbose_name='内存状态')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Assets')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '内存资产表',
                'db_table': 'opsmanage_ram_assets',
                'permissions': (('assets_read_ram', '读取内存资产权限'), ('assets_change_ram', '更改内存资产权限'), ('assets_add_ram', '添加内存资产权限'), ('assets_delete_ram', '删除内存资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Server_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('hostname', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('passwd', models.CharField(blank=True, default='root', max_length=100, null=True)),
                ('sudo_passwd', models.CharField(blank=True, max_length=100, null=True)),
                ('keyfile', models.SmallIntegerField(blank=True, null=True)),
                ('port', models.DecimalField(decimal_places=0, default=22, max_digits=6)),
                ('line', models.SmallIntegerField(blank=True, null=True)),
                ('cpu', models.CharField(blank=True, max_length=100, null=True)),
                ('cpu_number', models.SmallIntegerField(blank=True, null=True)),
                ('vcpu_number', models.SmallIntegerField(blank=True, null=True)),
                ('cpu_core', models.SmallIntegerField(blank=True, null=True)),
                ('disk_total', models.IntegerField(blank=True, null=True)),
                ('ram_total', models.IntegerField(blank=True, null=True)),
                ('kernel', models.CharField(blank=True, max_length=100, null=True)),
                ('selinux', models.CharField(blank=True, max_length=100, null=True)),
                ('swap', models.CharField(blank=True, max_length=100, null=True)),
                ('raid', models.SmallIntegerField(blank=True, null=True)),
                ('system', models.CharField(blank=True, max_length=100, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Assets')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '服务器资产表',
                'db_table': 'opsmanage_server_assets',
                'permissions': (('assets_read_server', '读取服务器资产权限'), ('assets_change_server', '更改服务器资产权限'), ('assets_add_server', '添加服务器资产权限'), ('assets_delete_server', '删除服务器资产权限'), ('assets_webssh_server', '登陆服务器资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Service_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_assets', to='asset.Project_Assets')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '业务分组表',
                'db_table': 'opsmanage_service_assets',
                'permissions': (('assets_read_service', '读取业务资产权限'), ('assets_change_service', '更改业务资产权限'), ('assets_add_service', '添加业务资产权限'), ('assets_delete_service', '删除业务资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Tags_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags_name', models.CharField(default=None, max_length=100, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '资产标签表',
                'db_table': 'opsmanage_tags_assets',
                'permissions': (('assets_read_tags', '读取标签资产权限'), ('assets_change_tags', '更改标签资产权限'), ('assets_add_tags', '添加标签资产权限'), ('assets_delete_tags', '删除标签资产权限'), ('assets_read_tree', '读取资产数权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Tags_Server_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='asset.Assets')),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_assets', to='asset.Tags_Assets')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '资产标签对应表',
                'db_table': 'opsmanage_tags_server',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='User_Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_assets', to='asset.Assets')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '用户资产表',
                'db_table': 'opsmanage_user_assets',
                'permissions': (('assets_add_user', '添加用户权限'), ('assets_change_user', '修改用户权限'), ('assets_delete_user', '删除用户权限'), ('assets_read_user', '读取用户权限')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Zone_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=100, unique=True)),
                ('zone_contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='机房联系人')),
                ('zone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='联系人号码')),
                ('zone_local', models.CharField(blank=True, max_length=200, null=True, verbose_name='机房地理位置')),
                ('zone_network', models.CharField(blank=True, max_length=100, null=True, verbose_name='机房网段')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '机房资产表',
                'db_table': 'opsmanage_zone_assets',
                'permissions': (('assets_read_zone', '读取机房资产权限'), ('assets_change_zone', '更改机房资产权限'), ('assets_add_zone', '添加机房资产权限'), ('assets_delete_zone', '删除机房资产权限')),
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='cabinet_assets',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinet_assets', to='asset.Zone_Assets'),
        ),
        migrations.AlterUniqueTogether(
            name='user_server',
            unique_together={('assets', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='tags_server_assets',
            unique_together={('aid', 'tid')},
        ),
        migrations.AlterUniqueTogether(
            name='service_assets',
            unique_together={('project', 'service_name')},
        ),
        migrations.AlterUniqueTogether(
            name='ram_assets',
            unique_together={('assets', 'device_slot')},
        ),
        migrations.AlterUniqueTogether(
            name='networkcard_assets',
            unique_together={('assets', 'macaddress')},
        ),
        migrations.AlterUniqueTogether(
            name='disk_assets',
            unique_together={('assets', 'device_slot')},
        ),
        migrations.AlterUniqueTogether(
            name='cabinet_assets',
            unique_together={('zone', 'cabinet_name')},
        ),
    ]
