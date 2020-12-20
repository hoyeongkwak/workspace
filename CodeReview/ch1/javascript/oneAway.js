var oneAway = function(string1, string2){
	var checkOneMissing = function(first, second){
		if(first.length !== second.length -1){
			return false;
		}else{
			var mulligan = false;
			var fP = 0;
			var sP = 0;
			while(fP < first.length){
				if(first[fP] !== second[sP]){
					if(mulligan){
						return false;
					}else{
						mulligan = true;
						sP++;
					}
				}else{
					fP++;
					sP++;
				}
			}
			return true;
		}
	};
	var checkOneDiff = function(first, second){
		if(first.length !== second.length){
			return false;
		}else{
			var mulligan = false;
			var fP = 0;
			var sP = 0;
			while(fP < first.length){
				if(first[fP] !== second[sP]){
					if(mulligan){
						return false;
					}else{
						mulligan = true;
					}
				}
				fP++;
				sP++;
			}
			return true;
		}
	};
	return checkOneMissing(string1, string2) || checkOneMissing(string2, string1) || checkOneDiff(string1, string2);
};

console.log(oneAway('pale', 'ple'), true);
console.log(oneAway('pales', 'pale'), true);
console.log(oneAway('pale', 'bale'), true);
console.log(oneAway('pale', 'bake'), false);		

