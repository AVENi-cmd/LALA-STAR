(()=>{
const KEY='pref_lang';
const numbers={
  foodDammam:'966546273827',foodAhsa1:'966500517660',foodAhsa2:'966533511159',sweets:'966558423342',
  plasticDammam:'966550561719',plasticAhsa:'966506744437',office:'966138562508',email:'starcoldstore@yahoo.com'
};
const display={foodDammam:'054 627 3827',foodAhsa1:'050 051 7660',foodAhsa2:'053 351 1159',plasticDammam:'055 056 1719',plasticAhsa:'050 674 4437',sweets:'055 842 3342',office:'013 856 2508'};
const messages={
  foodDammam:'السلام عليكم، استفسار عن مواد غذائية - فرع الدمام',
  foodAhsa:'السلام عليكم، استفسار عن مواد غذائية - فرع الأحساء',
  plasticDammam:'السلام عليكم، استفسار عن منتجات البلاستيك - فرع الدمام',
  plasticAhsa:'السلام عليكم، استفسار عن منتجات البلاستيك - فرع الأحساء',
  sweets:'السلام عليكم، استفسار عن قطاع الحلويات والسناكات - فرع الأحساء'
};
const labels={
  ar:{food:'المواد الغذائية بالجملة',plastic:'المنتجات البلاستيكية والتعبئة والتغليف',sweets:'الحلويات والسناكات (الأحساء)',dammam:'الدمام',ahsa:'الأحساء',foodSales:'مبيعات المواد الغذائية',plasticSales:'مبيعات المنتجات البلاستيكية',office:'الإدارة المركزية',call:'اتصال',wa:'واتساب',map:'فتح الخريطة',inquiry:'استفسار',contact:'تواصل معنا',channels:'قنوات المبيعات والتواصل',email:'البريد الإلكتروني'},
  en:{food:'Wholesale Food Products',plastic:'Plastic Products & Packaging',sweets:'Sweets & Snacks (Al-Ahsa)',dammam:'Dammam',ahsa:'Al-Ahsa',foodSales:'Food Sales',plasticSales:'Plastic Products Sales',office:'Central Administration',call:'Call',wa:'WhatsApp',map:'Open Map',inquiry:'Inquiry',contact:'Contact Us',channels:'Sales & Contact Channels',email:'Email'}
};
const dictionary={
'تخطي إلى المحتوى الرئيسي':'Skip to main content','من نحن':'About Us','أنشطتنا':'Our Businesses','فروعنا':'Branches','تواصل معنا':'Contact Us',
'شركة لألأة النجوم التجارية · المملكة العربية السعودية':'LALA STAR TRADING CO. · Saudi Arabia','تجارة المواد الغذائية بالجملة منذ 1993':'Wholesale Food Products Since 1993',
'من الدمام إلى الأحساء، مسيرة تجارية بدأت عام 1993 وتوسعت مع الوقت في أنشطة البلاستيك والحلويات والوجبات الخفيفة.':'From Dammam to Al-Ahsa, a trading journey that began in 1993 and expanded into plastics, sweets, and snacks.',
'اكتشف قصتنا ←':'Discover Our Story →','عام التأسيس في الدمام':'Founded in Dammam','افتتاح فرع الأحساء':'Al-Ahsa Branch Opened','مواقع رئيسية للمواد الغذائية':'Main Food Locations',
'شركة لها مسار واضح':'A Clear Business Journey','تأسست شركة لألأة النجوم التجارية في الدمام عام 1993 في مجال بيع المواد الغذائية بالجملة، ثم توسعت أعمالها لتشمل أنشطة تجارية أخرى تحت مظلة الشركة.':'LALA STAR TRADING CO. was established in Dammam in 1993 as a wholesale food business, then expanded into additional commercial activities under the company.',
'تجارة وتوزيع بالجملة':'Wholesale Trade & Distribution','من الدمام بدأت الرحلة':'The Journey Began in Dammam','بداية الشركة — الدمام':'Company Founded — Dammam','بعد التوسع':'After Expansion','أنشطة البلاستيك والحلويات':'Plastics, Sweets & Snacks Activities','افتتاح فرع الأحساء واستمرار التوسع في الأنشطة التجارية.':'The Al-Ahsa branch opened and the company continued expanding its commercial activities.',
'المواد الغذائية بالجملة':'Wholesale Food Products','النشاط الرئيسي للشركة.':'The company’s core activity.','الدمام · الأحساء':'Dammam · Al-Ahsa','المنتجات البلاستيكية':'Plastic Products','منتجات البلاستيك والأدوات المنزلية.':'Plastic products and household supplies.',
'الحلويات والسناكات':'Sweets & Snacks','حلويات ووجبات خفيفة.':'Sweets and snack products.','الأحساء فقط':'Al-Ahsa Only','فروعنا ومواقعنا':'Our Branches & Locations','المواد الغذائية متوفرة في الدمام والأحساء، بينما الحلويات والوجبات الخفيفة في الأحساء فقط.':'Food products are available in Dammam and Al-Ahsa, while sweets and snacks are available in Al-Ahsa only.',
'الفرع الرئيسي — الدمام':'Main Branch — Dammam','المواد الغذائية — الدمام':'Food Products — Dammam','الفرع الرئيسي للشركة منذ 1993.':'The company’s main branch since 1993.','فرع المواد الغذائية — الأحساء':'Food Products Branch — Al-Ahsa','المواد الغذائية — الأحساء':'Food Products — Al-Ahsa','فرع الأحساء الذي افتتح عام 2018.':'The Al-Ahsa branch opened in 2018.',
'فتح الموقع على الخرائط ↗':'Open Location in Maps ↗','تواصل مع شركة لألأة النجوم التجارية':'Contact LALA STAR TRADING CO.','للاستفسارات والتواصل التجاري، يمكنكم التواصل معنا عبر الهاتف أو البريد الإلكتروني.':'For inquiries and business communication, contact us by phone or email.',
'الهاتف':'Phone','البريد الإلكتروني':'Email','طلب تسعيرة للجملة':'Wholesale Quote Request','الدمام':'Dammam','الأحساء':'Al-Ahsa',
'مزايا التوريد والتعامل معنا':'Supply & Business Benefits','أسعار جملة تنافسية':'Competitive Wholesale Pricing','أسطول توزيع يغطي الشرقية':'Distribution Fleet Covering the Eastern Region','سلامة التخزين وجودة الأصناف':'Safe Storage & Product Quality','خبرة تجارية راسخة منذ 1993':'Established Commercial Experience Since 1993',
'قطاعات العملاء':'Our Target Clients','متاجر التجزئة والتموينات':'Retail Stores & Groceries','المطاعم والمطابخ المركزية':'Restaurants & Central Kitchens','شركات الإعاشة':'Catering Companies','منافذ بيع البلاستيك ومواد التغليف':'Plastic & Packaging Outlets',
'الأسئلة الشائعة':'Frequently Asked Questions','شركة لألأة النجوم التجارية':'LALA STAR TRADING CO.','مستودع تجاري للسلع والمواد بالجملة':'Commercial warehouse for wholesale goods and products','المواد الغذائية — FOOD PRODUCTS':'Wholesale Food Products — FOOD PRODUCTS','المنتجات البلاستيكية — PLASTIC PRODUCTS':'Plastic Products — PLASTIC PRODUCTS','الحلويات والسناكات — SWEETS & SNACKS':'Sweets & Snacks — SWEETS & SNACKS'
};
const meta={ar:{title:'شركة لألأة النجوم التجارية | LALA STAR TRADING CO.',description:'شركة لألأة النجوم التجارية — تجارة المواد الغذائية بالجملة منذ 1993.'},en:{title:'LALA STAR TRADING CO. | Wholesale Food Products Since 1993',description:'LALA STAR TRADING CO. — wholesale food products since 1993, with plastics, sweets, and snacks activities in Dammam and Al-Ahsa.'}};
const wholesaleData={ar:{title:'حجم التوريد والخدمة التجارية',kicker:'WHOLESALE SUPPLY',stats:[['+5,000','صنف غذائي ومستلزم تجاري نشط'],['+30','عاماً من الخبرة منذ 1993'],['فرعان','مستودعات مركزية في الدمام والأحساء'],['توريد فوري','للطبالي والكراتين للمتاجر والمطاعم']]},en:{title:'Wholesale Supply Scale & Service',kicker:'WHOLESALE SUPPLY',stats:[['+5,000','active food & commercial items'],['+30','years of experience since 1993'],['2','central warehouse branches in Dammam & Al-Ahsa'],['Immediate Supply','pallet and carton orders for stores & restaurants']]}};
const current=localStorage.getItem(KEY)==='en'?'en':'ar';
const wa=(n,text)=>`https://wa.me/${n}?text=${encodeURIComponent(text)}`;
const tel=n=>`tel:+${n}`;
const num=(value)=>`<span class="contact-number" dir="ltr" style="unicode-bidi:isolate;">${value}</span>`;
function injectStyle(){
 if(document.querySelector('style[data-contact-theme]'))return;
 const s=document.createElement('style');s.dataset.contactTheme='1';
 s.textContent=`
.contact-channels{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:24px}
.contact-channel{background:rgba(255,255,255,.88);border:1px solid #dbe3ec;border-radius:18px;padding:20px;box-shadow:0 10px 25px -12px rgba(15,30,54,.16)}
.contact-channel h4{margin:0 0 12px;color:#1e293b;font-size:17px}
.contact-row{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;padding:12px 0;border-top:1px solid #eef2f6;font-size:14px}
.contact-row:first-of-type{border-top:0}.contact-label{color:#64748b;font-weight:600;margin-bottom:3px}
.contact-number{font-family:Inter,Arial,sans-serif;direction:ltr;unicode-bidi:isolate;color:#1e293b;font-weight:800;white-space:nowrap}
.contact-actions{display:flex;gap:8px;flex-wrap:wrap;align-items:center;flex:0 0 auto}
.contact-action{display:inline-flex;align-items:center;justify-content:center;min-height:34px;padding:6px 10px;border-radius:9px;font-size:12px;font-weight:800;border:1px solid #dbe3ec;background:#fff;color:#1e293b;white-space:nowrap}
.contact-action.whatsapp{background:#16a34a;border-color:#16a34a;color:#fff}.contact-action.call{color:#15803d}
.sweets-inquiry{display:flex;margin-top:14px}.sweets-inquiry .contact-action{width:100%;min-height:42px;text-align:center}.sweets-inquiry .contact-action.whatsapp{justify-content:center}
.activity-contacts{display:grid;gap:8px;margin-top:14px}.activity-contact{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px;border-radius:11px;background:#f8fafc;border:1px solid #e8edf3}
.activity-contact-main{min-width:0}.activity-contact strong{display:block;font-size:12px;color:#1e293b}.activity-contact-number{display:block;margin-top:2px;font-family:Inter,Arial,sans-serif;font-size:12px;font-weight:800;direction:ltr;unicode-bidi:isolate;color:#475569;white-space:nowrap}
.floating-whatsapp{position:fixed;inset-inline-end:20px;bottom:20px;z-index:1000}.floating-whatsapp-toggle{width:58px;height:58px;border:0;border-radius:50%;display:grid;place-items:center;background:#16a34a;color:#fff;box-shadow:0 12px 28px rgba(22,163,74,.3);cursor:pointer}
.floating-whatsapp-toggle svg{width:28px;height:28px;fill:currentColor}.floating-whatsapp-menu{position:absolute;inset-inline-end:0;bottom:68px;width:min(340px,calc(100vw - 32px));padding:10px;border:1px solid #dbe3ec;border-radius:18px;background:rgba(255,255,255,.97);backdrop-filter:blur(16px);box-shadow:0 18px 45px rgba(15,30,54,.18);opacity:0;visibility:hidden;transform:translateY(8px);transition:.2s ease}
.floating-whatsapp.open .floating-whatsapp-menu{opacity:1;visibility:visible;transform:none}.floating-whatsapp-menu h4{margin:4px 6px 9px;color:#1e293b;font-size:14px}
.wa-option{display:flex;align-items:center;gap:10px;width:100%;padding:11px 10px;border:0;border-radius:12px;background:transparent;color:#1e293b;text-align:start;cursor:pointer}.wa-option:hover{background:#f0fdf4}.wa-dot{width:10px;height:10px;flex:0 0 10px;border-radius:50%;background:#16a34a}.wa-option small{display:block;color:#64748b;margin-top:2px;font-family:Inter,Arial,sans-serif;direction:ltr;unicode-bidi:isolate;text-align:start;white-space:nowrap}
@media(max-width:850px){.contact-channels{grid-template-columns:1fr}.activity-contact{align-items:flex-start}.contact-row{flex-direction:column}.contact-actions{width:100%}.contact-action{flex:0 0 auto}.sweets-inquiry .contact-action{width:100%}.floating-whatsapp{inset-inline-end:14px;bottom:14px}.floating-whatsapp-toggle{width:54px;height:54px}}
@media(max-width:520px){.activity-contact{display:block}.activity-contact .contact-actions{margin-top:7px}.contact-actions{gap:8px}.sweets-inquiry{margin-top:12px}}
`;
 document.head.appendChild(s)
}
function action(n,text){return `<span class="contact-actions"><a class="contact-action call" href="${tel(n)}">${labels[current].call}</a><a class="contact-action whatsapp" href="${wa(n,text)}" target="_blank" rel="noopener noreferrer">${labels[current].wa}</a></span>`}
function contactRow(label,n,message){return `<div class="contact-row"><div><div class="contact-label">${label}</div>${num(display[n]||n)}</div>${action(numbers[n]||n,message)}</div>`}
function contactCard(title,rows){const d=document.createElement('div');d.className='contact-channel';d.innerHTML=`<h4>${title}</h4>`+rows.join('');return d}
function activityBlock(rows){const d=document.createElement('div');d.className='activity-contacts';d.innerHTML=rows.map(r=>`<div class="activity-contact"><div class="activity-contact-main"><strong>${r.label}</strong><span class="activity-contact-number" dir="ltr" style="unicode-bidi:isolate;">${display[r.key]}</span></div>${action(numbers[r.key],r.message)}</div>`).join('');return d}
function sweetsInquiry(){const d=document.createElement('div');d.className='sweets-inquiry';d.innerHTML=`<a class="contact-action whatsapp" href="${wa(numbers.foodAhsa1,messages.sweets)}" target="_blank" rel="noopener noreferrer">${current==='ar'?'استفسار عن توفر الحلويات بالجملة':'Ask about wholesale sweets availability'}</a>`;return d}
function injectContacts(){
 injectStyle();
 const businesses=document.querySelector('#businesses,.businesses');
 if(businesses){
   businesses.querySelectorAll('.activity-contacts,.sweets-inquiry').forEach(x=>x.remove());
   const cards=[...businesses.querySelectorAll('.business')];
   const food=cards.find(x=>/المواد الغذائية|Wholesale Food/i.test(x.textContent));
   const plastic=cards.find(x=>/البلاستيك|Plastic/i.test(x.textContent));
   const sweets=cards.find(x=>/الحلويات|Sweets/i.test(x.textContent));
   if(food)food.querySelector('.business-body')?.appendChild(activityBlock([
     {label:`${labels[current].foodSales} — ${labels[current].dammam}`,key:'foodDammam',message:messages.foodDammam},
     {label:`${labels[current].foodSales} — ${labels[current].ahsa}`,key:'foodAhsa1',message:messages.foodAhsa}
   ]));
   if(plastic)plastic.querySelector('.business-body')?.appendChild(activityBlock([
     {label:`${labels[current].plasticSales} — ${labels[current].dammam}`,key:'plasticDammam',message:messages.plasticDammam},
     {label:`${labels[current].plasticSales} — ${labels[current].ahsa}`,key:'plasticAhsa',message:messages.plasticAhsa}
   ]));
   if(sweets)sweets.querySelector('.business-body')?.appendChild(sweetsInquiry());
 }
 const branches=document.querySelector('#branches,.branches');
 if(branches){
   branches.querySelectorAll('.activity-contacts').forEach(x=>x.remove());
   [...branches.querySelectorAll('.branch')].forEach(card=>{
     const ahsa=/الأحساء|Al-Ahsa/i.test(card.textContent);const body=card.querySelector('.branch-body');if(!body)return;
     const rows=ahsa?[
       {label:'مبيعات المواد الغذائية — خط 1',key:'foodAhsa1',message:messages.foodAhsa},
       {label:'مبيعات المواد الغذائية — خط 2',key:'foodAhsa2',message:messages.foodAhsa},
       {label:'مبيعات المنتجات البلاستيكية',key:'plasticAhsa',message:messages.plasticAhsa}
     ]:[
       {label:'مبيعات المواد الغذائية',key:'foodDammam',message:messages.foodDammam},
       {label:'مبيعات المنتجات البلاستيكية',key:'plasticDammam',message:messages.plasticDammam}
     ];
     body.querySelectorAll('.map').forEach(x=>{x.style.marginTop='8px'});
     body.appendChild(activityBlock(rows));
   });
 }
 const contact=document.querySelector('#contact,.contact');
 if(contact){
   contact.querySelectorAll('.contact-channels').forEach(x=>x.remove());
   const container=contact.querySelector('.container')||contact;
   container.querySelector('.cards')?.remove();
   const wrap=document.createElement('div');wrap.className='contact-channels';
   wrap.appendChild(contactCard('قسم مبيعات الدمام',[
     contactRow('المواد الغذائية','foodDammam',messages.foodDammam),
     contactRow('المنتجات البلاستيكية','plasticDammam',messages.plasticDammam)
   ]));
   wrap.appendChild(contactCard('قسم مبيعات الأحساء',[
     contactRow('المواد الغذائية — خط 1','foodAhsa1',messages.foodAhsa),
     contactRow('المواد الغذائية — خط 2','foodAhsa2',messages.foodAhsa),
     contactRow('المنتجات البلاستيكية','plasticAhsa',messages.plasticAhsa)
   ]));
   wrap.appendChild(contactCard(labels[current].office,[contactRow(labels[current].office,'office','')]));
 }
}
function injectWholesale(){const anchor=document.querySelector('#branches,.branches,.contact');if(!anchor||document.querySelector('[data-wholesale-injected]'))return;const section=document.createElement('section');section.className='section alt';section.dataset.wholesaleInjected='1';section.innerHTML=`<div class="container"><div class="head"><div><div class="kicker">${wholesaleData[current].kicker}</div><h2>${wholesaleData[current].title}</h2></div><p>${current==='ar'?'توريد بالجملة للمتاجر والمطاعم والمنشآت التجارية في المنطقة الشرقية.':'Wholesale supply for stores, restaurants, and commercial establishments in the Eastern Region.'}</p></div><div class="stats-grid">${wholesaleData[current].stats.map(s=>`<div class="stat"><strong>${s[0]}</strong><small>${s[1]}</small></div>`).join('')}</div></div></section>`;anchor.parentNode.insertBefore(section,anchor)}
function translate(){document.documentElement.lang=current;document.documentElement.dir=current==='ar'?'rtl':'ltr';document.title=meta[current].title;const desc=document.querySelector('meta[name="description"]');if(desc)desc.content=meta[current].description;document.querySelectorAll('[data-ar][data-en]').forEach(el=>{el.textContent=current==='ar'?el.dataset.ar:el.dataset.en});const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);while(walker.nextNode()){const t=walker.currentNode.textContent.trim();if(dictionary[t])walker.currentNode.textContent=dictionary[t]}}
function floating(){document.querySelectorAll('.floating-whatsapp').forEach(x=>x.remove());const root=document.createElement('div');root.className='floating-whatsapp';const option=(key,label,message)=>`<a class="wa-option" target="_blank" rel="noopener noreferrer" href="${wa(numbers[key],message)}"><span class="wa-dot"></span><span>${label}<small dir="ltr" style="unicode-bidi:isolate;">${display[key]}</small></span></a>`;root.innerHTML=`<button class="floating-whatsapp-toggle" type="button" aria-label="WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 3.5A11.8 11.8 0 0 0 12.1 0C5.6 0 .3 5.3.3 11.8c0 2.1.6 4.1 1.6 5.9L.2 24l6.5-1.7c1.8.9 3.5 1.3 5.4 1.3h.1c6.5 0 11.8-5.3 11.8-11.8 0-3.1-1.3-6.1-3.5-8.3ZM12.2 21.6h-.1c-1.7 0-3.4-.5-4.8-1.3l-.3-.2-3.9 1 1-3.8-.2-.3a9.8 9.8 0 1 1 8.3 4.6Zm5.4-7.3c-.3-.2-1.8-.9-2.1-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-1.9-.9-3.1-1.6-4.3-3.6-.3-.5.3-.5.8-1.7.1-.3 0-.5-.1-.7-.1-.2-.7-1.7-1-1-.3-.5-.5-.4-.7-.4h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.6s1.1 3 1.3 3.2c.2.2 2.2 3.4 5.3 4.8 2 .9 2.8 1 3.8.9.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.6-.4Z"/></svg></button><div class="floating-whatsapp-menu"><h4>${labels[current].channels}</h4>${option('foodDammam',`${labels[current].foodSales} — ${labels[current].dammam}`,messages.foodDammam)}${option('foodAhsa1',`${labels[current].foodSales} — ${labels[current].ahsa}`,messages.foodAhsa)}${option('plasticDammam',`${labels[current].plasticSales} — ${labels[current].dammam}`,messages.plasticDammam)}${option('plasticAhsa',`${labels[current].plasticSales} — ${labels[current].ahsa}`,messages.plasticAhsa)}${option('sweets',current==='ar'?'مبيعات الحلويات والمقرمشات — الأحساء':'Sweets & Snacks Sales — Al-Ahsa',messages.sweets)}</div>`;document.body.appendChild(root);root.querySelector('button').addEventListener('click',()=>root.classList.toggle('open'));document.addEventListener('click',e=>{if(!root.contains(e.target))root.classList.remove('open')})}
function secure(){document.querySelectorAll('a[href^="https://wa.me/"],a[href^="https://www.google.com/maps/"]').forEach(a=>{a.target='_blank';a.rel='noopener noreferrer'});document.querySelectorAll('a[href^="tel:"]').forEach(a=>{if(!a.dataset.salesChannel)a.dataset.salesChannel='1'});document.querySelectorAll('.contact-number,.activity-contact-number,.wa-option small').forEach(el=>{el.setAttribute('dir','ltr');el.style.unicodeBidi='isolate'})}
function init(){translate();injectWholesale();injectContacts();floating();secure()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();