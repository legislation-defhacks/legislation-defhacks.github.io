//javascript file with functions 

(function (){
	"use strict";

	/*Sets up event listeners for button pressing and sets up the puzzle pieces and the background.
	selector for the page. */
	window.onload = function() {
		addStatesToDropDown(); 
		//document.getElementById("searchbystate").onclick = findRepresentatives; 
	};

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
					//for(int i = 0; i < data.length; i++) {
  						
  					//}
		});
	} 

})();