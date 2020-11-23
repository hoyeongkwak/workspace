import React from 'react';
import Layout from './Layout';
const DynamicPage = () => {
  return (
    <Layout href="./DynamicPage.css">
      <h2>Mission Complete!</h2>
      <p>당신의 점수는 
	  <span className = "Score" id="myscore">0</span>
      <span>점입니다.</span></p>
	  <p>단어당 평균 답변 시간은
	  <span className = "AvgTime" id="AverageTime"></span></p>
	  <input className="re-button" id="restart_button" type="button" value="다시 시작"/>
    </Layout>
  );
};
export default DynamicPage;

//let myscore = document.getElementById("restart_button");
/*
function setScore(){
	console.log(localStorage.getItem("score"));
	myscore.innerHTML = "0";
}

setScore();
*/