var app = angular.module('myApp', ['ngSanitize']);

app.controller('myCtrl', function($scope, $http, $location, $sce) {
    
    
    $scope.init = function(page){
        
        $scope.changeLanguage('fr');
        $scope.page=$location.path().replace("/", "");
        
        if ($location.path()===""){
            $scope.page="CV";
        }
        
    };
   
    $scope.getData = function(lang){
        $http.get("ressources/CV-"+lang+".json").success(function(response) {
            $scope.cv = response.CV;
        });
        $http.get("ressources/portal-"+lang+".json").success(function(response) {
            $scope.portal = response;
        });
        
    }

    $scope.changeLanguage = function(language){
        $scope.getData(language);
    };
    
    $scope.changePage = function(page){
        $location.path(page);
        $scope.page=page;
    };
    
    $scope.trustHTML = function(text){
        return($sce.trustAsHtml(text));
    };
    
});

