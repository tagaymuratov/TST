let sideNav = document.querySelector('.sideNav');
let burger = document.querySelector('.burger');
let sideNavClose = document.querySelector('.sideNavClose');
let header_search_clean = document.querySelector('.header_search-clean');
let header_search_input = document.querySelector('.header_search-input')
let side_search_clean = document.querySelector('.side_search-clean');
let side_search_input = document.querySelector('.side_search-input')


burger.onclick = () => sideNav.style.left = 0;
sideNavClose.onclick = () => sideNav.style.left = '100%';
header_search_clean.onclick = () => {
  header_search_input.value = '';
  header_search_clean.style.visibility = 'hidden';
};
header_search_input.oninput = (event) => { 
  header_search_clean.style.visibility = (event.target.value != '') ? 'visible' : 'hidden';
};
side_search_clean.onclick = () => {
  side_search_input.value = '';
  side_search_clean.style.visibility = 'hidden';
};
side_search_input.oninput = (event) => {
  side_search_clean.style.visibility = (event.target.value != '') ? 'visible' : 'hidden';
};