function check() {
    var score = 0;
    var q1 = document.test.ques1.value;
    var q2 = document.test.ques2.value;
    var q3 = document.test.ques3.value;
    var q4 = document.test.ques4.value;
    var q5 = document.test.ques5.value;
    var q6 = document.test.ques6.value;
    var q7 = document.test.ques7.value;
    var q8 = document.test.ques8.value;
    var q9 = document.test.ques9.value;
    var q10 = document.test.ques10.value;
    var result = document.getElementById('result');
    var test = document.getElementById("test");
    if (q1 == "llamo") { score += 10 }
    if (q2 == "azul") { score += 10 }
    if (q3 == "Hola") { score += 10 }
    if (q4 == "gusta") { score += 10 }
    if (q5 == "usted") { score += 10 }
    if (q6 == "Me") { score += 10 }
    if (q7 == "once") { score += 10 }
    if (q8 == "la cabeza") { score += 10 }
    if (q9 == "todo") { score += 10 }
    if (q10 == "nuevo") { score += 10 }
    test.style.display = "none";

    

    if (score <= 10) {
        result.textContent = `Your score is ${score}. The recommended level for you is A1.`
    } else if (10<score<=20) {
        result.textContent = `Your score is ${score}. The recommended level for you is A2.`
    } else if (20 <= score < 40){
        result.textContent = `Your score is ${score}. The recommended level for you is B1.`
    } else if (40 <= score < 60){
        result.textContent = `Your score is ${score}. The recommended level for you is B2.`
    } else if (60 <= score < 80){
        result.textContent = `Your score is ${score}. The recommended level for you is C1.`
    } else {
        result.textContent = `Your score is ${score}. The recommended level for you is C2.`
  }
}