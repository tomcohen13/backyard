var root = document.querySelector(':root');
const theme = document.querySelector("#theme");
const Bg1 = document.querySelector(".bg-1");
const Bg2 = document.querySelector(".bg-2");
const Bg3 = document.querySelector(".bg-3");
// const logo1 = document.getElementById("#logo1")
// console.log(logo1)
// const logo2 = document.getElementById("logo2")
const date =  new Date()
let hour = date.getHours()

// theme background values
let lightColorLightness;
let whiteColorLightness;
let darkColorLightness;

const changeBG = () => {
    root.style.setProperty('--light-color-lightness', lightColorLightness)
    root.style.setProperty('--white-color-lightness', whiteColorLightness)
    root.style.setProperty('--dark-color-lightness', darkColorLightness)
};


window.setTimeout(function(){ // Set interval for checking
    var date = new Date(); // Create a Date object to find out what time it is
    // console.log(date.getHours())
    if((date.getHours() >= 21 | date.getHours() < 7) && darkColorLightness != '92%'){ // Check the time
        // console.log('night time')
        darkColorLightness = '92%';
        whiteColorLightness = '10%';
        lightColorLightness = '0%';
    
        changeBG();
    }
}, 100);