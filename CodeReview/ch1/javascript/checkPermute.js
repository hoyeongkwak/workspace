var checkPermute = function(stringOne, stringTwo){
	if(stringOne.length != stringTwo.length){
		return false;
	}else{
		var sortStringOne = stringOne.split('').sort().join('');
		var sortStringTwo = stringTwo.split('').sort().join('');
		return sortedStringOne === soertedStringTwo;
	}
};

console.log(checkPermute('aba', 'aab'), true);
console.log(checkPermute('aba', 'aaba'), false);
console.log(checkPermute('aba', 'aa'), false);