var app = angular.module("calendar", []);

app.controller("calendarWidget", function($scope) { 

});

app.directive("calendar", function() {

    return {

        restrict: "E",

        templateUrl: "templates/calendar.html",

        scope: {

            selected: "="
        },

        link: function(scope) {         

        }

    }
});
