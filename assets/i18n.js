(()=>{
  const CORE='assets/i18n-core.js';
  const pairs={
    'الرئيسية':'Home','من نحن':'About Us','الأقسام التجارية':'Categories','أنشطتنا':'Our Businesses','فروعنا':'Branches','تواصل معنا':'Contact Us','طلب توريد جملة':'Request Quote','طلب تسعيرة للجملة':'Wholesale Quote Request','شركة لألأة النجوم التجارية · المملكة العربية السعودية':'LALA STAR TRADING CO. · Saudi Arabia','تجارة المواد الغذائية بالجملة منذ 1993':'Wholesale Food Products Since 1993','تجارة وتوزيع بالجملة':'Wholesale Trade & Distribution','المواد الغذائية بالجملة':'Wholesale Food Products','النشاط الرئيسي للشركة.':'The company’s core activity.','المنتجات البلاستيكية':'Plastic Products','المنتجات البلاستيكية والتعبئة والتغليف':'Plastic Products & Packaging','منتجات البلاستيك والأدوات المنزلية.':'Plastic products and household supplies.','البلاستيك والمنتجات الورقية':'Plastics & Paper Products','الحلويات والسناكات':'Sweets & Snacks','الحلويات والمقرمشات':'Sweets & Snacks','الحلويات والسناكات (الأحساء)':'Sweets & Snacks (Al-Ahsa)','حلويات ووجبات خفيفة.':'Sweets and snack products.','أصناف الحلويات والوجبات الخفيفة.':'Sweets and snack products.','الأحساء فقط':'Al-Ahsa Only','فرع الأحساء فقط':'Al-Ahsa Only','أسعار جملة تنافسية':'Competitive Wholesale Pricing','أسطول توزيع يغطي الشرقية':'Distribution Fleet Covering the Eastern Region','أسطول توزيع يغطي المنطقة الشرقية':'Distribution Fleet Covering the Eastern Region','سلامة التخزين وجودة الأصناف':'Safe Storage & Product Quality','تخزين آمن وجودة منتجات موثوقة':'Safe Storage & Product Quality','خبرة تجارية راسخة منذ 1993':'Established Commercial Experience Since 1993','أكثر من 5,000 صنف جاهز للتوزيع الفوري':'Over 5,000 Products Ready for Distribution','استعراض الأصناف':'Explore Products','عرض المزيد':'View More','الفرع الرئيسي — الدمام':'Main Branch — Dammam','فرع الأحساء':'Al-Ahsa Branch','قسم المواد الغذائية':'Foodstuffs Division','قسم البلاستيك والورقيات':'Plastics Division','قسم الحلويات':'Sweets Division','اتصال هاتفي':'Call Us','محادثة واتساب':'WhatsApp Order','ساعات العمل':'Working Hours','السبت – الخميس':'Saturday – Thursday','شركة لألأة النجوم لتجارة المواد الغذائية بالجملة':'Trading Company for Wholesale Food Stuffs','السجل التجاري':'Commercial Register','السجل التجاري: 2252101993 · الرقم الضريبي: 310275588900003 · موثق لدى منصة الأعمال':'CR: 2252101993 · VAT: 310275588900003 · Verified on Saudi Business Platform','جميع الحقوق محفوظة © 2026 شركة لألأة النجوم التجارية':'All Rights Reserved © 2026 Lala Star Trading Co.','منصة التوريد المعتمدة لقطاع الأعمال (B2B)':'Designed for Wholesale Excellence','فتح الموقع على الخرائط ↗':'Open Location in Maps ↗','اتصال':'Call','واتساب':'WhatsApp','البريد الإلكتروني':'Email','الهاتف':'Phone','استفسار':'Inquiry','الأسئلة الشائعة':'Frequently Asked Questions','FAQ':'Frequently Asked Questions','لألأة النجوم للمواد الغذائية - الدمام':'LALA STAR FOOD PRODUCTS - DAMMAM','قمة الهامات للبلاستيك والمنظفات':'QIMAT AL-HAMAT PLASTICS & DETERGENTS','لألأة النجوم للمواد الغذائية - الأحساء':'LALA STAR FOOD PRODUCTS - AL-AHSA','لألأة النجوم للبلاستيك والمنظفات':'LALA STAR PLASTICS & DETERGENTS - AL-AHSA','مذاق راقي للحلويات':'Mazaq Raqi Sweets',
    'الدمام هي الفرع الرئيسي للشركة. وفي عام 2018 تم افتتاح فرع الأحساء، ثم توسعت الأنشطة في البلاستيك والحلويات والوجبات الخفيفة في مواقعها المخصصة.':'Dammam is the company’s headquarters. In 2018, the Al-Ahsa branch was established, followed by specialized expansions in plastics, sweets, and snacks.',
    'انطلاق النشاط في بيع المواد الغذائية بالجملة.':'Launch of wholesale food trade operations.',
    'تأسست أنشطة مستقلة تحت مظلة الشركة لتخدم أسواقًا ومنتجات مختلفة.':'Independent commercial divisions established under the corporate umbrella to serve diverse markets.',
    'خدمات وتجربة توريد مصممة لتسهيل التعامل التجاري مع المنشآت في المنطقة الشرقية.':'Tailored supply solutions designed to streamline B2B procurement across the Eastern Province.',
    'حلول تسعير موجهة للمشتريات والكميات التجارية.':'Targeted wholesale pricing strategies for bulk commercial orders.',
    'توزيع يخدم احتياجات المنشآت التجارية في المنطقة الشرقية.':'Scheduled regional logistics serving businesses efficiently.',
    'اهتمام بظروف التخزين وجودة المنتجات أثناء دورة التوريد.':'Strict temperature control and safe storage throughout the supply chain.',
    'مسيرة تجارية ممتدة منذ تأسيس الشركة في الدمام.':'Extensive commercial reliability and market legacy since 1993.',
    'أنشطة مستقلة تحت مظلة الشركة، مع الحفاظ على وضوح كل نشاط وموقعه.':'Specialized commercial divisions under one corporate umbrella with dedicated facilities.',
    'نخدم مجموعة متنوعة من المنشآت التجارية التي تعتمد على التوريد بالجملة.':'Serving diverse commercial sectors relying on reliable bulk supply.',
    'احتياجات إعادة التوريد اليومية والمخزون التجاري.':'Daily replenishment and inventory management for retail groceries.',
    'أصناف وكميات مناسبة للتشغيل التجاري المستمر.':'Bulk quantities and ingredients optimized for foodservice operations.',
    'حلول توريد للمنشآت التي تحتاج إلى كميات منتظمة.':'Scheduled large-scale supply contracts for institutional catering.',
    'منتجات بلاستيكية وأدوات تلائم احتياجات منافذ البيع.':'Wholesale disposable, packaging, and household consumable lines.',
    'سعة تخزينية عالية':'High Storage Capacity',
    'أسطول نقل مبرد وجاف':'Refrigerated & Dry Transport Fleet',
    'معايير مطابقة لهيئة الغذاء والدواء':'SFDA Fully Compliant Standards',
    'الأسئلة المتكررة':'Frequently Asked Questions',
    'إجابات سريعة على أبرز الأسئلة قبل بدء التعامل التجاري.':'Quick answers to essential inquiries before starting B2B trade.',
    'هل توفرون التوصيل للدمام والأحساء وضواحيها؟':'Do you deliver across Dammam, Al-Ahsa, and surrounding areas?',
    'نعم، يتوفر أسطول نقل منتظم للمنشآت التجارية.':'Yes, a dedicated transport fleet serves commercial establishments on schedule.',
    'ما هي آلية الحصول على قائمة الأسعار والكميات؟':'How can we obtain wholesale price lists and bulk quotations?',
    'حضورك ورؤية المنتجات واختيار المنتج المناسب لك أو الإتصال عبر الهاتف للحصول على تسعيرة فورية.':'By visiting our facilities in person or contacting our sales desks directly for immediate quotes.',
    'هل يمكن طلب تسعيرة حسب الفرع؟':'Can quotations be requested by specific branch or division?',
    'نعم، يمكن تحديد الفرع المستهدف عند التواصل لإرسال طلب التسعيرة المناسب.':'Yes, inquiries can be directed specifically to Dammam or Al-Ahsa sales desks.',
    'كيف أبدأ التعامل التجاري مع الشركة؟':'How do I start a business partnership with the company?',
    'يمكنك التواصل عبر الهاتف أو البريد الإلكتروني وذكر نشاط المنشأة والأصناف والكميات المطلوبة للبدء.':'Contact our sales representatives with your business details and requested volumes to begin.'
  };
  const aliases={'النشاط الأساسي للشركة.':'النشاط الرئيسي للشركة.','منتجات البلاستيك والأدوات المنزلية.':'المنتجات البلاستيكية والتعبئة والتغليف','حلويات ووجبات خفيفة.':'الحلويات والسناكات','سلامة التخزين وجودة الأصناف':'تخزين آمن وجودة منتجات موثوقة','الأحساء فقط':'فرع الأحساء فقط'};
  const arByEn=Object.fromEntries(Object.entries(pairs).map(([ar,en])=>[en,ar]));
  const salesNames=(el,raw)=>{
    if(!el.closest('.contact-channel'))return null;
    const title=(el.closest('.contact-channel').querySelector('h4')?.textContent||'').replace(/\s+/g,' ').trim();
    const mapAr={'قسم مبيعات الدمام':{'المواد الغذائية':'لألأة النجوم للمواد الغذائية - الدمام','المنتجات البلاستيكية':'قمة الهامات للبلاستيك والمنظفات'},'قسم مبيعات الأحساء':{'المواد الغذائية — خط 1':'لألأة النجوم للمواد الغذائية - الأحساء','المواد الغذائية — خط 2':'لألأة النجوم للمواد الغذائية - الأحساء','المنتجات البلاستيكية':'لألأة النجوم للبلاستيك والمنظفات','الحلويات والمقرمشات':'مذاق راقي للحلويات'}};
    const mapEn={'Dammam Sales':{'Wholesale Food Products':'LALA STAR FOOD PRODUCTS - DAMMAM','Plastic Products':'QIMAT AL-HAMAT PLASTICS & DETERGENTS'},'Al-Ahsa Sales':{'Wholesale Food Products — Line 1':'LALA STAR FOOD PRODUCTS - AL-AHSA','Wholesale Food Products — Line 2':'LALA STAR FOOD PRODUCTS - AL-AHSA','Plastic Products':'LALA STAR PLASTICS & DETERGENTS - AL-AHSA','Sweets & Snacks':'Mazaq Raqi Sweets'}};
    if(mapAr[title]?.[raw]){const ar=mapAr[title][raw];return [ar,pairs[ar]];}
    if(mapEn[title]?.[raw]){const en=mapEn[title][raw];return [arByEn[en],en];}
    return null;
  };
  const businessImages=()=>{
    const items=[
      ['.business-no-image:nth-child(2) .business-placeholder','assets/wide_high_resolution_supermarket_warehouse_aisle.png','المنتجات البلاستيكية'],
      ['.business-no-image:nth-child(3) .business-placeholder','assets/sweets-snacks.webp','الحلويات والسناكات']
    ];
    items.forEach(([selector,src,alt])=>{
      const box=document.querySelector(selector); if(!box || box.querySelector('img'))return;
      const img=document.createElement('img'); img.src=src; img.alt=alt; img.width=1536; img.height=1024; img.loading='lazy'; img.decoding='async'; img.style.width='100%'; img.style.height='100%'; img.style.objectFit='cover'; img.style.display='block'; box.textContent=''; box.appendChild(img);
    });
  };
  const style=()=>{if(document.querySelector('style[data-b2b-hero-polish]'))return;const s=document.createElement('style');s.dataset.b2bHeroPolish='1';s.textContent=`
.hero, #hero, .hero-section { background: linear-gradient(135deg, #0b1524 0%, #112238 50%, #080f1a 100%) !important; color: #ffffff !important; }
.hero h1, .hero h2, .hero p, .hero span { color: #ffffff !important; }
`;document.head.appendChild(s);};
  const setText=(el,value)=>{const textNodes=[...el.childNodes].filter(n=>n.nodeType===3 && n.nodeValue.trim());if(textNodes.length){textNodes[0].nodeValue=value;for(let i=1;i<textNodes.length;i++)textNodes[i].nodeValue='';}else if(el.children.length===0)el.textContent=value;};
  const footerVerification=(lang)=>{
    const footer=document.querySelector('.verification[data-i18n-footer="1"]');
    if(!footer)return;
    footer.querySelectorAll('[data-footer-ar][data-footer-en]').forEach(el=>{
      el.textContent=lang==='en'?el.getAttribute('data-footer-en'):el.getAttribute('data-footer-ar');
    });
    const numbers=footer.querySelectorAll('.footer-number');
    ['2252101993','310275588900003'].forEach((value,i)=>{if(numbers[i])numbers[i].textContent=value;});
  };
  const translateNode=(node,lang)=>{
    const raw=node.nodeValue.replace(/\s+/g,' ').trim();
    if(!raw)return;
    let ar=arByEn[raw]||raw;
    let en=pairs[raw]||raw;
    if(aliases[raw]){ar=aliases[raw];en=pairs[ar]||en;}
    if(lang==='en' && pairs[raw]){node.nodeValue=node.nodeValue.replace(raw,en);}
    else if(lang==='ar' && arByEn[raw]){node.nodeValue=node.nodeValue.replace(raw,ar);}
  };
  const mark=()=>{
    style();
    businessImages();
    const lang=document.documentElement.lang==='en'?'en':'ar';
    document.documentElement.lang=lang;
    document.documentElement.dir=lang==='en'?'ltr':'rtl';
    const selectors='h1,h2,h3,h4,h5,h6,p,span,a,button,small,strong,label,li,.kicker';
    document.querySelectorAll(selectors).forEach(el=>{
      if(el.closest('script,style,noscript,.verification[data-i18n-footer="1"]'))return;
      const raw=el.textContent.replace(/\s+/g,' ').trim();
      if(!raw)return;
      let ar=el.getAttribute('data-ar')||'';
      let en=el.getAttribute('data-en')||'';
      const sales=salesNames(el,raw);
      if(sales){[ar,en]=sales;}
      else if(aliases[raw]){ar=aliases[raw];en=pairs[ar]||en;}
      else if(pairs[raw]){ar=raw;en=pairs[raw];}
      else if(arByEn[raw]){en=raw;ar=arByEn[raw];}
      if(ar&&en){el.setAttribute('data-ar',ar);el.setAttribute('data-en',en);el.setAttribute('data-i18n',el.getAttribute('data-i18n')||ar);setText(el,lang==='en'?en:ar);}
    });
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    const nodes=[];
    while(walker.nextNode())nodes.push(walker.currentNode);
    nodes.forEach(node=>{
      if(node.parentElement?.closest('script,style,noscript,.verification[data-i18n-footer="1"]'))return;
      const raw=node.nodeValue.replace(/\s+/g,' ').trim();
      if(!raw)return;
      if(lang==='en' && pairs[raw])node.nodeValue=node.nodeValue.replace(raw,pairs[raw]);
      else if(lang==='ar' && arByEn[raw])node.nodeValue=node.nodeValue.replace(raw,arByEn[raw]);
    });
    document.querySelectorAll('a[href^="tel:"]').forEach(a=>{if(!a.textContent.trim())return;a.setAttribute('data-ar','اتصال');a.setAttribute('data-en','Call');setText(a,lang==='en'?'Call':'اتصال');});
    footerVerification(lang);
    document.querySelectorAll('a[href*="wa.me"]').forEach(a=>{if(!a.textContent.trim())return;a.setAttribute('data-ar','واتساب');a.setAttribute('data-en','WhatsApp');setText(a,lang==='en'?'WhatsApp':'واتساب');});
  };
  const boot=()=>{
    const original=window.setLanguage;
    if(typeof original==='function')window.setLanguage=(lang)=>{original(lang);setTimeout(mark,0);setTimeout(mark,120);};
    const originalToggle=window.toggleLanguage;
    if(typeof originalToggle==='function')window.toggleLanguage=()=>{originalToggle();setTimeout(mark,0);setTimeout(mark,120);};
    setTimeout(mark,0);
    setTimeout(mark,150);
    const observer=new MutationObserver(()=>{clearTimeout(observer._timer);observer._timer=setTimeout(mark,30);});
    observer.observe(document.body,{subtree:true,childList:true,characterData:true});
  };
  const s=document.createElement('script');s.src=CORE;s.onload=boot;document.head.appendChild(s);
})();