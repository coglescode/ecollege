
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

function openDrawer(courseId) {
            const course = courses.find(c => c.id === courseId);
            if (!course) return;

            // Mapping target field data structures
            const sub = subjects.find(s => s.id === course.subject) || { name: course.subject };
            document.getElementById('drawer-subject-badge').innerText = sub.name;
            document.getElementById('drawer-image').src = course.image;
            document.getElementById('drawer-title').innerText = course.title;
            document.getElementById('drawer-instructor').innerText = "Lead Instructor: " + course.instructor;
            document.getElementById('drawer-rating').innerText = "★ " + course.rating;
            document.getElementById('drawer-students').innerText = course.students + " students";
            document.getElementById('drawer-desc').innerText = course.description;
            document.getElementById('drawer-overview').innerText = course.overview;

            // Render detailed curriculums inside course overview
            const container = document.getElementById('drawer-modules');
            if (course.modules && course.modules.length > 0) {
                container.innerHTML = course.modules.map((m, index) => `
                    <div class="p-4 bg-slate-50 border border-slate-150 rounded-xl">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-indigo-600 block mb-1">Step 0${index + 1}</span>
                        <h4 class="font-bold text-slate-800 text-sm mb-1">${m.title}</h4>
                        <p class="text-xs text-slate-500 leading-relaxed">${m.desc}</p>
                    </div>
                `).join('');
            } else {
                container.innerHTML = `<p class="text-xs text-slate-400">Curriculum structure is currently updated by the registrar office.</p>`;
            }

            // Remove hidden status and animate in
            const drawer = document.getElementById('course-drawer');
            drawer.classList.remove('hidden');
            setTimeout(() => {
                document.getElementById('drawer-overlay').classList.remove('opacity-0');
                document.getElementById('drawer-content').classList.remove('translate-x-full');
            }, 50);

            // Stop scroll leaking on layout underneath
            document.body.classList.add('overflow-hidden');
        }

        function closeDrawer() {
            document.getElementById('drawer-overlay').classList.add('opacity-0');
            document.getElementById('drawer-content').classList.add('translate-x-full');

            setTimeout(() => {
                document.getElementById('course-drawer').classList.add('hidden');
                document.body.classList.remove('overflow-hidden');
            }, 300);
        }



