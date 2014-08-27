var fruitServices = angular.module('fruitServices', ['ngResource']);
fruitServices.factory('FruitLocationService', ['$resource',
  function($resource){
    return $resource('api\\/', {}, {
      query: {method:'GET', params:{}, isArray: true}
    });
  }
]);
