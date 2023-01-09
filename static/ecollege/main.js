
document.addEventListener('DOMContentLoaded', function() {
  



  const innerWitdh = window.innerWidth;
  console.log(innerWitdh);
  
   
   if(innerWitdh >= 1200 ) {
    passed1200();
   }

  window.addEventListener("resize",  () => passed1200());

});

function passed1200(){

  const subjectSidebar = document.querySelector(".contents");
  const dropdown_btn = document.querySelector("#dropdownMenuButton1"); 
  const contents_ul = document.querySelector("#modules"); 

  if(window.innerWidth >= 1199){
    contents_ul.removeAttribute("class");
    dropdown_btn.removeAttribute("data-bs-toggle");
    dropdown_btn.removeAttribute("class");     
  } else {
    contents_ul.setAttribute("class", "dropdown-menu");
    dropdown_btn.setAttribute("data-bs-toggle", "dropdown");
    dropdown_btn.setAttribute("class", "dropdown-toggle p-2")
  }
  
}




