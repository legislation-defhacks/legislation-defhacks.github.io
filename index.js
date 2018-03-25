//javascript file with functions 

(function (){

	var key = ""
	"use strict";

	/*Sets up event listeners for button pressing and sets up the puzzle pieces and the background.
	selector for the page. */
	window.onload = function() {
		addStatesToDropDown(); 
		//document.getElementById("searchbystate").onclick = findRepresentatives; 
	};

	//setting up our ajax request to get data. 
	//takes in the url that we are requesting and the 
	//onload function that is used once the data is loaded. 
	function ajaxRequest(url, onloadFunction) {
		var ajax = new XMLHttpRequest(); 
		ajax.onload = onloadFunction; 
		ajax.open("GET", url, true);
		ajax.setRequestHeader("X-API-Key", "FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9");
		ajax.send(); 
	}


	//could do a boolean for house of representatives or not. 
	function searchByState() {
		var stateSelector = document.getElementById("state-selector");
		var selectedState = stateSelector.options[stateSelector.selectedIndex].value;
		var senateUrl = "https://api.propublica.org/congress/v1/members/" + "senate" + "/" + selectedState + "/current.json";
		var representativeUrl = "https://api.propublica.org/congress/v1/members/" + "house/" + selectedState + "/1/current.json";

	}

	//adds the state lables to the dropdown with each of the choices. 
	function addStatesToDropDown() {
		d3.json("state-arr.json", function(data) {
			var stateSelector = 
  					document.getElementById("state-selector");
  			data.forEach(function(d) {
  				var newOption = document.createElement("option");
  				newOption.label = d.abbreviation;
  				newOption.innerHTML = d.name + "(" + d.abbreviation + ")";
  				stateSelector.appendChild(newOption);
  			});
		});
	} 

})();