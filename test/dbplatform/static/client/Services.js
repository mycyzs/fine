services = angular.module('webApiService', ['ngResource', 'utilServices']);

//生产代码
var POST = "POST";
var GET = "GET";

//测试代码
//var sourceRoute = "./Client/MockData";
//var fileType = ".html";
//var POST = "GET";
//var GET = "GET";
services.factory('sysService', ['$resource', function ($resource) {
    return $resource(site_url + ':actionName/', {},
        {
            get_count_obj: {method: POST, params: {actionName: 'get_count_obj'}, isArray: false},
            add_sys: {method: POST, params: {actionName: 'add_sys'}, isArray: false},
            search_user: {method: POST, params: {actionName: 'search_user'}, isArray: false},
            modify_sys: {method: POST, params: {actionName: 'modify_sys'}, isArray: false},
            delete_sys: {method: POST, params: {actionName: 'delete_sys'}, isArray: false},
            search_mha: {method: POST, params: {actionName: 'search_mha'}, isArray: false},
            add_cluster: {method: POST, params: {actionName: 'add_cluster'}, isArray: false},
            search_cluster_info: {method: POST, params: {actionName: 'search_cluster_info'}, isArray: false},
            modify_cluster: {method: POST, params: {actionName: 'modify_cluster'}, isArray: false},
            delete_cluster: {method: POST, params: {actionName: 'delete_cluster'}, isArray: false},
            add_mysql_instance: {method: POST, params: {actionName: 'add_mysql_instance'}, isArray: false},
            search_instance_info: {method: POST, params: {actionName: 'search_instance_info'}, isArray: false},
            modify_instance: {method: POST, params: {actionName: 'modify_instance'}, isArray: false},
            delete_instance: {method: POST, params: {actionName: 'delete_instance'}, isArray: false},
            search_oracle_instance: {method: POST, params: {actionName: 'search_oracle_instance'}, isArray: false},
            add_oracle_instance: {method: POST, params: {actionName: 'add_oracle_instance'}, isArray: false},
            search_instance_detail: {method: POST, params: {actionName: 'search_instance_detail'}, isArray: false},
            modify_oracle_instance: {method: POST, params: {actionName: 'modify_oracle_instance'}, isArray: false},
            update_status: {method: POST, params: {actionName: 'update_status'}, isArray: false},

            // get_host_list: {method: POST, params: {actionName: 'get_host_list'}, isArray: false},
            search_oracle_cluster: {method: POST, params: {actionName: 'search_oracle_cluster'}, isArray: false},
            add_oracle_cluster: {method: POST, params: {actionName: 'add_oracle_cluster'}, isArray: false},
            modify_oracle_cluster: {method: POST, params: {actionName: 'modify_oracle_cluster'}, isArray: false},


            // 系统公用接口
            // 主机ip
            get_app_server_list: {method: POST, params: {actionName: 'get_app_server_list'}, isArray: false},
            get_all_server_list: {method: POST, params: {actionName: 'get_all_server_list'}, isArray: false},
            get_host_info_by_ip: {method: POST, params: {actionName: 'get_host_info_by_ip'}, isArray: false},
            // 系统名称
            search_sys_info: {method: POST, params: {actionName: 'search_sys_info'}, isArray: false},
            // 集群名称

            // 实例名称
            flash_instance: {method:POST, params: {actionName: 'flash_instance'}, isArray: false},


        });
}])

//mha 节点信息管理服务
.factory('mhaInfoService', ['$resource', function ($resource) {
    return $resource(site_url + ':actionName/', {},
        {
            get_message_all: {method: POST, params: {actionName: 'get_message_all'}, isArray: false},
            add_mha_node: {method: POST, params: {actionName: 'add_mha_node'}, isArray: false},
            del_mha_node: {method: POST, params: {actionName: 'del_mha_node'}, isArray: false},
            modify_mha: {method: POST, params: {actionName: 'modify_mha'}, isArray: false},
            get_message_term: {method: POST, params: {actionName: 'get_message_term'}, isArray: false},
            get_status: {method: POST, params: {actionName: 'get_status'}, isArray: false},
            start_mha: {method: POST, params: {actionName: 'start_mha'}, isArray: false},
            switch_mha: {method: POST, params: {actionName: 'switch_mha'}, isArray: false},
            get_sys_cluster: {method: POST, params: {actionName: 'get_sys_cluster'}, isArray: false},
            get_cluster_instance: {method: POST, params: {actionName: 'get_cluster_instance'}, isArray: false},
            mha_deploy: {method: POST, params: {actionName: 'mha_deploy'}, isArray: false},
        });
}])

    //lvs节点信息管理服务
    .factory('lvsService', ['$resource', function ($resource) {
        return $resource(site_url + ':actionName/', {},
            {
                search_lvs_info: {method: POST, params: {actionName: 'search_lvs_info'}, isArray: false},
                add_lvs: {method: POST, params: {actionName: 'add_lvs'}, isArray: false},
                modify_lvs: {method: POST, params: {actionName: 'modify_lvs'}, isArray: false},
                delete_lvs: {method: POST, params: {actionName: 'delete_lvs'}, isArray: false},
                search_qs_info: {method: POST, params: {actionName: 'search_qs_info'}, isArray: false},
                add_qs: {method: POST, params: {actionName: 'add_qs'}, isArray: false},
                modify_qs: {method: POST, params: {actionName: 'modify_qs'}, isArray: false},
                delete_qs: {method: POST, params: {actionName: 'delete_qs'}, isArray: false},
                get_sysname: {method: POST, params: {actionName: 'get_sysname'}, isArray: false},
                get_middle_install_file: {method: POST, params: {actionName: 'get_middle_install_file'}, isArray: false},
                get_middle_exist_port: {method: POST, params: {actionName: 'get_middle_exist_port'}, isArray: false},
                install_qs_instance: {method: POST, params: {actionName: 'install_qs_instance'}, isArray: false},
                install_lvs_instance: {method: POST, params: {actionName: 'install_lvs_instance'}, isArray: false},
                search_middle_install_task: {method: POST, params: {actionName: 'search_middle_install_task'}, isArray: false},
                search_middle_installtask_detail: {method: POST, params: {actionName: 'search_middle_installtask_detail'}, isArray: false},
                get_master_count: {method: POST, params: {actionName: 'get_master_count'}, isArray: false},
                get_lvs_count: {method: POST, params: {actionName: 'get_lvs_count'}, isArray: false},
                get_qsinfo: {method: POST, params: {actionName: 'get_qsinfo'}, isArray: false},
                get_ddb_param: {method: POST, params: {actionName: 'get_ddb_param'}, isArray: false},
                get_ddb_info: {method: POST, params: {actionName: 'get_ddb_info'}, isArray: false},
                checkconn: {method: POST, params: {actionName: 'checkconn'}, isArray: false},
                modify_ddb_param: {method: POST, params: {actionName: 'modify_ddb_param'}, isArray: false},
                // checkddbconfiginfo: {method: POST, params: {actionName: 'checkddbconfiginfo'}, isArray: false},
            })
    }])
    .factory('accountService', ['$resource', function ($resource) {
        return $resource(site_url + ':actionName/', {},
            {
                //账号管理
                get_accountinfos: {method: POST, params: {actionName: 'get_accountinfos'}, isArray: false},
                add_accountinfo: {method: POST, params: {actionName: 'add_accountinfo'}, isArray: false},
                del_accountinfo: {method: POST, params: {actionName: 'del_accountinfo'}, isArray: false},
                update_accountinfo: {method: POST, params: {actionName: 'update_accountinfo'}, isArray: false},
                get_account: {method: POST, params: {actionName: 'get_account'}, isArray: false},
                get_sysname: {method: POST, params: {actionName: 'get_sysname'}, isArray: false},
                //权限申请
                get_db_instance: {method: POST, params: {actionName: 'get_db_instance'}, isArray: false},
                get_db_account: {method: POST, params: {actionName: 'get_db_account'}, isArray: false},
                add_db_account: {method: POST, params: {actionName: 'add_db_account'}, isArray: false},
                get_oracle_db_instance: {method: POST, params: {actionName: 'get_oracle_db_instance'}, isArray: false},
                add_oracle_db_account: {method: POST, params: {actionName: 'add_oracle_db_account'}, isArray: false},
            });
    }])

    //系统配置
    .factory('settingService', ['$resource', function ($resource) {
        return $resource(site_url + ':actionName/', {},
            {
                //系统配置
                get_settings: {method: POST, params: {actionName: 'get_settings'}, isArray: false},
                get_setting_by_id: {method: POST, params: {actionName: 'get_setting_by_id'}, isArray: false},
                add_setting: {method: POST, params: {actionName: 'add_setting'}, isArray: false},
                update_setting: {method: POST, params: {actionName: 'update_setting'}, isArray: false},
                delete_setting: {method: POST, params: {actionName: 'delete_setting'}, isArray: false},

                //平台账号管理
                get_platform_accounts: {method: POST, params: {actionName: 'get_platform_accounts'}, isArray: false},
                get_platform_account_by_id: {method: POST, params: {actionName: 'get_platform_account_by_id'}, isArray: false},
                add_platform_account: {method: POST, params: {actionName: 'add_platform_account'}, isArray: false},
                update_platform_account: {method: POST, params: {actionName: 'update_platform_account'}, isArray: false},
                delete_platform_account: {method: POST, params: {actionName: 'delete_platform_account'}, isArray: false},

                //mysql参数管理
                get_mysql_parameters: {method: POST, params: {actionName: 'get_mysql_parameters'}, isArray: false},
                get_mysql_param_by_id: {method: POST, params: {actionName: 'get_mysql_param_by_id'}, isArray: false},
                add_mysql_param: {method: POST, params: {actionName: 'add_mysql_param'}, isArray: false},
                update_mysql_param: {method: POST, params: {actionName: 'update_mysql_param'}, isArray: false},
                delete_mysql_param: {method: POST, params: {actionName: 'delete_mysql_param'}, isArray: false},

                //mysql参数模板管理
                get_mycnf_templates: {method: POST, params: {actionName: 'get_mycnf_templates'}, isArray: false},
                get_mycnf_template_by_id: {method: POST, params: {actionName: 'get_mycnf_template_by_id'}, isArray: false},
                add_mycnf_template: {method: POST, params: {actionName: 'add_mycnf_template'}, isArray: false},
                update_mycnf_template: {method: POST, params: {actionName: 'update_mycnf_template'}, isArray: false},
                delete_mycnf_template: {method: POST, params: {actionName: 'delete_mycnf_template'}, isArray: false},

                get_mycnf_template_entries: {method: POST, params: {actionName: 'get_mycnf_template_entries'}, isArray: false},
                get_mycnf_template_entry_by_id: {method: POST, params: {actionName: 'get_mycnf_template_entry_by_id'}, isArray: false},
                add_mycnf_template_entry: {method: POST, params: {actionName: 'add_mycnf_template_entry'}, isArray: false},
                update_mycnf_template_entry: {method: POST, params: {actionName: 'update_mycnf_template_entry'}, isArray: false},
                delete_mycnf_template_entry: {method: POST, params: {actionName: 'delete_mycnf_template_entry'}, isArray: false},


                //操作日志
                search_operate_log: {method: POST, params: {actionName: 'search_operate_log'}, isArray: false},
                search_operate_type: {method: POST, params: {actionName: 'search_operate_type'}, isArray: false},


            });
    }]).factory('dataDumpService', ['$resource', function ($resource) {
    return $resource(site_url + ':actionName/', {},
        {
            //mysql导入导出
            get_mysql_instance: {method: POST, params: {actionName: 'get_mysql_instance'}, isArray: false},
            get_mysql_backup_path: {method: POST, params: {actionName: 'get_mysql_backup_path'}, isArray: false},
            execute_dataExport_shell: {method: POST, params: {actionName: 'execute_dataExport_shell'}, isArray: false},
            execute_dataImport_shell: {method: POST, params: {actionName: 'execute_dataImport_shell'}, isArray: false},
            get_filename: {method: POST, params: {actionName: 'get_filename'}, isArray: false},
            // get_ftp_info: {method: POST, params: {actionName: 'get_ftp_info'}, isArray: false},
            get_root_password: {method: POST, params: {actionName: 'get_root_password'}, isArray: false},
            get_mysql_backup_path_size: {method: POST, params: {actionName: 'get_mysql_backup_path_size'}, isArray: false},
                get_syscode: {method: POST, params: {actionName: 'get_syscode'}, isArray: false},
            //oracle的导入导出
            //获取系统名称集合
            get_appName_list: {method: POST, params: {actionName: 'get_appName_list'}, isArray: false},
            //获取DB_INSTANCE 信息
            get_instanceName_list: {method: POST, params: {actionName: 'get_instanceName_list'}, isArray: false},
            dump_oracle: {method: POST, params: {actionName: 'dump_oracle'}, isArray: false},
            get_impdir: {method: POST, params: {actionName: 'get_impdir'}, isArray: false},
            imp_ora: {method: POST, params: {actionName: 'imp_ora'}, isArray: false},
            execute_oracle_export_shell: {method: POST, params: {actionName: 'execute_oracle_export_shell'}, isArray: false},
            execute_oracle_import_shell: {method: POST, params: {actionName: 'execute_oracle_import_shell'}, isArray: false},
            get_oracle_backup_path_size: {method: POST, params: {actionName: 'get_oracle_backup_path_size'}, isArray: false}


        });


}])
// SQL上线
    .factory('sqlOnline', ['$resource', function ($resource) {
        return $resource(site_url + ':actionName/', {},
            {
                //获取集群
                get_instance_by_sys: {method: POST, params: {actionName: 'get_instance_by_sys'}, isArray: false},
                execute_sql: {method: POST, params: {actionName: 'execute_sql'}, isArray: false},
                search_sql_task: {method: POST, params: {actionName: 'search_sql_task'}, isArray: false},
                search_sqltask_detail: {method: POST, params: {actionName: 'search_sqltask_detail'}, isArray: false},
                check_sql: {method: POST, params: {actionName: 'check_sql'}, isArray: false},
                search_incep_param: {method: POST, params: {actionName: 'search_incep_param'}, isArray: false},
                refresh_param: {method: POST, params: {actionName: 'refresh_param'}, isArray: false},
                modify_incep_param: {method: POST, params: {actionName: 'modify_incep_param'}, isArray: false},
                get_oracle_by_sys: {method: POST, params: {actionName: 'get_oracle_by_sys'}, isArray: false},
                search_keyword: {method: POST, params: {actionName: 'search_keyword'}, isArray: false},
                add_keyword: {method: POST, params: {actionName: 'add_keyword'}, isArray: false},
                modify_keyword: {method: POST, params: {actionName: 'modify_keyword'}, isArray: false},
                delete_keyword: {method: POST, params: {actionName: 'delete_keyword'}, isArray: false},
                check_oracle_sql1: {method: POST, params: {actionName: 'check_oracle_sql1'}, isArray: false},
                exec_oracle_sql: {method: POST, params: {actionName: 'exec_oracle_sql'}, isArray: false},
                search_oracle_sql_detail: {method: POST, params: {actionName: 'search_oracle_sql_detail'}, isArray: false},
            });
    }])


    .factory('mysqlService', ['$resource', function ($resource) {
        return $resource(site_url + ':actionName/', {},
            {
                //实例部署
                find_mysql_parameter1: {method: POST, params: {actionName: 'find_mysql_parameter1'}, isArray: false},
                find_mysql_parameter2: {method: POST, params: {actionName: 'find_mysql_parameter2'}, isArray: false},
                parameter_commit: {method: POST, params: {actionName: 'parameter_commit'}, isArray: false},
                parameter_commit1: {method: POST, params: {actionName: 'parameter_commit1'}, isArray: false},
                get_exist_port: {method: POST, params: {actionName: 'get_exist_port'}, isArray: false},
                get_install_file: {method: POST, params: {actionName: 'get_install_file'}, isArray: false},
                get_mysql_user: {method: POST, params: {actionName: 'get_mysql_user'}, isArray: false},
                install_mysql_instance: {method: POST, params: {actionName: 'install_mysql_instance'}, isArray: false},
                search_install_task: {method: POST, params: {actionName: 'search_install_task'}, isArray: false},
                search_installtask_detail: {method: POST, params: {actionName: 'search_installtask_detail'}, isArray: false},
                install_master_slave: {method: POST, params: {actionName: 'install_master_slave'}, isArray: false},
                get_instances: {method: POST, params: {actionName: 'get_instances'}, isArray: false},
                install_slave_instance: {method: POST, params: {actionName: 'install_slave_instance'}, isArray: false},
                get_backup_path_by_instance_id: {method: POST, params: {actionName: 'get_backup_path_by_instance_id'}, isArray: false},
                create_relation: {method: POST, params: {actionName: 'create_relation'}, isArray: false},
                search_Relatetask_detail: {method: POST, params: {actionName: 'search_Relatetask_detail'}, isArray: false},
                //参数修改
                get_mysql_db_param_value: {method: POST, params: {actionName: 'get_mysql_db_param_value'}, isArray: false},
                get_mysql_cnf_param_value: {method: POST, params: {actionName: 'get_mysql_cnf_param_value'}, isArray: false},
                modify_mysql_param: {method: POST, params: {actionName: 'modify_mysql_param'}, isArray: false},

            })

    }]).factory('instanceStartStop', ['$resource', function ($resource) {
    return $resource(site_url + ':actionName/', {},
        {
            //mysql实例启停
            get_instance_info: {method: POST, params: {actionName: 'get_instance_info'}, isArray: false},
            start_instance: {method: POST, params: {actionName: 'start_instance'}, isArray: false},
            stop_instance: {method: POST, params: {actionName: 'stop_instance'}, isArray: false},

        });

}]).factory('instanceUpgrade', ['$resource', function ($resource) {
    return $resource(site_url + ':actionName/', {},
        {
            //mysql实例升级
            get_mysql_version_instance: {method: POST, params: {actionName: 'get_mysql_version_instance'}, isArray: false},
            get_host_mysql_instance: {method: POST, params: {actionName: 'get_host_mysql_instance'}, isArray: false},
            get_role_mha_tatus: {method: POST, params: {actionName: 'get_role_mha_tatus'}, isArray: false},
            upgrade_mysql_instance: {method: POST, params: {actionName: 'upgrade_mysql_instance'}, isArray: false},
        });

}])

    .factory('CheckService', ['$resource', function ($resource) {
        return $resource(site_url + ':actionName/', {},
            {
                // 项目管理模块
                get_item_list: {method: POST, params: {actionName: 'get_item_list', isArray: false}},
                add_item: {method: POST, params: {actionName: 'add_item', isArray: false}},
                delete_item: {method: POST, params: {actionName: 'delete_item', isArray: false}},
                modify_item: {method: POST, params: {actionName: 'modify_item', isArray: false}},
                item_detail: {method: POST, params: {actionName: 'item_detail', isArray: false}},
                // 模板管理模块
                get_temp_list: {method: POST, params: {actionName: 'get_temp_list', isArray: false}},
                delete_temp: {method: POST, params: {actionName: 'delete_temp', isArray: false}},
                add_temp: {method: POST, params: {actionName: 'add_temp', isArray: false}},
                get_item_name: {method: POST, params: {actionName: 'get_item_name', isArray: false}},
                get_item_default1: {method: POST, params: {actionName: 'get_item_default1', isArray: false}},
                get_item_default2: {method: POST, params: {actionName: 'get_item_default2', isArray: false}},
                show_temp_detail: {method: POST, params: {actionName: 'show_temp_detail', isArray: false}},
                modify_temp: {method: POST, params: {actionName: 'modify_temp', isArray: false}},
                // 任务管理模块
                get_task_list: {method: POST, params: {actionName: 'get_task_list'}, isArray: false},
                add_task: {method: POST, params: {actionName: 'add_task'}, isArray: false},
                delete_task: {method: POST, params: {actionName: 'delete_task', isArray: false}},
                modify_task: {method: POST, params: {actionName: 'modify_task', isArray: false}},
                get_temp_names: {method: POST, params: {actionName: 'get_temp_names', isArray: false}},
                get_db_names: {method: POST, params: {actionName: 'get_db_names', isArray: false}},
                get_task_detail: {method: POST, params: {actionName: 'get_task_detail', isArray: false}},
                run_task: {method: POST, params: {actionName: 'run_task', isArray: false}},
                //结果展现模块
                search_task_result: {method: POST, params: {actionName: 'search_task_result', isArray: false}},
                get_report_db_list: {method: POST, params: {actionName: 'get_report_db_list', isArray: false}},
                compare_values: {method: POST, params: {actionName: 'compare_values', isArray: false}},
                get_item_info: {method: POST, params: {actionName: 'get_item_info', isArray: false}},

            })
    }])


;//这是结束符，请勿删除