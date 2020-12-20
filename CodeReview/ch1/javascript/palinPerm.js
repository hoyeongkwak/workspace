var palinPerm = function(string){
	var chars = {};
	var currChar;
	var mulligan = false;
	var isPerm = true;
	string.split('').forEach((char) => {
		if(char !== ' '){
			currChar = char.toLowerCase();
			if(chars[currChar] === undefined){
				char[currChar] = 0;
			}
			chars[currChar]++;
		}
	});
	Object.keys(chars).forEach((char) => {
		if(chars[char] % 2 > 0){
			if(mulligan){
				isPerm = false;
			}else{
				mulligan = true;
			}
		}
	});
	return isPerm;
};

console.log(palinPerm('Tact Coa'), 'true');
console.log(palinPerm('Tact boa'), 'false');

