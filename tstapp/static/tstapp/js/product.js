let subImgs = document.querySelectorAll('.subImg');
let mainImg = document.querySelector('.mainImg');
let modal = document.querySelector('.modal');
let modalClose = document.querySelector('.modal-close');
let modalContent = document.querySelector('.modal-content');
subImgs[0].parentNode.classList.add('active');
modalContent.src = subImgs[0].nextElementSibling.src;

subImgs.forEach((elem) =>{
  elem.parentNode.onmouseenter = () => {
    mainImg.src = elem.src;
    modalContent.src = elem.nextElementSibling.src
    subImgs.forEach((elem2)=>{elem2.parentNode.classList.remove('active');});
    elem.parentNode.classList.add('active');
  }
  elem.parentNode.onclick = () => {
    mainImg.src = elem.src;
    modalContent.src = elem.nextElementSibling.src
    subImgs.forEach((elem2)=>{elem2.parentNode.classList.remove('active');});
    elem.parentNode.classList.add('active');
  }
});

mainImg.onclick = ()=>{modal.style.display = 'block';}
modalClose.onclick = ()=>{modal.style.display = 'none';}