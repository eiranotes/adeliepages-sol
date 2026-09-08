(() => {
  const name = document.querySelector('#pack-name');
  const english = document.querySelector('#pack-english');
  const description = document.querySelector('#pack-description');
  const tags = document.querySelector('#pack-tags');
  const count = document.querySelector('#pack-count');
  const grid = document.querySelector('#sticker-grid');
  const search = document.querySelector('#sticker-search');
  const status = document.querySelector('#search-status');
  const empty = document.querySelector('#catalog-empty');
  const clear = document.querySelector('#clear-search');
  const dialog = document.querySelector('#sticker-dialog');
  const dialogImage = document.querySelector('#dialog-image');
  const dialogName = document.querySelector('#dialog-name');
  const dialogIndex = document.querySelector('#dialog-index');
  const close = document.querySelector('.dialog-close');
  const prev = document.querySelector('#dialog-prev');
  const next = document.querySelector('#dialog-next');

  let pack = null;
  let visible = [];
  let activeIndex = 0;
  let lastTrigger = null;

  const currentSlug = () => (location.hash || '#lemon').slice(1);

  function renderPack(data) {
    const slug = currentSlug();
    pack = data.find((item) => item.slug === slug) || data[0];
    document.title = `${pack.name} — Adelie Pages`;
    name.textContent = pack.name;
    english.textContent = pack.english;
    description.textContent = pack.description;
    count.textContent = `스티커 ${pack.stickers.length}개`;
    tags.innerHTML = '';
    pack.tags.forEach((tag) => {
      const span = document.createElement('span');
      span.textContent = tag;
      tags.appendChild(span);
    });
    search.value = '';
    renderStickers(pack.stickers);
  }

  function renderStickers(items) {
    visible = items;
    grid.innerHTML = '';
    items.forEach((sticker, index) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'sticker-item';
      button.dataset.index = index;
      button.innerHTML = `<span class="sticker-thumb"><img src="${sticker.thumb}" alt=""></span><span class="sticker-name">${sticker.name}</span>`;
      button.addEventListener('click', () => openDialog(index, button));
      grid.appendChild(button);
    });
    empty.hidden = items.length !== 0;
    status.textContent = items.length === pack.stickers.length ? `${items.length}개의 스티커` : `${items.length}개 찾음`;
  }

  function filter() {
    const q = search.value.trim().toLocaleLowerCase('ko');
    if (!q) return renderStickers(pack.stickers);
    renderStickers(pack.stickers.filter((sticker) => sticker.name.toLocaleLowerCase('ko').includes(q) || sticker.id.toLowerCase().includes(q)));
  }

  function openDialog(index, trigger) {
    activeIndex = index;
    lastTrigger = trigger;
    updateDialog();
    dialog.showModal();
  }

  function updateDialog() {
    const sticker = visible[activeIndex];
    if (!sticker) return;
    dialogImage.src = sticker.image;
    dialogImage.alt = sticker.name;
    dialogName.textContent = sticker.name;
    dialogIndex.textContent = `${activeIndex + 1} / ${visible.length}`;
    prev.disabled = visible.length < 2;
    next.disabled = visible.length < 2;
  }

  function move(delta) {
    if (!visible.length) return;
    activeIndex = (activeIndex + delta + visible.length) % visible.length;
    updateDialog();
  }

  fetch('./catalog.json')
    .then((res) => { if (!res.ok) throw new Error('catalog'); return res.json(); })
    .then((data) => {
      renderPack(data);
      window.addEventListener('hashchange', () => renderPack(data));
    })
    .catch(() => { description.textContent = '팩 정보를 불러오지 못했습니다.'; });

  search.addEventListener('input', filter);
  clear.addEventListener('click', () => { search.value = ''; filter(); search.focus(); });
  close.addEventListener('click', () => dialog.close());
  prev.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => lastTrigger?.focus());
  dialog.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') move(-1);
    if (event.key === 'ArrowRight') move(1);
  });
})();
