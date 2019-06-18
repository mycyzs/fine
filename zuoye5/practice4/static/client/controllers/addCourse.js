controllers.controller("addCourse", function ($scope, $modal, errorModal, sysService, loading, confirmModal, msgModal, $modalInstance, objectItem) {

    $scope.args = {
        title: '',
        tip: '',
        content: '',
        bk_biz_id: '',
        is_show: false
    };

    if (objectItem) {
        $scope.args = {
            title: objectItem.title,
            tip: objectItem.tip,
            content: objectItem.content,
            is_show: objectItem.is_show,
            image_base64: "data:image/jpeg;base64," + objectItem.image,
            bk_biz_name: objectItem.bk_biz_name,
            bk_biz_id: objectItem.bk_biz_id,
            id: objectItem.id,
            is_update: objectItem.is_update
        }
    }

    $scope.searchBiz = function () {
        sysService.search_biz({}, {}, function (res) {
            if (res.result) {
                $scope.biz_list = res.data
            } else {
                errorModal.open(['系统错误，联系管理员'])
            }
        })
    };
    $scope.searchBiz();


    $scope.confirm = function () {
        var formData = new FormData();
        formData.append('file', $('#file')[0].files[0]);
        formData.append('title', $scope.args.title);
        formData.append('tip', $scope.args.tip);
        formData.append('bk_biz_id', $scope.args.bk_biz_id);
        formData.append('content', $scope.args.content);
        if ($scope.args.id) {
            formData.append('id', $scope.args.id);
        }
        if ($scope.args.is_update) {
            $.ajax({
                url: 'update_course',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: function () {
                    msgModal.open('success', '创建成功')

                }
            });
            $modalInstance.close();
        } else {
            $.ajax({
                url: 'create_course',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: function () {
                    msgModal.open('success', '创建成功')

                }
            });
            $modalInstance.close();
        }


    };


    $scope.cancel = function () {
        $modalInstance.dismiss("cancel");
    }

    if ($scope.args.is_show) {
        sysService.add_history({}, {id: $scope.args.id}, function () {

        })
    }
});