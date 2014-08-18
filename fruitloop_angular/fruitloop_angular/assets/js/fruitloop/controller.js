// initialize an angular app with the name fruitApp
// load dependencies here if needed
var fruitApp = angular.module('fruitApp', []);

// create an anguar controller to serve the static data
fruitApp.controller('FruitLocationCtrl', function ($scope) {
    $scope.region = 'World';
    $scope.trees = [
        {'type': 'Cherry tree',
         'snippet': 'Somewhere in NE Portland'},
        {'type': 'Apple tree',
         'snippet': 'Somewhere in Sellwood'},
        {'type': 'Blackberry bush',
         'address': 'Somewhere in Buckman'}
    ];
});