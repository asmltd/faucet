/**
 * Created by hariharaselvam on 7/12/16.
 */
window[appName].controller('sdn_add_flow_controller', function ($rootScope, $scope, $state, $stateParams, $http, $window, $location, $q, $filter) {

    console.log("Called");

    if ($scope.logged_in == undefined || $scope.logged_in == "") {
        window.location = "index.html";
    }

    $scope.itemperpage = 10;
    $scope.sw_pagination = {};
    $scope.sw_pagination.current = 1;

    function HttpRequest(method, action, URL, parameter) {

        $rootScope.showLoader = true;

        var $promise = '';
        if (method === "post") {
            $promise = $http.post(URL, parameter);
        } else {
            $promise = $http.get(URL, parameter);
        }
        $promise.then(function (response) {
            var result = angular.fromJson(response.data);
            processTheData(action, result);

            $rootScope.showLoader = false;

        });
    };

    function processTheData(action, response) {

        if (response["authentication"] == false) {
            window.location = "index.html";
        }

        switch (action) {


            case 'add_flow':
                if (response["ok"]) {
                    bootbox.alert("Flow added successfully!");


                }
                else {
                    bootbox.alert("Add Flow failed!");
                }

                console.log(response);
                break;

        }

    }


    $scope.flow_delete = function (id, rev) {

        var param = {"cancel": true};

        bootbox.confirm("Are you sure you want to delete the flow " + id + "?", function (result) {
            if (result) {
                param = {"id": id, "rev": rev};
                HttpRequest('post', 'delete_flow', window.flaskURL + 'delete_flow', param);
            }
        });

    }

    $scope.add_flow = function () {
        HttpRequest('post', 'add_flow', window.flaskURL + 'add_flow', JSON.parse($scope.flow));
    }


});

