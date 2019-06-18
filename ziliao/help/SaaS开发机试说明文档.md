SaaS开发机试说明文档

## 1. 首页可以直接使用压缩包中的`index.html`

`任务执行记录`页推荐直接通过MagicBox拖拽

MagicBox地址：http://magicbox.bk.tencent.com

## 2. 相关组件调用访问链接

组件调用请参考`开发框架`内的说明文档`blueking/component/README`

> 有两种方式访问组件，shortcuts或ComponentClient。使用示例如下：

> 1. 使用shortcuts
> 
> 1.1 get_client_by_request
> 
>     from blueking.component.shortcuts import get_client_by_request
>     # 从环境配置获取APP信息，从request获取当前用户信息
>     client = get_client_by_request(request)
>     kwargs = {'bk_biz_id': 1}
>     result = client.cc.get_app_host_list(kwargs)
> 
> ...

开发过程中涉及的接口文档：

- 主机查询接口文档：https://paas-poc.o.qcloud.com/esb/api_docs/system/CC/search_host/
- 业务查询接口文档：https://paas-poc.o.qcloud.com/esb/api_docs/system/CC/search_business/
- 集群查询接口文档：https://paas-poc.o.qcloud.com/esb/api_docs/system/CC/search_set/
- 作业启动接口文档：https://paas-poc.o.qcloud.com/esb/api_docs/system/JOB/execute_job/
- 作业模板详情查询接口文档：https://paas-poc.o.qcloud.com/esb/api_docs/system/JOB/get_job_detail/
- 作业状态查询接口文档：https://paas-poc.o.qcloud.com/esb/api_docs/system/JOB/get_job_instance_status/
- 作业日志查询接口文档：https://paas-poc.o.qcloud.com/esb/api_docs/system/JOB/get_job_instance_log/


## 3. 配置平台主机查询接口参数示例

```python

# bk_app_id为配置平台的业务id
# bk_set_id为配置平台的集群id

kwargs = {
        "page": {"start": 0, "limit": 5, "sort": "bk_host_id"},
        "ip": {
            "flag": "bk_host_innerip|bk_host_outerip",
            "exact": 1,
            "data": []
        },
        "condition": [
            {
                "bk_obj_id": "host",
                "fields": [
                ],
                "condition": []
            },
            {"bk_obj_id": "module", "fields": [], "condition": []},
            {"bk_obj_id": "set", "fields": [], "condition": [
                {
                    "field": "bk_set_id",
                    "operator": "$eq",
                    "value": bk_set_id
                }
            ]},
            {
                "bk_obj_id": "biz",
                "fields": [
                    "default",
                    "bk_biz_id",
                    "bk_biz_name",
                ],
                "condition": [
                    {
                        "field": "bk_biz_id",
                        "operator": "$eq",
                        "value": bk_biz_id
                    }
                ]
            }
        ]
    }
```

## 4. Ajax请求注意事项

因为测试环境和正式环境的app访问地址携带了`/[t|o]/bk_app_id/`前缀，故需要在ajax请求地址前固定添加以上前缀，所以若你使用的是开发框架
自带的mako模板渲染，需要在`index.html`的`head`部分增加以下内容（`index.html`中已经提前放好，直接去掉注释即可）：

```javascript
<script type="text/javascript">
    var app_id = "${APP_ID}";
    var site_url = "${SITE_URL}";	  // app的url前缀,在ajax调用的时候，应该加上该前缀
    var static_url = "${STATIC_URL}"; // 静态资源前缀
</script>
```

并且在发起ajax请求时，固定添加前缀`site_url`，比如：

```javascript
<script type="text/javascript">
$.ajax({
    // url: '${ SITE_URL }api/get_hosts/',
    url: site_url + 'api/get_hosts/',
    type: 'GET',
    data: {},
    success: function (res) {

    }
});
</script>
```


## 5. POST请求出现403(csrf验证失败)的解决方法

在页面中引入开发框架目录下的：`static/js/csrftoken.js`，且确保在`jquery`后面引入

```html
<script src="${STATIC_URL}js/csrftoken.js" type="text/javascript"></script>
```

## 6. 关于考试提供的作业的使用方法说明

1. 考试环境中会提供一个内置好的作业模板，该模板位于`考试专用业务下`，且只能下发到该业务下的主机上执行，作业中只有一个脚本步骤，脚本内容见`stat.sh`
2. 根据作业模板启动作业时，接口调用涉及的部分参数（如`step_id`、`script_id`）必须通过作业模板查询接口获得
