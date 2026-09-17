(()=>{
  const install=()=>{
    if(document.querySelector('style[data-faq-fix]'))return;
    const style=document.createElement('style');
    style.dataset.faqFix='1';
    style.textContent=`
.faq-list .faq-answer,
.faq-list .faq-item p,
.faq-list [data-faq-answer]{display:none !important;overflow:hidden !important;}
.faq-list .faq-item.active .faq-answer,
.faq-list .faq-item.active p,
.faq-list .faq-item.open p,
.faq-list .faq-item.open .faq-answer{display:block !important;overflow:visible !important;}
.faq-list .faq-item{display:block !important;height:auto !important;max-height:none !important;box-sizing:border-box;}
.faq-list .faq-item .faq-question{display:block;position:relative;width:100%;box-sizing:border-box;padding-inline-end:48px;cursor:pointer;}
.faq-list .faq-item .faq-question::after{content:'+';position:absolute;inset-inline-end:18px;top:50%;transform:translateY(-50%);font-size:22px;line-height:1;}
.faq-list .faq-item.active .faq-question::after,.faq-list .faq-item.open .faq-question::after{content:'−';}
.faq-list .faq-item .faq-answer-inner{display:block;box-sizing:border-box;width:100%;padding:15px 22px 18px;line-height:1.8;overflow-wrap:anywhere;word-break:normal;}
@media(max-width:520px){.faq-list .faq-item .faq-question{padding-inline-end:44px;padding-inline-start:16px;line-height:1.7;overflow-wrap:anywhere}.faq-list .faq-item .faq-answer-inner{padding:14px 16px 17px;overflow-wrap:anywhere;word-break:normal;}}
`;
    document.head.appendChild(style);
  };
  const init=()=>{
    install();
    document.querySelectorAll('.faq-list .faq-item').forEach(item=>{
      const question=item.querySelector('.faq-question');
      if(!question||question.dataset.faqToggleBound)return;
      question.dataset.faqToggleBound='1';
      question.addEventListener('click',event=>{
        event.preventDefault();
        const wasOpen=item.classList.contains('active')||item.classList.contains('open');
        document.querySelectorAll('.faq-list .faq-item').forEach(other=>{
          other.classList.remove('active','open');
          if(other.tagName.toLowerCase()==='details')other.open=false;
        });
        if(!wasOpen){
          item.classList.add('active');
          if(item.tagName.toLowerCase()==='details')item.open=true;
        }
      });
    });
  };
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();
