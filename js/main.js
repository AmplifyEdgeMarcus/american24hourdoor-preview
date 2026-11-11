(function(){
  var b=document.querySelector('.menu-btn'),n=document.getElementById('mnav');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Close menu':'Open menu');});}
  var y=document.getElementById('yr'); if(y) y.textContent=new Date().getFullYear();
  // Front-end only form handling. Replace with a real backend (see comment in contact.html).
  var f=document.getElementById('service-form');
  if(f){f.addEventListener('submit',function(e){
    e.preventDefault();
    var req=f.querySelectorAll('[required]'),ok=true;
    req.forEach(function(i){var bad=!i.value.trim();i.style.borderColor=bad?'#C8102E':'';if(bad)ok=false;});
    var s=f.querySelector('.form-status');
    if(!ok){s.style.display='block';s.style.background='#FDE8EB';s.style.color='#6B0A1A';s.textContent='Please fill in your name and phone number.';return;}
    if(f.getAttribute('action').charAt(0)!=='#'){f.submit();return;}
    s.style.display='block';s.style.background='';s.style.color='';
    s.textContent='Thanks! Your request is ready to send. (Demo: the form backend is not connected yet.)';
  });}
})();
