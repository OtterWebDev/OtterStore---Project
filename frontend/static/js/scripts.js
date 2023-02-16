//copy menu for mobile
function copyMenu (){
    
    // copy inside nav to nav

    var mainNav = document.querySelector('.header-nav nav');
    var navPlace = document.querySelector('.off-canvas nav');
    navPlace.innerHTML = mainNav.innerHTML;

    //copy .header-top .wrapper to .thetop-nav
    var topNav = document.querySelector('.header-top .wrapper');
    var topPlace = document.querySelector('.off-canvas .thetop-nav');
    topPlace.innerHTML = topNav.innerHTML;
}
copyMenu(); 
 
// show mobile menu 

const menuButton = document.querySelector('.trigger'),
    closeButton = document.querySelector('.t-close'),
    addclass = document.querySelector('.site');

menuButton.addEventListener('click',function
(){
    addclass.classList.toggle('showmenu')
})
closeButton.addEventListener('click',function(){
    addclass.classList.remove('showmenu')
})

// show sub menu on mobile 

const submenu = document.querySelectorAll('.has-child .icon-small');
submenu.forEach((menu) => menu.addEventListener('click', toggle));

function toggle(e) {
    e.preventDefault();
    submenu.forEach((item) => item != this ? item.closest('.has-child') .classList.remove('expand') :null);
    if (this.closest('.has-child').classList != 'expand');
    this.closest('.has-child').classList.toggle('expand');
}



// Slider

const swiper = new Swiper('.swiper', {
    // Optional parameters
    
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
  });

// Show Search

const searchButton = document.querySelector('.t-search'),
      tClose  = document.querySelector('.search-close'),
      showClass = document.querySelector('.site');

searchButton.addEventListener('click',function(){
    showClass.classList.toggle('showsearch')
})

tClose.addEventListener('click',function(){
    showClass.classList.remove('showsearch')
})

// Show Departments Menu

const dptButton = document.querySelector('.dpt-cat .dpt-trigger'),
      dptClass = document.querySelector('.site');
dptButton.addEventListener('click',function(){
    dptClass.classList.toggle('showdpt')
})

// Product Image Slider

var productThumb = new Swiper ('.small-image',{
    loop: true,
    spaceBetween: 10,
    slidesPerView: 3,
    freeMode: true,
    watchSlideProgress: true,
    breakpoints: {
        481:{
            spaceBetween:32,
        }
    }
});
var productBig = new Swiper ('.big-image', {
    loop:true,
    autoHeight:true,
    navigation:{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    thumbs: {
        swiper: productThumb
    }
});

/* // filter

const FtoShow = '.filter';
const Fpopup = document.querySelector(FtoShow);
const Ftrigger = document.querySelector('.filter-trigger');

Ftrigger.addEventListener('click', () => {
        setTimeout(() => {
        if(!Fpopup.classList.contains('show')) {
            Fpopup.classList.add('show');
            }
            }, 250)
        })

// Auto close by click outside .filter 
document.addEventListener('click', (e) => {
    const isClosest = e.target.closest(FtoShow);
    if (!isClosest && Fpopup.classList.contains('show')) {
        Fpopup.classList.remove('show')
        }
})


// Show cart on click

const divtoShow = '.mini-cart';
const divPopup = document.querySelector(divtoShow);
const divTrigger = document.querySelector('.cart-trigger');

divTrigger.addEventListener('click', () =>{
    setTimeout(() => {
        if(!divPopup.classList.contains('show')){
            divPopup.classList.add('show');
        }
    },250)
})

// close by click outside

document.addEventListener('click', (e) => {
    const isClosest = e.target.closest(divtoShow);
    if (!isClosest && divPopup.classList.contains('show')){
        divPopup.classList.remove('show')
    }
})

// Show Modal on load 

window.onload = function() {
    document.querySelector('.site').classList.toggle('showmodal')
}
document.querySelector('.modalclose').addEventListener('click',function (){
    document.querySelector('.site').classList.remove('showmodal')
}) */

// Registration Form

const cButton    = document.querySelector('.btn-groupc');
const cStep      = document.querySelectorAll('.stepc');

let stepnum = 0;

cButton.addEventListener('click',(e) =>{
    if ($(e.target).hasClass("btn-next")){
        stepnum++;
        if(stepnum > cStep.length){
            stepnum = cStep.length;
        }
    }
    if ($(e.target).hasClass("btn-prev")){
        stepnum--;
    }
    updateSteps();
});

function updateSteps(){
    cStep.forEach((stepc) =>{
        stepc.classList.contains('active') && stepc.classList.remove('active');
    });
    cStep[stepnum].classList.add('active');

    if ((stepnum) === 0 ){
        $(cButton).children('.btn-prev').prop('disabled',true);   
    } else if (stepnum === cStep.length){
        $(cButton).children('.btn-next').prop('disabled',true);
    } else {
        $(cButton).children('.btn-prev').prop('disabled',false);
        $(cButton).children('.btn-next').prop('disabled',false);
    }
};

const vButton = document.querySelector('.btn-groupv');
const vStep      = document.querySelectorAll('.stepv');

let stepnum1 = 0;

vButton.addEventListener('click',(e) =>{
    if ($(e.target).hasClass("btn-next")){
        stepnum1++; 
        if(stepnum1 > vStep.length){
            stepnum1 = vStep.length;
        }      
    }
    if ($(e.target).hasClass("btn-prev")){
        stepnum1--;
    }
    updateSteps1();
});

function updateSteps1(){
    vStep.forEach((stepv) =>{
        stepv.classList.contains('active') && stepv.classList.remove('active');
    });
    vStep[stepnum1].classList.add('active');

    if ((stepnum1) === 0 ){
        $(vButton).children('.btn-prev').prop('disabled',true);   
    } else if (stepnum1 === vStep.length){
        $(vButton).children('.btn-next').prop('disabled',true);
    } else {
        $(vButton).children('.btn-prev').prop('disabled',false);
        $(vButton).children('.btn-next').prop('disabled',false);
    }
};









