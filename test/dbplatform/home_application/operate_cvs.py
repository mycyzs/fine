# -*- coding:utf-8 -*-

import csv, codecs
import os
from django.http import HttpResponse
from common.log import logger
from conf.default import PROJECT_ROOT
from home_application.models import *


# 导出cvs文件
def download_file(file_path, file_name):
    try:
        file_path = file_path
        file_buffer = open(file_path, 'rb').read()
        response = HttpResponse(file_buffer, content_type='APPLICATION/OCTET-STREAM')
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        response['Content-Length'] = os.path.getsize(file_path)
        return response
    except Exception as e:
        logger.exception("download file error:{0}".format(e.message))
        return False


def down_cvs(request):
    try:
        instances = DbInstance.objects.filter(dbcluster__sysname__db_type='MySQL')
        data_list = []
        for i in instances:
            mysql_instance = MysqlInstance.objects.get(dbinstance=i)
            data_list.append([i.dbcluster.sysname.sys_name,i.dbcluster.sysname.sys_code, i.dbcluster.sysname.department, i.dbcluster.cluster_name, i.instance_name, i.ip, i.port, i.role,
            mysql_instance.mysql_version, i.base_dir, mysql_instance.param_dir, mysql_instance.backup_path, mysql_instance.is_read_only

            ])
        f = codecs.open('MySQL-Info.csv', 'wb', "gbk")
        writer = csv.writer(f)
        writer.writerow([u"系统名",u"系统简称", u"所属产品线",u"集群名", u"实例名", u"IP地址", u"端口", u"主从角色", u"数据库版本",u"安装目录",u"参数路径", u"备份路径", u"是否只读"])
        writer.writerows(data_list)
        f.close()
        file_path = "{0}/MySQL-Info.csv".format(PROJECT_ROOT).replace("\\", "/")
        file_name = "MySQL-Info.csv"
        return download_file(file_path, file_name)
    except Exception as e:
        logger.exception('download cvs file error:{0}'.format(e.message))
        return False


def down_oracle_csv(request):
    try:
        instance = DbInstance.objects.filter(dbcluster__sysname__db_type="Oracle")
        data_list = []
        for i in instance:
            oracle_instance = OracleInstance.objects.get(dbinstance=i)
            oracle_cluster = OracleCluster.objects.get(dbcluster_id=i.dbcluster_id)
            sys_name = i.dbcluster.sysname.sys_name
            sys_code = i.dbcluster.sysname.sys_code
            cluster_name = i.dbcluster.cluster_name
            cluster_vip = i.dbcluster.cluster_vip
            is_cluster = oracle_cluster.is_cluster
            dns_name = oracle_cluster.dns_name
            db_version = oracle_cluster.db_version
            db_unique_name = oracle_cluster.db_unique_name
            scan_ip2 = oracle_cluster.scan_ip2
            scan_ip3 = oracle_cluster.scan_ip3
            status = i.status
            role = i.role
            port = i.port
            base_dir = i.base_dir
            db_vip = oracle_instance.db_vip
            service_names = oracle_instance.service_names
            up_time = oracle_instance.up_time
            param_path = oracle_instance.param_path
            pip = oracle_instance.private_ip
            db_name = oracle_instance.db_name
            data_list.append([sys_name,sys_code,cluster_name ,is_cluster, cluster_vip,dns_name,db_version,db_unique_name,scan_ip2,scan_ip3,status,role,port,base_dir,db_vip,
                              service_names,up_time,param_path,pip,db_name])
        f = codecs.open('Oracle-Info.csv', 'wb', "gbk")
        writer = csv.writer(f)
        writer.writerow(
            [u"系统名", u"系统简称", u"集群名",u"是否集群", u"SCANIP1",u"域名",u"数据库版本",u"数据库唯一名",u"SCANIP2",u"SCANIP3",u"状态", u"角色", u"端口", u"ORACLE_HOME",
             u"实例vip", u"服务名", u"启动时间",u"spfile路径",u"心跳IP",u"数据库"])
        writer.writerows(data_list)
        f.close()
        file_path = "{0}/Oracle-Info.csv".format(PROJECT_ROOT).replace("\\", "/")
        file_name = "Oracle-Info.csv"
        return download_file(file_path, file_name)


    except Exception, e:
        logger.log(e)
        return False
