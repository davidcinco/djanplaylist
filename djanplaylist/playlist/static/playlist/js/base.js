const menuBtn = document.getElementById("menu-mobile");

menuBtn.addEventListener("click", () => {
    if(document.getElementById("nav-mobile").style.display == "none"){
        document.getElementById("nav-mobile").style.display = "block";
    } else{
        document.getElementById("nav-mobile").style.display = "none";
    }
    
})
