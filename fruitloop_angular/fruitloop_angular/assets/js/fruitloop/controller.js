// initialize an angular app with the name fruitApp
// load dependencies here if needed
var fruitApp = angular.module('fruitApp', [
  'leaflet-directive',
  'fruitServices',
  'fruitDirectives'
  ])

// create an anguar controller to serve the static data
.controller('FruitLocationCtrl', function ($scope, leafletData, FruitLocationService) {

    var addData = function(fruitLocation) {
        // add new marker to the map
        $scope.markers.push({
          // convert from str to float
          lat: parseFloat(fruitLocation.latitude),
          lng: parseFloat(fruitLocation.longitude)
        });
        // add new item to the location list
        $scope.fruitLocations.push({
          lat: parseFloat(fruitLocation.latitude),
          lng: parseFloat(fruitLocation.longitude),
          address: fruitLocation.address,
          comment: fruitLocation.comment,
          fruit_type: fruitLocation.fruit_type,
          fruit_name: fruitLocation.fruit_name
        });
    };

    var loadData = function() {
      // set variables
      $scope.markers = [];
      var bbox = [];

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
    };

    // load initial location points via the API endpoint
    loadData();
    // inital values for the leaflet map, they will be overwritten once
    // $promise returns the data
    $scope.center = {lat: 45.50, lng: -122.5, zoom: 10};

    // default settings for the leaflet map
    $scope.defaults = {scrollWheelZoom: false};

    // the function is submit the POST request to the API and
    // once the submission was successful, the point will be added to the
    // location array
    $scope.addFruit = function(fruit) {
      // submit POST request
      FruitLocationService.save(
        {
          address: fruit.address,
          fruit_type: String(fruit.type),
          comment: fruit.comment
        }).$promise.then(function(data) {
            // if successful, add the data to the location array
            addData(data);
            // reset the variable fruit to clear the form
            $scope.fruit = null;
        }, function(error) {
            // if submission was unsuccessful, print out the error
            console.log(error);
        });
    };
});
