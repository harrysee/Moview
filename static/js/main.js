'use strict';
const tabmenu = document.querySelectorAll(".btn"); // 탭메뉴를 변수에 지정
const containers = document.querySelectorAll('.container');
const nextbtn = document.querySelector('.next_btn');
const logobtn = document.querySelector('.logo');

const logHidden = function(){
    var loginbox = document.querySelector('.login-box')
    console.log(loginbox)
    if(loginbox.style.display === '') loginbox.style.display = 'none'
    else loginbox.style.display = ''
}
_init()

function _init(){ // 시작 시 해야할 것들
    allhidden();
    for(var i =0; i<tabmenu.length; i++){
        tabmenu[i].addEventListener('click', event => onButtonClick(event));
    }
    nextbtn.addEventListener('click',function(){
        var startbox = document.querySelector('.start-page')
        window.scroll({
            behavior: 'smooth',
            left:0,
            top: startbox.offsetHeight
        });
    });
    logobtn.addEventListener('click', event => logHidden())
}

function allhidden(){ // 모두 숨기기
    for(var i=0; i<containers.length; i++){
        containers[i].style.display = 'none';
    }
}

function onButtonClick(e){   // 버튼 클릭 이벤트
    const dataset = e.target.dataset;
    const key = dataset.key;

    allhidden();
    containers[key].style.display = '';
}





