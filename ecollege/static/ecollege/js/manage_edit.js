
document.addEventListener('DOMContentLoaded', function() {
  



  const innerWitdh = window.innerWidth;
  const innerHeight = window.innerHeight;
  console.log(innerWitdh);

  setColclass(innerWitdh);

});

function setColclass(innerWidth){
  const id_slug = document.querySelector("#id_slug");
  const id_title = document.querySelector("#id_title");

  if(innerWidth >= 1200){
    id_slug.parentElement.setAttribute("class", "col-xl-5 p-0 ml-3");
    id_title.parentElement.setAttribute("class", "col-xl-5  p-0 m-0");
    document.querySelector("#edit_course").setAttribute("class", "container");    
  }
}
