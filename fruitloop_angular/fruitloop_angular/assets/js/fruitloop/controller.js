// initialize an angular app with the name fruitApp
// load dependencies here if needed
var fruitApp = angular.module('fruitApp', ['leaflet-directive', 'fruitServices']);

// create an anguar controller to serve the static data
fruitApp.controller('FruitLocationCtrl', function ($scope, leafletData, FruitLocationService) {

    // set variables
    $scope.markers = new Array();
    var bbox = new Array();

    // retrieve the data from API endpoint with initial load
    FruitLocationService.query().$promise.then(
      function (response) {
        // copy the data to the $scope for the table to show
        $scope.fruitLocations = response;
        // loop through the data set and set the markers on the map
        $scope.fruitLocations.forEach(function(fruitLocation){
          $scope.markers.push({
            // convert from str to float
            lat: parseFloat(fruitLocation.latitude),
            lng: parseFloat(fruitLocation.longitude)
          });
          // get the coordinates of the markers to determine the max bounds
          bbox.push([
            parseFloat(fruitLocation.latitude),
            parseFloat(fruitLocation.longitude)
          ]);
        });
        // get the map element
        leafletData.getMap().then(function(map) {
          // change the map to fit all markers
          map.fitBounds(bbox);
        });
      }
    );

    // $scope.fruitLocations will be undefined because the API request is async
    console.log($scope.fruitLocations);

    // inital values for the leaflet map, they will be overwritten once
    // $promise returns the data
    $scope.center = {lat: 45.50, lng: -122.5, zoom: 10};

    // default settings for the leaflet map
    $scope.defaults = {scrollWheelZoom: false};
});
