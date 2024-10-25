let sideNav = document.querySelector('.sideNav');
let burger = document.querySelector('.burger');
let sideNavClose = document.querySelector('.sideNavClose');

burger.onclick = () => sideNav.style.left = 0;
sideNavClose.onclick = () => sideNav.style.left = '100%';