// let a = "안녕";     // 변수
// const b = "베어유"; // 상수 : 값을 바꿀 수 없다

// a = "잘가";
// alert(a);





// function func_name() {

// }

// // 화살표 함수(Arrow Function)
// const func_const_name = ()=>{

// }

let red_btn = document.getElementById("red_btn");
let content = document.getElementById("content")
btn.addEventListener("click", () => {
    // click이라는 이벤트가 발생하면 뒤에 있는 코드가 실행됨
    content.style.backgroundColor = "red";
})