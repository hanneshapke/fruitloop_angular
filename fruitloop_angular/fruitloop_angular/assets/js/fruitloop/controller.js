// initialize an angular app with the name fruitApp
// load dependencies here if needed
var fruitApp = angular.module('fruitApp', ['fruitServices']);

// create an anguar controller to serve the static data
fruitApp.controller('FruitLocationCtrl', function ($scope, FruitLocationService) {
    $scope.region = 'World';
    // retrieve the data from API endpoint
    $scope.fruitLocations = FruitLocationService.query();
});