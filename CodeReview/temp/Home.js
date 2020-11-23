import React from 'react';
import { Link } from 'react-router-dom';
import homestyle from './Home.css';
import Layout from './Layout';

const Home = () => {
  return (
    <Layout href="./Home.css">
      <p className="show-remain">남은 시간 :  
      <span className = "show-sec" id="remainSec"> 10</span>
      <span>sec</span></p>

      <p className="scoreTitle">점수 : 
      <span className = "showScore" id="ExamScore"> 0</span>
      <span>점</span></p>

      <p id="show-word">문제 단어</p>

      <input className="input-word" id="input_word"  type="text" placeholder="입력"/>
      <p></p>
      <input className="start-button" id="input_start" type="button" value="시작"/>
      <p>
        <Link to="/dynamic" id="linkso">Navigate to Dynamic Page</Link>
      </p>
    </Layout>
  );
};
export default Home;


let scoreNo = 0; //점수
let sec = 10; //문제별 푸는 시간
let examTotalCount = 0; //총 문제수
let examCount = 0; // 문제수 Count
let showSec = document.getElementById("remainSec");
let inputword = "";
let showword = "";
var interval
var requestURL = 'https://my-json-server.typicode.com/kakaopay-fe/resources/words';
var request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();
request.onload = function(){
	var typing = request.response;
	examTotalCount = typing.length;
}

function initValue(){	
	console.log("init");
	scoreNo = request.response.length;
	sec = 10;
	examCount = 0;
	showword = "문제 단어"
	sec = request.response[examCount].second;
	document.getElementById("input_word").value = "";
	localStorage.setItem("score", scoreNo);
}
var inputbox = document.getElementById("input_word");

function startInterval(){
	interval = setInterval(function() {
	    sec--;
	    document.getElementById("remainSec").innerHTML = sec;
	    if (sec == 0) 
	    {
			scoreNo--;
	    	if(examCount == examTotalCount-1){
				localStorage.setItem("score", scoreNo);
				displayWordInfo();
	    		clearInterval(interval);
				window.location.href = "/dynamic";
	    	}else{
	    		examCount++;
		      	clearInterval(interval);
		      	setWordInfo();
		      	displayWordInfo();
		      	startInterval();
	    	}
	    }
	  }, 100)
}
function stopInterval(){
	clearInterval(interval);
}
function displayWordInfo(){
	document.getElementById("ExamScore").innerHTML = scoreNo;
	document.getElementById("show-word").innerHTML = showword;
	document.getElementById("remainSec").innerHTML = sec;
}
function setWordInfo(){
	showword = request.response[examCount].text
	sec = request.response[examCount].second;
}

window.onload = function(){
	let inputbox = document.getElementById("input_word");
	let startButton = document.getElementById("input_start");
	let linkso = document.getElementById("linkso");
	startButton.onclick = function(){
		if(startButton.value == "시작"){
			startButton.value = "초기화";
			initValue();
			setWordInfo();
			displayWordInfo();
			startInterval();
		}else{
			startButton.value = "시작"
			initValue();
			displayWordInfo();
			stopInterval();
		}
	}
	inputbox.onkeyup = function(event){
		if(event.key === "Enter")
		{
			if(inputbox.value == showword)
			{
				if(examCount < examTotalCount)
				{
					examCount++;
					stopInterval();
					setWordInfo();
					displayWordInfo();
					startInterval();
				}
			}
			inputbox.value = "";
		}
	}
	linkso.onclick = function(){
		console.log("abc");
	}
}
