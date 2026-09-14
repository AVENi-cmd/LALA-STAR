(()=>{
  const KEY='lalastar-language';
  const translations={
    'تخطي إلى المحتوى الرئيسي':'Skip to main content',
    'من نحن':'About Us','أنشطتنا':'Our Businesses','فروعنا':'Branches','تواصل معنا':'Contact',
    'شركة لألأة النجوم التجارية · المملكة العربية السعودية':'LALA STAR TRADING CO. · Saudi Arabia',
    'تجارة المواد الغذائية بالجملة منذ 1993':'Wholesale Food Trade Since 1993',
    'من الدمام إلى الأحساء، مسيرة تجارية بدأت عام 1993 وتوسعت مع الوقت في أنشطة البلاستيك والحلويات والوجبات الخفيفة.':'From Dammam to Al-Ahsa, a trading journey that began in 1993 and expanded over time into plastics, sweets, and snacks.',
    'اكتشف قصتنا ←':'Discover Our Story →','تواصل معنا':'Contact Us',
    'عام التأسيس في الدمام':'Year Founded in Dammam','افتتاح فرع الأحساء':'Al-Ahsa Branch Opened','مواقع رئيسية للمواد الغذائية':'Main Food Locations',
    'شركة لها مسار واضح':'A Clear Business Journey',
    'تأسست شركة لألأة النجوم التجارية في الدمام عام 1993 في مجال بيع المواد الغذائية بالجملة، ثم توسعت أعمالها لتشمل أنشطة تجارية أخرى تحت مظلة الشركة.':'LALA STAR TRADING CO. was established in Dammam in 1993 as a wholesale food business, then expanded into additional activities under the company.',
    'تجارة وتوزيع بالجملة':'Wholesale Trade & Distribution','من الدمام بدأت الرحلة':'The Journey Began in Dammam',
    'الدمام هي الفرع الرئيسي للشركة. وفي عام 2018 تم افتتاح فرع الأحساء، ثم توسعت الأنشطة في البلاستيك والحلويات والوجبات الخفيفة في مواقعها المخصصة.':'Dammam is the company’s main branch. In 2018, the Al-Ahsa branch opened, followed by expansion into plastics, sweets, and snacks at their designated locations.',
    'بداية الشركة — الدمام':'Company Founded — Dammam','انطلاق النشاط في بيع المواد الغذائية بالجملة.':'The business began with wholesale food products.',
    'بعد التوسع':'After Expansion','أنشطة البلاستيك والحلويات':'Plastics, Sweets & Snacks Activities','تأسست أنشطة مستقلة تحت مظلة الشركة لتخدم أسواقًا ومنتجات مختلفة.':'Independent activities were established under the company to serve different markets and product categories.',
    'افتتاح فرع الأحساء':'Al-Ahsa Branch Opening','افتتاح فرع الأحساء واستمرار التوسع في الأنشطة التجارية.':'The Al-Ahsa branch opened and the company continued expanding its commercial activities.',
    'أنشطتنا':'Our Businesses','أنشطة مستقلة تحت مظلة الشركة، مع الحفاظ على وضوح كل نشاط وموقعه.':'Independent activities under one company, with each activity and location clearly defined.',
    'المواد الغذائية بالجملة':'Wholesale Food Products','النشاط الرئيسي للشركة.':'The company’s core activity.','الدمام · الأحساء':'Dammam · Al-Ahsa',
    'المنتجات البلاستيكية':'Plastic Products','منتجات البلاستيك والأدوات المنزلية.':'Plastic products and household supplies.',
    'الحلويات والسناكات':'Sweets & Snacks','حلويات ووجبات خفيفة.':'Sweets and snack products.','الأحساء فقط':'Al-Ahsa Only',
    'فروعنا ومواقعنا':'Our Branches & Locations','المواد الغذائية متوفرة في الدمام والأحساء، بينما الحلويات والوجبات الخفيفة في الأحساء فقط.':'Food products are available in Dammam and Al-Ahsa, while sweets and snacks are available in Al-Ahsa only.',
    'الفرع الرئيسي — الدمام':'Main Branch — Dammam','المواد الغذائية — الدمام':'Food Products — Dammam','الفرع الرئيسي للشركة منذ 1993.':'The company’s main branch since 1993.',
    'فرع المواد الغذائية — الأحساء':'Food Products Branch — Al-Ahsa','المواد الغذائية — الأحساء':'Food Products — Al-Ahsa','فرع الأحساء الذي افتتح عام 2018.':'The Al-Ahsa branch opened in 2018.',
    'فتح الموقع على الخرائط ↗':'Open Location in Maps ↗','تواصل مع شركة لألأة النجوم التجارية':'Contact LALA STAR TRADING CO.',
    'للاستفسارات والتواصل التجاري، يمكنكم التواصل معنا عبر الهاتف أو البريد الإلكتروني.':'For inquiries and business communication, contact us by phone or email.',
    'الهاتف':'Phone','البريد الإلكتروني':'Email','لبيع المواد الغذائية بالجملة · المملكة العربية السعودية':'Wholesale Food Trade · Saudi Arabia',
    'شركة لألأة النجوم التجارية':'LALA STAR TRADING CO.','لبيع المواد الغذائية بالجملة':'Wholesale Food Trade',
    'شركة لألأة النجوم التجارية — لبيع المواد الغذائية بالجملة':'LALA STAR TRADING CO. — Wholesale Food Trade',
    'مستودع تجاري للسلع والمواد بالجملة':'Commercial warehouse for wholesale goods and products',
    'المواد الغذائية — FOOD PRODUCTS':'Wholesale Food Products — FOOD PRODUCTS',
    'المنتجات البلاستيكية — PLASTIC PRODUCTS':'Plastic Products — PLASTIC PRODUCTS',
    'الحلويات والسناكات — SWEETS & SNACKS':'Sweets & Snacks — SWEETS & SNACKS',
    'مستودع تجاري للمواد والسلع بالجملة':'Commercial warehouse for wholesale goods and products'
  };
  const meta={
    title:'LALA STAR TRADING CO. | Wholesale Food Trade Since 1993',
    description:'LALA STAR TRADING CO. — wholesale food trade since 1993, with plastics, sweets, and snacks activities in Dammam and Al-Ahsa.',
    ogTitle:'LALA STAR TRADING CO. | Wholesale Food Trade Since 1993',
    ogDescription:'Wholesale food trade since 1993, with plastics, sweets, and snacks activities in Dammam and Al-Ahsa.'
  };
  const arabicTitle='شركة لألأة النجوم التجارية | LALA STAR TRADING CO.';
  const arabicDescription='شركة لألأة النجوم التجارية — تجارة المواد الغذائية بالجملة منذ 1993.';
  const setMeta=(en)=>{
    document.title=en?meta.title:arabicTitle;
    const d=document.querySelector('meta[name="description"]'); if(d)d.content=en?meta.description:arabicDescription;
    const ogt=document.querySelector('meta[property="og:title"]'); if(ogt)ogt.content=en?meta.ogTitle:arabicTitle;
    const ogd=document.querySelector('meta[property="og:description"]'); if(ogd)ogd.content=en?meta.ogDescription:'شركة لألأة النجوم التجارية — بيع المواد الغذائية بالجملة منذ 1993، مع أنشطة البلاستيك والحلويات والوجبات الخفيفة في الدمام والأحساء.';
    const ogl=document.querySelector('meta[property="og:locale"]'); if(ogl)ogl.content=en?'en_US':'ar_SA';
  };
  const apply=(lang)=>{
    const en=lang==='en';
    document.documentElement.lang=en?'en':'ar';
    document.documentElement.dir=en?'ltr':'rtl';
    document.querySelectorAll('[data-i18n-ar]').forEach(el=>{el.textContent=en?el.dataset.i18nEn:el.dataset.i18nAr});
    document.querySelectorAll('[data-ar]').forEach(el=>{el.textContent=en?el.dataset.en:el.dataset.ar});
    const btn=document.getElementById('langBtn'); if(btn){btn.textContent=en?'AR':'EN';btn.setAttribute('aria-label',en?'Switch to Arabic':'تغيير اللغة');}
    const menu=document.querySelector('.menu'); if(menu)menu.setAttribute('aria-label',menu.getAttribute('aria-expanded')==='true'?(en?'Close menu':'إغلاق القائمة'):(en?'Open menu':'فتح القائمة'));
    setMeta(en);
  };
  const prepare=()=>{
    document.querySelectorAll('body *').forEach(el=>{
      if(el.children.length===0){
        const ar=(el.textContent||'').trim(); const en=translations[ar];
        if(en){el.dataset.i18nAr=ar;el.dataset.i18nEn=en;}
      }
    });
    document.querySelectorAll('img[alt]').forEach(img=>{const ar=img.alt.trim(),en=translations[ar];if(en){img.dataset.altAr=ar;img.dataset.altEn=en;}});
  };
  const init=()=>{prepare();document.querySelectorAll('img[data-alt-ar]').forEach(img=>img.alt=img.dataset.altAr);document.querySelectorAll('.links a[data-ar]').forEach(a=>{a.dataset.i18nAr=a.dataset.ar;a.dataset.i18nEn=a.dataset.en});const saved=localStorage.getItem(KEY);apply(saved==='en'?'en':'ar');const btn=document.getElementById('langBtn');if(btn)btn.addEventListener('click',()=>{const next=document.documentElement.lang==='en'?'ar':'en';localStorage.setItem(KEY,next);document.querySelectorAll('img[data-alt-ar]').forEach(img=>img.alt=next==='en'?img.dataset.altEn:img.dataset.altAr);apply(next);});};
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
