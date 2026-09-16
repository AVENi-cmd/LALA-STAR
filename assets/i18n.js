(()=>{
  const CORE='assets/i18n-core.js';
  const pairs={
    'المواد الغذائية بالجملة':'Wholesale Food Products',
    'النشاط الأساسي للشركة.':"The company's core activity.",
    'المنتجات البلاستيكية':'Plastic Products',
    'المنتجات البلاستيكية والمستلزمات الاستهلاكية.':'Plastic products and household supplies.',
    'الحلويات والسناكات':'Sweets & Snacks',
    'أصناف الحلويات والوجبات الخفيفة.':'Sweets and snack products.',
    'فرع الأحساء فقط':'Al-Ahsa Only',
    'أسعار جملة تنافسية':'Competitive Wholesale Pricing',
    'أسطول توزيع يغطي المنطقة الشرقية':'Distribution Fleet Covering the Eastern Region',
    'تخزين آمن وجودة منتجات موثوقة':'Safe Storage & Product Quality',
    'خبرة تجارية راسخة منذ 1993':'Established Commercial Experience Since 1993'
  };
  const aliases={
    'النشاط الرئيسي للشركة.':'النشاط الأساسي للشركة.',
    'منتجات البلاستيك والأدوات المنزلية.':'المنتجات البلاستيكية والمستلزمات الاستهلاكية.',
    'حلويات ووجبات خفيفة.':'أصناف الحلويات والوجبات الخفيفة.',
    'أسطول توزيع يغطي الشرقية':'أسطول توزيع يغطي المنطقة الشرقية',
    'سلامة التخزين وجودة الأصناف':'تخزين آمن وجودة منتجات موثوقة',
    'الأحساء فقط':'فرع الأحساء فقط'
  };
  const arByEn=Object.fromEntries(Object.entries(pairs).map(([ar,en])=>[en,ar]));
  const style=()=>{
    if(document.querySelector('style[data-b2b-hero-polish]'))return;
    const s=document.createElement('style');s.dataset.b2bHeroPolish='1';s.textContent=`
.hero, #hero, .hero-section {
  background: linear-gradient(135deg, #0b1524 0%, #112238 50%, #080f1a 100%) !important;
  color: #ffffff !important;
}
.hero h1, .hero h2, .hero p, .hero span { color: #ffffff !important; }
`;document.head.appendChild(s);
  };
  const mark=()=>{
    style();
    const lang=document.documentElement.lang==='en'?'en':'ar';
    document.querySelectorAll('h3,p,span,.kicker').forEach(el=>{
      const raw=el.textContent.trim();
      let ar=el.getAttribute('data-ar')||'';
      let en=el.getAttribute('data-en')||'';
      if(aliases[raw]){ar=aliases[raw];en=pairs[ar]||en;}
      else if(!ar&&!en){
        if(pairs[raw]){ar=raw;en=pairs[raw];}
        else if(arByEn[raw]){en=raw;ar=arByEn[raw];}
        else if(raw==='FAQ'){ar='الأسئلة الشائعة';en='FAQ';}
      }
      if(!ar||!en)return;
      el.setAttribute('data-ar',ar);el.setAttribute('data-en',en);el.setAttribute('data-i18n',el.getAttribute('data-i18n')||ar);
      el.textContent=lang==='en'?en:ar;
    });
    document.querySelectorAll('a[href^="tel:"]').forEach(a=>{if(a.textContent.trim()){a.setAttribute('data-ar','اتصال');a.setAttribute('data-en','Call');a.textContent=lang==='en'?'Call':'اتصال';}});
    document.querySelectorAll('a[href*="wa.me"]').forEach(a=>{if(a.textContent.trim()){a.setAttribute('data-ar','واتساب');a.setAttribute('data-en','WhatsApp');a.textContent=lang==='en'?'WhatsApp':'واتساب';}});
  };
  const s=document.createElement('script');s.src=CORE;s.onload=()=>{
    const original=window.setLanguage;
    window.setLanguage=(lang)=>{if(original)original(lang);setTimeout(mark,0);};
    const originalToggle=window.toggleLanguage;
    if(originalToggle)window.toggleLanguage=()=>{originalToggle();setTimeout(mark,0);};
    setTimeout(mark,0);
  };document.head.appendChild(s);
})();