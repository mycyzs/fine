    $(function(){
        var get_business = function () {
            $.ajax({
                url: site_url+'get_biz',
                type: 'GET',
                success: function(res){
                    var html_str = ''
                    for(var biz in res.data){
                        html_str +='<option value="'+res.data[biz]["bk_biz_id"]+'">'+res.data[biz]["bk_biz_name"]+'</option>'
                    }
                    $('#biz_sel').html(html_str)
                    get_ip($('#biz_sel').val())
                }
            })
        };
        var get_ip = function (biz_id) {
            $.ajax({
                url: site_url+'get_ip?id='+biz_id,
                type: 'GET',
                success: function(res){
                    var html_str = ''
                    for(var ip in res.data){
                        html_str +='<option value="'+res.data[ip]['host']["bk_cloud_id"][0]['id']+'/'+res.data[ip]['host']["bk_host_innerip"]+'">'+res.data[ip]['host']["bk_host_innerip"]+'</option>'
                    }
                    $('#ip_sel').html(html_str)
                }
            })
        };
        get_business();
        $('#biz_sel').change(function () {
            get_ip($('#biz_sel').val())
        });
        $('#get_data').click(function () {
            var data = {
                'biz':$('#biz_sel').val(),
                'ip':$('#ip_sel').val(),
                'script':$('#script').val(),
            }
            $.ajax({
                url: site_url+'data',
                type: 'post',
                data:data,
                success: function(res){
                    $('#res').text(res.data)
                }
            })
        })
    });
