


// for change image and add it to the img-container
var img = document.getElementById('img');
var imgBtn = document.getElementById('choose-img');
var img_cont = document.querySelector('.img-cont');
let imgView;
let text_p;

imgBtn.addEventListener('click',function(){
    img.click()
})

img.addEventListener('change',(e) =>{
    var img_src = URL.createObjectURL(e.target.files[0]);
    imgView = document.createElement('img');
    imgView.setAttribute('src',img_src)

    
    img_cont.innerHTML = '';
    img_cont.appendChild(imgView)

})




// for choose and take verse and add it in the img-container
var choose_verse = document.getElementById('choose_verse');

choose_verse.addEventListener('change',(e)=>{
    if (imgView){

        if (document.querySelector('.text')){
            document.querySelector('.text').remove()
        }
        text_p = document.createElement('p');
        text_p.setAttribute('class','text')
        console.log(choose_verse)
        text_p.textContent = choose_verse.options[choose_verse.selectedIndex].text;
        img_cont.appendChild(text_p)
    }else{
        alert('اختر الصورة اولا')
    }
})




// for update the scale of the image
var img_scale_btn = document.getElementById('scale');

img_scale_btn.addEventListener('click',function(){
  
    if (imgView){

        if (img_scale_btn.value == 10){
            imgView.style.scale = 2;
        }else{

            imgView.style.scale = '1.' + img_scale_btn.value;
        }
    }
    else{
        alert('اختر الصورة اولا')
    }

})


// for update the font_size of the text font
var font_size = document.getElementById('font_size');

font_size.addEventListener('click',function(){
  
    if (text_p){
        text_p.style.fontSize = font_size.value + 'px';
    }
    else{
        alert('اختر الصورة اولا')
        font_size.value = 20;
    }

})



// update x, y of the text_p

var x = document.getElementById('x');
var y = document.getElementById('y');

let current_x = 50;
let current_y = 50;


function UpdateTextPositions (){
    text_p.style.top = current_y + '%';
    text_p.style.left = current_x + '%';
}


x.addEventListener('click',function(){
    if(text_p){
        current_x = x.value;
        UpdateTextPositions()
    }
    else{
        alert('اختر النص اولا')
    }
})


y.addEventListener('click',function(){
    if(text_p){
        current_y = y.value;
        UpdateTextPositions()
    }
    else{
        alert('اختر النص اولا')
    }
    
})