const arrow = document.querySelector('[arrow]');
const cont = document.querySelector('[container_]');

cont.addEventListener('mouseenter',function(){
    cont.classList.remove('bg-color-4');
    cont.classList.add('bg-color-3');
});
cont.addEventListener('mouseleave',function(){
    cont.classList.remove('bg-color-3');
    cont.classList.add('bg-color-4');
});
cont.addEventListener('click', function(){
    window.location.href = '../../../Larson'
});
